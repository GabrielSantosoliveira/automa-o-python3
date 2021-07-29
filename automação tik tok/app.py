import pyautogui
from time import sleep
def AbrirChrome(navegador):
    navegador = navegador.strip().lower().capitalize()

    
    # configuração
    pyautogui.PAUSE = 1  
    
    # abrir o navegador
    pyautogui.press('win')
    pyautogui.write(navegador)
    pyautogui.press('enter')

    print('Pronto')

def AbrirTikTok(url):
    import time

    #configuração
    pyautogui.PAUSE = 1

    #abrirTikTok
    pyautogui.write(url)
    time.sleep(3)
    pyautogui.press('enter')


def VerificarLike(img):
    
    pyautogui.PAUSE = 1
    #loop

    while True:

        if pyautogui.locateOnScreen(img ,confidence=0.1):
            print('ok')

            LocalizaçãoDobutão = pyautogui.locateOnScreen(img , confidence=0.1)
            LocalDoButão = pyautogui.center(LocalizaçãoDobutão) 

            posisãox , posisãoy = LocalDoButão

            pyautogui.moveTo(posisãox,posisãoy)

            pyautogui.scroll(-16)
        else:
            pyautogui.scroll(-3)


#pyautogui.alert('Olhe o Terminal ')
#navegador = str(input('digite seu #navegador >> '))
#AbrirChrome(navegador)
#
#sleep(1)
#
#url = 'https://www.tiktok.com/pt-BR?#lang=pt_BR'
#sleep(2)
#AbrirTikTok(url)
pyautogui.alert('a')
VerificarLike('TIKTOK.png')