from django.db import models


class Comment(models.Model):

    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        'user.User', on_delete=models.CASCADE, related_name='comments'
    )
    protest = models.ForeignKey(
        'protests.Protest', on_delete=models.CASCADE, related_name='comments'
    )

    class Meta:
        ordering = ('-timestamp',)
