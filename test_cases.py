import requests
import json
import unittest
 
 
class TestStringMethods(unittest.TestCase):
     
    def test_get(self):
        self.assertEqual(requests.get("http://shufflecards.azurewebsites.net/deck").text, '{"deck":[]}')
     
    def test_no_deck(self):
        s = requests.Session()
        self.assertTrue(s.get("http://shufflecards.azurewebsites.net/deck").text == '{"deck":[]}')
        self.assertTrue(s.get("http://shufflecards.azurewebsites.net/deck/shuffle").text == '{"deck":[]}')
        self.assertTrue(s.get("http://shufflecards.azurewebsites.net/deck/pop").text == '{"deck":[],"dealt":[]}')
  
 
    def test_post_empty(self):
        s = requests.Session()
        s_json = []
        self.assertTrue(s.post("http://shufflecards.azurewebsites.net/deck", json=s_json).status_code == 400)
        self.assertTrue(s.get("http://shufflecards.azurewebsites.net/deck").text, '{"deck":[]}')
  
    def test_post_one_session(self):
        s = requests.Session()
        s_json = [1,2,3,4,5,6,7]
        s.post("http://shufflecards.azurewebsites.net/deck", json=s_json)
        s_get = json.loads(s.get("http://shufflecards.azurewebsites.net/deck").text)
        self.assertTrue(s_get['deck'] == s_json)
        self.assertTrue('dealt' not in s_get['deck'])        
         
 
#      
#      
    def test_shuffle_session(self):
        s = requests.Session()
        s_json = [1,2,3,4,5,6,7]
# 
# 
        self.assertTrue(s.post("http://shufflecards.azurewebsites.net/deck", json=s_json).text == '{"deck":[1,2,3,4,5,6,7]}')
        self.assertTrue(s.get("http://shufflecards.azurewebsites.net/deck").text == '{"deck":[1,2,3,4,5,6,7]}')
        #the length should still be the same
        json_shuffle = json.loads(s.get("http://shufflecards.azurewebsites.net/deck/shuffle").text)
        self.assertTrue(len(json_shuffle['deck']) == len(s_json),  msg="should not throw an error")
       
    def test_post_two_session(self):
        s = requests.Session()
        k = requests.Session()
        s_json = [1,2,3,4,5,6,7]
        k_json = [8,9,10,11,12,13,14]
        s.post("http://shufflecards.azurewebsites.net/deck", json=s_json).text
        k.post("http://shufflecards.azurewebsites.net/deck", json=k_json).text
   
        self.assertTrue(s.get("http://shufflecards.azurewebsites.net/deck").text == '{"deck":[1,2,3,4,5,6,7]}')
        self.assertTrue(k.get("http://shufflecards.azurewebsites.net/deck").text == '{"deck":[8,9,10,11,12,13,14]}')
    #     #the length should still be the same
        self.assertTrue(len(s.get("http://shufflecards.azurewebsites.net/deck/shuffle").text) == len('{"deck":[1,2,3,4,5,6,7]}'),  msg="should not throw an error")
        self.assertTrue(len(k.get("http://shufflecards.azurewebsites.net/deck/shuffle").text) == len('{"deck":[10,13,9,14,12,8,11]}'), msg="should not throw an error")
  
  
    def test_whole_flow(self):
        s = requests.Session()
        k = requests.Session()
        s_json = [1,2,3,4,5,6,7]
        k_json = [8,9,10,11,12,13,14]
        s.post("http://shufflecards.azurewebsites.net/deck", json=s_json)
        k.post("http://shufflecards.azurewebsites.net/deck", json=k_json)
         
        self.assertTrue(s.get("http://shufflecards.azurewebsites.net/deck").text == '{"deck":[1,2,3,4,5,6,7]}')
        self.assertTrue(k.get("http://shufflecards.azurewebsites.net/deck").text == '{"deck":[8,9,10,11,12,13,14]}')
          
    #     #the length should still be the same
        self.assertTrue(len(s.get("http://shufflecards.azurewebsites.net/deck/shuffle").text) == len('{"deck":[1,2,3,4,5,6,7]}'),  msg="should not throw an error")
        self.assertTrue(len(k.get("http://shufflecards.azurewebsites.net/deck/shuffle").text) == len('{"deck":[10,13,9,14,12,8,11]}'), msg="should not throw an error")
         
        s_pop = json.loads(s.get("http://shufflecards.azurewebsites.net/deck/pop").text)
        k_pop = json.loads(k.get("http://shufflecards.azurewebsites.net/deck/pop").text)
    #     #the length should still be one less
        self.assertTrue(len(s_pop['dealt'])>0, msg="should not throw an error")
        self.assertTrue(len(k_pop['dealt'])>0, msg="should not throw an error")
     
#         
    def test_whole_flow_one_session(self):
        s = requests.Session()
        s_json = [1,2,3,4]
        s.post("http://shufflecards.azurewebsites.net/deck", json=s_json)
        self.assertTrue(s.get("http://shufflecards.azurewebsites.net/deck").text == '{"deck":[1,2,3,4]}')
         
        #first pop
        s_pop = json.loads(s.get("http://shufflecards.azurewebsites.net/deck/pop").text)
        s_get = json.loads(s.get("http://shufflecards.azurewebsites.net/deck").text)
        self.assertTrue(len(s_pop['dealt']) == len(s_get['dealt']) > 0,  msg="should not throw an error")
         
        s_get = json.loads(s.get("http://shufflecards.azurewebsites.net/deck").text)
        self.assertTrue(len(s_get['deck']) == len(s_json)-1)
        self.assertTrue(len(s_get['dealt']) == 1)
 
    #     #second pop
        s_pop = json.loads(s.get("http://shufflecards.azurewebsites.net/deck/pop").text)
        s_get = json.loads(s.get("http://shufflecards.azurewebsites.net/deck").text)
        self.assertTrue(len(s_pop['dealt']) == len(s_get['dealt']) == 2,  msg="should not throw an error")
         
  
    #     #third pop
        s_pop = json.loads(s.get("http://shufflecards.azurewebsites.net/deck/pop").text)
        s_get = json.loads(s.get("http://shufflecards.azurewebsites.net/deck").text)
        self.assertTrue(len(s_pop['dealt']) == len(s_get['dealt']) == 3,  msg="should not throw an error")
         
  
    #     #last pop -- no deck, only dealt
        s_pop = json.loads(s.get("http://shufflecards.azurewebsites.net/deck/pop").text)
        s_get = json.loads(s.get("http://shufflecards.azurewebsites.net/deck").text)
        self.assertTrue(len(s_pop['dealt']) == len(s_get['dealt']) == 4,  msg="should not throw an error")
        self.assertTrue(len(s_pop['deck']) == len(s_get['deck']) == 0)
        
 
 
 
unittest.main()