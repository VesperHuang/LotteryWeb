from django.conf.urls import url
from django.contrib import admin
from . import view
from analysis import views as analysis_views
from mylottery import views as mylottery_views

urlpatterns = [
    url(r'^Hello$', view.hello),
    url(r'^admin/',admin.site.urls),
    url(r'^number_count$', analysis_views.number_count),
    url(r'^mylottery$', mylottery_views.mylottery),
    url(r'^mylottery_add$', mylottery_views.mylottery_add),
    url(r'^mylottery_adding$', mylottery_views.mylottery_adding),
]
