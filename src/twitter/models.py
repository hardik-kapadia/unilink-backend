from dataclasses import dataclass
from datetime import datetime


class TwitterUser:
    def __init__(
        self,
        id_,
        username,
        name,
        account_creation_date,
        description,
        pinned_tweet,
        profile_image_url,
        is_protected,
        followers_count,
        following_count,
        tweet_count,
        is_verified,
        location,
        most_recent_tweet_time,
        most_recent_mention,
        most_recent_like,
        recent_tweets,
        has_posted_media,
    ) -> None:

        self.id_ = id_
        self.username = username
        self.name = name
        self.account_creation_date = account_creation_date
        self.location = location
        self.description = description
        self.description_length = len(description) if description else 0
        self.has_pinned_tweet = True if pinned_tweet else False
        self.profile_image_url = profile_image_url
        self.is_profile_pic_default = (
            "default_profile_images" in str(self.profile_image_url).lower()
        )
        self.is_protected = is_protected
        self.followers_count = followers_count
        self.following_count = following_count
        self.tweet_count = tweet_count
        self.is_verified = is_verified
        self.most_recent_tweet_time = most_recent_tweet_time
        self.most_recent_mention = most_recent_mention
        self.most_recent_like = most_recent_like
        self.recent_tweets = recent_tweets
        self.has_posted_media = has_posted_media

    def __str__(self) -> str:
        return f"""
        id: {self.id_},
        username: {self.username},
        name: {self.name},
        account_creation_date: {self.account_creation_date},
        location: {self.location},
        description: {self.description},
        description_length: {self.description_length},
        has_pinned_tweet: {self.has_pinned_tweet},
        profile_image_url: {self.profile_image_url},
        is_protected: {self.is_protected},
        followers_count: {self.followers_count},
        following_count: {self.following_count},
        tweet_count: {self.tweet_count},
        is_verified: {self.is_verified},
        most_recent_tweet_time: {self.most_recent_tweet_time},
        most_recent mention: {self.most_recent_mention},
        most_recent_like: {self.most_recent_like}
        recent_tweets: {self.recent_tweets}
        is_profile_pic_default: {self.is_profile_pic_default}
        self.has_posted_media = {self.has_posted_media}
    """


@dataclass(init=True, repr=True, frozen=True)
class Tweet:

    id_: str
    text: str
    edit_history_tweet_ids: bool
    context_annotations: list
    attachments: bool
    created_at: datetime
    in_reply_to_user_id: bool
    possibly_sensitive: bool
    retweet_count: int
    reply_count: int
    like_count: int
    quote_count: int
