from django.db import models
from django.contrib.auth.models import User

class Thread(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='thread_user1')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='thread_user2')
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user1', 'user2')

    def __str__(self):
        return f'{self.user1} ↔ {self.user2}'

class Message(models.Model):
    thread  = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='messages')
    sender  = models.ForeignKey(User, on_delete=models.CASCADE)
    text    = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
