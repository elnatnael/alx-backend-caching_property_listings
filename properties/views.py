from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from .models import Property

@cache_page(60 * 15)  # Cache for 15 minutes
def property_list(request):
    properties = Property.objects.all()
    data = {
        "properties": [
            {
                "id": prop.id,
                "title": prop.title,
                "description": prop.description,
                "price": str(prop.price),
                "location": prop.location,
                "created_at": prop.created_at.isoformat()
            } 
            for prop in properties
        ]
    }
    return JsonResponse(data)