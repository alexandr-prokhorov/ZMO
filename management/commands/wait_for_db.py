from django.core.management.base import BaseCommand
import time
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    """
    Кастомная команда для проверки доступности базы данных.

    Команда периодически проверяет подключение к БД до тех пор,
    пока соединение не станет доступным.
    Полезно для использования в Docker-окружении при запуске контейнеров,
    когда сервису БД нужно время для инициализации.
    """
    def handle(self, *args, **options):
        """
        Основной метод выполнения команды.

        Логика работы:
        1. Выводит сообщение о начале ожидания БД
        2. В цикле пытается установить соединение с БД
        3. При неудаче - выводит сообщение и ждет 1 секунду
        4. При успешном подключении - выводит сообщение об успехе

        Использует:
        - connections['default'] - стандартное подключение к БД Django
        - OperationalError - исключение при проблемах с подключением
        """
        self.stdout.write('Waiting for database...')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
                db_conn.cursor()
            except OperationalError:
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
