from django import http
from django.test.client import Client
import unittest 


class HttpTestCase(unittest.TestCase):
    Encoding = "utf-8"
    
    def setUp(self):
        self.client = Client()
    
    def assertStatusCode(self, response, statusCode):
        self.assertEqual(response.status_code, statusCode, str.format("Actual status code: {}", response.status_code))
        
    def assertOk(self, response):
        self.assertStatusCode(response, 200)
        
    # 500 Internal Server Error
    def assertInternalServerError(self, response):
        self.assertStatusCode(response, 500)
        
    # 405 Method Not Allowed    
    def assertMethodNotAllowed(self, response):
        self.assertStatusCode(response, 405)
        
    # 400 Bad Request    
    def assertBadRequest(self, response):
        self.assertStatusCode(response, 400)
    
    def assertContentType(self, response, contentType):
        self.assertEqual(response['Content-Type'], contentType, "Actual Content-Type: " + response['Content-Type'])
        
    def assertContentTypeJson(self, response):
        self.assertContentType(response, 'application/json; charset=utf-8')
