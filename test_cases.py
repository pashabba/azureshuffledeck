import requests
import json
import unittest
 
 
class TestStringMethods(unittest.TestCase):
     
    def test_get(self):
        self.assertEqual(requests.get("http://shuffledeck.azurewebsites.net/deck").text, '{"deck":[]}')
     
    def test_no_deck(self):
        s = requests.Session()
        self.assertTrue(s.get("http://shuffledeck.azurewebsites.net/deck").text == '{"deck":[]}')
        self.assertTrue(s.get("http://shuffledeck.azurewebsites.net/deck/shuffle").text == '{"deck":[]}')
        self.assertTrue(s.get("http://shuffledeck.azurewebsites.net/deck/pop").text == '{"last card popped":[]}')
  
 
    def test_post_empty(self):
        s = requests.Session()
        s_json = []
        self.assertTrue(s.post("http://shuffledeck.azurewebsites.net/deck", json=s_json).status_code == 400)
        self.assertTrue(s.get("http://shuffledeck.azurewebsites.net/deck").text, '{"deck":[]}')
  
    def test_post_one_session(self):
        s = requests.Session()
        s_json = [1,2,3,4,5,6,7]
        s.post("http://shuffledeck.azurewebsites.net/deck", json=s_json)
        s_get = json.loads(s.get("http://shuffledeck.azurewebsites.net/deck").text)
        self.assertTrue(s_get['deck'] == s_json)
        self.assertTrue('dealt' not in s_get.keys())        
         
 
     
     
    def test_shuffle_session(self):
        s = requests.Session()
        s_json = [1,2,3,4,5,6,7]
# 
# 
        self.assertTrue(s.post("http://shuffledeck.azurewebsites.net/deck", json=s_json).text == '{"deck":[1,2,3,4,5,6,7]}')
        self.assertTrue(s.get("http://shuffledeck.azurewebsites.net/deck").text == '{"deck":[1,2,3,4,5,6,7]}')
        #the length should still be the same
        json_shuffle = json.loads(s.get("http://shuffledeck.azurewebsites.net/deck/shuffle").text)
        self.assertTrue(len(json_shuffle['deck']) == len(s_json),  msg="should not throw an error")
       
    def test_post_two_session(self):
        s = requests.Session()
        k = requests.Session()
        s_json = [1,2,3,4,5,6,7]
        k_json = [8,9,10,11,12,13,14]
        s.post("http://shuffledeck.azurewebsites.net/deck", json=s_json).text
        k.post("http://shuffledeck.azurewebsites.net/deck", json=k_json).text
   
        self.assertTrue(s.get("http://shuffledeck.azurewebsites.net/deck").text == '{"deck":[1,2,3,4,5,6,7]}')
        self.assertTrue(k.get("http://shuffledeck.azurewebsites.net/deck").text == '{"deck":[8,9,10,11,12,13,14]}')
    #     #the length should still be the same
        self.assertTrue(len(s.get("http://shuffledeck.azurewebsites.net/deck/shuffle").text) == len('{"deck":[1,2,3,4,5,6,7]}'),  msg="should not throw an error")
        self.assertTrue(len(k.get("http://shuffledeck.azurewebsites.net/deck/shuffle").text) == len('{"deck":[10,13,9,14,12,8,11]}'), msg="should not throw an error")
  
  
    def test_whole_flow(self):
        s = requests.Session()
        k = requests.Session()
        s_json = [1,2,3,4,5,6,7]
        k_json = [8,9,10,11,12,13,14]
        s.post("http://shuffledeck.azurewebsites.net/deck", json=s_json)
        k.post("http://shuffledeck.azurewebsites.net/deck", json=k_json)
         
        self.assertTrue(s.get("http://shuffledeck.azurewebsites.net/deck").text == '{"deck":[1,2,3,4,5,6,7]}')
        self.assertTrue(k.get("http://shuffledeck.azurewebsites.net/deck").text == '{"deck":[8,9,10,11,12,13,14]}')
          
    #     #the length should still be the same
        self.assertTrue(len(s.get("http://shuffledeck.azurewebsites.net/deck/shuffle").text) == len('{"deck":[1,2,3,4,5,6,7]}'),  msg="should not throw an error")
        self.assertTrue(len(k.get("http://shuffledeck.azurewebsites.net/deck/shuffle").text) == len('{"deck":[10,13,9,14,12,8,11]}'), msg="should not throw an error")
         
        s_pop = json.loads(s.get("http://shuffledeck.azurewebsites.net/deck/pop").text)
        k_pop = json.loads(k.get("http://shuffledeck.azurewebsites.net/deck/pop").text)
