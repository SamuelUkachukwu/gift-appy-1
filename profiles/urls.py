from django.urls import path
from . import views


urlpatterns = [
    path('', views.friends, name='friends'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('edit/<int:item_id>/', views.edit_wish, name='edit_wish'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('follow/<int:follow_id>', views.Follows.as_view(), name='follow'),
    path('delete/<int:item_id>/', views.delete_wish, name='delete_wish'),
]
