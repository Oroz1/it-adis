from rest_framework.response import Response
from rest_framework.generics import ListAPIView, ListCreateAPIView, GenericAPIView, RetrieveDestroyAPIView, CreateAPIView, RetrieveUpdateAPIView
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


class UsersStatusDetailApiView(ListAPIView):
    serializer_class = UsersStatusSerializer
    permission_classes = (AllowAny,)

    def list(self, request, pk):
        try:
            queryset = UsersStatus.objects.get(id=pk)
            serializer = self.serializer_class(queryset, many=False)
            return Response(serializer.data)
        except Exception:
            return Response({'detail': 'Данного статуса не существует'}, status=Status.HTTP_404_NOT_FOUND)


class CoursesReleaseApiView(ListAPIView):
    queryset = CoursesRelease.objects.filter(is_published=True)
    serializer_class = CoursesReleaseSerializer
    permission_classes = (AllowAny,)


class CoursesReleaseDetailApiView(ListAPIView):
    serializer_class = CoursesReleaseSerializer
    permission_classes = (AllowAny,)

    def list(self, request, pk):
        try:
            queryset = CoursesRelease.objects.get(id=pk)
            serializer = self.serializer_class(queryset, many=False)
            return Response(serializer.data)
        except Exception:
            return Response({'detail': 'Данного релиза не существует'}, status=Status.HTTP_404_NOT_FOUND)



