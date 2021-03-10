from django.db import models

# Create your models here.
class TicketingTool(models.Model):
    TOOL_ABC = "abc"
    TOOL_EFG = "efg"
    TOOL_XYZ = "xyz"
    AUTH_TYPE_PASSWORD = "password"
    AUTH_TYPE_TOKEN = "token"
    TICKITING_TOOL = [
        (TOOL_ABC,"Abc"),
        (TOOL_EFG,"Efg"),
        (TOOL_XYZ,"Xyz"),
    ]
    AUTH_TYPE = [
        (AUTH_TYPE_PASSWORD,"Password"),
        (AUTH_TYPE_TOKEN,"Token"),
    ]
    select_tool = models.CharField(max_length=10, choices=TICKITING_TOOL)
    endpoint = models.CharField(max_length=50, null=True)
    authentication_type = models.CharField(max_length=50, choices=AUTH_TYPE)
    username = models.CharField(max_length=50, default=None, null=True)
    password = models.CharField(max_length=50, default=None, null=True)
    token = models.CharField(max_length=50, default=None, null=True)

    def __str__(self):
        return self.select_tool

class Projects(models.Model):
    project_name = models.CharField(max_length=50, null=True)

class TicketingToolProject(models.Model):
    ticketing_tool = models.ForeignKey(TicketingTool, on_delete=models.CASCADE)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)