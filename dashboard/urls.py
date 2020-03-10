from django.urls import path

from dashboard import views
urlpatterns = [
    path("",views.open_dashboard_page,name="dashboard"),
    path("ajax/get_data/",views.getdata,name="getdata"),
    path("update_data/",views.update_data,name="update"),
    path("update_new/",views.update_data_new,name="new"),
    path("user_notification/",views.user_notification,name="user_notification"),

]
