from rest_framework import mixins, viewsets


class ListCreateDestroyModelViewSet(mixins.CreateModelMixin,
                                    mixins.DestroyModelMixin,
                                    mixins.ListModelMixin,
                                    viewsets.GenericViewSet):
    pass
