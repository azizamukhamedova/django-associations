__author__ = 'DarkSector'
from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from views import CreateDemoPageView, \
    ListDemoPageView, DetailDemoView, FooView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_ass.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^create/$',
        CreateDemoPageView.as_view(),
        name='create_demo'),

    url(r'^list/$',
        ListDemoPageView.as_view(),
        name='list_demo'),

    url(r'^detail/(?P<pk>\d+)/$',
        DetailDemoView.as_view(),
        name='detail_demo'),

    url(r'^foo/(?P<pk>\d+)/bar/(?P<demo_pk>\w+)/extend/(?P<demo2_pk>\w+)$',
        FooView.as_view(),
        name='foo_demo'),

    url(r'^$',
        TemplateView.as_view(template_name='index_demo.html'),
        name='index_demo'),

)