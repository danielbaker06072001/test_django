from django.urls import  path 

from pages.views import home_view, contact_view, about_view
from products.views import product_create_view,product_detail_view, dynamic_lookup_view,product_list_view

app_name = 'products'
urlpatterns = [
    path('list/', product_list_view, name = 'product_list'),
    path('create/', product_create_view),
    path('detail/', product_detail_view),
    path('render/<int:my_id>/', dynamic_lookup_view, name = 'render'),
    
]
