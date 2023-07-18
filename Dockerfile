FROM python:3.9

# タイムゾーン設定
ENV TZ=Asia/Tokyo 

# 必要なライブラリをインストール
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    xvfb \
    libglib2.0-0 \
    libnss3 \
    libgconf-2-4 \
    libfontconfig1

# Google Chromeをインストール
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install

# ChromeDriverをダウンロード＆インストール
RUN wget https://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip -d /usr/bin
RUN chmod +x /usr/bin/chromedriver

# プロジェクトディレクトリを作成
WORKDIR /app

# 必要なファイルをコピー (例えばyour_script.pyとrequirements.txt)
COPY your_script.py /app
COPY requirements.txt /app

# Pythonライブラリをインストール
RUN pip install -r /app/requirements.txt

# スクリプト実行
CMD ["python", "/app/your_script.py"]
