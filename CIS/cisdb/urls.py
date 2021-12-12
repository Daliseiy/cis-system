from django.urls import path,include
from django.contrib import admin
from . import views


urlpatterns = [ 
    path('create/',views.CitizenCreate.as_view(),name='create_data') ,
    path('update/<int:pk>/',views.CitizenUpdate.as_view(),name='update_data'),
    path('delete/<int:pk>/',views.CitizenDelete.as_view(),name='delete_data'),
    path('detail/<int:pk>/',views.CitizenDetail.as_view(),name="detail_data"),
    path('home/',views.HomeView.as_view(),name='home'),
    path('found/',views.FoundView.as_view(),name='found'),
    path('match/',views.match_view,name="match_data"),
    path('filter/',views.FIlterView,name="filter_view"),
    path('',views.citizen_search,name='search_data'),
    path('find/',include('cisdb.api.urls'))
]
