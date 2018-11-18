from django.urls import resolve
from django.test import TestCase
from lists.views import home_page
from django.http import HttpRequest
from lists.models import Item, Institutions
from django.template.loader import render_to_string

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
    
class ListViewTest(TestCase):

    def test_uses_list_template(self):
        inst_ = Institutions.objects.create()
        response = self.client.get(f'/lists/1/')
        self.assertTemplateUsed(response, 'list.html')

    def test_displays_only_items_for_that_list(self):
        correct_list = Institutions.objects.create()
        #Item.objects.create(text='itemey 1', list=correct_list)
        Item.objects.create(email = 'wtamu@wtamu.edu',
                            password = '1234',
                            confirm_password = '1234',
                            name = 'West Texas A&M University',
                            street = '2602 4 ave' ,
                            city = 'Canyon',
                            state = 'Texas',
                            zipcode = '79015',
                            mission = 'Mission',
                            list = correct_list)
        #Item.objects.create(text='itemey 2', list=correct_list)
        Item.objects.create(email = 'university2@gmail.com',
                            password = '5678',
                            confirm_password = '5678',
                            name = 'University 2',
                            street = 'cll 160 c n 16 c 35' ,
                            city = 'Bogota',
                            state = 'Cundinamarca',
                            zipcode = '110111',
                            mission = 'Mision',
                            list = correct_list)

        other_list = Institutions.objects.create()

        Item.objects.create(email = 'OTHERuniversity2@gmail.com',
                            password = '5678',
                            confirm_password = '5678',
                            name = 'OTHER University 2',
                            street = 'cll 160 c n 16 c 35' ,
                            city = 'Bogota',
                            state = 'Cundinamarca',
                            zipcode = '110111',
                            mission = 'Mision',
                            list = Institutions.objects.get(id=1))

        Item.objects.create(email = '2OTHERuniversity2@gmail.com',
                            password = '5678',
                            confirm_password = '5678',
                            name = '2 OTHER University 2',
                            street = 'cll 160 c n 16 c 35' ,
                            city = 'Bogota',
                            state = 'Cundinamarca',
                            zipcode = '110111',
                            mission = 'Mision',
                            list = Institutions.objects.get(id=1))

        response = self.client.get(f'/lists/1/')

        self.assertContains(response, 'wtamu@wtamu.edu')
        self.assertContains(response, 'university2@gmail.com')
        self.assertContains(response, 'OTHERuniversity2@gmail.com')
        self.assertContains(response, '2OTHERuniversity2@gmail.com') 

    def test_passes_correct_list_to_template(self):
        other_list = Institutions.objects.create()
        correct_list = Institutions.objects.create()
        response = self.client.get(f'/lists/{correct_list.id}/')
        self.assertEqual(response.context['list'], correct_list)  

class NewListTest(TestCase):

    def test_can_save_a_POST_request(self):
        self.client.post('/lists/new', data={  'email': 'A new item_email',
                    'password': 'A new item_password',
                    'confirm_password': 'A new item_confirm_password',
                    'name': 'A new item_name',
                    'street': 'A new item_street',
                    'city': 'A new item_city',
                    'state': 'A new item_state',
                    'zipcode': 'A new item_zipcode',
                    'mission': 'A new item_mission',
            })
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.email, 'A new item_email')
        self.assertEqual(new_item.password, 'A new item_password')
        self.assertEqual(new_item.confirm_password, 'A new item_confirm_password')
        self.assertEqual(new_item.name, 'A new item_name')
        self.assertEqual(new_item.street, 'A new item_street')
        self.assertEqual(new_item.city, 'A new item_city')
        self.assertEqual(new_item.state, 'A new item_state')
        self.assertEqual(new_item.zipcode, 'A new item_zipcode')
        self.assertEqual(new_item.mission, 'A new item_mission')
    
    def test_redirects_after_POST(self):
        response = self.client.post('/lists/new', data={  'email': 'A new item_email',
                    'password': 'A new item_password',
                    'confirm_password': 'A new item_confirm_password',
                    'name': 'A new item_name',
                    'street': 'A new item_street',
                    'city': 'A new item_city',
                    'state': 'A new item_state',
                    'zipcode': 'A new item_zipcode',
                    'mission': 'A new item_mission',
            })
        new_list = Institutions.objects.first()
        self.assertRedirects(response, f'/lists/{new_list.id}/')

