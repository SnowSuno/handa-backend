from fastapi_admin.app import app
from fastapi_admin.resources import Action, Dropdown, Field, Link, Model, ToolbarAction
from fastapi_admin.widgets import displays, filters, inputs

from app import models


@app.register
class Home(Link):
    label = "Home"
    icon = "fas fa-home"
    url = "/admin"


@app.register
class AdminResource(Model):
    label = "Admin"
    model = models.Admin
    icon = "fas fa-user"
    page_pre_title = "admin list"
    page_title = "admin model"

    fields = [
        "id",
        "username",
        Field(
            name="password",
            label="Password",
            display=displays.InputOnly(),
            input_=inputs.Password(),
        ),
        # Field(name="email", label="Email", input_=inputs.Email()),
        # Field(
        #     name="avatar",
        #     label="Avatar",
        #     display=displays.Image(width="40"),
        #     input_=inputs.Image(null=True, upload=upload),
        # ),
    ]

    # async def get_toolbar_actions(self, request: Request) -> List[ToolbarAction]:
    #     return []
