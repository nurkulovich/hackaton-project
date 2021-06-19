from rest_framework import generics, permissions
from review import serializers
from review.models import Review, Mark


class MarkApiView(generics.ListAPIView):
    queryset = Mark.objects.all()
    serializer_class = serializers.MarkSerializer
    permission_classes = (permissions.AllowAny, )


class MarkCreateView(generics.CreateAPIView):
    queryset = Mark.objects.all()
    serializer_class = serializers.ReviewSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReviewApiView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    permission_classes = (permissions.AllowAny, )


class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    permission_classes = (permissions.AllowAny, )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReviewRetrieveView(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = serializers.ReviewDetailSerializer
    permission_classes = (permissions.AllowAny, )

