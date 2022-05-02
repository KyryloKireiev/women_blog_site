from django.urls import path, re_path
from women.views import (about,
                         archive,
                         logout_user,
                         user_test_request)

from women.views import (
    WomenList,
    WomenCategory,
    PostDetail,
    AddArticle,
    SignUpUser,
    LoginUser,
    ContactFormView,
)

urlpatterns = [
#    path('', index, name="home"),
    path('', WomenList.as_view(), name="home"),
    path('post/<int:post_id>/', PostDetail.as_view(), name='post_detail'),
#    path('post/<int:post_id>/', post_detail, name='post_detail'),
#    path('category/<int:cat_id>/', show_category, name="category"),
    path('category/<int:cat_id>/', WomenCategory.as_view(), name="category"),
    path('about/', about, name="about"),
#    path('add/', add_article, name="add_article"),
    path("add/", AddArticle.as_view(), name="add_article"),
    path('feedback/', ContactFormView.as_view(), name='feedback'),
    path('sign_up/', SignUpUser.as_view(), name='sign_up'),
    path('sign_in/', LoginUser.as_view(), name='sign_in'),
    path('logout/', logout_user, name="logout"),
    path('test_user/', user_test_request, name="test_user"),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
]
