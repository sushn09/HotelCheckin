from django.contrib import admin
from django.urls import path
from enroll import views
from django.conf import settings
from django.conf.urls.static import static
# from enroll.views import image_upload

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.create_show.as_view(), name="create_and_show"),
    path('retrieve-record', views.retrieve_record.as_view(), name="retrieve_records"),
    path('<int:pk>/update', views.update_record.as_view(), name="update_records"),
    path('<int:id>/', views.delete_record.as_view(), name="delete_records"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)