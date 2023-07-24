from django.shortcuts import render
from .forms import ReviewForm
from .models import Review
from .model_wrapper import ReviewModel


def review_submission(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review_text = form.cleaned_data['review_text']
            review_model = ReviewModel()
            predicted_rating,sentiment = review_model.preprocess_review_text(review_text)

            movie_review = Review.objects.create(
                review_text=review_text,
                predicted_rating=predicted_rating,
                sentiment_status=sentiment
            )
            movie_review.save()

            return render(request, 'result.html', {
                'predicted_rating': predicted_rating,
                'sentiment_status': sentiment
            })
    else:
        form = ReviewForm()

    return render(request, 'review_submission.html', {'form': form})
