import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError


class Command(BaseCommand):
    help = 'Creates admin user from ADMIN_USER and ADMIN_PASSWORD environment variables'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.UserModel = get_user_model()
        self.username_field = self.UserModel._meta.get_field(self.UserModel.USERNAME_FIELD)

    def handle(self, *args, **options):
        if os.environ.get('ADMIN_USER') and os.environ.get('ADMIN_PASSWORD'):
            user_data = {}
            user_data['username'] = os.environ.get('ADMIN_USER')
            user_data['password'] = os.environ.get('ADMIN_PASSWORD')
            user_data['email'] = 'webmaster@example.com'
            try:
                self.UserModel._default_manager.create_superuser(**user_data)
            except IntegrityError:
                user = self.UserModel._default_manager.get(username=os.environ.get('ADMIN_USER'))
                user.set_password(os.environ.get('ADMIN_PASSWORD'))
                user.save()
