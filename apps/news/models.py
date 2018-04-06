from django.db import models


STATUS_CHOICES = (
    (1, 'published'),
    (2, 'draft'),
    (3, 'deleted')
)


class Topic(models.Model):
    name = models.CharField(max_length=255)
    status = models.PositiveSmallIntegerField(default=1, choices=STATUS_CHOICES)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    status = models.PositiveSmallIntegerField(default=1, choices=STATUS_CHOICES)

    topic = models.ManyToManyField(Topic)

    def __str__(self):
        return self.title
