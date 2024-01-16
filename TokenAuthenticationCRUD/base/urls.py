from django.urls import path,include
from .views import StudentCrud,CustomToken
from rest_framework.routers import DefaultRouter
# from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()

router.register('',StudentCrud,basename = 'student_crud')


urlpatterns =[
    path('',include(router.urls)),
    # path('gettoken',obtain_auth_token)
    path('gettoken',CustomToken.as_view(),name='token'),
]