import csv

from django.db.models import Sum
from django.http.response import HttpResponse


def get_csv_shopping_cart(ingredient_recipe):
    ingredients = ingredient_recipe.values(
        'ingredient__name', 'ingredient__measurement_unit'
    ).annotate(ingredient_amount=Sum('amount')).values_list(
        'ingredient__name', 'ingredient_amount',
        'ingredient__measurement_unit',
    )
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = (
        'attachment;'
        'filename="Shoppingcart.csv"'
    )
    writer = csv.writer(response)
    for item in list(ingredients):
        writer.writerow(item)
    return response
