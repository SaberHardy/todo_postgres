from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo_app.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),

    path('social-auth/', include('social_django.urls', namespace='social')),

    # path('members/', RedirectView.as_view(url='')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
