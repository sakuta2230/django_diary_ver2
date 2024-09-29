from django.shortcuts import redirect, render
from sampleApp.model.article1 import article
from datetime import datetime
import requests
from afinn import Afinn

import os
from dotenv import load_dotenv

load_dotenv()  # .env ファイルを読み込む

api_key = os.getenv("API_KEY")

# ここに他のコードを追加


api_url = 'https://api.openweathermap.org/data/2.5/weather'


diary_logger = logging.getLogger('diary')#ロガーを取得

def create_diary(request):    
    if request.method == 'POST':
        adtitle = request.POST['title']
        work_text = request.POST['work_text']
        private_text = request.POST['private_text']
        addate_str = request.POST['date']
        addate = datetime.strptime(addate_str, '%Y-%m-%d')
        sleep_duration = request.POST['sleep_duration']
        work_system = request.POST['work_system']
        expenditure = request.POST['expenditure']
        overall_mood = request.POST['overall_mood']
        overtime_hours = request.POST['overtime_hours']
        save_in_progress = 'save_in_progress' in request.POST  # 修正ポイント

        params = {
            'q': 'Tokyo',
            'appid': api_key,
            'dt': int(addate.timestamp())
        }
        response = requests.get(api_url, params=params)
        data = response.json()

        temperature = data['main']['temp']
        humidity = data['main']['humidity']

        article.objects.create(
            title=adtitle,
            work_text=work_text,
            private_text=private_text,
            date=addate,
            sleep_duration=sleep_duration,
            work_system=work_system,
            expenditure=expenditure,
            overall_mood=overall_mood,
            temperature=temperature,
            humidity=humidity,
            overtime_hours=overtime_hours,
            save_in_progress=save_in_progress
        )
        diary_logger.info(f"New diary entry created: {new_entry.title} on {new_entry.date}")#ロガーに記入
        
        return redirect('list')
    else:
        return render(request, 'creatediary.html', {})
