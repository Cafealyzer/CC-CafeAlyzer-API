from typing import List, Union
from beanie import PydanticObjectId
from models.user import User

user_collection = User

async def add_users(new_user: User) -> User:
    user = await new_user.create()
    return user


async def get_all_users() -> List[User]:
    users = await User.all().to_list()
    return users

async def get_user_by_id(id: PydanticObjectId) -> User:
    student = await user_collection.get(id)
    if student:
        return student
    return False

async def delete_users(id: PydanticObjectId) -> bool:
    users = await user_collection.get(id)
    if users:
        await users.delete()
        return True

async def update_users_data(id: PydanticObjectId, data: dict) -> Union[bool, User]:
    des_body = {k: v for k, v in data.items() if v is not None}
    update_query = {"$set": {field: value for field, value in des_body.items()}}
    user = await user_collection.get(id)
    if user:
        await user.update(update_query)
        return user
    return False
