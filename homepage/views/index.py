from django import forms
from django_mako_plus import view_function
from formlib import Formless
from homepage import models as hmod
from datetime import datetime

@view_function
def process_request(request):
    # this method doesn't need any more work

    # handle the form
    prices = []
    form = SearchForm(request)
    if form.is_valid():
        prices = form.commit()

    # set up the context and render
    context = {
        'prices': prices,
        'form': form,
    }
    return request.dmp.render('index.html', context)



class SearchForm(Formless):
    '''Searches the CurrencyPrice table'''
    CURRENCY_CHOICES = (
        ( 'BTC', 'Bitcoin' ),
        ( 'ETH', 'Ethereum' ),
        ( 'XRP', 'Ripple' ),
    )
    SORT_CHOICES = (
        ( 'symbol', 'Symbol' ),
        ( 'date', 'Date' ),
        ( 'price', 'Price (lowest first)' ),
        ( '-price', 'Price (highest first)' ),
    )

    def init(self):
        '''Adds the fields for this form'''
        self.fields['symbol'] = forms.ChoiceField(label='Symbol',choices=self.CURRENCY_CHOICES)
        self.fields['start_date'] = forms.DateField(label='Start Date',input_formats=['%Y-%m-%d'])
        self.fields['end_date'] = forms.DateField(label='End Date',input_formats=['%Y-%m-%d'])
        self.fields['sort'] = forms.ChoiceField(label='Sort',choices=self.SORT_CHOICES)
        # TODO:
        # Four fields go here: symbol, start_date, end_date, sort


    def commit(self):
        '''Returns a list of CurrencyPrice objects matching the user selections on the form'''
        # TODO:
        # Query the hmod.CurrencyPrice model on symbol + start_date + end_date
        # and sort by the sort field.
        # You can assume that all fields are submitted correctly
        # No need to have clean methods.
        # return a list (or query) here
        symbol = self.cleaned_data.get('symbol')
        start_date = self.cleaned_data.get('start_date')
        end_date = self.cleaned_data.get('end_date')
        sort = self.cleaned_data.get('sort')

        result = hmod.CurrencyPrice.objects.filter(symbol=symbol,date__gte=start_date,date__lte=end_date).order_by(sort)

        return result
