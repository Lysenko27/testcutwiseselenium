from tests import settings


class Page(object):

    def __init__(self, driver):
      self.driver = driver
      self.driver.set_page_load_timeout(60)
      self.driver.set_script_timeout(60)
      self.driver.implicitly_wait(60)
      self.base_url = settings.url


    def find_element(self, xpath):
         return self.driver.find_element_by_xpath(xpath)

    def reload_page(self):
        self.driver.execute_script("location.reload()")
