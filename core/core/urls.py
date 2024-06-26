
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .Utils import DataForwardAPIView

schema_view = get_schema_view(
    openapi.Info(
        title="APP API",
        default_version="v1",
        description="Brief descriptions about the api",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="bigdeli.ali3@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)




urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include('prescriptions.urls')),
    # path('user/', include('user.urls')),
    path('forward/', DataForwardAPIView.as_view()),
]

if settings.COMINGSOON:
    urlpatterns.insert(
        0, re_path(r"^", TemplateView.as_view(template_name="comingsoon.html"))
    )

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    

if settings.SHOW_DEBUGGER_TOOLBAR:
    urlpatterns += [path('__debug__/', include('debug_toolbar.urls')),
                    ]

api_urlpatterns = []

if settings.SHOW_SWAGGER:
    api_urlpatterns += [
        path("api-auth/", include("rest_framework.urls",
                                  namespace="rest_framework")),
        path(
            "swagger/api.json",
            schema_view.without_ui(cache_timeout=0),
            name="schema-json",
        ),
        path(
            "swagger/",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui",
        ),
        path(
            "redoc/",
            schema_view.with_ui("redoc", cache_timeout=0),
            name="schema-redoc",
        ),
    ]

# list your api urls here

urlpatterns += [path('api/', include(api_urlpatterns))]
    

handler400 = "core.error_views.error_400"  # bad_request
handler403 = "core.error_views.error_403"  # permission_denied
handler404 = "core.error_views.error_404"  # page_not_found
handler500 = "core.error_views.error_500"  # server_error
