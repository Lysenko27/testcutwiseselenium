from pages.base import Page

class HomePage(Page):
	def __init__(self, driver):
		super().__init__(driver)
		self.checkbox_show_descriptions = '//input[@name="request"]'
		self.city_in_result_list_search = 'span.suggest2-item__text'
		self.list_result_search = '//ul[@class="suggest2__items"]/li'
		self.first_result_search ='//span[@class="suggest2-item__text"]'
		self.title_city ='//h1[@class="title title_level_1"]'
		self.weather_days ='//div[@class="forecast-briefly__days"]/div'
		self.driver = driver

	def get_home_page(self):
		self.driver.get(self.base_url)

	def search(self,city_name):
		self.find_element(self.checkbox_show_descriptions).send_keys(city_name)
		self.find_element(self.first_result_search).click()

	def get_title_text(self):
		return self.find_element(self.title_city).text

	def search_list(self,city_name):
		self.find_element(self.checkbox_show_descriptions).send_keys(city_name)
		return (
		list(
		map(
		lambda e:
		e.find_element_by_css_selector(self.city_in_result_list_search).text
		,
		list(self.driver.find_elements_by_xpath(self.list_result_search))
		)
		)
		)

	def count_days_weather(self):
		return len(self.driver.find_elements_by_xpath(self.weather_days))