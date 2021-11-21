import requests
import json
import unittest


base_url ="http://localhost:5010"

class BasicTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        #print("----setUp--------------")
        pass   

    @classmethod
    def tearDownClass(self):
        #print("----tearDown-----------")
        pass


    
    def test_get_members(self):
        
        #print("\n------API Get /r/members ----")

        response = requests.get(f"{base_url}/r/members")
        #print(response.text)
        dict_d = json.loads(response.text)
            
        #print(dict_d)
        #print(response.status_code)
        self.assertEqual(200,response.status_code)
        self.assertTrue(dict_d)

    def test_members_ng_url(self):
        
        #print("\n------API Get Not Found ----")

        response = requests.get(f"{base_url}/rxx/members")

        #print(response.status_code)
        self.assertNotEqual(200,response.status_code)
        self.assertEqual(404,response.status_code)

        #self.assertFalse(response.text)

    def test_get_member_by_id(self):

        #print("\n------API Get /r/member/{id} ----")

        response = requests.get(f"{base_url}/r/member/1")
        #print(response.text)

        self.assertTrue(response.text)
        self.assertEqual(200,response.status_code)
        dict_d = json.loads(response.text)
        self.assertTrue(dict_d)


    def test_post_member(self):

        #print("\n------API POST /r/member ----")

        data = {
            'name': "POST FROM WEB",
            'category': "Web",
            'telNumber': "000-9999-8888",
            'memo': "POST",
            'email': "mail",
        }
        response = requests.post(
            f'{base_url}/r/member',
            json.dumps(data),
            headers={'Content-Type': 'application/json'})

        dict_d = json.loads(response.text)
        self.new_id = dict_d['id']
        #print(self.new_id, dict_d)
        self.assertEqual(200,response.status_code)
        self.assertTrue(dict_d)

    def test_put_member(self):

        #print(f"\n------API PUT /r/member/{id} ----")

        data = {
            'name': "Change POST FROM WEB",
            'category': "Web",
            'telNumber': "000-9999-8888",
            'memo': "PUT",
            'email': "mail",
        }
        response = requests.put(
            f'{base_url}/r/member/1',
            json.dumps(data),
            headers={'Content-Type': 'application/json'})

        dict_d = json.loads(response.text)
        self.assertTrue(dict_d)
        #print(dict_d)

        response = requests.get(f"{base_url}/r/member/1")
        #print(response.text)
        dict_d = json.loads(response.text)
        self.assertEqual(data['name'],dict_d['name'])

if __name__ == '__main__':
    unittest.main()


