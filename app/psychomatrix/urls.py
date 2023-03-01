from django.urls import path, re_path

from .views import SquareOfPythagorasViewSet

urlpatterns = [
    path('api/', SquareOfPythagorasViewSet.as_view({'post': 'create'})),
    # re_path(r'^(?P<date>\d{4}-\d{2}-\d{2})$', views.index, name='date'),
]
