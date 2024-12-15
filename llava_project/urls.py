from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')  # 템플릿 렌더링

urlpatterns = [
    path('', home, name='home'),  # 기본 경로 처리
    path('admin/', admin.site.urls),
    path('api/', include('llava_app.urls')),
]
