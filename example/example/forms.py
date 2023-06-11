from django import forms

from django_tom_select import forms as tsForms

from . import models


class AuthorWidget(tsForms.ModelTomSelectWidget):
    search_fields = ["username__istartswith", "email__icontains"]


class CoAuthorsWidget(tsForms.ModelTomSelectMultipleWidget):
    search_fields = ["username__istartswith", "email__icontains"]


class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = "__all__"
        widgets = {
            "author": AuthorWidget,
            "co_authors": CoAuthorsWidget,
            "category": tsForms.TomSelectWidget
        }
