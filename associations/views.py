from django.views.generic import TemplateView
from .raw import get_all_uris


class DASimpleView(TemplateView):
    template_name = 'associations_base.html'

    def get_context_data(self, **kwargs):
        context = super(DASimpleView, self).get_context_data(**kwargs)
        uris = get_all_uris()
        print(uris)
        return context
