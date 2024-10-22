from selenium import webdriver
from selenium.webdriver import ChromeOptions

opts = ChromeOptions()
opts.add_experimental_option("detach", True)

#passe a variavel opts para o webdriver

navegador = webdriver.Chrome(options = opts)
url = r"C:\Users\04396\Desktop\projetos\webscrap\produtos.html"
navegador.get(url)
print(navegador.title)