from haystack.views import SearchView
from forms import StateSelectSearchForm


class MySearchView(SearchView):
    """My custom search view."""
    form_class = StateSelectSearchForm

    def get_context_data(self, *args, **kwargs):
        context = super(MySearchView, self).get_context_data(*args, **kwargs)
        # do something
        return context
