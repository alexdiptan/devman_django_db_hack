from random import choice

from datacenter.models import Schoolkid, Mark, Chastisement, Lesson, Commendation, Subject

COMMENDATION = ['Молодец!', 'Отлично!', 'Хорошо!', 'Гораздо лучше, чем я ожидал!', 'Ты меня приятно удивил!',
                'Великолепно!', 'Прекрасно!', 'Ты меня очень обрадовал!', 'Именно этого я давно ждал от тебя!',
                'Сказано здорово – просто и ясно!', 'Ты, как всегда, точен!', 'Очень хороший ответ!',
                'Талантливо!', 'Ты сегодня прыгнул выше головы!', 'Я поражен!', 'Уже существенно лучше!',
                'Потрясающе!', 'Замечательно!', 'Прекрасное начало!', 'Так держать!', 'Ты на верном пути!',
                'Здорово!', 'Это как раз то, что нужно!', 'Я тобой горжусь!',
                'С каждым разом у тебя получается всё лучше!', 'Мы с тобой не зря поработали!',
                'Я вижу, как ты стараешься!', 'Ты растешь над собой!', 'Ты многое сделал, я это вижу! ',
                'Теперь у тебя точно все получится!']


def get_schoolkid(schoolkid_full_name):
    try:
        child = Schoolkid.objects.get(full_name__contains=schoolkid_full_name)
        return child
    except Schoolkid.DoesNotExist:
        print('There is no such schoolkid.')
    except Schoolkid.MultipleObjectsReturned:
        print('Expect one but returned more than one Schoolkid.')


def fix_marks(schoolkid):
    Mark.objects.filter(schoolkid=get_schoolkid(schoolkid)).filter(points__lt=4).update(points=4)


def remove_chastisement(schoolkid):
    child_chastisements = Chastisement.objects.filter(schoolkid=get_schoolkid(schoolkid))
    child_chastisements.delete()


def create_commendation(schoolkid_full_name, subject_name):
    child = get_schoolkid(schoolkid_full_name)
    child_lessons = Lesson.objects.filter(group_letter=child.group_letter, year_of_study=child.year_of_study)
    if child_lessons is None:
        print('Got None, exit.')
        return
    subject = Subject.objects.filter(title=subject_name).get(year_of_study=child.year_of_study)
    if subject is None:
        print('Got None, exit.')
        return
    last_lesson = child_lessons.filter(subject__title=subject_name).order_by('-date').first()
    if last_lesson is None:
        print('Got None, exit.')
        return
    lesson_teacher = last_lesson.teacher
    Commendation.objects.create(text=choice(COMMENDATION), created=last_lesson.date, schoolkid=child, subject=subject,
                                teacher=lesson_teacher)