#     #     #the length should still be one less

        self.assertTrue(s_pop['last card popped'], msg="should not throw an error")
        self.assertTrue(k_pop['last card popped'], msg="should not throw an error")
     
# #         
    def test_whole_flow_one_session(self):
        s = requests.Session()
        s_json = [1,2,3,4]
        s.post("http://shuffledeck.azurewebsites.net/deck", json=s_json)
        self.assertTrue(s.get("http://shuffledeck.azurewebsites.net/deck").text == '{"deck":[1,2,3,4]}')
         
    #     #first pop
        s_pop = json.loads(s.get("http://shuffledeck.azurewebsites.net/deck/pop").text)
        s_get = json.loads(s.get("http://shuffledeck.azurewebsites.net/deck").text)
        self.assertTrue(s_pop['last card popped'] not in s_get['deck'],  msg="should not throw an error")
        self.assertTrue(s_pop['last card popped'] in s_get['dealt'],  msg="should not throw an error")
         
        self.assertTrue(len(s_get['deck']) == len(s_json)-1)
 
    # #     #second pop
        s_pop = json.loads(s.get("http://shuffledeck.azurewebsites.net/deck/pop").text)
        s_get = json.loads(s.get("http://shuffledeck.azurewebsites.net/deck").text)
        self.assertTrue(s_pop['last card popped'] not in s_get['deck'],  msg="should not throw an error")
        self.assertTrue(s_pop['last card popped'] in s_get['dealt'],  msg="should not throw an error")
         
        self.assertTrue(len(s_get['deck']) == len(s_json)-2)         
  
    # #     #third pop
        s_pop = json.loads(s.get("http://shuffledeck.azurewebsites.net/deck/pop").text)
        s_get = json.loads(s.get("http://shuffledeck.azurewebsites.net/deck").text)
        self.assertTrue(s_pop['last card popped'] not in s_get['deck'],  msg="should not throw an error")
        self.assertTrue(s_pop['last card popped'] in s_get['dealt'],  msg="should not throw an error")
         
        self.assertTrue(len(s_get['deck']) == len(s_json)-3)
         
  
    # #     #last pop -- no deck, only dealt
        s_pop = json.loads(s.get("http://shuffledeck.azurewebsites.net/deck/pop").text)
        s_get = json.loads(s.get("http://shuffledeck.azurewebsites.net/deck").text)
        self.assertTrue(s_pop['last card popped'] not in s_get['deck'],  msg="should not throw an error")
        self.assertTrue(s_pop['last card popped'] in s_get['dealt'],  msg="should not throw an error")
         
        self.assertTrue(len(s_get['deck']) == len(s_json)-4)
        
    def test_delete(self):
        s = requests.Session()
        s_json = [1,2,3,4]
        s.post("http://shuffledeck.azurewebsites.net/deck", json=s_json)
        self.assertTrue(s.get("http://shuffledeck.azurewebsites.net/deck").text == '{"deck":[1,2,3,4]}')
        self.assertTrue(s.delete("http://shuffledeck.azurewebsites.net/deck").text == '{"deck":[],"dealt":[]}')
        self.assertTrue(s.get("http://shuffledeck.azurewebsites.net/deck").text == '{"deck":[]}')
        
    def test_two_session_delete(self):
        # first session data deleted, second one still exists
        s = requests.Session()
        k = requests.Session()
        s_json = [1,2,3,4]
        k_json = [5,6,7,8]
        
        s.post("http://shuffledeck.azurewebsites.net/deck", json=s_json)
        k.post("http://shuffledeck.azurewebsites.net/deck", json=k_json)

        self.assertTrue(s.get("http://shuffledeck.azurewebsites.net/deck").text == '{"deck":[1,2,3,4]}')
        self.assertTrue(s.delete("http://shuffledeck.azurewebsites.net/deck").text == '{"deck":[],"dealt":[]}')
        self.assertTrue(s.get("http://shuffledeck.azurewebsites.net/deck").text == '{"deck":[]}')
        
        self.assertTrue(k.get("http://shuffledeck.azurewebsites.net/deck").text == '{"deck":[5,6,7,8]}')

        
        
        
 
 
 
unittest.main()