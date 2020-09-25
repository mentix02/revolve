from django.db import models


class Participant(models.Model):

    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    protest = models.ForeignKey('protests.Protest', on_delete=models.CASCADE)

    class Meta:
        unique_together = ['user', 'protest']

    def __str__(self) -> str:
        return f'{self.protest.name} - {self.user.username}'
