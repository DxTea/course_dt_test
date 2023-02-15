from django.urls import path
from app.internal.transport.rest.handlers import me_endpoint

urlpatterns = [
    path('me/<int:telegram_id>/', me_endpoint, name="me_endpoint")
]
