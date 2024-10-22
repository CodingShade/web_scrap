from selenium import webdriver
from selenium.webdriver import ChromeOptions

opts = ChromeOptions()
opts.add_experimental_option("detach", True)

#passe a variavel opts para o webdriver

navegador = webdriver.Chrome(options = opts)
url = r"https://www.duque.g12.br"
navegador.get(url)