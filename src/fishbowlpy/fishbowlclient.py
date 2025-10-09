from .fishbowlloginmanager import FishBowlLoginManager
from .fishbowlapi import FishBowlAPI
from .drivertype import DriverType
from .utils.logger import getLogger

LOGGER = getLogger(__name__)


class FishBowlClient:
    """This class is used to interact with the FishBowlApp. This class provides the interface with the ability to
    configure the required configuration like driver paths, session key etc.
    
    :param login_manager(FishBowlLoginManager): An instance of the FishBowlLoginManager class.
    :param fishbowl_api(FishBowlAPI): An instance of the FishBowlAPI class.
    :param driver_type(DriverType): An instance of the DriverType class.
    :param **kwargs: Any other keyword arguments.
    
    :return: None
    
    Basic Usage:
    >>> from fishbowlpy.fishbowlclient import FishBowlClient
    >>> client = FishBowlClient()
    >>> client.get_bowls_names() 
    >>> client.get_posts(bowl_name='fishbowl')
    
    :copyright: (c) 2024 MIT Licensed
    """
    def __init__(self, **kwargs) -> None:
        """This class is used to interact with the FishBowlApp. This class provides the interface with the ability to
        configure the required configuration like driver paths, session key etc.
        
        :param login_manager(FishBowlLoginManager): An instance of the FishBowlLoginManager class.
        :param fishbowl_api(FishBowlAPI): An instance of the FishBowlAPI class.
        :param driver_type(DriverType): An instance of the DriverType class.
        :param driver_path(str): A path to the webdriver executable
        :param **kwargs: Any other keyword arguments.
        
        :return: None
        
        Basic Usage:
        >>> from fishbowlpy.fishbowlclient import FishBowlClient
        >>> client = FishBowlClient()
        >>> client.get_bowls_names() 
        >>> client.get_posts(bowl_name='fishbowl')
        
        :copyright: (c) 2024 MIT Licensed
        """
        
        self.__login_manager = kwargs['login_manager'] if 'login_manager' in kwargs else FishBowlLoginManager(**kwargs)

        self.__fishbowl_api = kwargs['fishbowl_api'] if 'fishbowl_api' in kwargs else FishBowlAPI(session_key=self.__login_manager.get_session_key())
    
    def refresh_session(self):
        """Refresh the session token and update the API client"""
        try:
            LOGGER.debug("Refreshing session...")
            
            # Refresh the token using login manager
            success = self.__login_manager.refresh_token()
            
            if success:
                # Update the API client with new session key
                new_session_key = self.__login_manager.get_session_key()
                self.__fishbowl_api.set_session_key(new_session_key)
                LOGGER.info("Session refreshed successfully")
            else:
                LOGGER.warning("Session refresh failed")
                
            return success
            
        except Exception as e:
            LOGGER.error(f"Error during session refresh: {e}")
            return False

    def _ensure_valid_session(self):
        """Check if session is valid and refresh if needed"""
        if hasattr(self.__login_manager, 'is_token_expired'):
            if self.__login_manager.is_token_expired():
                LOGGER.debug("Session expired or about to expire, refreshing...")
                return self.refresh_session()
        return True

    def get_bowls_names(self):
        """This is a placeholder method that will be used to get the names of the subscribed bowls"""
        # Hard coded for now
        # It shoould use the bs4 to parse html and get the proper names
        return ['tech-india', 'job-referrals']
    
    def get_posts(self, bowl_name:str):
        """This method returns the posts in the `bowl_name` in json format.
        
        :param bowl_name: Bowl name from where to get the posts.
        
        :return: Posts in json format.
        """
        self._ensure_valid_session()  # Session validation before API call
        return self.__fishbowl_api.get_posts(bowl_name=bowl_name)
    
    def get_post_comments(self, post_id: str, **kwargs):
        """This method returns the comments for a given post_id in json format.
        
        :param post_id: Post ID from where to get the comments.
        :param sort: Sort order for comments (default: 'byDate', options: 'byDate', 'byPopularity')
        :param start: Starting index for pagination (default: 0)
        :param count: Number of comments to return (default: 20)
        :param **kwargs: Additional parameters for flexible configuration
        
        :return: Comments in json format.
        
        Basic Usage:
        >>> from fishbowlpy.fishbowlclient import FishBowlClient
        >>> client = FishBowlClient()
        >>> comments = client.get_post_comments(post_id='12345')
        >>> comments = client.get_post_comments(post_id='12345', count=50, sort='byPopularity')
        """
        self._ensure_valid_session()  # Session validation before API call
        return self.__fishbowl_api.get_post_comments(post_id=post_id, **kwargs)