__author__ = 'sean.haung'
import unittest, requests, json, os

class TestHttpRequest(unittest.TestCase):
    bkend_url = 'http://127.0.0.1:5000'
    post_url = 'http://127.0.0.1:5000/add'
    delete_url = 'http://127.0.0.1:5000/delete'

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_parse_response_1(self):
        # Generate the url
        payload = {'id': '9'}
        r = requests.get(self.bkend_url, params=payload)
        print(r.url)

    def test_parse_response_2(self):
        # Response text
        r = requests.get(self.bkend_url)
        print(r.text)

    def test_parse_response_3(self):
        # Response json
        r = requests.get(self.bkend_url)
        payload = r.json()
        print(payload)
        print(payload['items'][0]['title'])


    def test_parse_response_4(self):
        # Response raw
        r = requests.get(self.bkend_url)
        print(r.raw)

    def test_post_1(self):
        # pass in json by data parameter
        payload = {'title': 'Keith'}
        r = requests.post(self.post_url, data=json.dumps(payload))
        print(r.json())

    def test_post_2(self):
        # pass by json parameter
        payload = {'title': 'Tom'}
        r = requests.post(self.post_url, json=payload)
        res = r.json()
        print(res)
        self.assertEqual(payload['title'], res['items'][0]['title'])

    def test_post_3(self):
        # pass by file
        root_path = os.path.dirname(os.path.dirname(__file__))
        test_path = os.path.join(root_path, 'test')
        json_file = os.path.join(test_path, 'member.json')
        # print(json_file)
        data = open(json_file, encoding='UTF-8')
        payload = json.load(data)
        # files = {'file': open(json_file, 'rb')}
        r = requests.post(self.post_url, json=payload)
        print(r.json())

    def test_status_code_1(self):
        # status_code
        r = requests.get(self.bkend_url)
        print(r.status_code)

    def test_status_code_2(self):
        # requests.codes.ok
        r = requests.get(self.bkend_url)
        self.assertEqual(requests.codes.ok, r.status_code)

    def test_headers(self):
        # check headers in python dic
        r = requests.get(self.bkend_url)
        print(r.headers)
        print(r.headers['Content-Type'])

    def test_delete_1(self):
        # delete entry

        # Get the latest entry
        r = requests.get(self.bkend_url)
        payload = r.json()
        the_id = payload['items'][0]['id']
        the_title = payload['items'][0]['title']

        path = (self.delete_url, str(the_id))
        delete_path = '/'.join(path)
        # delete entry
        res = requests.delete(delete_path)
        self.assertEqual(requests.codes.ok, res.status_code)
        # assert delete successful
        after_delete = res.json()
        self.assertNotEqual(the_id, after_delete['items'][0]['id'])

if __name__ == "__main__":
    unittest.main()