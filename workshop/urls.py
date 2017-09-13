# created by Chirath R, chirath.02@gmail.com
from django.conf.urls import url

from workshop.views import WorkshopRegisterView, WorkshopDetailView

urlpatterns = [
    url(r'^(?P<workshop_id>[0-9]+)/$', WorkshopDetailView.as_view(), name='workshop_detail'),
    url(r'^(?P<workshop_id>[0-9]+)/register/$', WorkshopRegisterView.as_view(), name='workshop_register'),
]
