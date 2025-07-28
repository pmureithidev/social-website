from django.contrib.auth.models import User
from account.models import Profile

class EmailAuthBackend:
    """
    Authenticate using an e-mail address.
    This allows users to sign in using their registered email addresses
    
    """

    def authenticate (self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return None
    
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

# create a profile automatically whenever a new user is created
def create_profile(backend, user, *args, **kwargs):
    Profile.objects.get_or_create(user=user)