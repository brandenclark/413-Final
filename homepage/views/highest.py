from django_mako_plus import view_function
from homepage import models as hmod
from django.http import HttpResponse
from django.db.models import Max


@view_function
def process_request(request, symbol:str):
    # TODO: complete this function
    # Query the maximum date for the given symbol.
    # and return it directly.  No need for a template.
    # If that doesn't make sense, search the web for
    # using HttpResponse directly in Django.

    high = hmod.CurrencyPrice.objects.filter(symbol=symbol).aggregate(Max('date'))['date__max']

    return HttpResponse(high)
