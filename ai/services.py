from langserve import RemoteRunnable
from core.services import BaseService
from users.models import User
from chats.models import Message
from chats.serializers import MessageSerializer

class AIService(BaseService):

    def __init__(
            self,
            user: User,
            runnable_ai_service_address: str = 'http://localhost') -> None:
        super().__init__(user)
        self.chain = RemoteRunnable(runnable_ai_service_address)

    def create_text_message(
            self,
            prompt: str,
            serialize: bool = True) -> Message | MessageSerializer:

        generated_text = self.chain.invoke(prompt)
        message = Message(content=generated_text)

        if serialize:
            return MessageSerializer(message)
        return Message
