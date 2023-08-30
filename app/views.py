from rest_framework import mixins, generics
from .serializers import NameSerializer
from .models import NameModel




class NameView ( generics.GenericAPIView, mixins.ListModelMixin ) : 
    queryset = NameModel.objects.all()
    serializer_class = NameSerializer

    def get (self, request) : 
        
        return self.list( request )
    
