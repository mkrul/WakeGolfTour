import bs4
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

browser = webdriver.Firefox(executable_path=r'/home/mkrul/Desktop/projects/WakeGolfTour/WGT_Website/geckodriver-linux')
browser.get('http://localhost:8000/')
print(browser.title)

elem = browser.find_element_by_partial_link_text("Tourn")
print(elem.text)
elem.click()
elem = browser.find_element_by_partial_link_text("Oak")
print(elem.text)
elem.click()
elem = browser.find_element_by_tag_name("h3")
print(elem.text)

try:
    wait = WebDriverWait(browser, 10)
    elem = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Tourn")))
    print(elem.text)
    elem.click()
    elem = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Oak")))
    print(elem.text)
    elem.click()
    elem.wait.until(EC.presence_of_element_located((By.TAG_NAME, "h3")))
    print(elem.text)
except TimeoutException:
    print("Locating links in WGT Website failed")

total = 0
for elem in soup_elems:
    score = int(elem.getText())
    total = total + score

print("Average tournament score: ", total / len(soup_elems))

scores = []
for elem in soup_elems:
    score = int(elem.getText())
    scores.append(score)
print("Average tournament score: ", sum(scores) / len(scores))

browser.close()

