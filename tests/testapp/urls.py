from django.urls import include, path

from .forms import (
    AddressChainedTomSelectWidgetForm,
    AlbumModelTomSelectWidgetForm,
    HeavyTomSelectMultipleWidgetForm,
    HeavyTomSelectWidgetForm,
    ModelTomSelectTagWidgetForm,
    TomSelectWidgetForm,
)
from .views import TemplateFormView, heavy_data_1, heavy_data_2

urlpatterns = [
    path(
        "tom_select_widget",
        TemplateFormView.as_view(form_class=TomSelectWidgetForm),
        name="tom_select_widget",
    ),
    path(
        "heavy_tom_select_widget",
        TemplateFormView.as_view(form_class=HeavyTomSelectWidgetForm),
        name="heavy_tom_select_widget",
    ),
    path(
        "heavy_tom_select_multiple_widget",
        TemplateFormView.as_view(
            form_class=HeavyTomSelectMultipleWidgetForm, success_url="/"
        ),
        name="heavy_tom_select_multiple_widget",
    ),
    path(
        "model_tom_select_widget",
        TemplateFormView.as_view(form_class=AlbumModelTomSelectWidgetForm),
        name="model_tom_select_widget",
    ),
    path(
        "model_tom_select_tag_widget",
        TemplateFormView.as_view(form_class=ModelTomSelectTagWidgetForm),
        name="model_tom_select_tag_widget",
    ),
    path(
        "model_chained_tom_select_widget",
        TemplateFormView.as_view(form_class=AddressChainedTomSelectWidgetForm),
        name="model_chained_tom_select_widget",
    ),
    path("heavy_data_1", heavy_data_1, name="heavy_data_1"),
    path("heavy_data_2", heavy_data_2, name="heavy_data_2"),
    path("tomselect/", include("django_tom_select.urls")),
]
