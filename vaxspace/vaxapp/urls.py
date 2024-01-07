from django.contrib import admin
from django.urls import path
from . import views
from vaxapp.views import overall_vaccination_graph


app_name = 'vaxapp'

urlpatterns = [
    path('', views.loginPage, name='loginPage'),
    path('user_register/', views.user_register, name='user_register'),
    path('index/', views.index, name='index'),
    path('update_admin/', views.update_admin, name='update_admin'),
    path('index/utilities/', views.utilities, name='utilities'),
    path('healthworker/', views.healthworker, name='healthworker'),
    path('update_healthworker/', views.update_healthworker, name='update_healthworker'),
    path('index/barangay/', views.barangay, name='barangay'),
    path('guardian/', views.guardian, name='guardian'),
    path('update_guardian/', views.update_guardian, name='update_guardian'),
    path('edit_guardian/<int:id>/', views.edit_guardian, name='edit_guardian'),
    path('edit_healthworker/<int:id>/', views.edit_healthworker, name='edit_healthworker'),
    path('edit_vaccine/<int:id>/', views.edit_vaccine, name='edit_vaccine'),
    path('edit_barangay/<int:id>/', views.edit_barangay, name='edit_barangay'),
    path('add_healthworker/', views.add_healthworker, name='add_healthworker'),
    path('index/add_vaccine/', views.add_vaccine, name='add_vaccine'),
    path('charts/', views.charts, name='charts'),
    path('tables/', views.tables, name='tables'),
    path('admin_tables/', views.admin_tables, name='admin_tables'),
    path('buttons/', views.buttons, name='buttons'),
    path('admin_tables/add_record/<int:id>/', views.add_record, name='admin_add_record'),
    path('tables/add_record/<int:id>/', views.add_record, name='add_record'), 
    path('view_record_staff/<int:id>/', views.view_record_staff, name='view_record_staff'),
    path('view_record/<int:id>/', views.view_record, name='view_record'),
    path('tables/confirmation/<int:id>/', views.confirmation, name='confirmation'),
    path('edit_schedule/<int:id>/', views.edit_schedule, name='edit_schedule'),
    path('remove_child/<int:id>/', views.remove_child, name='remove_child'),
    path('remove_sched/<int:id>/', views.remove_sched, name='remove_sched'),
    path('delete_child/<int:id>/', views.delete_child, name='delete_child'),
    path('delete_user/<int:id>/', views.delete_user, name='delete_user'),
    path('delete_worker/<int:id>/', views.delete_worker, name='delete_worker'),
    path('delete_vaccine/<int:id>/', views.delete_vaccine, name='delete_vaccine'),
    path('delete_brgy/<int:id>/', views.delete_brgy, name='delete_brgy'),
    path('save_to_admin/', views.save_to_admin, name='save_to_admin'),
    path('logout/', views.logout, name='logout'),
    path('index/overall-vaccination/', views.overall_vaccination_graph, name='overall_vaccination_graph'),
]