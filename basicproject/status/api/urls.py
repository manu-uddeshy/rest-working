from django.urls import path
from .views import StatusAPIView

urlpatterns = [
    path('',StatusAPIView.as_view()),
    # path('create/', StatusCreateAPIView.as_view()),
    # path('<int:pk>/', StatusDetailAPIView.as_view()),
    # path('<int:pk>/update', StatusUpdateAPIView.as_view()),
    # path('<int:pk>/delete',StatusDeleteAPIView.as_view()),
]
