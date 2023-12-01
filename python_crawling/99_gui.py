import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QListWidgetItem
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from googlesearch import search
from googleapiclient.discovery import build
import webbrowser

class YouTubeSearchApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('YouTube 검색')
        self.setGeometry(100, 100, 800, 600)

        self.layout = QVBoxLayout()

        self.search_label = QLabel('YouTube에서 검색할 내용을 입력하세요:')
        self.layout.addWidget(self.search_label)

        self.search_input = QLineEdit()
        self.search_input.returnPressed.connect(self.search_youtube)
        self.layout.addWidget(self.search_input)

        self.search_button = QPushButton('검색')
        self.search_button.clicked.connect(self.search_youtube)
        self.layout.addWidget(self.search_button)

        self.results_list = QListWidget()
        self.results_list.itemClicked.connect(self.play_youtube_video)
        self.layout.addWidget(self.results_list)

        self.setLayout(self.layout)

    def search_youtube(self):
        query = self.search_input.text()
        results = self.fetch_youtube_results(query)

        self.results_list.clear()
        for video in results:
            title = video['snippet']['title']
            link = f"https://www.youtube.com/watch?v={video['id']['videoId']}"
            thumbnail_url = video['snippet']['thumbnails']['default']['url']

            item = QListWidgetItem(self.results_list)
            item.setText(title)
            item.setToolTip(link)
            item.setTextAlignment(Qt.AlignCenter)

            thumbnail_label = QLabel()
            thumbnail_label.setPixmap(QPixmap(self.fetch_thumbnail(thumbnail_url)))
            self.results_list.setItemWidget(item, thumbnail_label)

    def fetch_youtube_results(self, query, num_results=5):
        api_key = 'AIzaSyARAx1FBa3fBbnGmC1azvd4-e85Hak1l8I'
        youtube = build('youtube', 'v3', developerKey=api_key)

        request = youtube.search().list(
            q=query,
            part='id,snippet',
            type='video',
            maxResults=num_results
        )

        response = request.execute()
        return response.get('items', [])

    def fetch_thumbnail(self, url):
        # Implement a proper image loading method here (e.g., using requests or QImage)
        # For simplicity, this example assumes you have a local image file
        return 'local_thumbnail.jpg'

    def play_youtube_video(self, item):
        link = item.toolTip()
        webbrowser.open(link)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = YouTubeSearchApp()
    window.show()
    sys.exit(app.exec_())
