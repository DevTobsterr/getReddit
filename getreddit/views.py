from django.shortcuts import render
from django.http import HttpResponse
import praw
import os

# Reddit Subreddit 
from .forms import reddit_subreddit_form
from .models import GetReddit_Subreddit
# Reddit UserInformation
from .models import GetReddit_UserInformation
from .forms import reddit_user_information_form


from .models import GetReddit_Subreddit_Images
from .forms import subreddit_images_form


import urllib

from .models import GetReddit_Subreddit_Images
from .forms import subreddit_images_form

# Create your views here.

def search_tool_home(request):
    return render(request,'getreddit/search_tool_home.html')

def reddit_home(request):
    return render(request, 'getreddit/reddit_home.html')


# Reddit Search Username
def reddit_user_information(request):
    user_information = {}
    user_information['user_information'] = reddit_user_information_form()
    return render(request, 'getreddit/reddit_search_account.html',user_information)

def reddit_user_information_results(request):
    redditor_user_information = {}
    GetReddit_UserInformation.objects.all().delete()
    if request.method == "POST":
        form = reddit_user_information_form(request.POST)
        if form.is_valid():
            user_choice_of_username = form.cleaned_data['user_choice_of_username']
            Reddit.search_user_information(user_choice_of_username)

            results = GetReddit_UserInformation.objects.all()
            return render(request, 'getreddit/reddit_search_account_results.html',{'results':results})
    else:
        search_information["warning"] = "Warning: User Not Found"
        return render(request,'getreddit/reddit_search_account_results.html',search_information)


def subreddit_images(request):
    subreddit_image_search_form = {}
    subreddit_image_search_form['subreddit_image_search'] = subreddit_images_form()
    return render(request, "getreddit/subreddit_images.html",subreddit_image_search_form)


def subreddit_images_results(request):
    if request.method == "POST":
        form = subreddit_images_form(request.POST, request.FILES)
        if form.is_valid():
            user_choice_of_subreddit = form.cleaned_data['user_choice_of_subreddit']
            user_choice_of_results = form.cleaned_data["user_choice_of_results"]
            print(user_choice_of_results)
    
            reddit = praw.Reddit(
                        client_id="DPn6cOtSZYZJug",
                        client_secret="WQj8aPewT55hn3JQcBO0M8f1o-AqIg",
                        user_agent="itoby24"
                            )

            subreddit = reddit.subreddit(user_choice_of_subreddit)
            meme_image_counter = 0
            for submission in reddit.subreddit(user_choice_of_subreddit).new(limit=user_choice_of_results):
                meme_image_counter += 1
                meme_export_file_name = "Reddit_Image{}".format(meme_image_counter)

                file_extension_0 = submission.url.split("/")[-1]
                file_extension_1 = file_extension_0.split(".")[-1]

                meme_export_file_name = "Reddit_Image{}.{}".format(meme_image_counter, file_extension_1)
                if file_extension_1 == "gifv":
                    pass 
                else:
                    try:
                        reddit_exported_image = urllib.request.urlretrieve(submission.url, meme_export_file_name)
                        reddit_images_model = GetReddit_Subreddit_Images(subreddit_image=request.FILES[reddit_exported_image])
                        reddit_images_model.save()
                    except:
                        print("Unsupported Image - Continuing")
                    print("Getting Image - {} - Please wait".format(meme_export_file_name))

            results = GetReddit_Subreddit_Images.objects.all()
            return render(request,"getreddit/subreddit_images_results.html",{'results':results})
    else:
        return render(request,"getreddit/subreddit_images_results.html")


# Reddit Search Subreddit

def reddit_search_subreddit(request):
    reddit_search_subreddit = {}
    reddit_search_subreddit['subreddit'] = reddit_subreddit_form()
    return render(request,'getreddit/reddit_search_subreddit.html', reddit_search_subreddit)

