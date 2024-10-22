from selenium import webdriver
from selenium.webdriver import ChromeOptions

opts = ChromeOptions()
opts.add_experimental_option("detach", True)

navegador = webdriver.Chrome(options = opts)
