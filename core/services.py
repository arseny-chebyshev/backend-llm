from abc import ABC
from users.models import User


class BaseService(ABC):
    def __init__(self, user: User) -> None:
        self.user = user
