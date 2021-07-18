from rest_framework import fields, serializers
from blog.models import Post
from users.models import Profile
#from blog.models import category


class  PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('__all__')

class  UserSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Profile
        fields = ('__all__')

