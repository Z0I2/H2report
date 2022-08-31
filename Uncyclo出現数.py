from ast import For
import requests
from bs4 import BeautifulSoup
import re
def main():
    toppage = requests.get("https://ja.uncyclopedia.info/")
    soup = BeautifulSoup(toppage.content, "html.parser")
    dict = {}
    for i in range(10000) :
        nexturl = "https://ja.uncyclopedia.info" + soup.select("#n-randompage>a")[0].get("href")
        page = requests.get(nexturl)
        soup = BeautifulSoup(page.content, "html.parser")
        print(i)
        print(soup.find('title').text)
        text = soup.select("#content")[0].text
        kanji = re.findall('[一-鿐]', text)
        for k in kanji:
            if(k in dict): dict[k] += 1 
            else: dict[k] = 1
    result = sorted(dict.items(), key=lambda x:x[1])
    print(result)
    f = open('./out_10000_uncyclo.txt', 'w', encoding='UTF-8')
    f.write(str(result))
if __name__ == "__main__":
    main()