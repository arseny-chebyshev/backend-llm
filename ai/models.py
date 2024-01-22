from core.models import BaseModel


class ContentTypes:
    """Enumerating class for possible
       generational model's
       input/output content type.
       When hinted as parameter -
       use any of values enumerated."""
    TEXT = 'text'
    IMAGE = 'image'
    AUDIO = 'audio'
    VIDEO = 'video'
    CODE = 'code'


class AIModel(BaseModel):
    ...
