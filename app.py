from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By

opts = ChromeOptions()
opts.add_experimental_option("detach", True)

#passe a variavel opts para o webdriver

navegador = webdriver.Chrome(options = opts)

url = r"C:\Users\04396\Desktop\projetos\webscrap\contato.html"
navegador.get(url)

campo_nome = navegador.find_element(By.ID,"nome")
campo_nome.send_keys("Thomas")

campo_mensagem = navegador.find_element(By.ID, "mensagem")
campo_mensagem.send_keys("Salveeeeee")

print(navegador.title)

titulo = navegador.find_element(By.ID, "titulo")
precos = navegador.find_elements(By.CLASS_NAME, "price")

for preco in precos:
    print(preco.text)
produtos = navegador.find_elements(By.CLASS_NAME, "product_name")

for produto in produtos:
    print(produto.text)

precos = navegador.find_elements(By.XPATH, "/html/body/div/div[1]/p")
print(preco.text)