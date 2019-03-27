from products.models import *


def categories(request):
    cat = ProductCategory.objects.select_related().only('name').all()
    return {'cat': cat}
