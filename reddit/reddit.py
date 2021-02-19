import praw
import os


# Reddit Class - Code in releation to Reddit Only.
class Reddit:
    def __init__(self, user_choice_of_subreddit, user_choice_of_results, user_choice_of_search):

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
                print("Search: Rising")
                print(submission.id)
                print(submission.author)
                print(submission.name)
                print(submission.title)
                print(submission.num_comments)
                print(submission.url)
                print("This post has: ", submission.score, " upvotes.")

        elif user_choice_of_search == "new":
            for submission in subreddit.new(limit=user_choice_of_results_final):
                print("Search: Rising")
                print(submission.id)
                print(submission.author)
                print(submission.name)
                print(submission.title)
                print(submission.num_comments)
                print(submission.url)
                print("This post has: ", submission.score, " upvote(s).")

        elif user_choice_of_search == "top":
            for submission in subreddit.top(limit=user_choice_of_results_final):
                print("Search: Rising")
                print(submission.id)
                print(submission.author)
                print(submission.name)
                print(submission.title)
                print(submission.num_comments)
                print(submission.url)
                print("This post has: ", submission.score, " upvotes.")

        elif user_choice_of_search == "rising":
            for submission in subreddit.rising(limit=user_choice_of_results_final):
                print("Search: Rising")
                print(submission.id)
                print(submission.author)
                print(submission.name)
                print(submission.title)
                print(submission.num_comments)
                print(submission.url)
                print("This post has: ", submission.score, " upvotes.")


        else:
            pass 




def test():
    
    reddit = praw.Reddit(
    client_id="DPn6cOtSZYZJug",
    client_secret="WQj8aPewT55hn3JQcBO0M8f1o-AqIg",
    user_agent="itoby24"
    )


    redditor = reddit.redditor("tahzeerr")

    account_has_verified_email = redditor.has_verified_email
    account_id = redditor.id
    account_img_link = redditor.icon_img
    account_comment_karma = redditor.comment_karma
    # account_is_suspended = redditor.is_suspended
    account_is_mod = redditor.is_mod
    account_is_gold = redditor.is_gold
    account_name = redditor.name
    account_link_karma = redditor.link_karma

    print(account_comment_karma)
    print(account_name)
    print(account_link_karma)
    print(account_is_mod)
    print(account_is_gold)
    print(account_img_link)
    print(account_id)
    print(account_has_verified_email)



test()
   
# Reddit("Verizon", 5, "new")
# Reddit("dankmemes" ,10, "new")






