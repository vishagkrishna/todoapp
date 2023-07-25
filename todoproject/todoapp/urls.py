from . import views
from django.urls import path

urlpatterns = [
path('',views.add,name='add'),
    # path('details',views.details,name='details')
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('fview',views.Tasklistview.as_view(),name='fview'),
    path('dview/<int:pk>/',views.Taskdetailview.as_view(),name='dview'),
    path('uview/<int:pk>/',views.Taskupdateview.as_view(),name='uview'),
    path('deview/<int:pk>/',views.Taskdeleteview.as_view(),name='deview'),
]