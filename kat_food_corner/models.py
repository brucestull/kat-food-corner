from django.db import models


class Food(models.Model):
    name = models.CharField(
        help_text="The name of the food",
        max_length=255,
    )

    def __str__(self):
        return self.name
