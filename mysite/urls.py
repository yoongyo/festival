from django.contrib import admin
from django.urls import path, re_path
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),

]
