from django.urls import path
from .views import dashboard,JobsView,JobsDetailView,JobsUpdateView

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("jobs/",JobsView.as_view(),name="jobs"),
    path("jobs/f=<int:pk>",JobsDetailView.as_view(),name="jobview"),
    path("jobs/update/f=<int:pk>",JobsUpdateView.as_view(),name="jobupdate"),
    
]
