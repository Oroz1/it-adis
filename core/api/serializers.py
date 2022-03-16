from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from core.models import *

class CoursesSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )
    class Meta:
        model = Courses
        fields = '__all__'


class UsersStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = UsersStatus
        fields = '__all__'


class CoursesReleaseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CoursesRelease
        fields = '__all__'



class UserSerializer(serializers.ModelSerializer):
    status = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )
    profession = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'name',
            'email',
            'status',
            'phone_number',
            'information',
            'profession',
            'is_active',
        )


class PagesSerializer(serializers.ModelSerializer):
    user_id = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name'
    )
    class Meta:
        model = Pages
        fields = '__all__'


class PostsSerializer(serializers.ModelSerializer):
    user_id = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='user'
    )
    class Meta:
        model = Posts
        fields = '__all__'


class TagsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tags
        fields = '__all__'


class ShiftsDaysSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = ShiftsDays
        fields = '__all__'


class CoursesTimesSerializer(serializers.ModelSerializer):

    class Meta:
        model = CoursesTimes
        fields = '__all__'


class CourseRegistrationsSerailizer(serializers.ModelSerializer):
    
    class Meta:
        model = CourseRegistrations
        fields = '__all__'


class HeadersBarsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = HeadersBars
        fields = '__all__'


class UrlsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Urls
        fields = '__all__'



class MenusTitlesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MenusTitles
        fields = '__all__'


class MenusElementsSerializer(serializers.ModelSerializer):
    menu = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='title'
    )
    url = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='url'
    )
    class Meta:
        model = MenusElements
        fields = '__all__'

    
class FootersBarsSerializer(serializers.ModelSerializer):
    urls = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='url'
    )
    class Meta:
        model = FootersBars
        fields = '__all__'

    
class FilesTypesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FilesTypes
        fields = '__all__'

    
class MediaFilesSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='title'
    )
    class Meta:
        model = MediaFiles
        fields = '__all__'


class CommentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Group
        fields = '__all__'

    
