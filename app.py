from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By

opts = ChromeOptions()
opts.add_experimental_option("detach", True)

#passe a variavel opts para o webdriver

navegador = webdriver.Chrome(options = opts)

url = r"C:\Users\04396\Desktop\projetos\webscrap\produtos.html"
navegador.get(url)
print(navegador.title)

titulo = navegador.find_element(By.ID, "titulo")
precos = navegador.find_elements(By.CLASS_NAME, "price")
for preco in precos:
    print(preco.text)
produtos = navegador.find_elements(By.CLASS_NAME, "product_name")

for produto in produtos:
    print(produto.text)
