from django.urls import path
from .views import *

app_name = "crudapp"

urlpatterns = [
    path(''             ,home        ,name='home'),
    path('add_author'  ,add_author  ,name='add_author'),
    path('del_author/<int:author_pk>'  ,del_author  ,name='del_author'),

    path('add_language',add_language,name='add_language'),
    path('del_language/<int:language_pk>'  ,del_language  ,name='del_language'),

    path('add_category',add_category,name='add_category'),
    path('del_category/<int:category_pk>'  ,del_category  ,name='del_category'),
    path('add_book'    ,add_book    ,name='add_book'),
    path('del_book/<int:book_pk>'    ,del_book    ,name='del_book'),
    path('update_book/<int:book_pk>'    ,update_book    ,name='update_book'),
]