from django.urls import path
from . import views_fbv, views_cbv

urlpatterns = [
    path('companies/', views_fbv.company_list),
    path('vacancies/', views_cbv.VacancyList.as_view()),
]
