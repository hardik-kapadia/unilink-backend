from dataclasses import dataclass

# @dataclass
# class Submission:
#     author: str
#     author_flair_text: str
#     clicked: bool
#     comments: any
#     created_utc: any
#     distinguished: bool
#     edited: bool
#     id: int
#     is_original_content: bool
#     is_self: bool
#     link_flair_text: str
#     locked: bool
#     name: str
#     num_comments: int
#     over_18: bool
#     saved: bool
#     score: int
#     selftext: str
#     spoiler: bool
#     stickied: bool
#     subreddit: any
#     title: str
#     upvote_ratio: float
#     url: any

#     def to_dict(self) -> dict:
#         return {key: str(value) for key, value in self.__dict__.items()}


# @dataclass
# class Redditor:
#     comment_karma: int
#     comments: any
#     submissions: any
#     created_utc: any
#     has_verified_email: bool
#     icon_img: any
#     id: str
#     is_employee: bool
#     is_friend: bool
#     is_mod: bool
#     is_gold: bool
#     link_karma: int
#     name: str
#     subreddit: dict

#     def to_dict(self) -> dict:
#         return {key: str(value) for key, value in self.__dict__.items()}
    

class Submission:
    def __init__(self,
                    author,
                    author_flair_text,
                    clicked,
                    comments,
                    created_utc,
                    distinguished,
                    edited,
                    id,
                    is_original_content,
                    is_self,
                    link_flair_text,
                    locked,
                    name,
                    num_comments,
                    over_18,
                    saved,
                    score,
                    selftext,
                    spoiler,
                    stickied,
                    subreddit,
                    title,
                    upvote_ratio,
                    url
                ):
        self.author = str(author)
        self.author_flair_text = author_flair_text
        self.clicked = clicked
        self.comments = str(comments)
        self.created_utc = created_utc
        self.distinguished = distinguished
        self.edited = edited
        self.id = id
        self.is_original_content = is_original_content 
        self.is_self = is_self
        self.link_flair_text = link_flair_text
        self.locked = locked
        self.name = name
        self.num_comments = num_comments
        self.over_18 = over_18
        self.saved = saved
        self.score = score
        self.selftext = selftext
        self.spoiler = spoiler
        self.stickied = stickied
        self.subreddit = str(subreddit)
        self.title = title
        self.upvote_ratio =upvote_ratio 
        self.url = url

    
class Redditor:
    def __init__(self,
                comment_karma,
                comments,
                submissions,
                created_utc,
                has_verified_email,
                icon_img,
                id,
                is_employee,
                is_friend,
                is_mod,
                is_gold,
                link_karma,
                name,
                subreddit
                ):
                self.comment_karma = str(comment_karma)
                self.comments = str(comments)
                self.submissions = str(submissions)
                self.created_utc = created_utc
                self.has_verified_email = has_verified_email
                self.icon_img = icon_img
                self.id = id
                self.is_employee =is_employee 
                self.is_friend = is_friend
                self.is_mod = is_mod
                self.is_gold = is_gold
                self.link_karma = link_karma
                self.name = str(name)
                self.subreddit = str(subreddit)
        