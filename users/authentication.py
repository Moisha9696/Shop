import logging

from django.contrib.auth.models import User

from users.models import Profile

logger = logging.getLogger(__name__)

class EmailAuthBackend:
    def authenticate(self, request, email=None, password=None, **kwargs):
        # Логируем вызов
        print("=== EmailAuthBackend.authenticate called ===")
        print(f"username: {email}")
        print(f"kwargs: {kwargs}")

        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user
            return None
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            logger.info(f"except : user : with {email} - DoesNotExist")
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


def create_profile(backend, user, *args, **kwargs):
    """
    Create user profile for social authentication
    """
    Profile.objects.get_or_create(user=user)
