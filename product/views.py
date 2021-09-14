from rest_framework import status, parsers, renderers, generics, filters
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend

from .models import Users, Cars, Clients, Orders
from .serializers import ClientSerializer, CarSerializer, OrderSerializer, UserSerializer, AuthTokenSerializer


class ClientsList(generics.ListCreateAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientSerializer


class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clients.objects.all()
    serializer_class = ClientSerializer


class CarsList(generics.ListCreateAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarSerializer


class CarsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarSerializer


class OrdersList(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['timestamp']
    search_fields = ['car_id__brand']


class OrdersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer


class UsersList(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer


class UsersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer


class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'username': user.username})
