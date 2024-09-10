from .views import detail_view2,list2, login_view2,signup_view2,logout_view2
from .views import creatediary_view2,dummy_view2
from .views import edit_view2,dashboard_view,draft_view,delete_view2,wordcloud,rule
from django.urls import path
app='sampleApp'
urlpatterns=[
   path('',list2.list,name='list'),
   path('detail/<int:article_id>',detail_view2.detail,name='detail'),
   path('login',login_view2.loginfunc,name='login'),
   path('logout',logout_view2.logoutfunc,name='logout'),
   path('signup',signup_view2.signupfunc,name='signup'),
   path('creatediary',creatediary_view2.create_diary,name='creatediary'),
   path('dummy/', dummy_view2.dummy, name='dummy'),
   path('edit/<int:article_id>',edit_view2.edit,name='edit'),
   path('dashboard',dashboard_view.display_dashboard,name='dashboard'),
   path('draft',draft_view.draft_articles_view,name='draft'),
   path('article/<int:article_id>/delete/', delete_view2.delete_article, name='delete_article'),
   path('wordcloud',wordcloud.generate_wordcloud,name='wordcloud'),
   path('rule',rule.rule_view,name='rule')

]

# path('',index1.index,name='index'),
# path('login_yobi',login_yobi.login_f,name='login_yobi'),
# path('detail/<int:article_id>/comment/',comment_view.add_comment,name='comment'),
#path('bunseki',bunseki.my_view,name='bunseki'),
# path('base3',toppage.toppage1,name='toppage'),
# path('addblog',addblog_view.add_blog,name='addblog'),
# path('kensyou',kensyou.kensyou,name='kensyou'),