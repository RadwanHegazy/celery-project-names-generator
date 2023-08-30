from celery import shared_task
from .models import NameModel


@shared_task( bind = True )
def UpdateNameModel ( self ) : 


    n = NameModel()
    new = n._update()

    return 'update  : ',new.id