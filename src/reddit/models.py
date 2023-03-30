from dataclasses import dataclass

@dataclass
class Submission:
    author: str
    author_flair_text: str
    clicked: bool
    comments: any
    created_utc: any
    distinguished: bool
    edited: bool
    id: int
    is_original_content: bool
    is_self: bool
    link_flair_text: str
    locked: bool
    name: str
    num_comments: int
    over_18: bool
    saved: bool
    score: int
    selftext: str
    spoiler: bool
    stickied: bool
    subreddit: any
    title: str
    upvote_ratio: float
    url: any

    def to_dict(self) -> dict:
        return {key: str(value) for key, value in self.__dict__.items()}


@dataclass
class Redditor:
    comment_karma: int
    comments: any
    submissions: any
    created_utc: any
    has_verified_email: bool
    icon_img: any
    id: str
    is_employee: bool
    is_friend: bool
    is_mod: bool
    is_gold: bool
    link_karma: int
    name: str
    subreddit: dict

    def to_dict(self) -> dict:
        return {key: str(value) for key, value in self.__dict__.items()}
