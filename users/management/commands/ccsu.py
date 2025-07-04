from django.core.management.base import BaseCommand

from users.models import User


class Command(BaseCommand):
    """
    Кастомная команда для создания суперпользователя.
    Создает администратора с предустановленными данными.
    """

    def handle(self, *args, **options):
        """
        Основной метод, выполняющий создание суперпользователя.

         Создает пользователя с правами:
            - is_staff (доступ в админку)
            - is_superuser (все права)
            - is_active (активный аккаунт)

         Пароль устанавливается отдельно через set_password для правильного хеширования.
         """
        admin = User.objects.create(
            email='admin@web.top',
            first_name='Admin',
            last_name='Adminov',
            is_staff=True,
            is_superuser=True,
            is_active=True
        )

        admin.set_password('qwerty')
        admin.save()
        print('Admin Created')
