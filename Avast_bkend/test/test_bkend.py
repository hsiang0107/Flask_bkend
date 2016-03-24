__author__ = 'sean.haung'
import unittest, requests, json, os

class TestHttpRequest(unittest.TestCase):
    bkend_url = 'http://127.0.0.1:5000'
    post_url = 'http://127.0.0.1:5000/add'

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
        print(r.json())

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
        print(r.json())

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

if __name__ == "__main__":
    unittest.main()