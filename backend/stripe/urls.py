from django.urls import include, path
from . import views

urlpatterns = []

urlpatterns += [
    path('buy/<uuid:uuid>/', views.BuyView.as_view()),
    # path('buy', views.BuyView.as_view()),
]
