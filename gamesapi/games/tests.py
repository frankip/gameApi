# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from django.utils.http import urlencode
from rest_framework import status
from rest_framework.test import APITestCase
from games.models import GameCategory


class GameCategoryTests(APITestCase):
    def create_game_category(self, name):
        """ Create new Game category helper method """
        url = reverse('gamecategory-list')
        data = {'name': name}
        response = self.client.post(url, data, format='json')
        return response

    def test_create_and_retrieve_game_category(self):
        """ 
        Ensure we can create a new GameCategory and then retrieve it 
        """
        new_game_category_name = 'New Game Category'
        response = self.create_game_category(new_game_category_name)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(GameCategory.objects.count(), 1)
        self.assertEqual(GameCategory.objects.get().name,
                         new_game_category_name)
        print("PK {0}".format(GameCategory.objects.get().pk))

    def test_create_duplicated_game_category(self):
        """Test we can create new category"""
        url = reverse('gamecategory-list')
        new_game_category_name = "New Game Category"
        data = {'name': new_game_category_name}
        response1 = self.create_game_category(new_game_category_name)
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)
        response2 = self.create_game_category(new_game_category_name)
        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_game_categories(self):
        """ Test we can retrieve game category """
        new_game_category_name = 'new Game Category'
        self.create_game_category(new_game_category_name)
        url = reverse('gamecategory-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.data['results'][0]['name'],
                         new_game_category_name)

    def test_update_game_category(self):
        """ Test we can update single field in game category """

        new_game_catgory_name = "Initial Name"
        response = self.create_game_category(new_game_catgory_name)
        url = reverse('gamecategory-detail', None, {response.data[pk]})
        updated_game_category_name = 'Updated Game Category Name'
        data = {'name': updated_game_category_name}
        patch_response = self.client.patch(url, data, format='json')
        self.assertEqual(patch_response.status_code, status.HTTP_200_OK)
        self.assertEqual(patch_response.data['name'],
                         updated_game_category_name)

    def test_filter_game_category_by_name(self):
        """ Ensure we are able to filtr game category by name"""
        game_category_name1 = "First game category"
        self.create_game_category(game_category_name1)
        game_category_name2 = "Second Game Category"
        self.create_game_category(game_category_name2)
        filter_by_name = {'name': game_category_name1}
        url = '{0}?{1}'.format(reverse('gamecategory-list'),
                               urlencode(filter_by_name))
        response = self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.data['results'][0]['name'],
                         game_category_name1)
