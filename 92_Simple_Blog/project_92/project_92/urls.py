
from django.contrib import admin
from django.urls import path
from project_92_app.views import blog_post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', blog_post),

]
