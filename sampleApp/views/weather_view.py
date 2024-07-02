def calculate_health_score(temperature, humidity):
    # 最高の健康スコアの基準値
    best_temperature = 25  # ℃
    best_humidity = 50  # %

    # 温度指数と湿度指数の計算
    temperature_index = abs(temperature - best_temperature)
    humidity_index = abs(humidity - best_humidity)

    # 健康スコアの計算
    health_score = 100 - temperature_index - humidity_index

    # 健康スコアが0未満にならないように調整
    health_score = max(health_score, 0)

    return health_score