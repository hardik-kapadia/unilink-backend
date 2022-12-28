from dataclasses import dataclass
from datetime import datetime
import json

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

@dataclass(init=True, repr=True, frozen=True)
class TwitterUser:

    id_: str
    username: str
    name: str
    account_creation_date: datetime
    description: str
    pinned_tweet: str
    profile_image_url: str
    is_protected: bool
    followers_count: int
    following_count: int
    tweet_count: int
    is_verified: bool
    location: str
    most_recent_tweet_time: datetime
    most_recent_mention: datetime
    most_recent_like: datetime
    recent_tweets: list[Tweet]
    has_posted_media: bool

    def __post_init__(self):
        object.__setattr__(self, 'has_pinned_tweet', True if self.pinned_tweet else False)
        object.__setattr__(self,'self.is_profile_pic_default', "default_profile_images" in str(self.profile_image_url).lower())

    def toJson(self):
        return json.dumps(self, default=myconverter)
    
def myconverter(o):
    if isinstance(o, datetime):
        return o.__str__()
    
    return o.__dict__

