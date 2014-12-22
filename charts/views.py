from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from charts.models import ArtCollection, ArtPiece, Artist

@require_http_methods(["GET"])
def collection_view(request, collection_id):
    c = ArtCollection.objects.get(id=collection_id).prefetch_related('pieces')\
        .prefetch_related('pieces__artists')\
        .prefetch_related('pieces__medium')

    context = {
        "collection": c,
        "pieces": c.pieces,
    }
    return render(request, 'charts/templates/collection.html', context)