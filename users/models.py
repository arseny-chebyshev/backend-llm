from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models import BaseModel
from django.conf import settings


class User(AbstractUser, BaseModel):

    balance = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def discord(self) -> 'DiscordUser':
        return self.discord_user

    class Meta:
        swappable = "AUTH_USER_MODEL"


class DiscordUser(BaseModel):
    """
    Represents a Discord user associated with a Django User.

    Attributes:
        `user` (User): Django User associated with the DiscordUser.
        `discord_id` (str): The user's ID (snowflake).
        `username` (str): The user's username (not unique across the platform).
        `discriminator` (str): The user's Discord-tag.
        `global_name` (str, optional): The user's display name, if set.
            For bots, this is the application name.
        `avatar` (str, optional): The user's avatar hash.
        `bot` (bool): Whether the user belongs to an OAuth2 application.
        `system` (bool): Whether the user is an Official Discord System user
            (part of the urgent message system).
        `mfa_enabled` (bool): Whether the user has two-factor authentication
            enabled on their account.
        `banner` (str, optional): The user's banner hash.
        `accent_color` (int, optional): The user's banner color encoded as an
            integer representation of a hexadecimal color code.
        `locale` (str, optional): The user's chosen language option.
        `verified` (bool): Whether the email on this account has been verified.
        `email` (str, optional): The user's email.
        `flags` (int, optional): The flags on a user's account.
        `premium_type` (int, optional): The type of Nitro subscription on
            a user's account.
        `public_flags` (int, optional): The public flags on a user's account.
        `avatar_decoration` (str, optional): The user's avatar decoration hash.
    """
    user: User = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='discord_user',
        null=True, blank=True
    )
    discord_id = models.CharField(
        max_length=255,
        help_text="The user's Discord ID (snowflake)"
    )
    username = models.CharField(
        max_length=255,
        help_text="The user's username (not unique across the platform)"
    )

    discriminator = models.CharField(
        max_length=4,
        help_text="The user's Discord-tag"
    )

    global_name = models.CharField(
        max_length=255,
        null=True, blank=True,
        help_text="The user's display name, if set. For bots, "
        "this is the application name"
    )

    avatar = models.CharField(
        max_length=255,
        null=True, blank=True,
        help_text="The user's avatar hash"
    )

    bot = models.BooleanField(
        default=False,
        help_text="Whether the user belongs to an OAuth2 application"
    )

    system = models.BooleanField(
        default=False,
        help_text="Whether the user is an Official Discord System user (part of the urgent message system)"
    )

    mfa_enabled = models.BooleanField(
        default=False,
        help_text="Whether the user has two-factor authentication enabled on their account"
    )

    banner = models.CharField(
        max_length=255,
        null=True, blank=True,
        help_text="The user's banner hash")

    accent_color = models.IntegerField(
        null=True,
        blank=True,
        help_text="The user's banner color encoded as an integer representation of a hexadecimal color code"
    )

    locale = models.CharField(
        max_length=255,
        null=True, blank=True,
        help_text="The user's chosen language option"
    )

    verified = models.BooleanField(
        default=False,
        help_text="Whether the email on this account has been verified"
    )

    email = models.EmailField(
        null=True,
        blank=True,
        help_text="The user's email"
    )

    flags = models.IntegerField(
        null=True,
        blank=True,
        help_text="The flags on a user's account"
    )

    premium_type = models.IntegerField(
        null=True, blank=True,
        help_text="The type of Nitro subscription on a user's account"
    )

    public_flags = models.IntegerField(
        null=True, blank=True,
        help_text="The public flags on a user's account"
    )

    avatar_decoration = models.CharField(
        max_length=255,
        null=True, blank=True,
        help_text="The user's avatar decoration hash"
    )

    @property
    def balance(self):
        return self.user.balance

    def save(self, *args, **kwargs):
        self.user.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.username}#{self.discriminator}"

