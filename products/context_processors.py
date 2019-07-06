from products.models import *


def categories(request):
    cat = ProductCategory.objects.only('name').all()
    return {'cat': cat}
