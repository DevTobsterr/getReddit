from django.db import models


# Create your models here.

class GetReddit_Subreddit(models.Model):
    reddit_author = models.CharField(max_length=32)
    reddit_title = models.CharField(max_length=32)
    reddit_url = models.CharField(max_length=100, default="")
    reddit_name = models.CharField(max_length=32)
    reddit_upvotes = models.CharField(max_length=6)
    reddit_no_of_comments = models.CharField(max_length=10)



class GetReddit_UserInformation(models.Model):
    account_name = models.CharField(max_length=32)
    account_id = models.CharField(max_length=32)
    account_img_link = models.CharField(max_length=128)
    account_comment_karma = models.CharField(max_length=32)
    account_link_karma = models.CharField(max_length=32)
    account_is_mod = models.CharField(max_length=32)
    account_is_gold = models.CharField(max_length=32)





