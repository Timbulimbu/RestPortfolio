from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
from django.urls import path, include

from drf_yasg import openapi
from drf_yasg.views import get_schema_view


from rest_framework import routers, permissions
from restapi.views import (
    MeViewSet,
    ProjectViewSet,
    PricingViewSet,
    SkillViewSet, 
    ContactViewSet,    
)

schema_view = get_schema_view(
   
   openapi.Info(
       title="Portfolio API Documentation",
       default_version='v1',
       description="Backend only for Portfolio API Documentaion",
       terms_of_service="https://www.google.com/policies/terms/",  #https://www.itcbootcamp.com/info_pages/privacy_policy, whatever
       
       contact=openapi.Contact(
           name="Natalie Marten",
           url="https://t.me/NatalieMarten",
           email="natalie.marten.73@gmail.com",
           ),
       
       license=openapi.License(
           name="MIT License",
           url="https://opensource.org/licenses/MIT/",
        ) 
       
    ),  
   
    public=True, 
    permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()

router.register(r'me', MeViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'pricings', PricingViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'contacts', ContactViewSet)

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include(router.urls)),
    
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('redoc/', include('django.contrib.admindocs.urls')),
    path('graphql/', include('graphapi.urls')), 
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

