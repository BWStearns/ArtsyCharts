# Django
from django.contrib.auth.models import User
# External
from rest_framework import routers, serializers, viewsets
# Internal
from charts.models import ArtCollection, ArtPiece, Artist, Medium

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#################
# COLLECTIONS
#################
class ArtCollectionSerializer(serializers.HyperlinkedModelSerializer):

    pieces = serializers.RelatedField(many=True)

    class Meta:
        model = ArtCollection
        fields = ('owner', 'title', 'description', 'pieces')


# ViewSets define the view behavior.
class ArtCollectionViewSet(viewsets.ModelViewSet):
    queryset = ArtCollection.objects.all()
    serializer_class = ArtCollectionSerializer

#################
# ARTISTS
#################
class ArtistSerializer(serializers.HyperlinkedModelSerializer):

    pieces = serializers.RelatedField(many=True)

    class Meta:
        model = Artist
        fields = ('name', 'birth', 'death', 'pieces')


# ViewSets define the view behavior.
class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


#################
# MEDIA
#################
class MediumSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Medium
        fields = ('name',)


# ViewSets define the view behavior.
class MediumViewSet(viewsets.ModelViewSet):
    queryset = Medium.objects.all()
    serializer_class = MediumSerializer


#################
# PIECES
#################

class ArtPieceSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ArtPiece
        fields = (
            'id',
            'title',
            'medium',
            'image_url',
            'thumb_url',
            'artists',
            'collections',
            'primary_artist',
        )


# ViewSets define the view behavior.
class ArtPieceViewSet(viewsets.ModelViewSet):
    queryset = ArtPiece.objects.all()
    serializer_class = ArtPieceSerializer



#################
# Routers provide an easy way of automatically determining the URL conf.
#################
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'art_collections', ArtCollectionViewSet)
router.register(r'art_pieces', ArtPieceViewSet)
router.register(r'artists', ArtistViewSet)
router.register(r'media', MediumViewSet)
