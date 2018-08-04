from django.conf.urls import url
from django.contrib import admin
from . import view
from analysis import views as analysis_views
from mylottery import views as mylottery_views

urlpatterns = [
    url(r'^index$', view.index),
    url(r'^admin/',admin.site.urls),
    url(r'^number_count$', analysis_views.number_count),
    url(r'^number_grid$', analysis_views.number_grid),
    url(r'^user_sign_in$', view.user_sign_in),
    url(r'^user_sign_out$', view.user_sign_out),
    url(r'^user_reg$', mylottery_views.user_reg),
    url(r'^firebase_operate$', mylottery_views.firebase_operate),
    url(r'^mylottery$', mylottery_views.mylottery),
    url(r'^mylottery_add$', mylottery_views.mylottery_add),
    url(r'^mylottery_adding$', mylottery_views.mylottery_adding),
    url(r'^mylottery_add_ajax$', mylottery_views.mylottery_add_ajax),
    url(r'^ajax_post$', mylottery_views.ajax_post),
    url(r'^ajax_category$', mylottery_views.ajax_category),
]
