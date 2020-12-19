from django.urls import path

from . import views

urlpatterns = [
    path('', views.emp_mng_view, name="manage_view"),
    path('add', views.add_emp_view, name="add_view"),
    path('view/<int:id>', views.display_emp_view, name="display_view"),
]
