from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = "blockchain_api"
urlpatterns = [
    path('search/address/<str:address>/', views.SearchByAddressView.as_view(), name="search_address"),
    path('search/transaction/<str:transaction>', views.SearchByTransactionView.as_view(), name="search_transaction"),
    path('searches/', views.UserSearchesView.as_view(), name="past_searches"),
    path('addresses/', views.UserAddressesView.as_view(), name="mine_addresses"),
    path('balance/', views.UserBalanceView.as_view(), name="balance"),
    path('orders/', views.UserOrdersView.as_view(), name="orders"),
    path('orders/<str:order>/complete', views.UserOrderCompleteView.as_view(), name="complete_order"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
