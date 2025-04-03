import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

if __name__ == "__main__":
    from apps.db_train_alternative.models import Blog, Author, AuthorProfile, Entry, Tag

    # TODO Сделайте здесь запросы

    from django.db import connection

    print("Число запросов = ", len(connection.queries), " Запросы = ", connection.queries)
    """
    Число запросов =  0  Запросы =  []
    """
    entry = Entry.objects.get(id=5)
    print("Число запросов = ", len(connection.queries), " Запросы = ", connection.queries)
    """
    Число запросов =  1  Запросы =  [...]
    """
    blog = entry.blog
    print("Число запросов = ", len(connection.queries), " Запросы = ", connection.queries)
    """
    Число запросов =  2  Запросы =  [...,...]
    """
    print('Результат запроса = ', blog)
    """
    Результат запроса =  Путешествия по миру
    """