import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains

navegador = webdriver.Firefox()
navegador.get("https://mousetester.com/")
print('Navegador Abrindo...')
time.sleep(2)
procurar_xpath = navegador.find_element_by_xpath('//*[@id="clickMe"]').click()
mouse = ActionChains(navegador)

mouse.context_click(procurar_xpath).perform()

