# Функции для "взлома" электронного дневника
Функции решают задачу исправления оценок, удаление замечаний и добавления
похвалы. Функции предназначены для запуска в shell-оболочке django.
## Описание функций
### fix_marks
Принимает на вход экземпляр модели Schoolkid. Исправляет все оценки которые
меньше или равны 3.
#### Пример запуска в shell
```python
>>> child = Schoolkid.objects.get(full_name__contains='Фролов Иван')
>>> print(child)
Фролов Иван Григорьевич 6А
>>> def fix_marks(schoolkid):
...     child_marks = Mark.objects.filter(schoolkid=schoolkid)
...     for child_mark in child_marks.filter(points__lt=4):
...         child_mark.points = 4
...         child_mark.save()
... 
>>> fix_marks(child)
>>>
```
### remove_chastisement
Принимает на вход экземпляр модели Schoolkid. Удаляет все замечания по ученику.
#### Пример запуска в shell
```python
>>> child = Schoolkid.objects.get(full_name__contains='Фролов Иван')
>>> print(child)
Фролов Иван Григорьевич 6А
def remove_chastisement(schoolkid):
    child_chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    child_chastisements.delete()
>>> remove_chastisement(child)
>>>
```
### create_commendation
Принимает на вход полное имя ученика и название предмета, по которому будет проставляться
похвала. Фразы для похвалы хранятся в списке commendations. Каждый раз выбирается случайная фраза.
Похвала вставляется для последнего проведенного урока по предмету.
#### Пример запуска в shell
```python
>>> create_commendation('Фролов Иван Григорьевич', 'Музыка')
```