"""MI_eSE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from eSE import notify_business_results,post_apdu_result,get_scripts_status,cancel_scripts,put_apdu_scripts


urlpatterns = [
    url(r'SHSRC/tsm/NotifyBusinessResults', notify_business_results.receive_data),
    # url(r'SHSRC/MI/TSM/1/1/PutApduScripts', put_apdu_scripts.receive_data),
    # url(r'SHSRC/tsm/PutApduScripts', put_apdu_scripts.receive_data),
    url(r'SHSRC/tsm/PutApduScripts', post_apdu_result.receive_data),
    url(r'SHSRC/tsm/GetScriptsStatus', get_scripts_status.receive_data),
    url(r'SHSRC/tsm/CancelScripts', cancel_scripts.receive_data),
]
