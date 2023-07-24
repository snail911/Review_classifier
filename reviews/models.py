from django.db import models

class Review(models.Model):
    review_text = models.TextField()
    predicted_rating = models.FloatField()
    sentiment_status = models.CharField(max_length=10)
