from django_mako_plus import view_function
from homepage import models as hmod
from django.http import HttpResponse
from django.db.models import Min


@view_function
def process_request(request, symbol:str):
    # TODO: complete this function
    # Query the minimum date for the given symbol.
    # and return it directly.  No need for a template.
    # If that doesn't make sense, search the web for
    # using HttpResponse directly in Django.
    low = hmod.CurrencyPrice.objects.filter(symbol=symbol).aggregate(Min('date'))['date__min']

    return HttpResponse(low)
