from django.urls import path

from . import views
app_name = 'fridgelookup'
urlpatterns = [
    # ex: /fridgelookup/
    path('', views.index, name='index'),
    # ex: /fridgelookup/5/results/
    path('<int:fridge_id>/results/', views.results, name='results'),
    # ex: /fridgelookup/5/update/
    path('<int:fridge_id>/update/', views.update, name='update'),
    # ex: /fridgelookup/5/details/
    path('<int:fridge_id>/', views.detail, name='detail')
]