from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django_dhcp.models import NetworkNode
from views import NetworkNodeCreateView, NetworkNodeDetail


urlpatterns = patterns('',
                       url(r'^node_list/$', ListView.as_view(
                           queryset=NetworkNode.objects.all(),
                           context_object_name='nodes',
                           template_name='django_dhcp/list.html'), name="node_list"),
                       url(r'^(?P<pk>[0-9]+)/$',
                           NetworkNodeDetail.as_view(
                               template_name='django_dhcp/detail.html',
                               context_object_name='node'), name="detail"),
                       url(r'^create/$', CreateView.as_view(model=NetworkNode,
                           template_name='django_dhcp/create.html',
                           success_url=reverse_lazy('node_list')),
                           name="create"),
                       url(r'^update/(?P<pk>[0-9]+)/$',
                           UpdateView.as_view(model=NetworkNode,
                                              template_name='django_dhcp/update.html'),
                           name="update"),

                       )

try:
    from djangoautoconf import create_tastypie_resource
    urlpatterns += (r'^api/node/', include(create_tastypie_resource(NetworkNode)))
except:
    pass