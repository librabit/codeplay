import requests
from bs4 import BeautifulSoup
import lxml

url = "https://comic.naver.com/webtoon/weekday"
cheat = {"accept-language" : "ko_KR", "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52"}

resource = requests.get(url, headers = cheat)
resource.raise_for_status()

soup = BeautifulSoup(resource.text, "lxml")


# sat_all = soup.find("div", attrs={"class" : "col col_selected"})

# sat_all_title = sat_all.find_all("a", attrs={"class" : "title"})

# count = 1

# for top10 in sat_all_title:
#     print(f"토요웹툰 {count}위 : {top10.get_text()}")
#     count += 1
#     if count >= 11:
#         break

days = ["월", "화", "수", "목", "금", "토", "일"]
days_webtoon = []

webtoon_all = soup.find("div", attrs={"class" : "list_area daily_all"})

daily_list = webtoon_all.find_all("div", attrs={"class" : "col"})

for day in range(7):
    days_webtoon.append(daily_list[day].find_all("a", attrs = {"class" : "title"}))

print("=" * 30)
print("네이버 웹툰 일일별 탑10 리스트")
print("=" * 30)

for i in range(7):
    print(f"{days[i]}요일 베스트 5")
    count = 1
    for j in days_webtoon[i]:
        print(f"{count}위 = {j.get_text()}")
        count += 1
        if count >= 6:
            break
    print("-" * 30)







# sat = soup.find_all("div", attrs={"class" : "col"})

# list = sat[1].find_all("a", attrs={"class":"title"})
# print(list)

# count = 0

# for top10 in list:
#     print(top10.get_text())
#     count += 1
#     if count >= 9:
#         break