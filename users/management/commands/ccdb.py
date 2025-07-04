from django.core.management.base import BaseCommand
import pyodbc
from config.settings import USER, PASSWORD, HOST, DRIVER, PAD_DATABASE, DATABASE


class Command(BaseCommand):
    """
    Django-команда для создания базы данных через ODBC-соединение.

    Использует параметры подключения из настроек для создания новой БД.
    Обрабатывает возможные ошибки подключения и выполнения SQL-запроса.
    """

    def handle(self, *args, **options):
        """
        Основной метод выполнения команды.

        Шаги выполнения:
            1. Формирует строку подключения к серверу СУБД
            2. Устанавливает соединение с автокоммитом
            3. Пытается выполнить CREATE DATABASE
            4. Обрабатывает возможные ошибки на каждом этапе

        Выводит сообщения о результате выполнения операции.
        """
        ConnectionString = f'''DRIVER={DRIVER};
                                SERVER={HOST};
                                DATABASE={PAD_DATABASE};
                                UID={USER};
                                PWD={PASSWORD};'''

        try:
            conn = pyodbc.connect(ConnectionString)
        except pyodbc.ProgrammingError as ex:
            print(ex)
        else:
            conn.autocommit = True
            try:
                conn.execute(fr"CREATE DATABASE {DATABASE};")
            except pyodbc.ProgrammingError as ex:
                print(ex)
            else:
                print(f'База данных {DATABASE} успешно создана')
