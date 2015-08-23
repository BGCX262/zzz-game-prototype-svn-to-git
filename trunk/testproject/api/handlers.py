from piston.handler import BaseHandler
from piston.utils import rc
from django.core import serializers
from testproject.viewmodels import Account
from testproject.utils import ObjectToDict
from django.test.client import Client  
import logging, json

logger = logging.getLogger('logger')


class UserHandler(BaseHandler):
    allowed_methods = ('GET', 'POST')
    anonimous = True
    
    def read(self, request, user_id = None):
        if user_id:
            a = Account()
            a.VkAccountId = "2312tgi1929"
            a.BonusPoints = 12
            a.Experiense = 0
            a.Level = 0
            a.CoinsNumber = 0
            a.Rubies = 0
            a.Energy = 0
            
            return ObjectToDict(a)     
        else:
            return rc.BAD_REQUEST
        
    def create(self, request, user_id = None):
        if user_id:
            # update user data            
            return rc.ALL_OK     
        else:
            return rc.BAD_REQUEST
        
class UserCreateHandler(BaseHandler):
    allowed_methods = ('POST')
    anonimous = True
    
    def create(self, request):
        if "vkaccountid" in request.POST: 
            accountId = request.POST["vkaccountid"]
            if accountId:
                # create new user, return user data
                a = Account()
                a.VkAccountId = accountId
                a.BonusPoints = 12
                a.Experiense = 0
                a.Level = 0
                a.CoinsNumber = 0
                a.Rubies = 0
                a.Energy = 0
                    
                return ObjectToDict(a)
            
        return rc.BAD_REQUEST 
    
    def update(self, request):        
        pass