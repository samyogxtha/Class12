import pyautogui, time, win32clipboard, webbrowser ,sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def n():
    print('\n\n')
n()


win32clipboard.OpenClipboard()
data = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()

ytlink = ('https://www.ytmp3x.com/'+data)

print(ytlink)




webbrowser.open(ytlink)
time.sleep(5)





pyautogui.click(x=529, y=427)
time.sleep(5)
pyautogui.click(x=529, y=427)







n()
'''
options = Options()

options.add_experimental_option('excludeSwitches', ['enable-logging'])


driver = webdriver.Chrome(executable_path="C:/chromedriver.exe",chrome_options=options)
driver.implicitly_wait(2)

driver.get(ytlink)


l = driver.find_element('/html/body/div[2]/div[2]/div/div[2]/div[3]/ul/li[1]')
l.click()
driver.quit()
'''

n()