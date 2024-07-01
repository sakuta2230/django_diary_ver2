from faker import Faker
from sampleApp.model.article1 import article  # モデルをインポートする際にモジュール名を変更
import random
from django.shortcuts import redirect
from datetime import datetime

def dummy(request):
    fake = Faker('ja_JP')  # 日本語のダミーデータを生成するためにロケールを設定
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 7, 31)

    for _ in range(10):  # 10個の記事を生成
        article.objects.create(
            title=fake.sentence(),
            work_text=fake.paragraph(nb_sentences=5),  # 仕事に関する内容
            private_text=fake.paragraph(nb_sentences=5),  # プライベートに関する内容
            date=fake.date_between(start_date=start_date, end_date=end_date),  # 期間を指定
            sleep_duration=random.randint(0, 12),  # PositiveSmallIntegerFieldに合わせて修正
            work_system=random.choice(['出勤', '出張', 'テレワーク', '休み']),
            temperature=round(random.uniform(0, 40), 2),  # 気温
            humidity=round(random.uniform(0, 100), 2),  # 湿度
            expenditure=random.randint(0, 50),  # PositiveSmallIntegerFieldに合わせて修正
            overall_mood=random.randint(0, 10),
            overtime_hours=random.randint(0, 24),  # 残業時間を0から24の範囲で設定
            save_in_progress=False  # 下書きとして保存するかどうか
        )
    return redirect('list')



