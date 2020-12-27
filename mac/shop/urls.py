from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path("",views.index,name="ShopHome"),
    path("about/",views.about,name="AboutUs"),
    path("contact/",views.contact,name="ContactUs"),
    path("tracker/",views.tracker,name="TrackStatus"),
    path("search/",views.search,name="Search"),
    path("products/<int:myid>",views.prodview,name="ProdView"),
    path("checkout/",views.checkout,name="CheckOut"),
]