from django.db import models
import random
from string import ascii_lowercase




class NameModel (models.Model) : 
    name = models.CharField(max_length=1000)
    updated_at = models.TimeField(auto_now=True)

    def _generate (self) :
        strings = ascii_lowercase

        random_name = '' 
        for i in range(random.randrange(5,20)) : 
            random_name += strings[random.randrange(0,len(strings) - 1)]

        return random_name

    def _rand (self) : 

        random_name = self._generate()
        
        n = NameModel.objects.create( name = random_name )
        n.save()

        return n

    def _update ( self ) : 

        random_name = self._generate()
        n = NameModel.objects.all()[ random.randrange(0,NameModel.objects.all().count() - 1) ]

        n.name = random_name
        n.save()

        return n
        

