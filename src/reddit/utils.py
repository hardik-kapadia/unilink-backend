import yaml
import tweepy
import praw
from src.reddit.settings import Settings
from src.reddit.models import Submission, Redditor

class RedditWrapper:
    def __init__(self):
        self.settings = Settings()
        self.reddit = praw.Reddit(
            client_id=self.settings.client_id,
            client_secret=self.settings.client_secret,
            # password=self.settings.password,
            user_agent=self.settings.user_agent,
            username=self.settings.username,
        )
        print(self.reddit)
        pass
    def map_submission(self,submission):
        mapped_submission = Submission(
            submission.author,
            submission.author_flair_text,
            submission.clicked,
            submission.comments,
            submission.created_utc,
            submission.distinguished,
            submission.edited,
            submission.id,
            submission.is_original_content,
            submission.is_self,
            submission.link_flair_text,
            submission.locked,
            submission.name,
            submission.num_comments,
            submission.over_18,
            submission.saved,
            submission.score,
            submission.selftext,
            submission.spoiler,
            submission.stickied,
            submission.subreddit,
            submission.title,
            submission.upvote_ratio,
            submission.url,
        )
        return mapped_submission


    def map_redditor(self,redditor_object):
        mapped_redditor = Redditor(
            redditor_object.comment_karma,
            redditor_object.comments,
            redditor_object.submissions,
            redditor_object.created_utc,
            redditor_object.has_verified_email,
            redditor_object.icon_img,
            redditor_object.id,
            redditor_object.is_employee,
            redditor_object.is_friend,
            redditor_object.is_mod,
            redditor_object.is_gold,
            redditor_object.link_karma,
            redditor_object.name,
            redditor_object.subreddit,
        )
        return mapped_redditor


    def get_new_post(self,rslash):
        subreddit = self.reddit.subreddit(rslash)
        for submission in subreddit.new(limit=1):
            mapped_submission = self.map_submission(submission)
            return mapped_submission


    def get_hot_post(self,rslash):
        subreddit = self.reddit.subreddit(rslash)
        print(subreddit.title)
        c = 0
        for submission in subreddit.hot(limit=2):
            if c == 0:
                c += 1
                continue
            mapped_submission = self.map_submission(submission)
            return mapped_submission


    def get_top_post(self,rslash):
        subreddit = self.reddit.subreddit(rslash)
        print(subreddit.title)
        for submission in subreddit.top(limit=1):
            print(f'submission: {submission}')
            mapped_submission = self.map_submission(submission)
            print(f'mapped_submission {mapped_submission}')
            return mapped_submission


    def get_redditor_by_username(self,redditor_name):
        redditor_object = self.reddit.redditor(redditor_name)
        print(f'redditor_object : {redditor_object}')
        return self.map_redditor(redditor_object)
