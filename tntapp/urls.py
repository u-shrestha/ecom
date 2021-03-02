from django.urls import path
from .views import *

app_name = "tntapp"
urlpatterns = [
    	
	path('', ProductListView.as_view(), name='productlist'),
	path('product/<int:pk>/order', ProductDetailView.as_view(), name="productdetail"),

]
