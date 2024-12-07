from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager





class CustomUser(AbstractUser):
    """Кастомная модель для пользователей с именем пользователя вместо email"""


    email = None
    username = models.CharField(
        max_length=150,
        unique=True,
        db_index=True,
    )
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    profile_description = models.TextField(null=True, blank=True)

    objects = CustomUserManager()

    class Meta:
        verbose_name_plural = 'Пользователи'
        verbose_name = 'Пользователь'

class CustomUserFollower(models.Model):
    following = models.ForeignKey(
        CustomUser,
        verbose_name="на кого подписался",
        on_delete=models.CASCADE,
        related_name="my_followers"  # мои подписчики
    )
    follower = models.ForeignKey(
        CustomUser,
        verbose_name="кто подписался",
        on_delete=models.CASCADE,
        related_name="my_following"  # мои подписки
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"{self.follower} подписан на {self.following}"



class Publication(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    likes_count = models.PositiveIntegerField(default=0)
    comments_count = models.PositiveIntegerField(default=0)



class Like(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    publication = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'publication',)


class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    publication = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.TextField()