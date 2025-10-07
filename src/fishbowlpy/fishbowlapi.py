import requests
from .utils.logger import getLogger
from .urlmanager import FishbowlURLManager

LOGGER = getLogger(__name__)

class FishBowlAPI:
    
    def __init__(self, session_key: str):
        LOGGER.debug("Creating fishbowlapi object")
        self.__session_key = session_key or None 
        self.__url_manager = FishbowlURLManager()

    def get_posts(self, bowl_name:str, sort:str=None, start:int=None, count:int=None):
        kwargs = {k:v for k,v in locals().items() if v is not None and k not in ['self', 'bowl_name']}
        bowl_details = self.get_bowl_details(bowl_name)
        bowl_id = bowl_details['_id']
        LOGGER.debug(bowl_id)
        posts = self.get_posts_by_bowl_id(bowl_id, **kwargs)
        return posts


    def get_bowl_details(self, bowl_name):
        url = self.__url_manager.get_bowl_details_url(bowl_name)
        headers = self.__url_manager.get_headers(self.__session_key)
        data = requests.get(url = url, headers = headers, verify = True, timeout = 60)
        return dict(data.json())

    def get_posts_by_bowl_id(self, bowl_id, sort:str=None, start:int=None, count:int=None):
        kwargs = {k:v for k,v in locals().items() if v is not None and k not in ['self', 'bowl_id']}
        url = self.__url_manager.get_posts_url(bowl_id, **kwargs)
        headers = self.__url_manager.get_headers(self.__session_key)
        LOGGER.debug(url)
        data = requests.get(url = url, headers = headers, verify = True, timeout = 60)
        LOGGER.debug(len(dict(data.json())))
        return dict(data.json())

    def get_post_comments(self, post_id: str, sort: str = 'byDate', start: int = 0, count: int = 20, **kwargs):
        """Get comments for a specific post.
        
        :param post_id: The ID of the post to fetch comments for
        :param sort: Sort order for comments (default: 'byDate', options: 'byDate', 'byPopularity')
        :param start: Starting index for pagination (default: 0)
        :param count: Number of comments to return (default: 20, max: 100)
        :param **kwargs: Additional query parameters
        :return: Comments data in JSON format
        
        Basic Usage:
        >>> api = FishBowlAPI(session_key='your_key')
        >>> comments = api.get_post_comments(post_id='12345')
        >>> comments = api.get_post_comments(post_id='12345', count=50, sort='byPopularity')
        """
        params = {k: v for k, v in locals().items() if v is not None and k not in ['self', 'post_id', 'kwargs']}
        params.update(kwargs)
        
        url = self.__url_manager.get_comments_url(post_id, **params)
        headers = self.__url_manager.get_headers(self.__session_key)
        
        LOGGER.debug(f"Fetching comments for post: {post_id}")
        LOGGER.debug(f"URL: {url}")
        
        data = requests.get(url=url, headers=headers, verify=True, timeout=60)
        result = dict(data.json())
        
        LOGGER.debug(f"Retrieved comments response")
        return result