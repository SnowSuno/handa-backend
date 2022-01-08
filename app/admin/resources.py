
from fastapi_admin.app import app
from fastapi_admin.resources import Field, Link, Model, ComputeField
from fastapi_admin.widgets import displays, filters, inputs

from app import models

from . import custom


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
    filters = [
        filters.Search(
            name="username",
            label="username",
            search_mode="contains",
            placeholder="search for an username"
        )
    ]
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
        # custom.fields.HashedPasswordField(
        #     name="hashed_password",
        #     label="password",
        #     display=displays.InputOnly(),
        #     input_=inputs.Password()
        # ),
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
class TodoResource(Model):
    label = "Todos"
    model = models.Todo
    icon = "fas fa-clipboard-list"
    page_pre_title = "todo list"
    page_title = "todo model"
    filters = [
        custom.filters.ForeignFieldSearch(
            name="creator",
            label="creator",
            key_field="username",
            placeholder="search by creator",
            null=True
        )
    ]
    fields = [
        "id",
        "title",
        "is_done",
        Field(
            name="creator_id",
            label="creator",
            display=displays.InputOnly(),
            # input_=inputs.Input(help_text="creator_id"),
            input_=inputs.ForeignKey(
                model=models.User,
                null=False,
                default=None
            ),
        ),
        custom.fields.ForeignKeyDisplayField(
            model=models.User,
            name="creator_id",
            label="creator",
            display_field="username",
            display=displays.Display(),
            input_=inputs.DisplayOnly()
        )


    ]


@app.register
class DocumentationLink(Link):
    label = "Documentation"
    url = "https://service-handa.herokuapp.com/docs"
    icon = "fas fa-file-code"
    target = "_blank"
