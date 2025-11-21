from django.http import JsonResponse
from api.serializer import ProductSerializer
from api.models import Product


def Prodict_list(requiest):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return JsonResponse({
        "data": serializer.data
    })
