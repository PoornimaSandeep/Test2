import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
print(soup)

results = soup.find(class_name="")
job_elements = results.find_all("div", class_="title is-5")
print(results.prettify())