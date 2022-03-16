from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status as Status
from core.api.serializers import *
from core.models import *


class UsersStatusApiView(ListAPIView):
    queryset = UsersStatus.objects.all()
    serializer_class = UsersStatusSerializer
    permission_classes = (AllowAny,)


class UsersStatusDetailApiView(RetrieveAPIView):
    queryset = UsersStatus.objects.all()
    serializer_class = UsersStatusSerializer
    permission_classes = (AllowAny,)


class CoursesReleaseApiView(ListAPIView):
    queryset = CoursesRelease.objects.filter(is_published=True)
    serializer_class = CoursesReleaseSerializer
    permission_classes = (AllowAny,)


class CoursesReleaseDetailApiView(RetrieveAPIView):
    queryset = CoursesRelease.objects.filter(is_published=True)
    serializer_class = CoursesReleaseSerializer
    permission_classes = (AllowAny,)



class CoursesApiView(ListAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
    permission_classes = (AllowAny,)


class CoursesDetailApiView(RetrieveAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
    permission_classes = (AllowAny,)


class UserApiView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class UserDetailApiView(RetrieveAPIView): 
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class PagesApiView(ListAPIView):
    queryset = Pages.objects.filter(is_published=True)
    serializer_class = PagesSerializer
    permission_classes = (AllowAny,)


class PagesDetailApiView(RetrieveAPIView):
    queryset = Pages.objects.filter(is_published=True)
    serializer_class = PagesSerializer
    permission_classes = (AllowAny,)


class PostsApiView(ListAPIView):
    queryset = Posts.objects.filter(is_published=True)
    serializer_class = PostsSerializer
    permission_classes = (AllowAny,)


class PostsDetailApiView(RetrieveAPIView):
    queryset = Posts.objects.filter(is_published=True)
    serializer_class = PostsSerializer
    permission_classes = (AllowAny,)


class TagsApiView(ListAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
    permission_classes = (AllowAny,)


class TagsDetailApiView(RetrieveAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
    permission_classes = (AllowAny,)


class ShiftsDaysApiView(ListAPIView):
    queryset = ShiftsDays.objects.all()
    serializer_class = ShiftsDaysSerializer
    permission_classes = (AllowAny,)


class ShiftsDaysDetailApiView(RetrieveAPIView):
    queryset = ShiftsDays.objects.all()
    serializer_class = ShiftsDaysSerializer
    permission_classes = (AllowAny,)


class CoursesTimesApiView(ListAPIView):
    queryset = CoursesTimes.objects.all()
    serializer_class = CoursesTimesSerializer
    permission_classes = (AllowAny,)


class CoursesTimesDetailApiView(RetrieveAPIView):
    queryset = CoursesTimes.objects.all()
    serializer_class = CoursesTimesSerializer
    permission_classes = (AllowAny,)


class CourseRegistrationsApiView(ListAPIView):
    queryset = CourseRegistrations.objects.all()
    serializer_class = CourseRegistrationsSerailizer
    permission_classes = (AllowAny,)


class CourseRegistrationsCreateApiView(CreateAPIView):
    serializer_class = CourseRegistrationsSerailizer
    permission_classes = (AllowAny,)



class CourseRegistrationsDetailApiView(RetrieveAPIView):
    queryset = CourseRegistrations.objects.all()
    serializer_class = CourseRegistrationsSerailizer
    permission_classes = (AllowAny,)


class HeadersBarsApiView(ListAPIView):
    queryset = HeadersBars.objects.all()
    serializer_class = HeadersBarsSerializer
    permission_classes = (AllowAny,)


class HeadersBarsDetailApiView(RetrieveAPIView):
    queryset = HeadersBars.objects.all()
    serializer_class = HeadersBarsSerializer
    permission_classes = (AllowAny,)

class UrlsApiView(ListAPIView):
    queryset = Urls.objects.all()
    serializer_class = UrlsSerializer
    permission_classes = (AllowAny,)


class UrlsDetailApiView(RetrieveAPIView):
    queryset = Urls.objects.all()
    serializer_class = UrlsSerializer
    permission_classes = (AllowAny,)


class MenusTitlesApiView(ListAPIView):
    queryset = MenusTitles.objects.all()
    serializer_class = MenusTitlesSerializer
    permission_classes = (AllowAny,)


class MenusTitlesDetailApiView(RetrieveAPIView):
    queryset = MenusTitles.objects.all()
    serializer_class = MenusTitlesSerializer
    permission_classes = (AllowAny,)


class MenusElementsApiView(ListAPIView):
    queryset = MenusElements.objects.filter(is_published=True)
    serializer_class = MenusElementsSerializer
    permission_classes = (AllowAny,)


class MenusElementsDetailApiView(RetrieveAPIView):
    queryset = MenusElements.objects.filter(is_published=True)
    serializer_class = MenusElementsSerializer
    permission_classes = (AllowAny,)


class FootersBarsApiView(ListAPIView):
    queryset = FootersBars.objects.all()
    serializer_class = FootersBarsSerializer
    permission_classes = (AllowAny,)


class FootersBarsDetailApiView(RetrieveAPIView):
    queryset = FootersBars.objects.all()
    serializer_class = FootersBarsSerializer
    permission_classes = (AllowAny,)


class FilesTypesApiView(ListAPIView):
    queryset = FilesTypes.objects.all()
    serializer_class = FilesTypesSerializer
    permission_classes = (AllowAny,)


class FilesTypesDetailApiView(RetrieveAPIView):
    queryset = FilesTypes.objects.all()
    serializer_class = FilesTypesSerializer
    permission_classes = (AllowAny,)


class MediaFilesApiView(ListAPIView):
    queryset = MediaFiles.objects.all()
    serializer_class = MediaFilesSerializer
    permission_classes = (AllowAny,)


class MediaFilesDetailApiView(RetrieveAPIView):
    queryset = MediaFiles.objects.all()
    serializer_class = MediaFilesSerializer
    permission_classes = (AllowAny,)


class CommentsApiView(ListAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = (AllowAny,)


class CommentsDetailApiView(RetrieveAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = (AllowAny,)


class GroupApiView(ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (AllowAny,)


class GroupDetailApiView(RetrieveAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (AllowAny,)




