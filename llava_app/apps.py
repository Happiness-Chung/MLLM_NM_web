from django.apps import AppConfig

class LlavaAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # 기본 자동 ID 필드
    name = 'llava_app'  # 앱 이름
    verbose_name = 'LLaVA Application'  # 관리자 페이지에서 표시할 앱 이름
