import io
from PIL import Image
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from rest_framework import status
from rest_framework_jwt import utils
from rest_framework_jwt.compat import get_user_model

User = get_user_model()
factory = APIRequestFactory()


class JSONWebTokenAuthenticationTests(APITestCase):
    """JSON Web Token Authentication"""

    def setUp(self):
        self.client = APIClient()
        self.username = 'buildingblocks'
        self.email = 'buildingblocks@example.com'
        self.password='buildingblocks'
        self.user = User.objects.create_user(self.email, self.password, username=self.username)
        payload = utils.jwt_payload_handler(self.user)
        token = utils.jwt_encode_handler(payload)
        self.auth = 'Token {0}'.format(token)

    def generate_image_file(self):
        file = io.BytesIO()
        image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        return file

    def test_create_hotel_without_auth(self):
        """
        should not allow without auth
        """
        response = self.client.post('http://localhost:8000/api/v1/hotel/', {})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_hotel_with_auth(self):
        """
        """
        payload = {
        'name' : 'testname',
        'address' : 'no 1, test street, test city.',
        'images': self.generate_image_file()
        }
        response = self.client.post('http://localhost:8000/api/v1/hotel/', payload, HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_of_hotels(self):
        """
        we no need auth to fetch list of hostels
        """
        response = self.client.get('http://localhost:8000/api/v1/hotel/', {})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_get_hotel_detail(self):
    #     """
    #     we no need auth to fetch list of hostels
    #     """
    #     response = self.client.get('http://localhost:8000/api/v1/hotel/1/', {}, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)    

    # def test_update_hotel_with_auth(self):
    #     """
    #     should allow
    #     """
    #     payload = {
    #     'name' : 'new_testname',
    #     'address' : 'new: no 1, test street, test city.',
    #     'images': self.generate_image_file()
    #     }
    #     response = self.client.put('http://localhost:8000/api/v1/hotel/1/', payload, HTTP_AUTHORIZATION=self.auth)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_delete_hotel_without_auth(self):
    #     """
    #     should not allow without auth
    #     """
    #     response = self.client.delete('http://localhost:8000/api/v1/hotel/1/', {})
    #     self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # def x_test_delete_hotel_with_auth(self):
    #     """
    #     should allow
    #     """
    #     response = self.client.delete('http://localhost:8000/api/v1/hotel/1/', {}, HTTP_AUTHORIZATION=self.auth)
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)