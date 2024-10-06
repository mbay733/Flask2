from api import app, db, request
from api.models.user import UserModel

# url: /users/<int:user_id>
def get_user_by_id(user_id):
    ...

# url: /users
def get_users(user_id):
    ...
# url: /users
def create_user():
    ...