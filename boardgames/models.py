from django.db import models
# Create your models here.
class Boardgame(models.Model):
    TYPE_CHOICES = [
        ('Custom', 'Custom'),
        ('Original', 'Original'),
    ]

    owner = models.ForeignKey(
        to="users.User",
        related_name="boardgames",
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=2000)
    instruction = models.TextField(max_length=4000)
    image_url = models.URLField(max_length=5000, blank=True)
    type = models.CharField(max_length=255, choices=TYPE_CHOICES)
    genre = models.CharField(max_length=255)
    max_players = models.PositiveIntegerField()
    min_players = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(
        to='users.User',
        related_name='boardgames_likes',
        blank=True
    )

    def __str__(self):
        return self.title