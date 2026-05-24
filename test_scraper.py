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

    print("Status:", response.status_code)

    soup = BeautifulSoup(response.text, "html.parser")  
    print(f"Requested URL: {url}")
    print("Final URL:", response.url)

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

# print(scrape_food("banana"))
# print(scrape_food("apple"))


