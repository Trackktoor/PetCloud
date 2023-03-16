from django.contrib import admin
from django.urls import path
from news.views import *
from registr.views import *
from oblako.views import *

from registr.views import SignUp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registr/', SignUp.as_view(), name = 'signup'),
    #path('editprofile/', editprofile, name='editprofile'),
    path('news_form/', news_add),
    path('files_add/', filesadd, name='filesadd')

]
