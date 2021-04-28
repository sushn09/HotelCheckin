from django.contrib import admin
from django.urls import path
from enroll import views
from django.conf import settings
from django.conf.urls.static import static
# from enroll.views import image_upload

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.create_show, name="create_and_show"),
    path('retrieve-record', views.retrieve_record, name="retrieve_records"),
    path('delete/<int:id>/', views.delete_record, name="delete_records"),
    path('<int:id>/', views.update_record, name="update_records"),
    # path('', views.image_upload, name="image_upload"), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)