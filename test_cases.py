import requests
import json
import unittest


class TestStringMethods(unittest.TestCase):
    
    def test_get(self):
        self.assertEqual(requests.get("https://shufflecards.azurewebsites.net/api/getDeck").text, '[]')
    
    # def test_no_deck(self):
    #     s = requests.Session()
    #     self.assertTrue(s.get("http://localhost:5000/getDeck").text == '[]')
    #     self.assertTrue(s.get("http://localhost:5000/shuffleCard").text == '[]')
    #     self.assertTrue(s.get("http://localhost:5000/popCard").text == '[]')


    # def test_post_empty(self):
    #     s = requests.Session()
    #     s_json = []
    #     self.assertTrue(s.post("http://localhost:5000/createDeck", json=s_json).text == "[]")
    #     self.assertTrue(s.get("http://localhost:5000/getDeck").text, '[]')

    # def test_post_one_session(self):
    #     s = requests.Session()
    #     s_json = [1,2,3,4,5,6,7]
    #     s.post("http://localhost:5000/createDeck", json=s_json)
    #     print s.get("http://localhost:5000/getDeck").text
    #     self.assertTrue(s.get("http://localhost:5000/getDeck").text == "[1,2,3,4,5,6,7]")
    
    
    # def test_shuffle_session(self):
    #     s = requests.Session()
    #     s_json = [1,2,3,4,5,6,7]
    #     self.assertTrue(s.post("http://localhost:5000/createDeck", json=s_json).text == "[1,2,3,4,5,6,7]")
    #     self.assertTrue(s.get("http://localhost:5000/getDeck").text == "[1,2,3,4,5,6,7]")
    #     #the length should still be the same
    #     self.assertTrue(len(s.get("http://localhost:5000/shuffleCard").text) == len('[1,2,3,4,5,6,7]'),  msg="should not throw an error")
    
    # def test_post_two_session(self):
    #     s = requests.Session()
    #     k = requests.Session()
    #     s_json = [1,2,3,4,5,6,7]
    #     k_json = [8,9,10,11,12,13,14]
    #     s.post("http://localhost:5000/createDeck", json=s_json)
    #     k.post("http://localhost:5000/createDeck", json=k_json)

    #     self.assertTrue(s.get("http://localhost:5000/getDeck").text == "[1,2,3,4,5,6,7]")
    #     self.assertTrue(k.get("http://localhost:5000/getDeck").text == "[8,9,10,11,12,13,14]")
        
    #     #the length should still be the same
    #     self.assertTrue(len(s.get("http://localhost:5000/shuffleCard").text) == len('[1,2,3,4,5,6,7]'),  msg="should not throw an error")
    #     self.assertTrue(len(k.get("http://localhost:5000/shuffleCard").text) == len('[8,9,10,11,12,13,14]'), msg="should not throw an error")


    # def test_whole_flow(self):
    #     s = requests.Session()
    #     k = requests.Session()
    #     s_json = [1,2,3,4,5,6,7]
    #     k_json = [8,9,10,11,12,13,14]
    #     s.post("http://localhost:5000/createDeck", json=s_json)
    #     k.post("http://localhost:5000/createDeck", json=k_json)

    #     self.assertTrue(s.get("http://localhost:5000/getDeck").text == '[1,2,3,4,5,6,7]')
    #     self.assertTrue(k.get("http://localhost:5000/getDeck").text == '[8,9,10,11,12,13,14]')
        
    #     #the length should still be the same
    #     self.assertTrue(len(s.get("http://localhost:5000/shuffleCard").text) == len('[1,2,3,4,5,6,7]'),  msg="should not throw an error")
    #     self.assertTrue(len(k.get("http://localhost:5000/shuffleCard").text) == len('[8,9,10,11,12,13,14]'), msg="should not throw an error")

    #     #the length should still be one less
    #     self.assertTrue(len(s.get("http://localhost:5000/popCard").text) >= 3,  msg="should not throw an error") # "[]"
    #     self.assertTrue(len(k.get("http://localhost:5000/popCard").text) >= 3, msg="should not throw an error")

    # def test_post_two_session_fail(self):
    #     s = requests.Session()
    #     k = requests.Session()
    #     s_json = [1,2,3,4,5,6,7]
    #     k_json = [8,9,10,11,12,13,14]
    #     s.post("http://localhost:5000/createDeck", json=s_json)
    #     k.post("http://localhost:5000/createDeck", json=k_json)

    #     self.assertTrue(s.get("http://localhost:5000/getDeck").text == '[1,2,3,4,5,6,7]')
    #     self.assertTrue(k.get("http://localhost:5000/getDeck").text == '[8,9,10,11,12,13,14]')
    #     print s.get("http://localhost:5000/shuffleCard").text
    #     print k.get("http://localhost:5000/shuffleCard").text


    #     self.assertTrue(s.get("http://localhost:5000/shuffleCard").text != '[1,2,3,4,5,6,7]',  msg="Cards shuffled, so most likely it will throw an error")
    #     self.assertTrue(k.get("http://localhost:5000/shuffleCard").text != '[8,9,10,11,12,13,14]', msg="Cards shuffled, so most likely it will throw an error")

    # def test_whole_flow_one_session(self):
    #     s = requests.Session()
    #     s_json = [1,2,3,4]
    #     s.post("http://localhost:5000/createDeck", json=s_json)
    #     self.assertTrue(s.get("http://localhost:5000/getDeck").text == '[1,2,3,4]')
    #     #the length should still be the same
    #     self.assertTrue(len(s.get("http://localhost:5000/shuffleCard").text) == len('[1,2,3,4]'),  msg="should not throw an error")
        
        
    #     #first pop
    #     self.assertTrue(len(s.get("http://localhost:5000/popCard").text) >= 3,  msg="should not throw an error") # "[]"
    #     json_get = json.loads(s.get("http://localhost:5000/getDeck").text)
    #     self.assertTrue(json_get['dealt'] != [],  msg="should not throw an error")
    #     self.assertTrue(json_get['deck'] != [],  msg="should not throw an error")
        
    #     #second pop
    #     self.assertTrue(len(s.get("http://localhost:5000/popCard").text) >= 3,  msg="should not throw an error") # "[]"
    #     json_get = json.loads(s.get("http://localhost:5000/getDeck").text)
    #     self.assertTrue(json_get['dealt'] != [],  msg="should not throw an error")
    #     self.assertTrue(json_get['deck'] != [],  msg="should not throw an error")

    #     #third pop
    #     self.assertTrue(len(s.get("http://localhost:5000/popCard").text) >= 3,  msg="should not throw an error") # "[]"
    #     json_get = json.loads(s.get("http://localhost:5000/getDeck").text)
    #     self.assertTrue(json_get['dealt'] != [],  msg="should not throw an error")
    #     self.assertTrue(json_get['deck'] != [],  msg="should not throw an error")

    #     #last pop -- no deck, only dealt
    #     self.assertTrue(len(s.get("http://localhost:5000/popCard").text) >= 3,  msg="should not throw an error") # "[]"
    #     json_get = json.loads(s.get("http://localhost:5000/getDeck").text)
    #     self.assertTrue(json_get['dealt'] != [],  msg="should not throw an error")
    #     self.assertTrue(json_get['deck'] == [],  msg="should not throw an error")



unittest.main()