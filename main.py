import sys
import requests
from bs4 import BeautifulSoup
import pyperclip

req = requests.get(sys.argv[1])


content = req.text

soup = BeautifulSoup(content,"html.parser")

href_list = []

for a in soup.find_all('a', href=True):
    href_list.append(a['href'])


search_word = input("Что ищем : ")

rez_list = []

print("<><><><><><><><><><><><><><><><><><><>")

count = 0
for i in range(len(href_list)):

    if href_list[i].find(search_word) != -1:
        count = count + 1
        print(f"{count} результат : {href_list[i]}")
        rez_list.append(href_list[i])

print("<><><><><><><><><><><><><><><><><><><>")


id_copy   = int(input("\nнапиши id: "))

pyperclip.copy(rez_list[id_copy-1])
print(f"добавлено в буввер : {rez_list[id_copy-1]}")



# os.system("deactivate")