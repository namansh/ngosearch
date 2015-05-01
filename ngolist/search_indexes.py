from haystack import indexes
from ngolist.models import Ngolist

 
class NgolistIndex (indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    state = indexes.CharField(model_attr='State')
    
    #city = indexes.CharField(model_attr='City')
    #pub_date = indexes.DateTimeField(model_attr='created')
 
    def get_model(self):
        return Ngolist
    
    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

