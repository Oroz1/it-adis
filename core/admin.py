from dataclasses import fields
from email import message
from re import search
from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from rest_framework.authtoken.models import Token
from django import forms
from .models import *


admin.site.site_header = 'It Adis'


class UserAdminForm(forms.ModelForm):
    information = forms.CharField(label='Доп. информация', widget=CKEditorUploadingWidget())
    
    class Meta:
        model = Pages
        fields = '__all__'


class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('id', 'username', 'name', 'phone_number', 'email')
    ordering = ('-created_at',)
    list_display = ('id', 'username', 'name', 'get_professions', 'phone_number', 'email', 'is_active',)
    list_display_links = ('id', 'name', 'username',)
    fieldsets = (
        (None, {'fields': ('username', 'name', 'email', 'information', 'profession', 'phone_number', 'is_active', 'status', 'is_superuser', 'password', 'created_at', 'updated_at',)},
         ),
    )
    add_fieldsets = (
        (None, {
            'fields': ('username', 'name', 'email', 'phone_number', 'status', 'information', 'profession', 'password1', 'password2', 'is_superuser',)}
         ),
    )
    readonly_fields = ('created_at', 'updated_at')

    def get_professions(self, obj):
        temp = ''
        for profession in obj.profession.all():
            temp += f'{profession.title}, '
        return temp

    get_professions.short_description = 'Профессии'


admin.site.register(User, UserAdminConfig)


@admin.register(UsersStatus)
class UsersStarus(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)

class PagesAdminForm(forms.ModelForm):
    content = forms.CharField(label='Контент', widget=CKEditorUploadingWidget())
    
    class Meta:
        model = Pages
        fields = '__all__'

@admin.register(Pages)
class PagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'user_id', 'is_published',) 
    list_filter = ['user_id', 'is_published']
    list_display_links = ('id', 'title',)
    search_fields = ('title', 'user_id',)
    readonly_fields = ('created_at', 'updated_at')
    form = PagesAdminForm


class PostsAdminForm(forms.ModelForm):
    content = forms.CharField(label='Контент', widget=CKEditorUploadingWidget())
    
    class Meta:
        model = Posts
        fields = '__all__'


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user_id', 'is_published',)
    list_filter = ['user_id', 'is_published']
    list_display_links = ('id', 'title',)
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('title', 'user_id',)
    form = PostsAdminForm


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)
    search_fields = ['title']
    readonly_fields = ('created_at', 'updated_at')


class CoursesAdminForm(forms.ModelForm):
    content = forms.CharField(label='Контент', widget=CKEditorUploadingWidget())
     
    class Meta:
        model = Courses
        fields = '__all__'


@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_tags', 'get_image',)
    list_display_links = ('id', 'title',)
    list_filter = ['tags',]
    search_fields = ['title']
    fields = ('title', 'image', 'short_content', 'css_file', 'content', 'note','tags', 'get_full_image')
    form = CoursesAdminForm
    def get_full_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" alt="" width="50%">')
    def get_tags(self, obj):
        temp = ''
        for tag in obj.tags.all():
            temp = temp + tag.title + ', '
        return temp
    
    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" alt="" width="100px">')
    
    get_tags.short_description = 'Теги'
    get_image.short_description = 'Изображение'
    get_full_image.short_description = 'Заголовочная кортина'

    readonly_fields = ('created_at', 'updated_at', 'get_full_image')



@admin.register(ShiftsDays)
class ShiftsDaysAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)
    search_fields = ['title']
    readonly_fields = ('created_at', 'updated_at')


@admin.register(CoursesTimes)
class CoursesTimesAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'group', 'shift_time', 'start_time', 'end_time',)
    list_display_links = ('id', 'course',)
    list_filter = ('id', 'course', 'group', 'shift_time',)
    search_fields = ['course', 'id',]
    readonly_fields = ('created_at', 'updated_at')


