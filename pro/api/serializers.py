from rest_framework import serializers

from pro.models import *

class TicketingToolSerializer(serializers.ModelSerializer):
    select_tool_display = serializers.SerializerMethodField()
    authentication_type_display = serializers.SerializerMethodField()

    def get_select_tool_display(self, tickiting_tool):
        if tickiting_tool.select_tool:
            return dict(TicketingTool.TICKITING_TOOL)[tickiting_tool.select_tool]
        else:
            return tickiting_tool

    def get_authentication_type_display(self, tickiting_tool):
        if tickiting_tool.authentication_type:
            return dict(TicketingTool.AUTH_TYPE)[tickiting_tool.authentication_type]
        else:
            return tickiting_tool.authentication_type

    class Meta:
        model = TicketingTool
        fields = (
            "select_tool_display",
            "select_tool",
            "endpoint",
            "authentication_type_display",
            "authentication_type",
            "username",
        )
