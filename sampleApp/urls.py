from .views import detail1, dummy_view,index1,list1, login_view,login_yobi,signup_view,logout_view,comment_view,bunseki,honyaku,bunseki2,honyakucount
from .views import toppage,graph,honyakucount2,graph2,score1,addblog_view,creatediary_view,sleep_hst,expenditure_view,combined_graph,dummy_view
from .views import kensyou,edit_view,allscatter,dashboard,draft,wordcloud,delete_view
from django.urls import path
app='sampleApp'
urlpatterns=[
   path('',list1.list,name='list'),
   path('detail/<int:article_id>',detail1.detail,name='detail'),
   path('login',login_view.loginfunc,name='login'),
   path('logout',logout_view.logoutfunc,name='logout'),
   path('signup',signup_view.signupfunc,name='signup'),
   path('honyaku',honyaku.translation,name='honyaku'),
   path('bunseki2',bunseki2.count_word_frequency,name='word_frequency'),
   path('honyakucount',honyakucount.plot,name='honyakucount'),
   path('graph2',graph2.graph_view2,name='graph'),
   path('honyakucount2',honyakucount2.honyakucount2_view,name='honyakucount2'),
   path('detail/<int:article_id>/score',score1.analyze_sentiment,name="score1"),
   path('creatediary',creatediary_view.create_diary,name='creatediary'),
   path('kashika',sleep_hst.display_histogram,name='kashika'),
   path('kashika2',expenditure_view.display_scatter,name='kashika2'),
   path('combined',combined_graph.combined_graphs,name='combined'),
   path('dummy/', dummy_view.dummy, name='dummy'),
   path('edit/<int:article_id>',edit_view.edit,name='edit'),
   path('detail/<int:article_id>/comment/',comment_view.add_comment,name='comment'),
   path('allscatter',allscatter.display_scatterall,name='allscatter'),
   path('dashboard',dashboard.display_dashboard,name='dashboard'),
   path('draft',draft.draft_articles_view,name='draft'),
   path('wordcloud',wordcloud.generate_wordcloud,name='wordcloud'),
    path('article/<int:article_id>/delete/', delete_view.delete_article, name='delete_article'),


]

# path('',index1.index,name='index'),
# path('login_yobi',login_yobi.login_f,name='login_yobi'),
# path('detail/<int:article_id>/comment/',comment_view.add_comment,name='comment'),
#path('bunseki',bunseki.my_view,name='bunseki'),
# path('base3',toppage.toppage1,name='toppage'),
# path('addblog',addblog_view.add_blog,name='addblog'),
# path('kensyou',kensyou.kensyou,name='kensyou'),