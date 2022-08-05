from django.urls import path, include

from rest_framework.routers import SimpleRouter, DefaultRouter

from profiles_api import views


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet, base_name='profile')
router.register('feed', views.UserProfileFeedViewSet, base_name='feed')

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view(), name='login'),
    path('', include(router.urls)),
    #router.urls,
    path('home/', views.index, name='index')
]
