from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer, LoginUserSerializer, ProdtSerializer
from django.contrib.auth import login
from knox.views import LoginView as KnoxLoginView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import permission_classes
from posts.models import Post

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })
        

class LoginAPI(generics.GenericAPIView):
  # permission_classes = [] #disables permission
  permission_classes = ()
  serializer_class = LoginUserSerializer
  def post(self, request, *args, **kwargs):
      serializer = self.get_serializer(data=request.data) 
      serializer.is_valid(raise_exception=True)
      user = serializer.validated_data
      return Response({
          "token": AuthToken.objects.create(user)[1] , 
          "user": UserSerializer(user, context=self.get_serializer_context()).data
      })
      
class ManageUserView(generics.RetrieveUpdateAPIView):
  serializer_class = UserSerializer
  permission_classes = (permissions.IsAuthenticated,)

  def get_object(self):
    return self.request.user
  
class PostgetView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = ProdtSerializer

 