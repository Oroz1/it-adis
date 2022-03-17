# Generated by Django 3.2.12 on 2022-03-17 08:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Заметки')),
                ('username', models.CharField(max_length=150, unique=True, verbose_name='Имя пользователя')),
                ('name', models.CharField(blank=True, max_length=150, verbose_name='Полная имя')),
                ('email', models.EmailField(max_length=254, verbose_name='Элетронная почта')),
                ('phone_number', models.CharField(max_length=15, null=True, verbose_name='Номер телефона')),
                ('information', models.TextField(verbose_name='Информация о пользователе')),
                ('is_staff', models.BooleanField(default=True, verbose_name='Подтверждение')),
                ('is_active', models.BooleanField(default=True, verbose_name='Подтверждение по почте')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Статус администратора')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'ordering': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='CourseRegistrations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Заметки')),
                ('full_name', models.CharField(max_length=255, verbose_name='Имя и фамилия')),
                ('phone_number', models.CharField(max_length=15, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('personal_info', models.TextField(verbose_name='Допалнительная информация')),
            ],
            options={
                'verbose_name': 'Запись на курс',
                'verbose_name_plural': 'Записи на курсы',
                'ordering': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Заметки')),
                ('slug', models.SlugField(verbose_name='Slug название')),
                ('title', models.CharField(max_length=255, verbose_name='Название курса')),
                ('image', models.ImageField(upload_to='courses/', verbose_name='Заголовочная кортина')),
                ('short_content', models.TextField(verbose_name='Краткое описание')),
                ('content', models.TextField(verbose_name='Контент')),
                ('css_file', models.FileField(blank=True, null=True, upload_to='css_files/', verbose_name='CSS файл')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
                'ordering': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='FilesTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Заметки')),
                ('title', models.CharField(max_length=10, verbose_name='Название формата')),
            ],
            options={
                'verbose_name': 'Формат файла',
                'verbose_name_plural': 'Форматы файлов',
                'ordering': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='HeadersBars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Заметки')),
                ('title', models.CharField(max_length=400, verbose_name='Название заголовка')),
                ('under_title', models.CharField(max_length=400, verbose_name='Название подзаголовка')),
                ('background_image', models.ImageField(upload_to='headers_background/', verbose_name='Фоновое изображение')),
            ],
            options={
                'verbose_name': 'заголовок',
                'verbose_name_plural': 'заголовки',
                'ordering': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='MenusTitles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Заметки')),
                ('title', models.CharField(max_length=255, verbose_name='Название меню')),
            ],
            options={
                'verbose_name': 'Название меню',
                'verbose_name_plural': 'Название меню',
            },
        ),
        migrations.CreateModel(
            name='Professions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Заметки')),
                ('title', models.CharField(max_length=100, verbose_name='название профессии')),
            ],
            options={
                'verbose_name': 'профессия',
                'verbose_name_plural': 'профессии',
                'ordering': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Заметки')),
                ('question', models.CharField(max_length=1000, verbose_name='Вопрос')),
                ('answer', models.TextField(verbose_name='Ответ (Контетн)')),
                ('css_file', models.FileField(blank=True, null=True, upload_to='css_files/', verbose_name='CSS файл')),
            ],
            options={
                'verbose_name': 'часто задаваемый вопрос',
                'verbose_name_plural': 'часто задаваемые вопросы',
                'ordering': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='ShiftsDays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Заметки')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'График смены',
                'verbose_name_plural': 'Графики смен',
                'ordering': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Заметки')),
                ('title', models.CharField(max_length=255, verbose_name='Название тега')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
                'ordering': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='TypeOfCourses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Заметки')),
                ('title', models.CharField(max_length=50, verbose_name='Название формата')),
            ],
            options={
                'verbose_name': 'Формат обучение',
                'verbose_name_plural': 'Форматы обучении',
            },
        ),
        migrations.CreateModel(
            name='Urls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Заметки')),
                ('title', models.CharField(max_length=255, verbose_name='Название ссылки')),
                ('url', models.CharField(max_length=2000, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Ссылка',
                'verbose_name_plural': 'Ссылки',
                'ordering': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='UsersStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Заметки')),
                ('title', models.CharField(max_length=100, verbose_name='Наименование статуа')),
                ('slug', models.SlugField(default=None, verbose_name='Slug название')),
            ],
            options={
                'verbose_name': 'Статус пользователя',
                'verbose_name_plural': 'Статусы пользователей',
                'ordering': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Заметки')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок поста')),
                ('short_content', models.TextField(verbose_name='Краткое описание поста')),
                ('content', models.TextField(verbose_name='Контент поста')),
                ('css_file', models.FileField(blank=True, null=True, upload_to='css_files/', verbose_name='CSS файл')),
                ('is_published', models.BooleanField(default=False, verbose_name='Опубликовать')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
                'ordering': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='Pages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Заметки')),
                ('slug', models.SlugField(verbose_name='Slug название')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок страницы')),
                ('content', models.TextField(verbose_name='Контент страницы')),
                ('css_file', models.FileField(blank=True, null=True, upload_to='css_files/', verbose_name='CSS файл')),
                ('is_published', models.BooleanField(default=False, verbose_name='Опубликовать')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Страница',
                'verbose_name_plural': 'Страницы',
                'ordering': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='MenusElements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Заметки')),
                ('title', models.CharField(max_length=255, verbose_name='Название меню элемента')),
                ('icon', models.CharField(max_length=255, verbose_name='Font-awesome иконка')),
                ('class_list', models.TextField(verbose_name='CSS Классы')),
                ('is_published', models.BooleanField(verbose_name='Опубликовать')),
                ('menu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.menustitles', verbose_name='Меню')),
                ('url', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.urls', verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Меню эелемент',
                'verbose_name_plural': 'Меню эелементы',
                'ordering': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='MediaFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Заметки')),
                ('title', models.CharField(max_length=255, verbose_name='Название файла')),
                ('file', models.FileField(upload_to='files/', verbose_name='Файл')),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.filestypes', verbose_name='Тип файла')),
            ],
            options={
                'verbose_name': 'Файл',
                'verbose_name_plural': 'Файлы',
                'ordering': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='Mails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Заметки')),
                ('subject', models.CharField(max_length=300, verbose_name='Тема')),
                ('message', models.TextField(verbose_name='Сообщение')),
                ('send_to', models.ManyToManyField(to='core.CourseRegistrations', verbose_name='Получатели')),
            ],
            options={
                'verbose_name': 'Письма',
                'verbose_name_plural': 'Письма',
                'ordering': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Заметки')),
                ('title', models.CharField(max_length=50, verbose_name='Название группы')),
                ('description', models.TextField(verbose_name='описание')),
                ('students', models.ManyToManyField(related_name='users', to=settings.AUTH_USER_MODEL, verbose_name='Студенты')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='Ментор')),
            ],
            options={
                'verbose_name': 'группа',
                'verbose_name_plural': 'группы',
                'ordering': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='FootersBars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Заметки')),
                ('title', models.CharField(max_length=255, verbose_name='Название раздела')),
                ('urls', models.ManyToManyField(to='core.Urls', verbose_name='Ссылка(и)')),
            ],
            options={
                'verbose_name': 'Подвал сайта',
                'verbose_name_plural': 'Подвал сайта',
                'ordering': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='CoursesTimes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Заметки')),
                ('slug', models.SlugField(verbose_name='Slug название')),
                ('start_time', models.TimeField(verbose_name='Начало веремени курса')),
                ('end_time', models.TimeField(verbose_name='Окончание времени курса')),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.courses', verbose_name='Курс')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.group', verbose_name='Группа')),
                ('shift_time', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.shiftsdays', verbose_name='График смены')),
            ],
            options={
                'verbose_name': 'Расписание курса',
                'verbose_name_plural': 'Расписание курсов',
                'ordering': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='CoursesRelease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Заметки')),
                ('slug', models.SlugField(verbose_name='Slug название')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('release_date', models.DateTimeField(verbose_name='Дата началы курса')),
                ('length_of_education', models.CharField(max_length=50, verbose_name='Длительность обучение')),
                ('level', models.CharField(max_length=50, verbose_name='Уровень курса')),
                ('is_active', models.BooleanField(verbose_name='Начался ли курс')),
                ('is_published', models.BooleanField(verbose_name='Опубликовать')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.courses', verbose_name='Курс')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.group', verbose_name='Называния группы')),
                ('type_of_courses', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.typeofcourses', verbose_name='Формат обучение')),
            ],
            options={
                'verbose_name': 'Релиз курса',
                'verbose_name_plural': 'Релизы курсов',
                'ordering': ['-updated_at'],
            },
        ),
        migrations.AddField(
            model_name='courses',
            name='tags',
            field=models.ManyToManyField(to='core.Tags', verbose_name='Теги'),
        ),
        migrations.AddField(
            model_name='courseregistrations',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.courses', verbose_name='Курс'),
        ),
        migrations.AddField(
            model_name='courseregistrations',
            name='course_time',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.shiftsdays', verbose_name='Время курса'),
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Заметки')),
                ('comment', models.TextField(verbose_name='Комментарий')),
                ('is_published', models.BooleanField(verbose_name='Опубликовать')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
                'ordering': ['-updated_at'],
            },
        ),
        migrations.AddField(
            model_name='user',
            name='profession',
            field=models.ManyToManyField(to='core.Professions', verbose_name='Профессии'),
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.ManyToManyField(to='core.UsersStatus', verbose_name='Статус(ы) пользователя'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