class CoursesApiView(ListAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
    permission_classes = (AllowAny,)


class CoursesDetailApiView(ListAPIView):
    serializer_class = CoursesSerializer
    permission_classes = (AllowAny,)

    def list(self, request, pk):
        try:
            queryset = Courses.objects.get(id=pk)
            serializer = self.serializer_class(queryset, many=False)
            return Response(serializer.data)
        except Exception:
            return Response({'detail': 'Данного курса не существует'}, status=Status.HTTP_404_NOT_FOUND)


class UserApiView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class UserDetailApiView(ListAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def list(self, request, pk):
        try:
            queryset = User.objects.get(id=pk)
            serializer = self.serializer_class(queryset, many=False)
            return Response(serializer.data)
        except Exception:
            return Response({'detail': 'Данного пользователя не существует'}, status=Status.HTTP_404_NOT_FOUND)


class PagesApiView(ListAPIView):
    queryset = Pages.objects.filter(is_published=True)
    serializer_class = PagesSerializer
    permission_classes = (AllowAny,)


class PagesDetailApiView(ListAPIView):
    serializer_class = PagesSerializer
    permission_classes = (AllowAny,)

    def list(self, request, pk):
        try:
            queryset = Pages.objects.get(id=pk)
            serializer = self.serializer_class(queryset, many=False)
            return Response(serializer.data)
        except Exception:
            return Response({'detail': 'Данной страницы не существует'}, status=Status.HTTP_404_NOT_FOUND)


class PostsApiView(ListAPIView):
    queryset = Posts.objects.filter(is_published=True)
    serializer_class = PostsSerializer
    permission_classes = (AllowAny,)


class PostsDetailApiView(ListAPIView):
    serializer_class = PostsSerializer
    permission_classes = (AllowAny,)

    def list(self, request, pk):
        try:
            queryset = Posts.objects.get(id=pk)
            serializer = self.serializer_class(queryset, many=False)
            return Response(serializer.data)
        except Exception:
            return Response({'detail': 'Данног поста не существует'}, status=Status.HTTP_404_NOT_FOUND)


class TagsApiView(ListAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer
    permission_classes = (AllowAny,)


class TagsDetailApiView(ListAPIView):
    serializer_class = TagsSerializer
    permission_classes = (AllowAny,)

    def list(self, request, pk):
        try:
            queryset = Tags.objects.get(id=pk)
            serializer = self.serializer_class(queryset, many=False)
            return Response(serializer.data)
        except Exception:
            return Response({'detail': 'Данного тега не существует'}, status=Status.HTTP_404_NOT_FOUND)


class ShiftsDaysApiView(ListAPIView):
    queryset = ShiftsDays.objects.all()
    serializer_class = ShiftsDaysSerializer
    permission_classes = (AllowAny,)


class ShiftsDaysDetailApiView(ListAPIView):
    serializer_class = ShiftsDaysSerializer
    permission_classes = (AllowAny,)

    def list(self, request, pk):
        try:
            queryset = ShiftsDays.objects.get(id=pk)
            serializer = self.serializer_class(queryset, many=False)
            return Response(serializer.data)
        except Exception:
            return Response({'detail': 'Данного смены дня не существует'}, status=Status.HTTP_404_NOT_FOUND)


class CoursesTimesApiView(ListAPIView):
    queryset = CoursesTimes.objects.all()
    serializer_class = CoursesTimesSerializer
    permission_classes = (AllowAny,)


class CoursesTimesDetailApiView(ListAPIView):
    serializer_class = CoursesTimesSerializer
    permission_classes = (AllowAny,)

    def list(self, request, pk):
        try:
            queryset = CoursesTimes.objects.get(id=pk)
            serializer = self.serializer_class(queryset, many=False)
            return Response(serializer.data)
        except Exception:
            return Response({'detail': 'Данноого регламента не существует'}, status=Status.HTTP_404_NOT_FOUND)


class CourseRegistrationsApiView(ListAPIView):
    queryset = CourseRegistrations.objects.all()
    serializer_class = CourseRegistrationsSerailizer
    permission_classes = (AllowAny,)


class CourseRegistrationsCreateApiView(CreateAPIView):
    serializer_class = CourseRegistrationsSerailizer
    permission_classes = (AllowAny,)



class CourseRegistrationsDetailApiView(ListAPIView):
    serializer_class = CourseRegistrationsSerailizer
    permission_classes = (AllowAny,)

    def list(self, request, pk):
        try:
            queryset = CourseRegistrations.objects.get(id=pk)
            serializer = self.serializer_class(queryset, many=False)
            return Response(serializer.data)
        except Exception:
            return Response({'detail': 'Данноой регистраций не существует'}, status=Status.HTTP_404_NOT_FOUND)


class HeadersBarsApiView(ListAPIView):
    queryset = HeadersBars.objects.all()
    serializer_class = HeadersBarsSerializer
    permission_classes = (AllowAny,)


class HeadersBarsDetailApiView(ListAPIView):
    serializer_class = HeadersBarsSerializer
    permission_classes = (AllowAny,)

    def list(self, request, pk):
        try:
            queryset = HeadersBars.objects.get(id=pk)
            serializer = self.serializer_class(queryset, many=False)
            return Response(serializer.data)
        except Exception:
            return Response({'detail': 'Данного заголовка для страницы не существует'}, status=Status.HTTP_404_NOT_FOUND)


class UrlsApiView(ListAPIView):
    queryset = Urls.objects.all()
    serializer_class = UrlsSerializer
    permission_classes = (AllowAny,)


class UrlsDetailApiView(ListAPIView):
    serializer_class = UrlsSerializer
    permission_classes = (AllowAny,)

    def list(self, request, pk):
        try:
            queryset = Urls.objects.get(id=pk)
            serializer = self.serializer_class(queryset, many=False)
            return Response(serializer.data)
        except Exception:
            return Response({'detail': 'Данного ссылки не существует'}, status=Status.HTTP_404_NOT_FOUND)


class MenusTitlesApiView(ListAPIView):
    queryset = MenusTitles.objects.all()
    serializer_class = MenusTitlesSerializer
    permission_classes = (AllowAny,)


class MenusTitlesDetailApiView(ListAPIView):
    serializer_class = MenusTitlesSerializer
    permission_classes = (AllowAny,)

    def list(self, request, pk):
        try:
            queryset = MenusTitles.objects.get(id=pk)
            serializer = self.serializer_class(queryset, many=False)
            return Response(serializer.data)
        except Exception:
            return Response({'detail': 'Данного название меню не существует'}, status=Status.HTTP_404_NOT_FOUND)


class MenusElementsApiView(ListAPIView):
    queryset = MenusElements.objects.filter(is_published=True)
    serializer_class = MenusElementsSerializer
    permission_classes = (AllowAny,)


class MenusElementsDetailApiView(ListAPIView):
    serializer_class = MenusElementsSerializer
    permission_classes = (AllowAny,)

    def list(self, request, pk):
        try:
            queryset = MenusElements.objects.get(id=pk)
            serializer = self.serializer_class(queryset, many=False)
            return Response(serializer.data)
        except Exception:
            return Response({'detail': 'Данного меню элемента не существует'}, status=Status.HTTP_404_NOT_FOUND)


class FootersBarsApiView(ListAPIView):
    queryset = FootersBars.objects.all()
    serializer_class = FootersBarsSerializer
    permission_classes = (AllowAny,)


class FootersBarsDetailApiView(ListAPIView):
    serializer_class = FootersBarsSerializer
    permission_classes = (AllowAny,)

    def list(self, request, pk):
        try:
            queryset = FootersBars.objects.get(id=pk)
            serializer = self.serializer_class(queryset, many=False)
            return Response(serializer.data)
        except Exception:
            return Response({'detail': 'Данной страныцы для подвала сайта не существует'}, status=Status.HTTP_404_NOT_FOUND)


class FilesTypesApiView(ListAPIView):
    queryset = FilesTypes.objects.all()
    serializer_class = FilesTypesSerializer
    permission_classes = (AllowAny,)


class FilesTypesDetailApiView(ListAPIView):
    serializer_class = FilesTypesSerializer
    permission_classes = (AllowAny,)

    def list(self, request, pk):
        try:
            queryset = FilesTypes.objects.get(id=pk)
            serializer = self.serializer_class(queryset, many=False)
            return Response(serializer.data)
        except Exception:
            return Response({'detail': 'Данного формата файла не существует'}, status=Status.HTTP_404_NOT_FOUND)


class MediaFilesApiView(ListAPIView):
    queryset = MediaFiles.objects.all()
    serializer_class = MediaFilesSerializer
    permission_classes = (AllowAny,)


class MediaFilesDetailApiView(ListAPIView):
    serializer_class = MediaFilesSerializer
    permission_classes = (AllowAny,)

    def list(self, request, pk):
        try:
            queryset = MediaFiles.objects.get(id=pk)
            serializer = self.serializer_class(queryset, many=False)
            return Response(serializer.data)
        except Exception:
            return Response({'detail': 'Данного файла не существует'}, status=Status.HTTP_404_NOT_FOUND)


class CommentsApiView(ListAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = (AllowAny,)


class CommentsDetailApiView(ListAPIView):
    serializer_class = CommentsSerializer
    permission_classes = (AllowAny,)

    def list(self, request, pk):
        try:
            queryset = Comments.objects.get(id=pk)
            serializer = self.serializer_class(queryset, many=False)
            return Response(serializer.data)
        except Exception:
            return Response({'detail': 'Данного файла не существует'}, status=Status.HTTP_404_NOT_FOUND)






