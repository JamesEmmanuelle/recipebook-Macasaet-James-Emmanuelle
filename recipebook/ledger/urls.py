from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index')
    path('/recipes/list', ledger, name='list')
    path ('/recipe/1', ledger, name='list1')
    path('/recipe/2', ledger, neame= 'list2')
]

app_name = 'ledger'