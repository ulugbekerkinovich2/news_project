from django.urls import path

from news_app import views

urlpatterns = [
    path('all/', views.NewsList.as_view(), name='news_list_view'),
    path('all/<int:id>/', views.news_detail, name='news_detail_view'),
    path('', views.index_page, name='index_page'),
    path('contact/', views.ContactPageView.as_view(), name='contact')
]
