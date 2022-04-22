from django.urls import path, re_path
from women.views import (index,
                         categories,
                         archive,
                         about,
                         add_article,
                         feedback,
                         sign_up,
                         sign_in,
                         post_detail,
                         show_category)

urlpatterns = [
    path('', index, name="home"),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('category/<int:cat_id>/', show_category, name="category"),
    path('about/', about, name="about"),
    path('add/', add_article, name="add_article"),
    path('feedback/', feedback, name='feedback'),
    path('sign_up', sign_up, name='sign_up'),
    path('sign_in', sign_in, name='sign_in'),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
]
