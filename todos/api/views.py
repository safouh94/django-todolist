# from django.db.models import Q

# social account
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from rest_auth.views import LoginView
from rest_auth.social_serializers import TwitterLoginSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from todos.models import Todo

from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
)

from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

# from rest_framework.permissions import (
#     AllowAny,
#     IsAuthenticated,
#     IsAdminUser,
#     IsAuthenticatedOrReadOnly
# )

# from rest_framework.permissions import AllowAny
# from .permissions import IsOwnerOrReadOnly

from .serializers import (
    TodoCreateUpdateSerializer,
    TodoDetailSerializer,
    TodoListSerializer
)


# class JSONWebTokenAPIView(APIView):


class TodoCreateAPIView(CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoCreateUpdateSerializer
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TodoDeleteAPIView(DestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoDetailSerializer
    # lookup_field = 'username'


class TodoDetailAPIView(RetrieveUpdateAPIView, DestroyAPIView):  # GET - DELETE - PUT
    queryset = Todo.objects.all()
    serializer_class = TodoDetailSerializer
    # lookup_field = 'username'

    # JSON Web Token
    # authentication_classes = (JSONWebTokenAuthentication, )
    permission_classes = (IsAuthenticated, )


class TodoListAPIView(ListAPIView, CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'text']

    # JSON Web Token
    # authentication_classes = (JSONWebTokenAuthentication, )
    permission_classes = (IsAuthenticated, )


class TodoUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoCreateUpdateSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    # lookup_field = 'username'

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


# social account
class TwitterLogin(LoginView):
    serializer_class = TwitterLoginSerializer
    adapter_class = TwitterOAuthAdapter
