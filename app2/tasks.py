from celery import shared_task
from app.models import NameModel



@shared_task( bind = True )
def CreateRandomNameModel ( self ) : 

    n = NameModel()
    new = n._rand()

    return "Created ", new.id