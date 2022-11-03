from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination, viewsets
from rest_framework.permissions import AllowAny

from ads.models import Ad
from ads.serializers import AdSerializer


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    pagination_class = AdPagination
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]



class CommentViewSet(viewsets.ModelViewSet):
    pass

