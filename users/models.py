from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    is_verified_email = models.BooleanField(default=False)


class EmailVerification(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    valid_until = models.DateTimeField()
    user_code = models.UUIDField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def send_email(self):
        url = reverse('users:confirm', kwargs={'email': self.user.email, 'user_code': self.user_code})
        verification_link = f'http://127.0.0.1:8000{url}'
        send_mail(
            subject='asddadsa',
            message=f'verificate your account {verification_link}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.user.email],
            fail_silently=False,
        )
