import unittest
from selenium import webdriver

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
    self.fail('Finish the test!')

    #She is invited to enter a new to-do item right away

    #She types "Buy peacock feathers" into a text box ( Edith's hobby
    #is fly-fishing lures)

    #When she hits enter the page updates, and now the page lists
    #1.- Buy peacock feathers as an item in the to-do list

    #There is still an item inviting her to add another item. She
    #enters "Use peacock feathers to make a fly"

    #the page updates again, and now she sees both items on the list

    #Edit wonders whether the site will remember her list. Then she sees 
    #that the site has generated a unique URL for her -- there is some 
    #explanatory text to that effect.

    #She visits that URL - here to-do list is still there

    #Satisfied, she goes back to sleep
    browser.quit()

if __name__ == '__main__':
  unittest.main()