from django.urls import path,include
from .views import ActorCRUD,MovieCRUD
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('actor',ActorCRUD,basename='actor')
router.register('movie',MovieCRUD,basename='movie_url')


urlpatterns = [
    path('',include(router.urls)),
]