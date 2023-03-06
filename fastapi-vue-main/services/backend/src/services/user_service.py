from ..models.user import User


class UserService:
    def login(self, email, password):
        user = User(email, password)
        print(f'React 에서 보낸 email :{user.get_email()}')
        print(f'React 에서 보낸 password :{user.get_password()}')
