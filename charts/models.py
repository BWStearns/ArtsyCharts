from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import User


class Artist(models.Model):

    name = models.CharField(max_length=100, default="Unknown")
    birth = models.DateField(null=True)
    death = models.DateField(null=True)
    pieces = models.ManyToManyField('ArtPiece', through="Authorship")

    class Meta:
        verbose_name = "Artist"
        verbose_name_plural = "Artists"

    def __str__(self):
        return self.name


class ArtCollection(models.Model):

    owner = models.ForeignKey(User)
    title = models.CharField(null=False, max_length=100)
    pieces = models.ManyToManyField('ArtPiece', through="CollectionMembership")
    description = models.TextField()

    class Meta:
        verbose_name = "ArtCollection"
        verbose_name_plural = "ArtCollections"

    def __str__(self):
        return self.title
    
class ArtPiece(models.Model):

    id = models.BigIntegerField(primary_key=True)
    title = models.CharField(null=False, max_length=200)
    medium = models.ForeignKey("Medium")
    image_url = models.URLField()
    thumb_url = models.URLField()

    # Dimensions (in inches for now....)
    width = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    length = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    price = models.DecimalField(null=True, max_digits=14, decimal_places=2)

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
        return self.title

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

    if len(instance.artists.all()) == 1:
        instance.primary_artist = instance.artists.all()[0]


class Medium(models.Model):

    name = models.CharField(null=False, max_length=50)

    class Meta:
        verbose_name = "Medium"
        verbose_name_plural = "Media"

    def __str__(self):
        return self.name


class Authorship(models.Model):

    piece = models.ForeignKey(ArtPiece)
    author = models.ForeignKey(Artist)

    class Meta:
        verbose_name = "Authorship"
        verbose_name_plural = "Authorships"
        auto_created=True

    def __str__(self):
        return "{0}, by {1}".format(self.piece.title, self.author.name)


class CollectionMembership(models.Model):

    piece = models.ForeignKey(ArtPiece)
    collection = models.ForeignKey(ArtCollection)

    class Meta:
        verbose_name = "CollectionMembership"
        verbose_name_plural = "CollectionMemberships"
        auto_created=True

    def __str__(self):
        return "{0}, in {1}".format(self.piece.title, self.collection.name)

