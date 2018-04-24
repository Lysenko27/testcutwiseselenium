import pytest

from pages.home_page import HomePage
from selenium import webdriver


def setup_module():
	global home_page
	global driver
	driver = webdriver.Chrome()
	home_page=HomePage(driver)
	home_page.get_home_page()

def test_search():
	"""Проверка правильности работы поиска"""
	city_name='Лондон'
	home_page.search(city_name)
	assert 'Погода в %sе'%city_name == home_page.get_title_text()

def test_check_search_list():
	"""Проверка правильности работы подсказок поиска"""
	city_name='Лондон'
	list_city = home_page.search_list(city_name)
	for city in list_city:
		assert city_name in city

def test_count_days():
	"""Проверка правильности, что показывает погоду на 10 дней"""
	assert home_page.count_days_weather() == 10


def teardown_module():
	driver.close()
