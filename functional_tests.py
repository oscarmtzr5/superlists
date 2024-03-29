import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(unittest.TestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()

  def tearDown(self):
    self.browser.quit()

  def test_can_start_a_list_and_retrieve_it_later(self):
    #Edith has heard of a new online to-do list. She goes 
    #to checkout its homepage
    self.browser.get('http://localhost:8000')

    #She notices the page title and header mention
    #to-do lists
    self.assertIn('To-Do', self.browser.title)
    header_text = self.browser.find_element_by_tag_name('h1').text
    self.assertIn('To-Do', header_text)

    #She is invited to enter a new to-do item right away
    inputbox = self.browser.find_element_by_id('id_new_item')
    self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
    )

    #She types "Buy peacock feathers" into a text box ( Edith's hobby
    #is fly-fishing lures)
    inputbox.send_keys('Buy peacock feathers')

    #When she hits enter the page updates, and now the page lists
    #1.- Buy peacock feathers as an item in the to-do list
    inputbox.send_keys(Keys.ENTER)

    table = self.browser.find_element_by_id('id_list_table')
    rows = table.find_elements_by_tag_name('tr')
    self.assertTrue(any('1: Buy peacock feathers' in row.text for row in rows),
                    "New to-do item did not appear in table"
    )

    #There is still an item inviting her to add another item. She
    #enters "Use peacock feathers to make a fly"
    self.fail('Finish the test!')
    #the page updates again, and now she sees both items on the list

    #Edit wonders whether the site will remember her list. Then she sees 
    #that the site has generated a unique URL for her -- there is some 
    #explanatory text to that effect.

    #She visits that URL - here to-do list is still there

    #Satisfied, she goes back to sleep
    browser.quit()

if __name__ == '__main__':
  unittest.main()