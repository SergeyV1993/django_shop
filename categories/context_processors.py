from products.models import *


def categories(request):
    cat = Category.objects.only('name').all()
    return {'cat': cat}
