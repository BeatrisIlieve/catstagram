from django.urls import path

from catstagram.common.views import IndexViewWithTemplate, like_photo, share_photo, comment_photo

urlpatterns = (
    path('', IndexViewWithTemplate.as_view(), name='index'),
    path('like/<int:photo_id>/', like_photo, name='like photo'),
    path('share/<int:photo_id>/', share_photo, name='share photo'),
    path('comment/<int:photo_id>/', comment_photo, name='comment photo'),
)