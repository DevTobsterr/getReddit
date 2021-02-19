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

        elif user_choice_of_search == "new":
            for submission in subreddit.new(limit=user_choice_of_results_final):
    
        elif user_choice_of_search == "top":
            for submission in subreddit.top(limit=user_choice_of_results_final):]

        elif user_choice_of_search == "rising":
            for submission in subreddit.rising(limit=user_choice_of_results_final):


        else:
            pass 


        


   
# Reddit("Verizon", 5, "new")
Reddit("dankmemes" ,10, "new")






