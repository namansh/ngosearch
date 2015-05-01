from django import forms
from haystack.forms import SearchForm


class StateSelectSearchForm(SearchForm):
    state = forms.CharField(label='State', required=False)

    def search(self):
        # First, store the SearchQuerySet received from other processing.
        sqs = super(StateSelectSearchForm, self).search()

        if not self.is_valid():
            return self.no_query_found()

        if self.cleaned_data['state']:
            sqs = sqs.filter(state=self.cleaned_data['state'])

        return sqs