@admin.register(CourseRegistrations)
class CourseRegistrationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone_number', 'email', 'course', 'course_time',)
    list_display_links = ('id', 'full_name',)
    list_filter = ['course', 'course_time']
    search_fields = ['full_name', 'id', 'course']
    readonly_fields = ('created_at', 'updated_at')


@admin.register(CoursesRelease)
class CoursesReleasesAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'group','release_date', 'is_active','is_published',)
    list_display_links = ('id', 'course',)
    search_fields = ['course', 'id']
    list_filter = ['is_active', 'is_published']
    readonly_fields = ('created_at', 'updated_at')


@admin.register(HeadersBars)
class HeadersBarsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'under_title')
    list_display_links = ('id', 'title',)
    search_fields = ['title', 'under_title','id']
    fields = ('created_at', 'updated_at', 'title', 'under_title', 'note', 'background_image', 'get_image')
    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.background_image.url}" alt="" width="50%">')
    readonly_fields = ('created_at', 'updated_at', 'get_image',)

    get_image.short_description = 'Фон'


@admin.register(Urls)
class UrlsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url')
    list_display_links = ('id', 'title',)
    search_fields = ('id', 'title')
    readonly_fields = ('created_at', 'updated_at',)


@admin.register(TypeOfCourses)
class TypeOfCoursesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title',)
    search_fields = ('id', 'title')
    readonly_fields = ('created_at', 'updated_at',)


@admin.register(Professions)
class ProfessionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title',)
    search_fields = ('id', 'title')
    readonly_fields = ('created_at', 'updated_at',)


@admin.register(MenusTitles)
class MenuesTitelsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)
    search_fields = ('id', 'title',)
    search_fields = ('id', 'title')


@admin.register(MenusElements)
class MenusElementsAdmin(admin.ModelAdmin):
    list_display = ('id', 'menu', 'title', 'icon', 'class_list', 'url', 'is_published',)
    list_display_links = ('id', 'menu', 'title',)
    search_fields = ('id', 'title',)
    list_filter = ('menu', 'url',)
    readonly_fields = ('created_at', 'updated_at',)


@admin.register(FootersBars)
class FootersBarsAdmin(admin.ModelAdmin):
    list_display = ('id','title',)
    list_display_links = ('id', 'title',)
    search_fields = ('id', 'title',)
    readonly_fields = ('created_at', 'updated_at',)


@admin.register(FilesTypes)
class FilesTypesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)
    readonly_fields = ('created_at', 'updated_at',)


@admin.register(MediaFiles)
class MediaFilesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'type', 'file_name',)
    list_display_links = ('id', 'title',)
    search_fields = ('id', 'title',)
    readonly_fields = ('created_at', 'updated_at',)

    def file_name(self, obj):
        return f'{obj.file.name}'

    file_name.short_description = 'Названия файла'


class MailsAdminForm(forms.ModelForm):
    message = forms.CharField(label='Сообщение', widget=CKEditorUploadingWidget())
     
    class Meta:
        model = Courses
        fields = '__all__'
        
@admin.register(Mails)
class MailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject',)
    list_display_links = ('id', 'subject',)
    search_fields = ('id', 'subject',)
    readonly_fields = ('created_at', 'updated_at',)
    form = MailsAdminForm


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user',)
    list_display_links = ('id', 'user',)
    search_fields = ('id', 'user',)
    readonly_fields = ('created_at', 'updated_at',)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'teacher')
    list_display_links = ('id', 'title',)
    search_fields = ('id', 'title',)
    list_filter = ('teacher',)
    readonly_fields = ('created_at', 'updated_at',)


class QuestionsAdminForm(forms.ModelForm):
    answer = forms.CharField(label='Ответ (Контетн)', widget=CKEditorUploadingWidget())
     
    class Meta:
        model = Questions
        fields = '__all__'


@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    form = QuestionsAdminForm
    list_display = ('id', 'question',)
    list_display_links = ('id', 'question',)
    search_fields = ('id', 'question',)
    readonly_fields = ('created_at', 'updated_at',)
# Register your models here.
