from django.core.cache import cache
from .models import Property
from django_redis import get_redis_connection
import logging

def get_all_properties():
    properties = cache.get('all_properties')
    if properties is None:
        properties = Property.objects.all()
        cache.set('all_properties', properties, 3600)  # cache for 1 hour
    return properties


logger = logging.getLogger(__name__)

def get_redis_cache_metrics():
    # Get the default Redis connection used by Django's cache framework
    conn = get_redis_connection("default")

    # Fetch Redis INFO stats
    info = conn.info()

    # Extract cache hit/miss counters
    hits = info.get("keyspace_hits", 0)
    misses = info.get("keyspace_misses", 0)

 # Calculate hit ratio safely (avoid division by zero)
    total = hits + misses
    hit_ratio = (hits / total) if total > 0 else None

    # Log for debug/monitoring
    logger.info(f"Cache Metrics: Hits={hits}, Misses={misses}, Hit Ratio={hit_ratio}")

    # Return as dictionary
    return {
        "hits": hits,
        "misses": misses,
        "hit_ratio": hit_ratio
    }