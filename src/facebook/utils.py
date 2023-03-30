import yaml
import facebook
from settings import Settings

class FacebookWrapper:
    def __init__(self):
        self.settings = Settings()
        self.graph = facebook.GraphAPI(access_token=self.settings.access_token)
        pass

    def get_user_id(self):
        user = self.graph.get_object(id="me", fields="about")
        return user
    
    def get_user_posts(self,id):
        posts = self.graph.get_object(id=id,fields='posts')
        return posts
    

if __name__ == '__main__':
    wrapper = FacebookWrapper()
    userid = wrapper.get_user_id()
    posts = wrapper.get_user_posts(userid)
    print(posts)