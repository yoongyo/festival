import graphene
from graphene_django.types import DjangoObjectType
from .models import Festival, FestivalArea, FestivalImage, FestivalSNS, FestivalComment


class FestivalType(DjangoObjectType):
    class Meta:
        model = Festival


class FestivalAreaType(DjangoObjectType):
    class Meta:
        model = FestivalArea


class FestivalImageType(DjangoObjectType):
    class Meta:
        model = FestivalImage


class FestivalCommentType(DjangoObjectType):
    class Meta:
        model = FestivalComment


class FestivalSNSType(DjangoObjectType):
    class Meta:
        model = FestivalSNS


class Query(graphene.AbstractType):
    all_festival = graphene.List(FestivalType)

    all_festivalArea = graphene.List(FestivalAreaType)

    all_festivalComment = graphene.List(FestivalCommentType)

    all_festivalSNS = graphene.List(FestivalSNSType)

    all_festivalImage = graphene.List(FestivalImageType)

    festival = graphene.Field(FestivalType,
                                id=graphene.Int())

    gallery = graphene.Field(FestivalImageType,
                                festival=graphene.Int()
                            )

    def resolve_all_festival(self, context, **kwargs):
        return Festival.objects.all()

    def resolve_all_festivalArea(self, context, **kwargs):
        return FestivalArea.objects.all()

    def resolve_all_festivalComment(self, context, **kwargs):
        return FestivalComment.objects.all()

    def resolve_all_festivalSNS(self, context, **kwargs):
        return FestivalSNS.objects.all()

    def resolve_all_festivalImage(self, context, **kwargs):
        return FestivalImage.objects.all()

    def resolve_festival(self, context, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Festival.objects.get(pk=id)

        return None

    def resolve_gallery(self, context, **kwargs):
        festival = kwargs.get('festival')

        if festival is not None:
            return FestivalImage.objects.filter(festival__pk=festival)

        return None

