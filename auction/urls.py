from django.urls import path
from .views import items_api, item_api, search_api, bid_api, question_api, answer_api, bids_api, questions_api, answers_api, get_user, profile_api

urlpatterns = [
    path('api/items/', items_api),
    path('api/item/<int:item_id>/', item_api),
    path('api/search/', search_api),
    path('api/bid/', bid_api),
    path('api/question/', question_api),
    path('api/answer/', answer_api),
    path('api/bids/<int:item_id>/', bids_api),
    path('api/questions/<int:item_id>/', questions_api),
    path('api/answers/<int:question_id>/', answers_api),
    path('api/user/', get_user),
    path('api/profile/', profile_api),
]