def reddit_search_subreddit_results(request):
    search_information = {}
    GetReddit_Subreddit.objects.all().delete()
    if request.method == "POST":
        form = reddit_subreddit_form(request.POST)
        if form.is_valid():
            user_choice_of_subreddit = form.cleaned_data["user_choice_of_subreddit"]
            user_choice_of_results = str(form.cleaned_data["user_choice_of_results"])
            user_choice_of_search = form.cleaned_data["user_choice_of_search"]
            # search_information["subreddit_information"] = user_choice_of_subreddit
            # search_information["number_of_results"] = user_choice_of_results
            # search_information["search_method"] = user_choice_of_search
            Reddit.search_subreddit(user_choice_of_subreddit, user_choice_of_results, user_choice_of_search)

            results = GetReddit_Subreddit.objects.all()
            return render(request,'getreddit/reddit_search_subreddit_results.html',{'results':results})
            # return render(request,'getreddit/reddit_results.html',search_information)
    else:
        search_information["warning"] = "Warning: Search Failed. Please Try again."
        return render(request,'getreddit/reddit_search_subreddit_results.html',search_information)
































class Reddit:
    def search_user_information(user_choice_of_username): 
        reddit = praw.Reddit(
        client_id="DPn6cOtSZYZJug",
        client_secret="WQj8aPewT55hn3JQcBO0M8f1o-AqIg",
        user_agent="itoby24"
        )

        redditor = reddit.redditor(user_choice_of_username)
        results = GetReddit_UserInformation()
        results.account_name = redditor.name
        results.account_id = redditor.id
        results.account_img_link = redditor.icon_img
        results.account_comment_karma = redditor.comment_karma
        results.account_link_karma = redditor.link_karma
        results.account_is_mod = redditor.is_mod
        results.account_is_gold = redditor.is_gold
        results.save()



    def search_subreddit(user_choice_of_subreddit, user_choice_of_results, user_choice_of_search):
        reddit = praw.Reddit(
        client_id="DPn6cOtSZYZJug",
        client_secret="WQj8aPewT55hn3JQcBO0M8f1o-AqIg",
        user_agent="itoby24"
        )

        user_choice_of_results_final = int(user_choice_of_results)
        user_choice_of_subreddit = user_choice_of_subreddit
        subreddit = reddit.subreddit(user_choice_of_subreddit)
        if user_choice_of_search == 'hot':
            for submission in subreddit.hot(limit=user_choice_of_results_final):
                results = GetReddit_Subreddit()
                results.reddit_author = submission.author
                results.reddit_title = submission.title
                results.reddit_url = submission.url
                results.reddit_name = submission.name
                results.reddit_upvotes = submission.score
                results.reddit_no_of_comments = submission.num_comments
                results.save()
        elif user_choice_of_search == "new":
            for submission in subreddit.new(limit=user_choice_of_results_final):
                results = GetReddit_Subreddit()
                results.reddit_author = submission.author
                results.reddit_title = submission.title
                results.reddit_url = submission.url
                results.reddit_name = submission.name
                results.reddit_upvotes = submission.score
                results.reddit_no_of_comments = submission.num_comments
                results.save()
        elif user_choice_of_search == "top":
            for submission in subreddit.top(limit=user_choice_of_results_final):
                results = GetReddit_Subreddit()
                results.reddit_author = submission.author
                results.reddit_title = submission.title
                results.reddit_url = submission.url
                results.reddit_name = submission.name
                results.reddit_upvotes = submission.score
                results.reddit_no_of_comments = submission.num_comments
                results.save()
        elif user_choice_of_search == "rising":
            for submission in subreddit.rising(limit=user_choice_of_results_final):
                results = GetReddit_Subreddit()
                results.reddit_author = submission.author
                results.reddit_title = submission.title
                results.reddit_url = submission.url
                results.reddit_name = submission.name
                results.reddit_upvotes = submission.score
                results.reddit_no_of_comments = submission.num_comments
                results.save()
        else:
            pass 
