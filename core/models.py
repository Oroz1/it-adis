from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone
from rest_framework import serializers


#__models___
class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление') 
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    note = models.TextField(verbose_name='Заметки', blank=True, null=True)

    class Meta:
        abstract = True


# Программный менеджер для регистрации пользователя через shell 
class CustomAccountManager(BaseUserManager):
    
    def create_superuser(self, username, name, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(username, name, password, **other_fields)

    def create_user(self, username, name, password, **other_fields):

        user = self.model(username=username,
                          name=name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class UsersStatus(TimeStampMixin):
    
    class Meta:
        verbose_name = 'Статус пользователя'
        verbose_name_plural = 'Статусы пользователей'
        ordering = ['-updated_at']
        
    title = models.CharField(max_length=100, verbose_name='Наименование статуа')
    slug = models.SlugField(verbose_name='Slug название', default=None)

    def __str__(self):
        return self.title


class Professions(TimeStampMixin):

    class Meta:
        verbose_name = 'профессия'
        verbose_name_plural = 'профессии'
        ordering = ['-updated_at']

    title = models.CharField(max_length=100, verbose_name='название профессии')

    def __str__(self):
        return f'{self.title}'


# Таблица пользователя 
class User(AbstractBaseUser, PermissionsMixin, TimeStampMixin):
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = 'Пользователи'
        ordering = ['-updated_at']

    username = models.CharField(max_length=150, unique=True, verbose_name='Имя пользователя')
    name = models.CharField(max_length=150, blank=True, verbose_name='Полная имя')
    email = models.EmailField(verbose_name='Элетронная почта')
    status = models.ManyToManyField('UsersStatus', verbose_name='Статус(ы) пользователя')
    phone_number = models.CharField(max_length=15, verbose_name='Номер телефона', null=True)
    information = models.TextField(verbose_name='Информация о пользователе')
    profession = models.ManyToManyField('Professions', verbose_name='Профессии')
    is_staff = models.BooleanField(default=True, verbose_name='Подтверждение')
    is_active = models.BooleanField(default=True, verbose_name='Подтверждение по почте')
    is_superuser = models.BooleanField(default=False, verbose_name='Статус администратора')
    objects = CustomAccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name',]

    def __str__(self):
        return f'{self.username} - {self.name}'

    
class Pages(TimeStampMixin):
        
    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'
        ordering = ['-updated_at']

    slug = models.SlugField(verbose_name='Slug название')
    title = models.CharField(max_length=255, verbose_name='Заголовок страницы')
    content = models.TextField(verbose_name='Контент страницы')
    css_file = models.FileField(upload_to='css_files/', null=True, blank=True, verbose_name='CSS файл')
    user_id = models.ForeignKey('User', on_delete=models.CASCADE, null=True, verbose_name='Пользователь')
    is_published = models.BooleanField(verbose_name='Опубликовать', default=False)

    def __str__(self):
        return self.title

    
class Posts(TimeStampMixin):
        
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-updated_at']

    title = models.CharField(max_length=255, verbose_name='Заголовок поста')
    short_content = models.TextField(verbose_name='Краткое описание поста')
    content = models.TextField(verbose_name='Контент поста')
    css_file = models.FileField(upload_to='css_files/', null=True, blank=True, verbose_name='CSS файл')
    user_id = models.ForeignKey('User', on_delete=models.CASCADE, null=True, verbose_name='Пользователь')
    is_published = models.BooleanField(verbose_name='Опубликовать', default=False)

    def __str__(self):
        return self.title


class Tags(TimeStampMixin):

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['-updated_at']

    title = models.CharField(verbose_name='Название тега', max_length=255)

    def __str__(self):
        return self.title

class Group(TimeStampMixin):

    class Meta:
        verbose_name = 'группа'
        verbose_name_plural = 'группы'
        ordering = ['-updated_at']

    title = models.CharField(max_length=50, verbose_name='Название группы')
    description = models.TextField(verbose_name='описание')
    students = models.ManyToManyField('User', verbose_name='Студенты', related_name="users")
    teacher = models.ForeignKey('User', on_delete=models.PROTECT, verbose_name='Ментор', related_name='user')

    def __str__(self):
        return f'{self.title}'


class Courses(TimeStampMixin):

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ['-updated_at']

    slug = models.SlugField(verbose_name='Slug название')
    title = models.CharField(max_length=255, verbose_name='Название курса')
    image = models.ImageField(upload_to='courses/', verbose_name='Заголовочная кортина')
    short_content = models.TextField(verbose_name='Краткое описание')
    content = models.TextField(verbose_name='Контент')
    css_file = models.FileField(upload_to='css_files/', null=True, blank=True, verbose_name='CSS файл')
    tags = models.ManyToManyField('Tags', verbose_name='Теги')

    @property
    def get_info(self):
        if self.id is not None:
            temp = CoursesRelease.objects.filter(course__id=self.id)
            serializer = CoursesReleaseSerializer(temp, many=True)
            return serializer.data
        return None  

    def __str__(self):
        return self.title


class ShiftsDays(TimeStampMixin):

    class Meta:
        verbose_name = 'График смены'
        verbose_name_plural = 'Графики смен'
        ordering = ['-updated_at']

    
    title = models.CharField(verbose_name='Название', max_length=255)

    def __str__(self) -> str:
        return self.title


class CoursesTimes(TimeStampMixin):

    class Meta:
        verbose_name = 'Расписание курса'
        verbose_name_plural = 'Расписание курсов'
        ordering = ['-updated_at']

    slug = models.SlugField(verbose_name='Slug название')    
    course = models.ForeignKey('Courses', on_delete=models.CASCADE, null=True, verbose_name='Курс')
    group = models.ForeignKey('Group', on_delete=models.PROTECT, verbose_name='Группа')
    shift_time = models.ForeignKey('ShiftsDays', on_delete=models.PROTECT, null=True, verbose_name='График смены')
    start_time = models.TimeField(verbose_name='Начало веремени курса')
    end_time = models.TimeField(verbose_name='Окончание времени курса')

    def __str__(self):
        return f'{self.course}'

    
class TypeOfCourses(TimeStampMixin):

    class Meta:
        verbose_name = 'Формат обучение'
        verbose_name_plural = 'Форматы обучении'

    title = models.CharField(max_length=50, verbose_name='Название формата')

    def __str__(self):
        return f'{self.title}'


class CourseRegistrations(TimeStampMixin):

    class Meta:
        verbose_name = 'Запись на курс'
        verbose_name_plural = 'Записи на курсы'
        ordering = ['-updated_at']

    full_name = models.CharField(max_length=255, verbose_name='Имя и фамилия')
    phone_number = models.CharField(max_length=15, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Почта')
    personal_info = models.TextField(verbose_name='Допалнительная информация', blank=True, null=True)
    course = models.ForeignKey('Courses', on_delete=models.PROTECT, null=True, verbose_name='Курс')
    course_time = models.ForeignKey('ShiftsDays', on_delete=models.PROTECT, null=True, verbose_name='Время курса')
    def __str__(self):
        return f'{self.full_name} - {self.course}'


class HeadersBars(TimeStampMixin):

    class Meta:
        verbose_name = 'заголовок'
        verbose_name_plural = 'заголовки'
        ordering = ['-updated_at']
    
    title = models.CharField(verbose_name='Название заголовка', max_length=400)
    under_title = models.CharField(verbose_name='Название подзаголовка', max_length=400)
    background_image = models.ImageField(upload_to='headers_background/', verbose_name='Фоновое изображение')

    def __str__(self):
        return self.title


class Urls(TimeStampMixin):

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'
        ordering = ['-updated_at']

    title = models.CharField(max_length=255, verbose_name='Название ссылки')
    url = models.CharField(max_length=2000, verbose_name='Ссылка')

    def __str__(self):
        return self.title


class MenusTitles(TimeStampMixin):

    class Meta:
        verbose_name = 'Название меню'
        verbose_name_plural = 'Название меню'

    title = models.CharField(max_length=255, verbose_name='Название меню')
    def __str__(self):
        return f'{self.title}'


class MenusElements(TimeStampMixin):

    class Meta:
        verbose_name = 'Меню эелемент'
        verbose_name_plural = 'Меню эелементы'
        ordering = ['-updated_at']

    menu = models.ForeignKey('MenusTitles', on_delete=models.PROTECT, null=True, verbose_name='Меню')
    title = models.CharField(max_length=255, verbose_name='Название меню элемента')
    icon = models.CharField(max_length=255, verbose_name='Font-awesome иконка')
    class_list =  models.TextField(verbose_name='CSS Классы')
    url = models.ForeignKey('Urls', on_delete=models.PROTECT, null=True, verbose_name='Ссылка')
    is_published = models.BooleanField(verbose_name='Опубликовать')

    def __str__(self) -> str:
        return self.title


class FootersBars(TimeStampMixin):

    class Meta:
        verbose_name = 'Подвал сайта'
        verbose_name_plural = 'Подвал сайта'
        ordering = ['-updated_at']

    title = models.CharField(max_length=255, verbose_name='Название раздела')
    urls = models.ManyToManyField('Urls', verbose_name='Ссылка(и)')

    def __str__(self):
        return self.title


class FilesTypes(TimeStampMixin):

    class Meta:
        verbose_name = 'Формат файла'
        verbose_name_plural = 'Форматы файлов'
        ordering = ['-updated_at']

    title = models.CharField(max_length=10, verbose_name='Название формата')

    def __str__(self):
        return self.title
        

class MediaFiles(TimeStampMixin):

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
        ordering = ['-updated_at']

    title = models.CharField(max_length=255, verbose_name='Название файла')
    type = models.ForeignKey('FilesTypes', on_delete=models.PROTECT, null=True, verbose_name='Тип файла')
    file = models.FileField(upload_to='files/', verbose_name='Файл')

    def __str__(self):
        return self.title


class Mails(TimeStampMixin):
    class Meta:
        verbose_name = 'Письма'
        verbose_name_plural = 'Письма'
        ordering = ['-updated_at']

    subject = models.CharField(max_length=300, verbose_name='Тема')
    message = models.TextField(verbose_name='Сообщение')
    send_to = models.ManyToManyField('CourseRegistrations', verbose_name='Получатели')

    def __str__(self):
        return f'{self.subject}'


class Comments(TimeStampMixin):

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-updated_at']

    comment = models.TextField(verbose_name='Комментарий')
    is_published = models.BooleanField(verbose_name='Опубликовать')
    user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='Пользователь')

    @property
    def get_user_name(self):
        if self.user is not None:
            return self.user.name
        return self.user.name
    
    @property
    def get_user_professions(self):
        if self.user is not None:
            return self.user.profession.all().values()
        return self.user

    def __str__(self):
        return f'{self.user}'


class Questions(TimeStampMixin):
    class Meta:
        verbose_name = 'часто задаваемый вопрос'
        verbose_name_plural = 'часто задаваемые вопросы'
        ordering = ['-updated_at']

    question = models.CharField(max_length=1000, verbose_name='Вопрос')
    answer = models.TextField(verbose_name='Ответ (Контетн)')
    css_file = models.FileField(upload_to='css_files/', null=True, blank=True, verbose_name='CSS файл')

    def __str__(self):
        return f'{self.question}'


class Attributes(TimeStampMixin):

    class Meta:
        verbose_name = 'атрибут'
        verbose_name_plural = 'атрибуты'
        ordering = ['-updated_at']

    title = models.CharField(max_length=255, verbose_name='название')
    value = models.CharField(max_length=255, verbose_name='значение')

    def __str__(self):
        return f'{self.title}'



class AttributsModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attributes
        fields = '__all__' 


class CoursesRelease(TimeStampMixin):
    
    class Meta:
        verbose_name = 'Релиз курса'
        verbose_name_plural = 'Релизы курсов'
        ordering = ['-updated_at']

    slug = models.SlugField(verbose_name='Slug название') 
    course = models.ForeignKey('Courses', on_delete=models.CASCADE, verbose_name='Курс')
    course_name = models.CharField(max_length=455, verbose_name='Название релиза')
    image = models.ImageField(upload_to='courses_rel/', verbose_name='Картина')
    group = models.ForeignKey('Group', on_delete=models.PROTECT, verbose_name='Называния группы')
    description = models.TextField(verbose_name='Описание')
    release_date = models.DateTimeField(verbose_name='Дата началы курса')
    attributes = models.ManyToManyField('Attributes', blank=True, verbose_name='атрибуты')
    length_of_education = models.CharField(max_length=50, verbose_name='Длительность обучение')
    level = models.CharField(max_length=50, verbose_name='Уровень курса')
    type_of_courses = models.ForeignKey('TypeOfCourses', on_delete=models.PROTECT, verbose_name='Формат обучение')
    is_active = models.BooleanField(verbose_name='Начался ли курс')
    is_published = models.BooleanField('Опубликовать')
    
    @property
    def get_course_name(self):
        if self.course is not None:
            return self.course.title
        return None

    @property
    def get_attributes(self):
        if self.attributes is not None:
    
            return AttributsModelSerializer(self.attributes.all(), many=True).data
        return self.attributes

    def __str__(self):
        return f'{self.course}'

    
class CoursesReleaseSerializer(serializers.ModelSerializer):
    type_of_courses = serializers.SlugRelatedField(slug_field='title', read_only=True, many=False)

    class Meta:
        model = CoursesRelease
        fields = (
            'release_date',
            'length_of_education',
            'level',
            'type_of_courses',
         )