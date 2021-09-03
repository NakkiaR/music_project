from django.urls import path
from . import views

urlpatterns = [
    path('music/', views.SongList.as_view()),
    path('music/<int:pk>/', views.SongDetail.as_view()) 
]

    # path('<int:player_id>', views.detail, name="detail"),

    # def detail(request, player_id):
    # player_from_db = Player.objects.get(pk=player_id)
    # return render(request, 'players/detail.html', {'player': player_from_db})
