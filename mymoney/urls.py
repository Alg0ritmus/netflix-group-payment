from django.urls import path

from . import views

app_name = "mymoney"
urlpatterns = [
    path('', views.index, name='index'),
    path('api/vydavky/<int:vydavky_id>/',views.dash_board_get_Vydavky,name="vydavky"),
    path('api/pridaj_vydavky/',views.pridaj_vydavky,name="pridaj_vydavky"),
    path('api/pridaj_polozky/<int:pridaj_polozky_id>/',views.pridaj_polozky,name="pridaj_polozky"),
    path('api/vymaz_polozky/<int:vymaz_polozky_id>/',views.vymaz_polozky,name="vymaz_polozky"),
    path('api/uprav_polozky/<int:edit_polozky_id>/',views.uprav_polozky,name="uprav_polozky"),
]