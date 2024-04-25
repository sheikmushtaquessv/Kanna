from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',data, name='data'),
    path('scrape/', scrape_data, name='Naukri'),
]
