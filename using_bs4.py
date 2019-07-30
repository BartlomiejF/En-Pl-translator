from bs4 import BeautifulSoup
import re, requests

def translate(word):
    req = requests.get(f"https://www.diki.pl/slownik-angielskiego?q={word}")
    page = BeautifulSoup(req.text, "html.parser")
    translated = page.find("li", re.compile("meaning*")).find("a", "plainLink").text
    return translated

if __name__ == "__main__":
    word_eng = input("wpisz slowo do przetlumaczenia: ")
    print(translate(word_eng))
