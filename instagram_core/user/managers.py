from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    """Кастомный менеджер для модели кастомного пользователя"""

    def create_user(self, username, password, **extra_fields):
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields['is_superuser'] = True
        extra_fields['is_staff'] = True
        extra_fields['is_active'] = True
        return self.create_user(username, password, **extra_fields)