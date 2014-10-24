from django.core.urlresolvers import reverse
from django.views.generic import CreateView, UpdateView, DetailView
from models import NetworkNode


class NetworkNodeCreateView(CreateView):
    model = NetworkNode
    """
    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})

    def form_valid(self, form):
        return super(NetworkNodeCreateView, self).form_valid(form)
    """

"""
class NetworkNodeUpdate(UpdateView):
    model = NetworkNode
"""


class NetworkNodeDetail(DetailView):
    model = NetworkNode