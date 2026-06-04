from django.urls import path
from .views import PayPeriodListCreateView, PayPeriodDetailView
from .timecard_views import TimecardView, PunchCreateView, PunchDetailView

urlpatterns = [
    path("", PayPeriodListCreateView.as_view(), name="pay-period-list"),
    path("<int:pk>/", PayPeriodDetailView.as_view(), name="pay-period-detail"),
]

timecard_urlpatterns = [
    path("<int:user_id>/", TimecardView.as_view(), name="timecard"),
    path("<int:user_id>/punches/", PunchCreateView.as_view(), name="punch-create"),
    path("punches/<int:punch_id>/", PunchDetailView.as_view(), name="punch-detail"),
]
