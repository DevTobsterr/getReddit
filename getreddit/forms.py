from django import forms


reddit_search_choice = (
    ("hot", "Reddit - HOT"),
    ("new", "Reddit - NEW"),
    ("top", "Reddit - TOP"),
    ("rising", "Reddit - RISING")
)

class reddit_subreddit_form(forms.Form):
    user_choice_of_subreddit = forms.CharField(max_length=32, required=True)
    user_choice_of_results = forms.IntegerField(max_value=1000, min_value=0, required=True)
    user_choice_of_search = forms.CharField(required=True, widget=forms.Select(choices=reddit_search_choice))

class reddit_user_information_form(forms.Form):
    user_choice_of_username = forms.CharField(max_length=64, required=True, help_text="Enter a Redditor Username to search")

class subreddit_images_form(forms.Form):
    user_choice_of_subreddit = forms.CharField(max_length=32, required=True)
    user_choice_of_results = forms.IntegerField(max_value=1000, min_value=0, required=True)

    