import pandas as pd
import pyautogui as at
from time import sleep

at.PAUSE = 0.5
#abrir o navegador crome
at.press("win")
at.write("chrome")
at.press("enter")
at.hotkey("win" , "up")

#entrar no site de prenchimento
at.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
at.press("enter")

#logar no site
sleep(2)
at.click(798 , 358) #essa posiçao varia de monitor para monitor
at.write("teste@gmail.com")
at.press("tab")
at.write("*****") #senha
at.press("tab")
at.press("enter")

#cadastro dos produtos
sleep(2)
tabela = pd.read_csv("produtos.csv")
for linha in tabela.index:
    at.click(x=836, y=242) 
    at.write(str(tabela.loc[linha, "codigo"]))
    at.press("tab")
    at.write(str(tabela.loc[linha, "marca"]))
    at.press("tab")
    at.write(str(tabela.loc[linha, "tipo"]))
    at.press("tab")
    at.write(str(tabela.loc[linha, "categoria"]))
    at.press("tab")
    at.write(str(tabela.loc[linha, "preco_unitario"]))
    at.press("tab")
    at.write(str(tabela.loc[linha, "custo"]))
    at.press("tab")
    if not pd.isna(tabela.loc[linha, "obs"]):
        at.write(str(tabela.loc[linha, "obs"]))
    at.press("tab")
    at.press("enter")
    at.scroll(5000)


