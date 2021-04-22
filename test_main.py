from main import app
import unittest

class BMITestCase(unittest.TestCase):

    # test that flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # test that home page loads
    def test_home_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertTrue(b'This is the Home Page' in response.data)

    def test_BMI_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/BMI', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_BMI_calculator(self):
        tester = app.test_client(self)
        response = tester.post(
            '/BMI', 
            data=dict(feet="5", inches="10", weight="150"),
            follow_redirects=True
        )
        self.assertIn(b'22.0', response.data)

class RetireTestCase(unittest.TestCase):

    # test that flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # test that home page loads
    def test_home_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertTrue(b'This is the Home Page' in response.data)

    def test_BMI_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/retire', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_BMI_calculator(self):
        tester = app.test_client(self)
        response = tester.post(
            '/retire', 
            data=dict(age="25", salary="65000", percent="10", goal="500000"),
            follow_redirects=True
        )
        self.assertIn(b'82', response.data)
    


if __name__ == '__main__':
    unittest.main()