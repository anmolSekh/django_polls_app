from django.urls import path
from . import view2

urlpatterns = [
    path("", view2.index, name="index"),
]