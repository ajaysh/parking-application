from django.conf.urls import url
from parking_reservation import views

app_name = 'parking_reservation'

urlpatterns = [
    url(r'^$', views.ParkingListView.as_view(), name='list'),
                                              # This name List is for the URL template tag
    url(r'^(?P<pk>\d+)/$', views.ParkingDetailview.as_view(), name='detail'),
    #   <pk> - primary key
    #   [-\w+] alphanumeric (alphabetic and numeric) characters
    #   primary key followed by one or more alphanumeric number
    url(r'^create/', views.ParkingCreateView.as_view(), name='create'),
    url(r'^update/(?P<pk>\d+)/$', views.ParkingUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', views.ParkingDeleteView.as_view(), name='delete'),
    url(r'^createslot/', views.ParkingslotCreateView.as_view(), name='createslot'),
    url(r'^updateslot/(?P<pk>\d+)/$', views.ParkingslotUpdateView.as_view(), name='updateslot'),

]
