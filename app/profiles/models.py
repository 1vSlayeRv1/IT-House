from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager



class UserManager(BaseUserManager):
    """
    Django требует, чтобы кастомные пользователи определяли свой собственный
    класс Manager. Унаследовавшись от BaseUserManager, мы получаем много того
    же самого кода, который Django использовал для создания User (для демонстрации).
    """

    def create_user(self, username, email, password=None):
        """ Создает и возвращает пользователя с имэйлом, паролем и именем. """
        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
        """ Создает и возввращет пользователя с привилегиями суперадмина. """
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class Profile(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    firstname = models.CharField(max_length=100, null=True, blank=True,
                                 verbose_name='Имя')
    lastname = models.CharField(max_length=100, null=True, blank=True,
                                verbose_name='Фамилия')
    phone = models.CharField(max_length=15, null=True,
                             blank=True, verbose_name='телефон')
    age = models.SmallIntegerField(
        null=True, blank=True, verbose_name='возраст')
    work_exp = models.SmallIntegerField(
        null=True, blank=True, verbose_name='опыт работы')
    knowledge = models.TextField(
        max_length=3000, null=True, blank=True, verbose_name='знания')
    role = models.ForeignKey(
        'Role', null=True, blank=True, on_delete=models.CASCADE)

    is_active = models.BooleanField(default=True)

    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    # Дополнительный поля, необходимые Django
    # при указании кастомной модели пользователя.

    # Свойство USERNAME_FIELD сообщает нам, какое поле мы будем использовать
    # для входа в систему. В данном случае мы хотим использовать почту.
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    # Сообщает Django, что определенный выше класс UserManager
    # должен управлять объектами этого типа.
    objects = UserManager()

    def get_id(self):
        return self.pk

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class FieldOfInterest(models.Model):
    field = models.CharField(max_length=100, null=False,
                             blank=False, verbose_name='сфера интереса')

    def __str__(self):
        return self.field

    class Meta:
        verbose_name = 'Сфера интереса'
        verbose_name_plural = 'Сферы интересов'


class Role(models.Model):
    role = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.role

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'
