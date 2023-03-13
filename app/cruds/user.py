from app.models import User
from app.cruds.base import CRUDBase
from app.schemas.user import CreateUserSchema, UpdateUserSchema


class UserCRUD(CRUDBase[User, CreateUserSchema, UpdateUserSchema]):
    pass


user_crud = UserCRUD(model=User)
