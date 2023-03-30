import yaml
import facebook
from settings import Settings
from pprint import pprint
class FacebookWrapper:
    def __init__(self):
        self.settings = Settings()
        self.graph = facebook.GraphAPI(access_token=self.settings.access_token)
        pass

    def get_user_id(self):
        user = self.graph.get_object(id="me", fields="about")
        return user
    
    def get_user_posts(self):
        res = self.graph.get_object(id='me',fields='posts')
        posts = res['posts']
        full_post = self.graph.get_object(id=posts['data'][0]['id'])
        print(full_post)
        return posts

    def get_user_details(self):
        res = self.graph.get_object(id='me',fields='name,birthday,email,gender,hometown,location')
        return res
        
