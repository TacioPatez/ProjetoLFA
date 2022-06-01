from xml.sax.xmlreader import Locator
from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://web.whatsapp.com/")
    time.sleep(30)

    arq = open("times.txt")
    page2 = browser.new_page()
    linhas = arq.readlines()

    for linha in linhas:
        if linha[0] == '-':
            linha = linha.replace('-','')
            page2.goto("https://lance.com.br/" + linha)
            imagem = page2.locator('//*[@id="main-container"]/div[4]/div[1]/div[1]/div[8]/div[1]/a/img')
            imagem.screenshot(path='picture.png')
            page2.click('.board-text')
            title = page2.query_selector('.title').inner_text()
            link = page2.url
            print(title)
        else:
            page.click('//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')
            page.fill('//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]', linha.strip())
            time.sleep(5)
            inicial = page.locator("//span[@title='"+linha.strip()+"']")
            inicial.click() 

            page.click('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/span')
            with page.expect_file_chooser() as fc_info:
                page.click('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div[1]/div/ul/li[1]/button/span')
            file_chooser = fc_info.value    
            file_chooser.set_files("picture.png")

            page.fill('//*[@id="app"]/div[1]/div[1]/div[2]/div[2]/span/div[1]/span/div[1]/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[2]', title.strip())
            page.keyboard.press("Enter")

            page.fill('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]', link)
            page.keyboard.press("Enter")

            print(linha.strip())



    time.sleep(20000)

    #browser.close()