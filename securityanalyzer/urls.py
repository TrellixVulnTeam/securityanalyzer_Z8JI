"""securityanalyzer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import re_path
from Home.views import home
from StaticAnalyzer.views import manifest_view, static_analyzer,view_source
from DynamicAnalyzer.views import dynamic_analyzer as dz

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', home.index, name='home'),
    re_path(r'^upload/$', home.Upload.as_view),

    # Static Analysis
    # Android
    re_path(r'^static_analyzer/$',static_analyzer.static_analyzer),
    re_path(r'^manifest_view/$', manifest_view.run),
    re_path(r'^view_file/$', view_source.run, name='view_source'),
    # Dynamic Analysis
    re_path(r'^dynamic_analysis/$',
            dz.dynamic_analysis,
            name='dynamic'),
    re_path(r'^android_dynamic/(?P<checksum>[0-9a-f]{32})$',
            dz.dynamic_analyzer,
            name='dynamic_analyzer'),
    re_path(r'^httptools$',
            dz.httptools_start,
            name='httptools'),
    re_path(r'^logcat/$', dz.logcat),
]