from rest_framework import generics
from rest_framework import permissions
from like.models import Like, DisLike
from rest_framework import serializers
from . import serializers


class LikeCreateView(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = serializers.LikeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DisLikeCreateView(generics.ListCreateAPIView):
    queryset = DisLike.objects.all()
    serializer_class = serializers.DisLikeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
