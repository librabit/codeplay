# # import sys
# # from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QListWidgetItem
# # from PyQt5.QtGui import QPixmap
# # from PyQt5.QtCore import Qt
# # from googlesearch import search
# # from googleapiclient.discovery import build
# # import webbrowser

# # class YouTubeSearchApp(QWidget):
# #     def __init__(self):
# #         super().__init__()

# #         self.init_ui()

# #     def init_ui(self):
# #         self.setWindowTitle('YouTube 검색')
# #         self.setGeometry(100, 100, 800, 600)

# #         self.layout = QVBoxLayout()

# #         self.search_label = QLabel('YouTube에서 검색할 내용을 입력하세요:')
# #         self.layout.addWidget(self.search_label)

# #         self.search_input = QLineEdit()
# #         self.search_input.returnPressed.connect(self.search_youtube)
# #         self.layout.addWidget(self.search_input)

# #         self.search_button = QPushButton('검색')
# #         self.search_button.clicked.connect(self.search_youtube)
# #         self.layout.addWidget(self.search_button)

# #         self.results_list = QListWidget()
# #         self.results_list.itemClicked.connect(self.play_youtube_video)
# #         self.layout.addWidget(self.results_list)

# #         self.setLayout(self.layout)

# #     def search_youtube(self):
# #         query = self.search_input.text()
# #         results = self.fetch_youtube_results(query)

# #         self.results_list.clear()
# #         for video in results:
# #             title = video['snippet']['title']
# #             link = f"https://www.youtube.com/watch?v={video['id']['videoId']}"
# #             thumbnail_url = video['snippet']['thumbnails']['default']['url']

# #             item = QListWidgetItem(self.results_list)
# #             item.setText(title)
# #             item.setToolTip(link)
# #             item.setTextAlignment(Qt.AlignCenter)

# #             thumbnail_label = QLabel()
# #             thumbnail_label.setPixmap(QPixmap(self.fetch_thumbnail(thumbnail_url)))
# #             self.results_list.setItemWidget(item, thumbnail_label)

# #     def fetch_youtube_results(self, query, num_results=5):
# #         api_key = 'AIzaSyARAx1FBa3fBbnGmC1azvd4-e85Hak1l8I'
# #         youtube = build('youtube', 'v3', developerKey=api_key)

# #         request = youtube.search().list(
# #             q=query,
# #             part='id,snippet',
# #             type='video',
# #             maxResults=num_results
# #         )

# #         response = request.execute()
# #         return response.get('items', [])

# #     def fetch_thumbnail(self, url):
# #         # Implement a proper image loading method here (e.g., using requests or QImage)
# #         # For simplicity, this example assumes you have a local image file
# #         return 'local_thumbnail.jpg'

# #     def play_youtube_video(self, item):
# #         link = item.toolTip()
# #         webbrowser.open(link)


# # if __name__ == '__main__':
# #     app = QApplication(sys.argv)
# #     window = YouTubeSearchApp()
# #     window.show()
# #     sys.exit(app.exec_())


# import matplotlib.pyplot as plt
# import numpy as np

# # 데이터 생성
# x = np.linspace(-2*np.pi, 2*np.pi, 100)  # -2파이부터 2파이까지 100개의 점으로 나눈 범위
# y = np.sin(x)

# # 그래프 그리기
# plt.plot(x, y, label='sin(x)')  # 선 그래프 그리기
# plt.title('Sine Function')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend()  # 범례 추가
# plt.grid(True)  # 그리드 표시

# # 그래프 표시
# plt.show()

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# 3차원 그래프를 그리기 위한 subplot 생성
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 데이터 생성
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))

# 3차원 그래프 그리기
ax.plot_surface(x, y, z, cmap='viridis')

# 그래프 축 레이블 설정
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Surface Plot')

# 그래프 표시
plt.show()

