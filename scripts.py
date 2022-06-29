from datacenter.models import Mark, Chastisement, Commendation, Lesson
from datacenter.models import Schoolkid
from random import choice
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


def fix_marks(kid_name):
    try:
        kid = Schoolkid.objects.get(full_name__contains=kid_name)
    except MultipleObjectsReturned:
        print('Найдено несколько учеников с таким именем, повторите вызов')
        return
    except ObjectDoesNotExist:
        print('Ученик не найден')
        return
    Mark.objects.filter(schoolkid=kid, points__in=[2, 3]).update(points=5)
    print('Ok')


def remove_chastisements(kid_name):
    try:
        kid = Schoolkid.objects.get(full_name__contains=kid_name)
    except MultipleObjectsReturned:
        print('Найдено несколько учеников с таким именем, повторите вызов')
        return
    except ObjectDoesNotExist:
        print('Ученик не найден')
        return
    Chastisement.objects.filter(schoolkid=kid).delete()
    print('Ok')


def create_commendation(kid_name, lesson_title):
    try:
        kid = Schoolkid.objects.get(full_name__contains=kid_name)
    except MultipleObjectsReturned:
        print('Найдено несколько учеников с таким именем, повторите вызов')
        return
    except ObjectDoesNotExist:
        print('Ученик не найден')
        return

    lesson = Lesson.objects.filter(subject__title=lesson_title).\
        order_by('?').first()
    if not lesson:
        print('Предмет указан неверно')
        return

    commendation_text = choice([
        'Молодец!', 'Отлично!', 'Хорошо!', 'Гораздо лучше, чем я ожидал!',
        'Ты меня приятно удивил!', 'Великолепно!', 'Прекрасно!',
        'Ты меня очень обрадовал!', 'Именно этого я давно ждал от тебя!',
        'Сказано здорово – просто и ясно!', 'Ты, как всегда, точен!',
        'Очень хороший ответ!', 'Талантливо!',
        'Ты сегодня прыгнул выше головы!', 'Я поражен!',
        'Уже существенно лучше!', 'Потрясающе!', 'Замечательно!',
        'Прекрасное начало!', 'Так держать!', 'Ты на верном пути!', 'Здорово!',
        'Это как раз то, что нужно!', 'Я тобой горжусь!',
        'С каждым разом у тебя получается всё лучше!',
        'Мы с тобой не зря поработали!', 'Я вижу, как ты стараешься!',
        'Ты растешь над собой!', 'Ты многое сделал, я это вижу!',
        'Теперь у тебя точно все получится!'
    ])
    Commendation.objects.create(
        text=commendation_text,
        schoolkid=kid,
        created=lesson.date,
        subject=lesson.subject,
        teacher=lesson.teacher
    )
    print('Ok')
