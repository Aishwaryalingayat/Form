import rest_framework
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from pro.models import *
from pro.api.serializers import *

from rest_framework import status

class GetTickitingToolProjectList(GenericAPIView):
    permission_classes = [AllowAny]
    def get(self, request, *args, **kwargs):

        tickiting_tools = TicketingTool.objects.all()

        return Response({
            "tools": TicketingToolSerializer(tickiting_tools, many=True).data
        })

class AddTickitingToolProjectList(GenericAPIView):
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):

        select_tool = request.data.get('select_tool')

        endpoint = request.data.get('endpoint')
        if not endpoint:
            return Response({"error_message": "Endpoint is required."}, status=status.HTTP_400_BAD_REQUEST)

        authentication_type = request.data.get('auth_type')
        username = request.data.get('username')
        password = request.data.get('password')
        token = request.data.get('token')

        tickiting_tool = TicketingTool.objects.create(
            select_tool=select_tool,
            endpoint=endpoint,
            authentication_type=authentication_type,
            username=username,
            password=password,
            token=token
        )

        return Response({
            "tool": TicketingToolSerializer(tickiting_tool).data
        })

