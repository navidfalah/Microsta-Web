from django.contrib.auth.base_user import BaseUserManager


class EmailUserManager(BaseUserManager):

    def create_user(self, email, password=None, **other_fields):
        if not email:
            raise ValueError("mobile is required!")
        user = self.model(email=email, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        return self.create_user(email, password, **other_fields)
    