from django.contrib.auth.models import User, Group
# from tutorial.quickstart.models import Post
from rest_framework import viewsets
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer, PostSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

# class PostViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows posts to be viewed or edited
#     """
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
