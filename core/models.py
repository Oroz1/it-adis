from calendar import c
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone


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

    email_confirmed = models.BooleanField(default=False, verbose_name='Подтверждение по почте')
    is_staff = models.BooleanField(default=True, verbose_name='Подтверждение')
    is_active = models.BooleanField(default=True,)
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
    user_id = models.ForeignKey('User', on_delete=models.CASCADE, null=True, verbose_name='Пользователь')
    published = models.BooleanField(verbose_name='Статус видимости', default=False)

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
    user_id = models.ForeignKey('User', on_delete=models.CASCADE, null=True, verbose_name='Пользователь')
    published = models.BooleanField(verbose_name='Статус видимости', default=False)

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


class Courses(TimeStampMixin):

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ['-updated_at']

    title = models.CharField(max_length=255, verbose_name='Название курса')
    image = models.ImageField(upload_to='courses/', verbose_name='Заголовочная кортина')
    short_content = models.TextField(verbose_name='Краткое описание')
    content = models.TextField(verbose_name='Контент')
    tags = models.ManyToManyField('Tags', verbose_name='Теги')


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
        verbose_name = 'Время курса'
        verbose_name_plural = 'Время курсов'
        ordering = ['-updated_at']
        
    course = models.ForeignKey('Courses', on_delete=models.CASCADE, null=True, verbose_name='Курс')
    shift_time = models.ForeignKey('ShiftsDays', on_delete=models.PROTECT, null=True, verbose_name='График смены')
    start_time = models.TimeField(verbose_name='Начало веремени курса')
    end_time = models.TimeField(verbose_name='Окончание времени курса')

    def __str__(self):
        return self.course

    
class CoursesRelease(TimeStampMixin):

    class Meta:
        verbose_name = 'Релиз курса'
        verbose_name_plural = 'Релизы курсов'
        ordering = ['-updated_at']

    course = models.ForeignKey('Courses', on_delete=models.CASCADE, verbose_name='Курс')
    group = models.CharField(max_length=300, verbose_name='Называния группы')
    release_date = models.DateTimeField(verbose_name='Дата началы курса')
    is_active = models.BooleanField(verbose_name='Начался ли курс')
    is_published = models.BooleanField('Опубликовать')

    def __str__(self):
        return self.course


class CourseRegistrations(TimeStampMixin):

    class Meta:
        verbose_name = 'Запись на курс'
        verbose_name_plural = 'Записи на курсы'
        ordering = ['-updated_at']

    full_name = models.CharField(max_length=255, verbose_name='Имя и фамилия')
    phone_number = models.CharField(max_length=15, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Почта')
    personal_info = models.TextField(verbose_name='Допалнительная информация')
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
    is_active = models.BooleanField(verbose_name='Видемость')

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
