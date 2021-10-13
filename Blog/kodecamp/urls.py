from django.urls import path
from .views import homeView,detailView

app_name = 'kodecamp'
urlpatterns = [
    path('', homeView,name = 'home'),
    path('detail/<int:post_id>/',detailView,name='detail')    
]
