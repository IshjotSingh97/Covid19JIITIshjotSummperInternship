from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('urgent',views.urgent,name='urgent'),
    path('techstack',views.techstack,name='techstack'),
    path('trackingtable',views.trackingtable,name='trackingtable'),
    path('getnews',views.getnews,name='getnews'),
    path('mythbusters',views.mythbusters,name='mythbusters'),
    path('acknowledgement',views.acknowledgement,name='acknowledgement'),
    path('comments',views.comments,name='comments'),
    path('getlike',views.getlike,name='getlike')
]