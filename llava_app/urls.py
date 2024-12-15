from django.urls import path
from . import views  # 뷰 함수 임포트

urlpatterns = [
    path('process_input/', views.process_input, name='process_input'),  # 입력 처리 API
]