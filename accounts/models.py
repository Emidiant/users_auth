"""Account app models."""
from datetime import datetime, timedelta

from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import jwt


class UserManager(BaseUserManager):
    """Own manager class for custom user inherited from BaseUserManager."""

    def create_user(self, username, password=None):
        """
        Create and returns user with a username and password.

        - **parameters**, **return**::

            :parameter password:
                user password
            :type password:str
            :parameter username:
                unique username up to 150 characters with indexing for the database
            :type username:str
            :return: return object User

        """
        if username is None:
            raise TypeError('Users must have a username.')

        user = self.model(username=username)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, password):
        """
        Creates and returns superuser with a username and password.

        - **parameters**, **return**::

            :parameter password:
                user password
            :type password:str
            :parameter username:
                unique username up to 150 characters with indexing for db
            :type username: str
            :return: return object User

        """
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom User class inherited from AbstractBaseUser

    - **parameters**, **return**::

            :parameter -username:
                unique username up to 150 characters with indexing for the database
            :type -username: str
            :parameter -first_name:
                first_name up to 30 characters
            :type -first_name: str
            :parameter -last_name:
                last_name up to 150 characters
            :type -last_name: str
            :parameter -is_superuser:
                determines if the user is superuser, default false
            :type -is_superuser: bool
            :parameter -is_staff:
                determines if the user is staff, default false
            :type -is_staff: bool
            :parameter -is_active:
                used instead of deleting a user to save his data
            :type -is_active: bool
            :parameter -last_login:
                date and time of the last authorization in the system
            :type -last_login: datetime
            :return: return object User
            :rtype: object

    """

    username = models.CharField(db_index=True, max_length=150, unique=True)
    is_active = models.BooleanField(default=True)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=150, null=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'

    objects = UserManager()

    def __str__(self):
        """String representation of the model for console display."""
        return self.username

    @property
    def token(self):
        """Lets get the user's token by calling user.token."""
        return self._generate_jwt_token()

    def get_full_name(self):
        """Method for Django processing."""
        return self.username

    def _generate_jwt_token(self):
        """
        Generates a JSON web token

        That token stores the ID of this user, the token expires 60 day from creation

        """
        dt = datetime.now() + timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')
