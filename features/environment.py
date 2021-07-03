from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def before_all(context):
	options = Options()
	options.headless = True
	context.browser = webdriver.Firefox(options=options)
	pass


def after_all(context):
	context.browser.quit()
	context.browser = None
	pass
