from django.urls import path
from .views import (ContactListCreate, ContactDetail, contact_list, contact_detail, contact_create, contact_update,
                    contact_delete)


urlpatterns = [
    path('', contact_list, name='contact-list'),
    path('contact/<int:pk>/', contact_detail, name='contact-detail'),
    path('contact/new/', contact_create, name='contact-create'),
    path('contact/<int:pk>/edit/', contact_update, name='contact-update'),
    path('contact/<int:pk>/delete/', contact_delete, name='contact-delete'),
]


