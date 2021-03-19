from django.db import models

CHOICE = (("danger","high"), ("primary","normal"), ("success","low"))

class TodoModel(models.Model):
    title = models.CharField(max_length=20)
    memo = models.TextField()
    priority = models.CharField(
        max_length = 50,
        choices = CHOICE
    )
    duedate = models.DateField()

    def __str__(self):
        return self.title