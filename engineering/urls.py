from django.urls import path
from . import views

urlpatterns = [
    path('INSTITUE OF ENGINEERING AND TECHNOLOGY', views.engineering_homepage, name='engineering'),
    path('INSTITUE OF ENGINEERING AND TECHNOLOGY/Events', views.engineering_event_page, name='engineering_events' ),
    path('INSTITUE OF ENGINEERING AND TECHNOLOGY/CS Department', views.cs_department, name='cs_department' ),
    path('INSTITUE OF ENGINEERING AND TECHNOLOGY/EC Department', views.ec_department, name='ec_department' ),
    path('INSTITUE OF ENGINEERING AND TECHNOLOGY/MECH Department', views.mech_department, name='mech_department' ),
    path('INSTITUE OF ENGINEERING AND TECHNOLOGY/CIVIL Department', views.civil_department, name='civil_department' ),
    path('INSTITUE OF ENGINEERING AND TECHNOLOGY/AIML Department', views.aiml_department, name='aiml_department' ),
    path('INSTITUE OF ENGINEERING AND TECHNOLOGY/Events/<name>', views.engineering_event_page_details, name='engineering_events_details' ),
    path('INSTITUE OF ENGINEERING AND TECHNOLOGY/CS Department/overview', views.cs_department_overview, name='cs_department_overview'),
    path('INSTITUE OF ENGINEERING AND TECHNOLOGY/?', views.error, name='error'),
    path('INSTITUE OF ENGINEERING AND TECHNOLOGY/placements', views.placements, name='placements'),
    path('INSTITUE OF ENGINEERING AND TECHNOLOGY/gallery', views.gallery, name='engineering_gallery'),

]
