import requests
from bs4 import BeautifulSoup

def scrape_food(food):

    url = f"https://www.yazio.com/en/foods/{food.lower()}.html"

    headers = {
        "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/137.0 Safari/537.36"
    )
    }

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")  
    
    calories = soup.find("div", class_="py-2 text-center")
    if calories:
        calories = calories.get_text(strip=True).replace("Caloric Value", "").strip()
    else:
        calories = None

    cards = soup.find_all("div", class_="flex-1 text-center")
    nutrients={}

    for card in cards:
        p_tags= card.find_all("p")

        value = p_tags[0].get_text(strip=True)
        label = p_tags[1].get_text(strip=True)
        nutrients[label] = value

    calories = soup.find("div", class_="py-2 text-center")
    if calories:
        calories = calories.get_text(strip=True).replace("Caloric Value", "").strip()
    else:
        calories = None
    nutrients["Calories"] = calories

    return nutrients

def get_facts(food):

    url = f"https://www.yazio.com/en/foods/{food.lower()}.html"

    headers = {
        "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/137.0 Safari/537.36"
    )
    }

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser") 

    activitiy_label = soup.find_all("p", class_="text-yettie-label-primary mt-2 text-[18px] font-bold")
    facts = {}

    for label in activitiy_label:
        activity = label.get_text(strip=True)
        card = label.parent

        value_div = card.find(
            "div",
            class_="text-yettie-green-500 absolute right-2 bottom-2 rounded-2xl bg-black px-2 py-1 text-center text-[24px] font-bold"
        )

        if value_div:
            facts[activity] = value_div.get_text(strip=True)
    return facts

get_facts("banana")

