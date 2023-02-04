from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('accounts/', include('allauth.urls')),
                  path('', include('home.urls')),
                  path('products/', include('products.urls')),
                  path('bag/', include('bag.urls')),
                  path('checkout/', include('checkout.urls')),
                  path('summernote/', include('django_summernote.urls')),
                  path('profile/', include('profiles.urls')),
                  path('afternoon_tea/', include('afternoon_tea.urls')),
                  path('cake_order/', include('cake_order.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# handling the 404 error
handler404 = "josie_annes_patisserie.views.error_404_view"
