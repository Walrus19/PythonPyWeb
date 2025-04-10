from django.shortcuts import render
from django.views import View
from .models import Author, AuthorProfile, Entry, Tag
from django.db.models import Q, Max, Min, Avg, Count, F


class TrainView(View):
    def get(self, request):
        # Создайте здесь запросы к БД
        max_self_esteem = Author.objects.aggregate(max_self_esteem=Max('self_esteem'))
        self.answer1 = Author.objects.filter(self_esteem=max_self_esteem['max_self_esteem'])

        #self.answer1 = None  # TODO Какие авторы имеют самую высокую уровень самооценки(self_esteem)?
        #self.answer2 = None  # TODO Какой автор имеет наибольшее количество опубликованных статей?
        max_author_id = Entry.objects.aggregate(max_author_id=Count('author_id'))

        self.answer2 = Author.objects.annotate(max_author_id=Count('entries')).order_by('-max_author_id').first()
        #self.answer3 = None  # TODO Какие статьи содержат тег 'Кино' или 'Музыка' ?
        self.answer3 = Entry.objects.filter(Q(tags__name='Кино') | Q(tags__name='Музыка')).distinct()
        self.answer4 = None  # TODO Сколько авторов женского пола зарегистрировано в системе?
        self.answer4 = Author.objects.filter(gender='ж').count()

        self.answer5 = None  # TODO Какой процент авторов согласился с правилами при регистрации?
        self.answer5 = round(Author.objects.filter(status_rule=1).count() * 100 / Author.objects.count(), 2)
        self.answer6 = None  # TODO Какие авторы имеют стаж от 1 до 5 лет?
        self.answer6 = Author.objects.filter(authorprofile__stage__range=(1, 5))
        self.answer7 = None  # TODO Какой автор имеет наибольший возраст?
        max_age = Author.objects.aggregate(max_age=Max('age'))
        self.answer7 = Author.objects.filter(age=max_age['max_age'])[0]
        self.answer8 = None  # TODO Сколько авторов указали свой номер телефона?
        self.answer8 = Author.objects.filter(phone_number__isnull = False).count()
        self.answer9 = None  # TODO Какие авторы имеют возраст младше 25 лет?
        self.answer9 = Author.objects.filter(age__lt=25).values()
        self.answer10 = None  # TODO Сколько статей написано каждым автором?
        #self.answer10 = Entry.objects.values('author__username').annotate(count=Count('id'), username=F('author__username'))
        self.answer10 = Author.objects.annotate(count=Count('entries'))
        context = {f'answer{index}': self.__dict__[f'answer{index}'] for index in range(1, 11)}

        return render(request, 'train_db/training_db.html', context=context)

