from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), related_name="profile", verbose_name="профиль",
                                on_delete=models.CASCADE)
    avatar = models.ImageField(null=True, blank=True, verbose_name="Аватар", upload_to="avatars/")
    profile_url = models.URLField(max_length=200, null=True, blank=True, verbose_name="Профиль на GitHub")
    about_info = models.TextField(max_length=300, null=True, blank=True, verbose_name="О себе")

    def __str__(self):
        return f"{self.user.username}'s Profile"

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
        permissions = [
            ('can_look_list_of_users', 'Может просмотреть страницу со списком пользователей')
        ]


