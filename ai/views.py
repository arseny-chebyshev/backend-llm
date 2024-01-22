from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from ai.services import AIService
from chats.serializers import MessageSerializer


class TextGenAPIView(APIView):
    def post(self, request: Request, *args, **kwargs):
        message = MessageSerializer(request.data)
        service = AIService(request.user)
        generated_message = service.create_text_message(
            message.content
        )
        return Response(
            generated_message.data
        )
