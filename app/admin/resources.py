
from fastapi_admin.app import app
from fastapi_admin.resources import Action, Dropdown, Field, Link, Model, ToolbarAction
from fastapi_admin.widgets import displays, filters, inputs

from app import models

from . import widgets as custom


@app.register
class Home(Link):
    label = "Home"
    icon = "fas fa-home"
    url = "/admin"


@app.register
class AdminResource(Model):
    label = "Admin"
    model = models.Admin
    icon = "fas fa-user-cog"
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

@app.register
class UserResource(Model):
    label = "Users"
    model = models.User
    icon = "fas fa-user"
    page_pre_title = "user list"
    page_title = "user model"

    fields = [
        Field(
            name="id",
            label="id",
            display=displays.InputOnly(),
            input_=inputs.DisplayOnly(),
        ),
        "username",
        "email",
        "nickname",
        Field(
            name="hashed_password",
            label="password",
            display=displays.InputOnly(),
            input_=custom.inputs.HashedPassword(),
        ),
        "is_verified",
        "is_active",
        "registered_at",
    ]


@app.register
class GithubLink(Link):
    label = "Github"
    url = "https://google.com/"
    icon = "fab fa-github"
    target = "_blank"
