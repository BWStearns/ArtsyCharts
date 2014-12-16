from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import User


class Artist(models.Model):

    class Meta:
        verbose_name = "Artist"
        verbose_name_plural = "Artists"

    def __str__(self):
        pass


class ArtCollection(models.Model):

    owner = models.ForeignKey(User)
    title = models.CharField(null=False, max_length=100)
    pieces = models.ManyToManyField('ArtPiece', through="CollectionMembership")
    description = models.TextField()

    class Meta:
        verbose_name = "ArtCollection"
        verbose_name_plural = "ArtCollections"

    def __str__(self):
        pass
    
class ArtPiece(models.Model):

    id = models.BigIntegerField(primary_key=True)
    title = models.CharField(null=False, max_length=200)
    image_url = models.URLField()
    thumb_url = models.URLField()

    artists = models.ManyToManyField(
        Artist, 
        null=True, 
        through='Authorship'
    )
    
    collections = models.ManyToManyField(
        ArtCollection,
        null=True,
        through="CollectionMembership"
    )

    primary_artist = models.ForeignKey(Artist, null=True, related_name="pieces_as_primary")

    class Meta:
        verbose_name = "ArtPiece"
        verbose_name_plural = "ArtPieces"

    def __str__(self):
        self.title

    @property
    def artsy_id(self):
        return hex(self.id)[2:-1]
    


@receiver(pre_save, sender=ArtPiece)
def art_piece_pre_save(sender, instance, *args, **kwargs):
    """
    art_piece pre_save hook. 
    Assigns primary artist if only one artist.
    Handles the Hex string ID from Artsy

    """
    if kwargs.get('created', False):
        instance.id = int(instance.id, base=16)

    if len(instance.artists) == 1:
        instance.primary_artist = instance.artists[0]


class Authorship(models.Model):

    piece = models.ForeignKey(ArtPiece)
    author = models.ForeignKey(Artist)

    class Meta:
        verbose_name = "Authorship"
        verbose_name_plural = "Authorships"

    def __str__(self):
        pass


class CollectionMembership(models.Model):

    piece = models.ForeignKey(ArtPiece)
    collection = models.ForeignKey(ArtCollection)

    class Meta:
        verbose_name = "CollectionMembership"
        verbose_name_plural = "CollectionMemberships"

    def __str__(self):
        pass

