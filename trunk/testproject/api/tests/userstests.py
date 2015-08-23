import unittest, json
from testproject.test.utils import HttpTestCase
from django.test.client import Client

class UserCreateHandlerTestCase(HttpTestCase):
    
    def test_GET_user(self):
        response = self.client.get("/api/user/")
        self.assertMethodNotAllowed(response)
    
    def test_PUT_user(self):
        data = {"vkaccountid": "1234567890"}
        response = self.client.put("/api/user/", data)
        self.assertMethodNotAllowed(response)
        
    def test_DELETE_user(self):
        response = self.client.delete("/api/user/")
        self.assertMethodNotAllowed(response)        
        
    def test_POST_user(self):
        data = {"vkaccountid": "1234567890"}        
        response = self.client.post("/api/user/", data)
                
        self.assertOk(response)
        self.assertContentTypeJson(response)
        
        content = json.loads(response.content, self.Encoding)

        self.assertIsNotNone(content)
        self.assertEquals(len(content.keys()), 7)        
        self.assertItemsEqual(content.keys(), ("rubies", "coinsnumber", "bonuspoints", "energy", "level", "vkaccountid", "experiense",))
        self.assertEqual(content["vkaccountid"], "1234567890")
        
    def test_POST_user_bad_request(self):
        response = self.client.post("/api/user/")                
        self.assertBadRequest(response)        

class UserHandlerTestCase(HttpTestCase):
    def test_DELETE_user(self):
        response = self.client.delete("/api/user/12/")
        self.assertMethodNotAllowed(response)
        
    def test_PUT_user(self):
        response = self.client.put("/api/user/12/")
        self.assertMethodNotAllowed(response)        
            
    def test_GET_user_by_id(self):
        response = self.client.get("/api/user/12/")
        self.assertOk(response)
        self.assertContentTypeJson(response)
        
        content = json.loads(response.content, self.Encoding)

        self.assertIsNotNone(content)
        self.assertEquals(len(content.keys()), 7)        
        self.assertItemsEqual(content.keys(), ("rubies", "coinsnumber", "bonuspoints", "energy", "level", "vkaccountid", "experiense",))
        
    def test_POST_user_update(self):
        data = dict()
        data["rubies"] = 8
        data["level"] = 5        
        response = self.client.post("/api/user/12/", data)        
        self.assertOk(response)       
        