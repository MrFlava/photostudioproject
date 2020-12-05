from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.HomePage, name='homepage'),

    path('photo_centres', views.PhotoCentres, name='photo-centres'),
    path('photo_center/<center_id>/offices', views.PhotoCentresOffice, name='photo-center-offices'),
    path('photo_center/<center_id>/stands', views.PhotoCentresStands, name='photo-center-stands'),

    re_path(r'office/(?P<office_id>\d+)/(?P<date_from>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z)/(?P<date_to>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z)/orders$', views.PhotoOfficeOrders, name='office-orders'),
    re_path(r'^office/(?P<office_id>\d+)/(?P<priority>ORDINARY_PRIORITY|URGENT_PRIORITY)/(?P<date_from>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z)/(?P<date_to>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z)/orders$', views.PhotoOfficeStatusOrders, name='office-status-orders'),
    re_path(r'^office/(?P<office_id>\d+)/(?P<priority>ORDINARY_PRIORITY|URGENT_PRIORITY)/(?P<date_from>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z)/(?P<date_to>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z)/orders/film_development$', views.PhotoOfficeFilmDevelopmentOrders, name='printing-and-development-orders'),
    re_path(r'^office/(?P<office_id>\d+)/(?P<priority>ORDINARY_PRIORITY|URGENT_PRIORITY)/(?P<date_from>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z)/(?P<date_to>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z)/orders/printing_and_development$', views.PhotoOfficePrintingDevelopmentOrders, name='printing-and-development-orders'),
    re_path(r'office/(?P<office_id>\d+)/(?P<date_from>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z)/(?P<date_to>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z)/item_orders$', views.PhotoOfficeItemOrders, name='office-item-orders'),
    path('office/<int:office_id>/<int:photos_quantity>/orders/customer', views.PhotoOfficeOrderCustomer, name='orders-customer'),
    path('office/<int:office_id>/<int:item_quantity>/items', views.PhotoOfficeItemProviders, name='office-item-providers'),
    path('office/<int:office_id>/popular_items', views.PhotoOfficePopularItems, name='office-popular-items'),

    re_path(r'^stand/(?P<stand_id>\d+)/(?P<date_from>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z)/(?P<date_to>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z)/orders$', views.PhotoStandStatusOrders, name='stand-status-orders'),
    re_path(r'^stand/(?P<stand_id>\d+)/(?P<date_from>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z)/(?P<date_to>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z)/orders/film_development$', views.PhotoStandFilmDevelopmentOrders, name='stand-film-development-orders'),
    re_path(r'^stand/(?P<stand_id>\d+)/(?P<date_from>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z)/(?P<date_to>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z)/orders/printing_and_development$', views.PhotoStandPrintingDevelopmenttOrders, name='stand-printing-dev-orders'),
    path('stand/<int:stand_id>/(?P<date_from>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z)/(?P<date_to>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z)/orders$', views.PhotoStandOrders, name='stand-orders'),
    path('stand/<int:stand_id>/item_orders', views.PhotoStandItemOrders, name='stand-item-orders'),
    path('stand/<int:stand_id>/<int:item_quantity>/items', views.PhotoStandItemProviders, name='stand-item-providers'),

]
