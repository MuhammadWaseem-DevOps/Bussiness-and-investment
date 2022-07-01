from django.urls import path, include

from . import views

app_name = 'investor'

urlpatterns = [
    path('dashboard/', views.InvestorDashboard.as_view(), name='dashboard'),
    path('project-list/',views.ProjectListView.as_view(), name='project_list'),
    path('select-share/',views.SelectShareView.as_view(), name='select_share'),
    path('share_detail/',views.ShareDetailView.as_view(), name='share_detail')
    

]
