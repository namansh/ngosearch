from django import forms
from haystack.forms import SearchForm
from haystack.inputs import Raw

class StateSelectSearchForm(SearchForm):
    state = forms.CharField(label='State', required=False)

    def search(self):
        # First, store the SearchQuerySet received from other processing.
        sqs = super(StateSelectSearchForm, self).search()
        sqs = sqs.filter(ngo_url = Raw("[* TO *]"))
        #sqs = sqs.filter(NGO_Name = Raw("[* TO *]"))
        #sqs = sqs.exclude(Website_Url__isnull = True).exclude(Website_Url__exact='')

        if not self.is_valid():
            return self.no_query_found()

        if self.cleaned_data['state']:
            sqs = sqs.filter(state=self.cleaned_data['state'])
            
            

        return sqs
