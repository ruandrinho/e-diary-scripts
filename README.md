# e-diary-scripts

Скрипты для операций с электронным дневником e-diary ([репозиторий проекта на GitHub](https://github.com/devmanorg/e-diary/))

## Как использовать

Скачайте файл `scripts.py` и загрузите в папку django-приложения e-diary на сервере электронного дневника.

Для начала работы зайдите через терминал в папку приложения и выполните команду:
``` 
python manage.py shell
```
Появится приглашение `>>>`, после которого вводятся команды на языке python.

Сначала нужно загрузить скрипты:
```
>>> from scripts import *
```
### Исправление оценок
```
>>> fix_marks('ФИО')
```
Вместо ФИО нужно подставить фамилию, имя и отчество ученика. Можно указать не полностью, например, без отчества. Если программа найдёт несколько учеников с заданным ФИО, оценки исправлены не будут.
### Удаление жалоб
```
>>> remove_chastisements('ФИО')
```
Вместо ФИО нужно подставить данные аналогично первому пункту.
### Добавление похвалы
```
>>> create_commendation('ФИО', 'Предмет')
```
Вместо ФИО нужно подставить данные аналогично первому пункту. Вторым параметром нужно указать название предмета.

## Как улучшить
1. Скачайте и установите e-diary [по инструкции](https://github.com/devmanorg/e-diary/)
2. Создайте свою БД или найдите существующую
3. Клонируйте данный репозиторий в папку приложения
4. После доработки скриптов создайте pull request

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
