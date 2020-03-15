from rest_framework import serializers
from Accounts.models import Profile
from Blog.models import Blog


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog
        fields = ('title', 'picture', 'mainContent', 'user', 'date', 'url')
