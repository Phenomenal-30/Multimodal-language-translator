from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", views.home, name="index"),
    path('get_new_value/', views.get_new_value, name='get_new_value'),
    path('translate_speech/', views.translate_speech, name='translate_speech'),
    path('get_voice/', views.get_voice, name='get_voice'),
]