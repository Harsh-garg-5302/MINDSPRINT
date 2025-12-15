from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    text = models.TextField()
    topic = models.ForeignKey(
        Topic, related_name="questions", on_delete=models.CASCADE, null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "question"


class Answer(models.Model):
    question = models.ForeignKey(
        Question, related_name="answers", on_delete=models.CASCADE
    )
    text = models.CharField(max_length=500)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "answer"


class UserBestScore(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="best_score"
    )
    best_score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.best_score}"