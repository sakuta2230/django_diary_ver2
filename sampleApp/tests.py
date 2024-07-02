from django.test import TestCase
from faker import Faker
from sampleApp.model.article1 import article
import random
from django.db import transaction


class ArticleTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        fake = Faker()
        for _ in range(10):  # 10個の記事を生成
            article.objects.create(
                title=fake.sentence(),
                text=fake.paragraph(),
                date=fake.date(),
                sleep_duration=fake.time_delta(),
                work_system=random.choice(['出勤', '出張', 'テレワーク', '休み']),
                temperature=random.uniform(0, 40),
                humidity=random.uniform(0, 100),
                expenditure=random.uniform(0, 10000),
                overall_mood=random.randint(0, 10)
            )

    @transaction.atomic
    def test_article_count(self):
        # articleモデルのインスタンス数が10であることを確認するテスト
        self.assertEqual(article.objects.count(), 10)

