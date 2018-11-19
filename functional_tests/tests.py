from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import time
import unittest

MAX_WAIT = 10
waitTime = 0
class NewVisitorTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    #helper method to check for text in rows
    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:  
            try:
                table = self.browser.find_element_by_id('id_list_table')  
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return  
            except (AssertionError, WebDriverException) as e:  
                if time.time() - start_time > MAX_WAIT:  
                    raise e  
                time.sleep(0.5)
    #id_peos_table
    def wait_for_row_in_list_tablePEOS(self, row_text):
        start_time = time.time()
        while True:  
            try:
                table = self.browser.find_element_by_id('id_peos_table')  
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return  
            except (AssertionError, WebDriverException) as e:  
                if time.time() - start_time > MAX_WAIT:  
                    raise e  
                time.sleep(0.5)

    #def test_can_start_a_list_and_retrieve_it_later(self):

    def test_can_start_a_list_for_one_user(self):

        self.browser.get(self.live_server_url)

        self.assertIn('New INSTITUTION', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h2').text  
        self.assertIn('New INSTITUTION', header_text)


        inputbox = self.browser.find_element_by_id('id_email')  
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter email'
        )


        inputbox.send_keys('WestTexas@wtamu.edu') 
        inputbox = self.browser.find_element_by_id('id_password')
        inputbox.send_keys('1234') 
        inputbox = self.browser.find_element_by_id('id_confirm_password')
        inputbox.send_keys('1234') 
        inputbox = self.browser.find_element_by_id('id_name')
        inputbox.send_keys('wEST TEXAS AM UNIVERSITY') 
        inputbox = self.browser.find_element_by_id('id_street')
        inputbox.send_keys('2602 6 TH AVE') 
        inputbox = self.browser.find_element_by_id('id_city')
        inputbox.send_keys('CANYON') 
        inputbox = self.browser.find_element_by_id('id_state')
        inputbox.send_keys('TEXAS') 
        inputbox = self.browser.find_element_by_id('id_zipcode')
        inputbox.send_keys('79015') 
        inputbox = self.browser.find_element_by_id('id_mission')
        inputbox.send_keys('MISSION') 
        time.sleep(waitTime)  

        inputbox.send_keys(Keys.ENTER)  
        self.wait_for_row_in_list_table('1: WestTexas@wtamu.edu 1234 1234 wEST TEXAS AM UNIVERSITY 2602 6 TH AVE CANYON TEXAS 79015 MISSION')

        inputbox = self.browser.find_element_by_id('id_email')
        inputbox.send_keys('johanAyala@gmail.com')
        inputbox = self.browser.find_element_by_id('id_password')
        inputbox.send_keys('12345') 
        inputbox = self.browser.find_element_by_id('id_confirm_password')
        inputbox.send_keys('12345') 
        inputbox = self.browser.find_element_by_id('id_name')
        inputbox.send_keys('Johan Ayala') 
        inputbox = self.browser.find_element_by_id('id_street')
        inputbox.send_keys('2602 6 TH AVE') 
        inputbox = self.browser.find_element_by_id('id_city')
        inputbox.send_keys('CANYON') 
        inputbox = self.browser.find_element_by_id('id_state')
        inputbox.send_keys('TEXAS') 
        inputbox = self.browser.find_element_by_id('id_zipcode')
        inputbox.send_keys('79015') 
        inputbox = self.browser.find_element_by_id('id_mission')
        inputbox.send_keys('MISSION') 

        inputbox.send_keys(Keys.ENTER)
        time.sleep(waitTime)
        # The page updates again, and now shows both items on the list
        self.wait_for_row_in_list_table('2: johanAyala@gmail.com 12345 12345 Johan Ayala 2602 6 TH AVE CANYON TEXAS 79015 MISSION')
        self.wait_for_row_in_list_table('1: WestTexas@wtamu.edu 1234 1234 wEST TEXAS AM UNIVERSITY 2602 6 TH AVE CANYON TEXAS 79015 MISSION')
    
        butoonPeos = self.browser.find_element_by_id('bPEOS1')
        butoonPeos.click()
        inputbox = self.browser.find_element_by_id('id_objective')
        inputbox.send_keys('Apply foundational knowledge and technical skills to work in a business environment')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_tablePEOS('1: Apply foundational knowledge and technical skills to work in a business environment')
        time.sleep(waitTime)
        #Go back to the pages of institutions
        buttonGoBack = self.browser.find_element_by_id('goBackButton')
        buttonGoBack.click()
        butoonPeos = self.browser.find_element_by_id('bSO1')
        butoonPeos.click()
        inputbox = self.browser.find_element_by_id('id_studentOutcome')
        inputbox.send_keys('An ability to analyze a complex computing problem and to apply principles of computing and other relevant disciplines to identify solutions.')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_tablePEOS('1: An ability to analyze a complex computing problem and to apply principles of computing and other relevant disciplines to identify solutions.')
        time.sleep(waitTime)

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # Edith starts a new Institution
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_email')
        inputbox.send_keys('WestTexas@wtamu.edu') 
        inputbox = self.browser.find_element_by_id('id_password')
        inputbox.send_keys('1234') 
        inputbox = self.browser.find_element_by_id('id_confirm_password')
        inputbox.send_keys('1234') 
        inputbox = self.browser.find_element_by_id('id_name')
        inputbox.send_keys('wEST TEXAS AM UNIVERSITY') 
        inputbox = self.browser.find_element_by_id('id_street')
        inputbox.send_keys('2602 6 TH AVE') 
        inputbox = self.browser.find_element_by_id('id_city')
        inputbox.send_keys('CANYON') 
        inputbox = self.browser.find_element_by_id('id_state')
        inputbox.send_keys('TEXAS') 
        inputbox = self.browser.find_element_by_id('id_zipcode')
        inputbox.send_keys('79015') 
        inputbox = self.browser.find_element_by_id('id_mission')
        inputbox.send_keys('MISSION') 
        time.sleep(waitTime)  

        inputbox.send_keys(Keys.ENTER)  
        time.sleep(waitTime)
        self.wait_for_row_in_list_table('1: WestTexas@wtamu.edu 1234 1234 wEST TEXAS AM UNIVERSITY 2602 6 TH AVE CANYON TEXAS 79015 MISSION')


        # He notices that her list has a unique URL
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')

        # Now a new user, Francis, comes along to the site.

        ## We use a new browser session to make sure that no information
        ## of Edith's is coming through from cookies etc
        self.browser.quit()
        self.browser = webdriver.Firefox()

        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        inputbox = self.browser.find_element_by_id('id_email')
        inputbox.send_keys('johanAyala@gmail.com')
        inputbox = self.browser.find_element_by_id('id_password')
        inputbox.send_keys('12345') 
        inputbox = self.browser.find_element_by_id('id_confirm_password')
        inputbox.send_keys('12345') 
        inputbox = self.browser.find_element_by_id('id_name')
        inputbox.send_keys('Johan Ayala') 
        inputbox = self.browser.find_element_by_id('id_street')
        inputbox.send_keys('2602 6 TH AVE') 
        inputbox = self.browser.find_element_by_id('id_city')
        inputbox.send_keys('CANYON') 
        inputbox = self.browser.find_element_by_id('id_state')
        inputbox.send_keys('TEXAS') 
        inputbox = self.browser.find_element_by_id('id_zipcode')
        inputbox.send_keys('79015') 
        inputbox = self.browser.find_element_by_id('id_mission')
        inputbox.send_keys('MISSION') 
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: johanAyala@gmail.com 12345 12345 Johan Ayala 2602 6 TH AVE CANYON TEXAS 79015 MISSION')

        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('johanAyala@gmail.com 12345 12345 Johan Ayala 2602 6 TH AVE CANYON TEXAS 79015 MISSION', page_text)

    def test_layout_and_styling(self):
        # Edith goes to the home page
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # She notices the input box is nicely centered
        inputbox = self.browser.find_element_by_id('id_email')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            497.5,
            delta=10
        )
        # She starts a new list and sees the input is nicely
        # centered there too
        inputbox = self.browser.find_element_by_id('id_email')
        inputbox.send_keys('johanAyala@gmail.com')
        inputbox = self.browser.find_element_by_id('id_password')
        inputbox.send_keys('12345') 
        inputbox = self.browser.find_element_by_id('id_confirm_password')
        inputbox.send_keys('12345') 
        inputbox = self.browser.find_element_by_id('id_name')
        inputbox.send_keys('Johan Ayala') 
        inputbox = self.browser.find_element_by_id('id_street')
        inputbox.send_keys('2602 6 TH AVE') 
        inputbox = self.browser.find_element_by_id('id_city')
        inputbox.send_keys('CANYON') 
        inputbox = self.browser.find_element_by_id('id_state')
        inputbox.send_keys('TEXAS') 
        inputbox = self.browser.find_element_by_id('id_zipcode')
        inputbox.send_keys('79015') 
        inputbox = self.browser.find_element_by_id('id_mission')
        inputbox.send_keys('MISSION') 
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: johanAyala@gmail.com 12345 12345 Johan Ayala 2602 6 TH AVE CANYON TEXAS 79015 MISSION')

        inputbox = self.browser.find_element_by_id('id_email')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            497.5,
            delta=10
        )
        