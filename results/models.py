from django.db import models

# Create your models here.
class Result(models.Model):
    RESULT_CHOICES = [
        ('Win', 'Win'),
        ('Loss', 'Loss'),
        ('Draw', 'Draw'),
    ]
    boardgame = models.ForeignKey(
        to='boardgames.Boardgame',
        related_name='results',
        on_delete=models.CASCADE,
    )
    result = models.TextField(max_length=100, choices=RESULT_CHOICES)
    owner = models.ForeignKey(
        to="users.User",
        related_name="results",
        on_delete=models.CASCADE,
        blank=True
    )

    def __str__(self):
        return self.result