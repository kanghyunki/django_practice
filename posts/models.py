from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#models안에 Model이라는 class를 상속받는다.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    image = models.ImageField(upload_to='posts', null=True)
    created_at = models.DateTimeField()
    liked_users = models.ManyToManyField(User, related_name='liked_posts')

    def __str__(self):
        if self.user:
            return f'{self.user.get_username()}: {self.body}'

        return f'{self.body}'
#여기서 말하는 self는 원래는 post.author 이렇게하는건데 self라고 함
