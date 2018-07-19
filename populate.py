# set up django first
import os, os.path
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "finalexam.settings")
django.setup()

# normal imports
from homepage import models as hmod
from datetime import date
import csv

# empty the table
hmod.CurrencyPrice.objects.all().delete()

# TODO: open and read data.csv line by line
# on each line (except header), create a CurrencyPrice object
# (hint: python comes with a csv library -- see the docs)

with open('data.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        cp = hmod.CurrencyPrice()

        cp.symbol = row['symbol']
        cp.price = row['price']
        cp.date = date(year=int(row['year']),day=int(row['day']),month=int(row['month']))

        cp.save()