class ListAndItemModelsTest(TestCase):

    def test_saving_and_retrieving_items(self):
        list_ = Institutions()
        list_.save()

        first_item = Item()
        first_item.email = '2OTHERuniversity2@gmail.com'
        first_item.password = '5678'
        first_item.confirm_password = '5678'
        first_item.name = '2 OTHER University 2'
        first_item.street = 'cll 160 c n 16 c 35' 
        first_item.city = 'Bogota'
        first_item.state = 'Cundinamarca'
        first_item.zipcode = '110111'
        first_item.mission = 'Mision'
        first_item.list = list_
        first_item.save()

        second_item = Item()
        second_item.email = 'university2@gmail.com'
        second_item.password = '5678'
        second_item.confirm_password = '5678'
        second_item.name = 'University 2'
        second_item.street = 'cll 160 c n 16 c 35' 
        second_item.city = 'Bogota'
        second_item.state = 'Cundinamarca'
        second_item.zipcode = '110111'
        second_item.mission = 'Mision'
        second_item.list = list_
        second_item.save()

        saved_list = Institutions.objects.first()
        self.assertEqual(saved_list, list_)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.email , '2OTHERuniversity2@gmail.com')
        self.assertEqual(first_saved_item.password, '5678')
        self.assertEqual(first_saved_item.list, list_)
        self.assertEqual(second_saved_item.email, 'university2@gmail.com')
        self.assertEqual(first_saved_item.password, '5678')
        self.assertEqual(second_saved_item.list, list_)

class NewItemTest(TestCase):

    def test_can_save_a_POST_request_to_an_existing_list(self):
        other_list = Institutions.objects.create()
        correct_list = Institutions.objects.create()

        self.client.post(
            f'/lists/{correct_list.id}/add_item',
            data={  'email': 'A new item_email',
                    'password': 'A new item_password',
                    'confirm_password': 'A new item_confirm_password',
                    'name': 'A new item_name',
                    'street': 'A new item_street',
                    'city': 'A new item_city',
                    'state': 'A new item_state',
                    'zipcode': 'A new item_zipcode',
                    'mission': 'A new item_mission',
            }
        )

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.email, 'A new item_email')
        self.assertEqual(new_item.password, 'A new item_password')
        self.assertEqual(new_item.confirm_password, 'A new item_confirm_password')
        self.assertEqual(new_item.name, 'A new item_name')
        self.assertEqual(new_item.street, 'A new item_street')
        self.assertEqual(new_item.city, 'A new item_city')
        self.assertEqual(new_item.state, 'A new item_state')
        self.assertEqual(new_item.zipcode, 'A new item_zipcode')
        self.assertEqual(new_item.mission, 'A new item_mission')
        self.assertEqual(new_item.list, correct_list)

    def test_redirects_to_list_view(self):
        other_list = Institutions.objects.create()
        correct_list = Institutions.objects.create()

        response = self.client.post(
            f'/lists/{correct_list.id}/add_item',
            data={  'email': 'A new item_email',
                    'password': 'A new item_password',
                    'confirm_password': 'A new item_confirm_password',
                    'name': 'A new item_name',
                    'street': 'A new item_street',
                    'city': 'A new item_city',
                    'state': 'A new item_state',
                    'zipcode': 'A new item_zipcode',
                    'mission': 'A new item_mission',
            }
        )

        self.assertRedirects(response, f'/lists/{correct_list.id}/')
