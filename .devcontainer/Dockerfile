# ベースイメージの指定
FROM python:3

# 環境変数の設定
ENV PYTHONUNBUFFERED 1

# 作業ディレクトリを作成し、そこに移動
WORKDIR /workspace

# 必要なシステムパッケージをインストール
RUN apt-get update && apt-get install -y fonts-ipafont-gothic

# ホストからコンテナに requirements.txt をコピーする
COPY ../requirements.txt .

# パッケージのインストール（ホストのファイルをマウントするので COPY は不要）
RUN pip install --no-cache-dir -r requirements.txt

# 残りのアプリケーションファイルをコンテナにコピーする
COPY . .

# アプリケーションを起動するコマンド
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
