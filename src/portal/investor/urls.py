from django.urls import path, include

from . import views

app_name = 'investor'

urlpatterns = [
    path('dashboard/', views.InvestorDashboard.as_view(), name='dashboard'),
    path('project-list/',views.ProjectListView.as_view(), name='project_list'),
    path('buy-share/<str:pk>/',views.BuyShareView.as_view(), name='buy_share'),
    path('view-share/<str:pk>/',views.ViewShareDetail.as_view(), name='view_share'),
    path('share_detail/',views.ShareDetailView.as_view(), name='share_detail')
    

]
