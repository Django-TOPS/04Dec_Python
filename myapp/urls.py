from django.contrib import admin
from django.urls import path
from myapp import views
from BatchProj import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
   path('',views.index,name='/'),
   path('about/',views.about,name='about'),
   path('contact/',views.contact,name='contact'),
   path('notes/',views.notes,name='notes'),
   path('userlogout/',views.userlogout,name='userlogout'),
   path('updateprofile/',views.updateprofile,name='updateprofile'),
   path('adminview/',views.adminview,name='adminview'),
   path('deletedata/<int:id>',views.deletedata),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)