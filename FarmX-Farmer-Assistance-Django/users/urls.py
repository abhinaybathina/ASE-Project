from django.urls import path
from weather import views as weather_views
from farm import views as farm_views
from blog import views as blog_views
from announcements import views as announcement_views
from . import views


urlpatterns = [
    path('weather/', weather_views.weather_request, name='WeatherRequest'),
    path('weather/response/', weather_views.weather_response, name='WeatherResponse'),
    path('farm/', farm_views.FarmListView.as_view(), name='farm-list'),
    path('farm/<int:pk>/', farm_views.FarmDetailView.as_view(), name='farm-detail'),
    path('farm/new/', farm_views.FarmCreateView.as_view(), name='farm-create'),
    path('farm/<int:pk>/update/', farm_views.FarmUpdateView.as_view(), name='farm-update'),
    path('farm/<int:pk>/delete/', farm_views.FarmDeleteView.as_view(), name='farm-delete'),
    path('blog/new/', blog_views.PostCreateView.as_view(), name='post-create'),
    path('blog/', blog_views.PostListView.as_view(), name='post-list'),
    path('blog/<int:pk>/', blog_views.PostDetailView.as_view(), name='post-detail'),
    path('blog/<int:pk>/update/', blog_views.PostUpdateView.as_view(), name='post-update'),
    path('blog/<int:pk>/delete/', blog_views.PostDeleteView.as_view(), name='post-delete'),
    path('staff-announcement/', announcement_views.AnnouncementsListView.as_view(), name='announcements-list'),
    path('staff-announcement/<int:pk>/', announcement_views.AnnouncementsDetailView.as_view(), name='announcement-detail'),
    path('staff-announcement/new/', announcement_views.AnnouncementsCreateView.as_view(), name='announcement-create'),
    path('staff-announcement/<int:pk>/update/', announcement_views.AnnouncementsUpdateView.as_view(), name='announcement-update'),
    path('staff-announcement/<int:pk>/delete/', announcement_views.AnnouncementsDeleteView.as_view(), name='announcement-delete'),
    path('announcements/', views.announcements_list, name='user-list-announcements'),
    path('query-farm/', views.query_farm_data, name='QueryFarmData'),
    path('crop-wise-details/', views.yield_estimates_staff, name='CropWiseData')
]

