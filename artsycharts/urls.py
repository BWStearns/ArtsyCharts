# Django
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.models import User
# External

# Internal
from charts.api import router
from charts import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'artsycharts.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # Actual html views
    url(r'^collections/(\d+)/$', views.collection_view, ),

    # API and Admin stuff
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
)
