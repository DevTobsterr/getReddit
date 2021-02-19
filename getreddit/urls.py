from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.search_tool_home, name="search_tool_home"),

    # Reddit URLS
    path('reddit/', views.reddit_home, name="reddit_home"),
        # Reddit - Subreddit Search
    path('reddit/search/subreddit/', views.reddit_search_subreddit, name="reddit_search_subreddit"),
    path('reddit/search/subreddit/results/', views.reddit_search_subreddit_results, name="reddit_search_subreddit_results"),
        # Reddit - Account Information Search
    path('reddit/search/reddit_user_information/', views.reddit_user_information, name="reddit_user_information"),
    path('reddit/search/reddit_user_information/results/', views.reddit_user_information_results, name="reddit_user_information_results"),
    
        # Reddit - Posts by Username Search
    



    # path('reddit/search/results/', views.reddit_results, name="reddit_results"),
    # path('reddit/search/general', views.reddit_general, name="reddit_general"),
    # path('', views.search_tool_home, name="search_tool_home"),

    # path('reddit/search/', views.reddit_results, name="reddit_results"),
    # path('reddit/search/general/', views.reddit_results, name="reddit_results"),
    # path('reddit/search/general/results', views.reddit_results, name="reddit_results"),

    # TikTok URLS


]
