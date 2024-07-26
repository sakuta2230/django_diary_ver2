from django.shortcuts import render
from sampleApp.model.health_score import HealthScore
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

def display_dashboard(request):
    # データの取得
    data = HealthScore.objects.all().values('overall_mood_score', 'work_text_score', 'weather_score', 'work_system_score', 'expenditure_score', 'sleep_duration_score')
    df = pd.DataFrame(data)

    # 最新の全体的な気分スコアを取得
    latest_overall_mood = df['overall_mood_score'].iloc[-1]

    # 基本的な統計量の計算
    mean_value = round(df['overall_mood_score'].mean(), 1)
    median_value = df['overall_mood_score'].median()
    max_value = df['overall_mood_score'].max()
    min_value = df['overall_mood_score'].min()

    # 変動率の計算
    latest_overall_mood_percentage = round((latest_overall_mood - mean_value) / mean_value * 100, 1)

    # 相関の計算
    correlation_matrix = df.corr()
    correlations = correlation_matrix['overall_mood_score'].drop('overall_mood_score')
    top_3_variables = correlations.abs().nlargest(3).index.tolist()

    # 目標変数の改善に関する指示
    top_variable_1, top_variable_2, top_variable_3 = top_3_variables
    top_variable_1_action = "上げる" if correlations[top_variable_1] > 0 else "下げる"
    top_variable_2_action = "上げる" if correlations[top_variable_2] > 0 else "下げる"
    top_variable_3_action = "上げる" if correlations[top_variable_3] > 0 else "下げる"

    # 相関係数を含む散布図の生成
    scatter_plots_html = []
    for variable in top_3_variables:
        correlation_coefficient = correlations[variable]
        scatter_fig = px.scatter(df, x=variable, y='overall_mood_score', title=f'{variable} vs 全体的な気分スコア<br>(相関係数: {correlation_coefficient:.2f})',
                                 labels={variable: variable, 'overall_mood_score': '全体的な気分スコア'}, height=350)
        scatter_fig.update_layout(title_font_size=14)
        scatter_plots_html.append(scatter_fig.to_html(full_html=False))

    # フィルタに基づく選択された散布図の生成
    selected_variable = request.GET.get('variable', 'work_text_score')
    selected_scatter_fig = px.scatter(df, x=selected_variable, y='overall_mood_score', title=f'{selected_variable} vs 全体的な気分スコア',
                                      labels={selected_variable: selected_variable, 'overall_mood_score': '全体的な気分スコア'}, height=400)
    selected_scatter_plot_html = selected_scatter_fig.to_html(full_html=False)

    # 最新値を示すヒストグラムの生成
    histogram_fig = px.histogram(df, x='overall_mood_score', title='全体的な気分スコアのヒストグラム',
                                 labels={'overall_mood_score': '全体的な気分スコア'}, height=400)
    histogram_fig.add_vline(x=latest_overall_mood, line_width=3, line_dash="dash", line_color="red",
                            annotation_text="最新", annotation_position="top right")
    histogram_html = histogram_fig.to_html(full_html=False)

    context = {
        'latest_overall_mood': latest_overall_mood,
        'latest_overall_mood_percentage': latest_overall_mood_percentage,
        'mean_value': mean_value,
        'median_value': median_value,
        'max_value': max_value,
        'min_value': min_value,
        'top_variable_1': top_variable_1,
        'top_variable_1_action': top_variable_1_action,
        'top_variable_2': top_variable_2,
        'top_variable_2_action': top_variable_2_action,
        'top_variable_3': top_variable_3,
        'top_variable_3_action': top_variable_3_action,
        'scatter_plot_1_html': scatter_plots_html[0],
        'scatter_plot_2_html': scatter_plots_html[1],
        'scatter_plot_3_html': scatter_plots_html[2],
        'selected_scatter_plot_html': selected_scatter_plot_html,
        'histogram_html': histogram_html,
    }

    return render(request, 'dashboard.html', context)
