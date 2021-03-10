"""Registry of installed applications that stores configuration."""
from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """Created applications in the project user_auth."""

    name = 'accounts'
