from django.contrib import admin
from . import settings
from django.urls import include, path
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from accounts import views as accounts_views
from matcher import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', accounts_views.signup, name='signup'),
    path('my_socks/', views.my_socks, name='my_socks'),
    path('my_matches/', views.my_matches, name='my_matches'),
    path('accounts/', include('accounts.urls')),
    path('matcher/', include('matcher.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)