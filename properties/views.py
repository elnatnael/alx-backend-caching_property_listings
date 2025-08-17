from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .models import Property

@cache_page(60 * 15)  # Cache for 15 minutes (60 seconds * 15)
def property_list(request):
    properties = Property.objects.all()
    data = {
        "data": [
            {
                "id": property.id,
                "title": property.title,
                "price": property.price,
                # Add other fields as needed
            }
            for property in properties
        ]
    }
    return JsonResponse(data)