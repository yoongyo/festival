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

    all_festivalArea = graphene.List(FestivalImageType)

    all_festivalComment = graphene.List(FestivalCommentType)

    all_festivalSNS = graphene.List(FestivalSNSType)

    all_festivalImage = graphene.List(FestivalImageType)

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

