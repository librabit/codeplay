import tkinter as tk
from tkinter import ttk
import requests
from bs4 import BeautifulSoup
import webbrowser

def search_youtube():
    query = entry.get()
    if query:
        url = f"https://www.youtube.com/results?search_query={query}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # 검색 결과에서 비디오 제목과 링크 추출
        video_links = soup.select('a.yt-uix-tile-link')
        results = [(link['title'], 'https://www.youtube.com' + link['href']) for link in video_links[:5]]

        # 결과를 GUI에 표시
        result_text.delete(1.0, tk.END)
        for i, (title, link) in enumerate(results, start=1):
            result_text.insert(tk.END, f"{i}. {title}\n")
            result_text.insert(tk.END, f"{link}\n\n", f"link_{i}")

# 클릭 가능한 링크를 열기 위한 콜백 함수
def open_link(event):
    for i in range(1, 6):
        if result_text.tag_ranges(f"link_{i}"):
            start, end = result_text.tag_ranges(f"link_{i}")
            if start <= event.x and event.x <= end:
                link = result_text.get(start, end)
                webbrowser.open(link)
                break

# 윈도우 생성
window = tk.Tk()
window.title("YouTube 검색")

# 레이블, 엔트리, 검색 버튼 생성
label = ttk.Label(window, text="검색어:")
label.grid(row=0, column=0, padx=10, pady=10)

entry = ttk.Entry(window, width=30)
entry.grid(row=0, column=1, padx=10, pady=10)

search_button = ttk.Button(window, text="검색", command=search_youtube)
search_button.grid(row=1, column=0, columnspan=2, pady=10)

# 검색 결과를 표시할 텍스트 박스 생성
result_text = tk.Text(window, wrap=tk.WORD, height=15, width=60)
result_text.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# 클릭 가능한 링크를 열기 위한 이벤트 바인딩
result_text.bind("<Button-1>", open_link)

# GUI 실행
window.mainloop()
