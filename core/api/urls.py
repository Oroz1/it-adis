from django.urls import path, include
from core.api.views import *
from rest_framework.authtoken import views
from rest_framework_swagger.views import get_swagger_view


urlpatterns = [
    path('swagger/', get_swagger_view(title='Pastebin API')),

    path('courses/', CoursesApiView.as_view()),
    path('courses/<int:pk>/', CoursesDetailApiView.as_view()),
    
    path('users_status/', UsersStatusApiView.as_view()),
    path('users_status/<int:pk>/', UsersStatusDetailApiView.as_view()),
    
    path('courses_release/', CoursesReleaseApiView.as_view()),
    path('courses_release/<int:pk>/', CoursesReleaseDetailApiView.as_view()),
    
    path('user/', UserApiView.as_view()),
    path('user/<int:pk>/', UserDetailApiView.as_view()),
    
    path('pages/', PagesApiView.as_view()),
    path('pages/<int:pk>/', PagesDetailPkApiView.as_view()),
    path('pages/<str:slug>/', PagesDetailSlugApiView.as_view()),
    
    path('posts/', PostsApiView.as_view()),
    path('posts/<int:pk>/', PostsDetailApiView.as_view()),
    
    path('tags/', TagsApiView.as_view()),
    path('tags/<int:pk>/', TagsDetailApiView.as_view()),
    
    path('shifts_days/', ShiftsDaysApiView.as_view()),
    path('shifts_days/<int:pk>/', ShiftsDaysDetailApiView.as_view()),
    
    path('courses_times/', CoursesTimesApiView.as_view()),
    path('courses_times/<int:pk>/', CoursesTimesDetailApiView.as_view()),
    
    path('course_registrations/', CourseRegistrationsApiView.as_view()),
    path('course_registrations/<int:pk>/', CourseRegistrationsDetailApiView.as_view()),
    path('course_registrations/create/', CourseRegistrationsCreateApiView.as_view()),

    path('headers_bars/', HeadersBarsApiView.as_view()),
    path('headers_bars/<int:pk>/', HeadersBarsDetailApiView.as_view()),
    
    path('urls/', UrlsApiView.as_view()),
    path('urls/<int:pk>/', UrlsDetailApiView.as_view()),
    
    path('menus_titles/', MenusTitlesApiView.as_view()),
    path('menus_titles/<int:pk>/', MenusTitlesDetailApiView.as_view()),

    path('menus_elements/', MenusElementsApiView.as_view()),
    path('menus_elements/<int:pk>/', MenusElementsDetailApiView.as_view()),
    
    path('footers_bars/', FootersBarsApiView.as_view()),
    path('footers_bars/<int:pk>/', FootersBarsDetailApiView.as_view()),

    path('files_types/', FilesTypesApiView.as_view()),
    path('files_types/<int:pk>/', FilesTypesDetailApiView.as_view()),
    
    path('media_files/', MediaFilesApiView.as_view()),
    path('media_files/<int:pk>/', MediaFilesDetailApiView.as_view()),

    path('comments/', CommentsApiView.as_view()),
    path('comments/<int:pk>/', CommentsDetailApiView.as_view()),

    path('groups/', GroupApiView.as_view()),
    path('groups/<int:pk>/', GroupDetailApiView.as_view()),

    path('questions/', QuestionsApiView.as_view()),
    path('questions/<int:pk>/', QuestionsDetailApiView.as_view()),

    path('mentors/', TeacherApiView.as_view()),
    path('mentors/<int:pk>/', TeacherDetailApiView.as_view()),

    path('attributes/', AttributesApiView.as_view()),
    path('attributes/<int:pk>/', AttributesDetailApiView.as_view()),
]
