from django.urls import path

from . import views

urlpatterns = [
    path('',views.IndexView.as_view()),
    path('series/',views.SeriesView.as_view()),
    path('serie/<int:serie_id>',views.SerieDetailView.as_view())
]