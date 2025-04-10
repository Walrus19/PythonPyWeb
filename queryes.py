import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

if __name__ == "__main__":
    from apps.db_train_alternative.models import Blog, Author, AuthorProfile, Entry, Tag

    # TODO Сделайте здесь запросы

    from django.db import connection

    # Составляем SQL-запрос
    sql = """
    SELECT id, headline
    FROM db_train_alternative_entry
    WHERE headline LIKE '%%тайны%%' OR body_text LIKE '%%город%%'
    """

    # Выполняем запрос
    with connection.cursor() as cursor:
        cursor.execute(sql)
        results = cursor.fetchall()

    # Выводим результаты
    for result in results:
        print(result)
    """
    (1, 'Изучение красот Мачу-Пикчу')
    (3, 'Знакомство с Парижем')
    (4, 'Открывая тайны Колизея')
    """