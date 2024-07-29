import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # これを追加して非GUIバックエンドを使用する
from wordcloud import WordCloud, STOPWORDS
from django.http import HttpResponse
from django.shortcuts import render
from sampleApp.model.article1 import article
import io
from janome.tokenizer import Tokenizer
from collections import Counter
from itertools import islice

def generate_wordcloud(request):
    # すべての記事を取得
    articles = article.objects.all()
    text = ""

    for article_instance in articles:
        text += article_instance.private_text + " "
        text += article_instance.work_text + " "

    # 形態素解析を使用して重要な単語を抽出
    t = Tokenizer()
    words = []
    for token in t.tokenize(text):
        part_of_speech = token.part_of_speech.split(',')[0]
        if part_of_speech in ['名詞', '動詞', '形容詞']:  # 名詞、動詞、形容詞を抽出
            words.append(token.surface)

    # 2語のかたまりを生成
    bigrams = [' '.join(pair) for pair in zip(words, islice(words, 1, None))]
    all_words = words + bigrams

    # 出現頻度をカウント
    word_freq = Counter(all_words)

    # 日本語フォントを指定
    font_path = '/usr/share/fonts/opentype/ipafont-gothic/ipagp.ttf'  # 取得したパスを使用

    # WordCloud を生成 (最大語数を制限)
    wordcloud = WordCloud(font_path=font_path, stopwords=set(STOPWORDS), width=800, height=400, background_color='white', max_words=30).generate_from_frequencies(word_freq)

    # 画像を生成してレスポンスにする
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.close(fig)
    buffer.seek(0)
    
    return HttpResponse(buffer, content_type='image/png')
