from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.BookCreateView.as_view(), name="book-create"),
    path("<pk>/", views.BookUpdateView.as_view(), name="book-update"),
    path("tomselect/", include("django_tom_select.urls")),
    path("admin/", admin.site.urls),
]
