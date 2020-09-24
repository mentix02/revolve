from django.db import models


class Participant(models.Model):

    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    protest = models.ForeignKey('protests.Protest', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.protest.name} - {self.user.username}'
