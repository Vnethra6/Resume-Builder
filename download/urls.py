from django.conf.urls import url
from .views import GeneratePdf

urlpatterns = [
    url('', GeneratePdf.as_view(), name='download')
]
