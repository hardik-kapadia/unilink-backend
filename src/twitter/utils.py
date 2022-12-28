import yaml
import tweepy

from src.twitter.settings import Settings

from src.twitter.models import Tweet, TwitterUser

import aiohttp


class TwitterWrapper:
    def __init__(self, filename: str = "twitter-oauth.yaml") -> None:

        settings = Settings()
        # temp_twitter_auth_data = {}

        # with open(filename, "r") as yamlfile:
        #     temp_twitter_auth_data = yaml.load(yamlfile, Loader=yaml.FullLoader)

        # self.twitter_auth_creds = temp_twitter_auth_data["TWITTER"]

        self.client = tweepy.Client(
            # access_token=self.twitter_auth_creds["ACCESS_TOKEN"],
            # access_token_secret=self.twitter_auth_creds["ACCESS_TOKEN_SECRET"],
            # consumer_key=self.twitter_auth_creds["COSUMER_KEY"],
            # consumer_secret=self.twitter_auth_creds["CONSUMER_SECRET"],
            # bearer_token=self.twitter_auth_creds["BEARER_TOKEN"],
            bearer_token=settings.bearer_token,
            wait_on_rate_limit=True,
        )

    async def get_access_token_and_refresh_token_from_authorization_code(
        authorization_code: str,
    ):
        async with aiohttp.ClientSession() as session:
            
            settings = Settings()

            headers = {"content-type": "application/x-www-form-urlencoded"}
            
            data = {
                "code": authorization_code,
                "client_id": settings.client_id,
                "grant_type": "authorization_code",
                "redirect_uri": settings.redirect_uri,
                "code_verifier": "challenge",
            }

            async with session.post(
                "https://api.twitter.com/2/oauth2/token", headers=headers, data=data
            ) as resp:
                print(resp.status)
                print(await resp.text())

        return "123"

    def get_user_data_from_username(self, screen_name: str):

        user_data = self.client.get_user(
            username=screen_name,
            user_fields=[
                "created_at",
                "location",
                "description",
                "pinned_tweet_id",
                "profile_image_url",
                "protected",
                "public_metrics",
                "verified",
            ],
        )

        user_id = user_data.data.id

        recent_tweets, has_posted_media = self.get_users_recent_tweets(user_id)

        return TwitterUser(
            user_data.data.id,
            user_data.data.username,
            user_data.data.name,
            user_data.data.created_at,
            user_data.data.description,
            user_data.data.pinned_tweet_id,
            user_data.data.profile_image_url,
            user_data.data.protected,
            user_data.data.public_metrics["followers_count"],
            user_data.data.public_metrics["following_count"],
            user_data.data.public_metrics["tweet_count"],
            user_data.data.verified,
            user_data.data.location,
            self.get_users_most_recent_tweet_time(screen_name),
            self.get_users_most_recent_mention(user_id),
            self.get_user_most_recent_like(user_id),
            recent_tweets,
            has_posted_media,
        )

    def get_users_most_recent_tweet_time(self, username):
        query = f"from:{username} -is:retweet"

        tweets = self.client.search_recent_tweets(
            query=query, tweet_fields=["created_at"], max_results=10
        )

        if tweets.data and len(tweets.data) > 0:
            return tweets.data[0].created_at

        return None

    def get_users_recent_tweets(self, user_id, max_tweets=100):

        tweets = self.client.get_users_tweets(
            user_id,
            tweet_fields=[
                "attachments",
                "created_at",
                "context_annotations",
                "in_reply_to_user_id",
                "possibly_sensitive",
                "public_metrics",
            ],
            max_results=max_tweets,
        )

        final_tweets = []

        if not tweets.data:
            return ([], 0)

        has_posted = False

        for tweet in tweets.data:

            tweet_context_annotations = []

            tweet_id = tweet.id
            tweet_text = tweet.text
            tweet_edit_history_tweet_ids = (
                True if tweet.edit_history_tweet_ids else None
            )
            tweet_temp_context_annotations = tweet.context_annotations
            tweet_attachments = True if tweet.attachments else False

            if not has_posted:
                if tweet_attachments:
                    has_posted = True

            for context in tweet_temp_context_annotations:

                entity_name = context["entity"]["name"]

                if not entity_name in tweet_context_annotations:
                    tweet_context_annotations.append(entity_name)

            tweet_created_at = tweet.created_at
            tweet_in_reply_to_user_id = True if tweet.in_reply_to_user_id else False
            tweet_possibly_sensitive = tweet.possibly_sensitive
            tweet_retweet_count = tweet.public_metrics["retweet_count"]
            tweet_reply_count = tweet.public_metrics["reply_count"]
            tweet_like_count = tweet.public_metrics["like_count"]
            tweet_quote_count = tweet.public_metrics["quote_count"]

            final_tweet = Tweet(
                tweet_id,
                tweet_text,
                tweet_edit_history_tweet_ids,
                tweet_context_annotations,
                tweet_attachments,
                tweet_created_at,
                tweet_in_reply_to_user_id,
                tweet_possibly_sensitive,
                tweet_retweet_count,
                tweet_reply_count,
                tweet_like_count,
                tweet_quote_count,
            )

            # print(final_tweet)

            final_tweets.append(final_tweet)

        return (final_tweets, has_posted)

    def get_users_most_recent_mention(self, id):

        tweets = self.client.get_users_mentions(
            id=id, tweet_fields=["created_at"], max_results=5
        )

        if tweets.data and len(tweets.data) > 0:
            return tweets.data[0].created_at

        return None

    def get_user_most_recent_like(self, id):

        tweets = self.client.get_liked_tweets(
            id=id, tweet_fields=["created_at"], max_results=5
        )

        if tweets.data and len(tweets.data) > 0:
            return tweets.data[0].created_at

        return None
