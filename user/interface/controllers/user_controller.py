from dependency_injector.wiring import inject, Provide
from containers import Container
from typing import Annotated
from fastapi import APIRouter, Depends
from pydantic import BaseModel

from user.application.user_service import UserService

router = APIRouter(prefix="/users")

class CreateUserBody(BaseModel):
    name: str
    email: str
    password: str

class UpdateUser(BaseModel):
    name: str | None = None
    password: str | None = None

@router.put("/{user_id}")
@inject
def update_user(
    user_id: str,
    user: UpdateUser,
    user_service: UserService = Depends(Provide[Container.user_service]),
    # user_service : UserService = Depends(container.user_service.provider),
    ):
    print("############",type(user_service))
    user = user_service.update_user(
        user_id=user_id,
        name=user.name,
        password=user.password,
    )

    return user

@router.post("", status_code=201)
@inject
def create_user(
    user : CreateUserBody,
    user_service: UserService = Depends(Provide[Container.user_service]),
    # user_service: UserService = Depends(Provide["user_service"]),
    ):
    print("############",type(user_service))
    created_user = user_service.create_user(
        name=user.name,
        email=user.email,
        password=user.password
    )

    return created_user

