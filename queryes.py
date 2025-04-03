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
    entry = Entry.objects.all()
    print("Число запросов = ", len(connection.queries), " Запросы = ", connection.queries)
    """
    Число запросов =  0  Запросы =  [], ввиду ленивости QuerySet
    """
    for row in entry:
        tags = [tag.name for tag in row.tags.all()]
        print("Число запросов = ", len(connection.queries), " Запросы = ", connection.queries)
        print('Результат запроса = ', tags)
    """
    Число запросов =  26 Запросы = [...]
    """
