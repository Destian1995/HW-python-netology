# Домашнее задание к лекции «Работа с удаленным репозиторием через GitHub»


### Задача №1: Публикация репозитория

В предыдущем задании вы создали локальный репозиторий. Чтобы продемонстрировать результат коллегам вам нужно опубликовать его на GitHub. 

**Важно:** для выполнения этой и всех остальных задач вам нужно создать профиль на [GitHub.com](https://github.com) и настроить SSH-ключ. Информация есть в лекциях.

1. Найдите на рабочем столе папку NeuroStartUp. Вы создали её в процессе решения квиза к предыдущей лекции. Откройте для неё терминал.
2. На сайте GitHub создайте новый пустой публичный репозиторий. Скопируйте ссылку на него.
3. В терминале свяжите локальный репозиторий с удалённым. Используйте кодовое слово `origin`.
4. Опубликуйте репозиторий на GitHub. Для этого используйте команду `git push -u origin main`
5. Перезагрузите страницу с репозиторием в браузере. Убедитесь, что в репозитории есть файл `README.md`, текст правильно отображается и видна вся история проекта.

**В качестве результата пришлите ссылку на ваш репозиторий на GitHub. Скопируйте ссылку из адресной строки браузера.**

[ССЫЛКА НА 1 задание](https://github.com/Destian1995/python-netology/tree/main)

### Задача №2: Создание веток

Вы решили немного доработать главную страницу вашего проекта. Но новый текст требует согласования, команда не готова сразу его менять. Они попросили показать как это будет выглядеть. Для этого вам нужно создать новую ветку и добавить туда новый текст.

1. Найдите на рабочем столе папку NeuroStartUp. Откройте для неё терминал.
2. Создайте новую ветку с названием `new-text` и переключитесь на неё.
3. Откройте файл `README.md` в текстовом редакторе и вставьте новый текст ниже того, что там уже есть. Нажмите на треугольник ниже, скопируйте текст, вставьте в файл и оформите при помощи Markdown, чтобы он выглядел как в примере:

<details>
    <summary>Текст для вставки в файл README.md</summary>
            
## Список клиентов

 Мы на столько крутые, что уже успели поработать со следующими компаниями:

1. ООО «Рога и копыта»
1. Издательство «Читый лист»
1. Космопорт «Черезтерновый Кзвёздный»
1. Дизайн-студия имени Слишком Известного Персонажа

Нас можно найти в [google.com](https://google.com/).
            
</details>

4. Сделайте коммит с изменениями.
5. Отправьте коммит в репозиторий: `git push -u origin new-text`.
6. Откройте репозиторий на GitHub в браузере, переключитесь на ветку `new-text` и скопируйте ссылку из адресной строки браузера.

**В качестве результата пришлите ссылку на ваш репозиторий на GitHub.**

[ССЫЛКА НА 2 задание](https://github.com/Destian1995/python-netology/tree/new-text)

### Задача №3: Слияние веток

Пока новый текст для главной страницы находится на согласовании вас попросили поработать над другим проектом. Ваш коллега закончил работу над новой фичей и её нужно слить в ветку `main`.

1. Склонируйте репозиторий по [ссылке](https://github.com/netology-code/git-2-homeworks-merge.git) на рабочий стол. Форкать репозиторий перед клонированием не нужно! 
2. Откройте терминал для появившейся после клонирования папки.
3. Прочитайте справку под задачей.
4. Слейте ветку `earlyorder` с веткой `main`.
5. Разрешите появившийся при слиянии конфликт. Оставьте один вариант текста на ваше усмотрение.
6. Создайте новый пустой публичный репозиторий на GitHub.
7. Свяжите ваш локальный репозиторий с только что созданным удалённым репозиторием. При связывании используйте кодовое слово `target`. Команда будет выглядеть так: `git remote add target ссылка-на-пустой-репозиторий`.
8. Отправьте локальные изменения ветки `main` в удалённый новый репозиторий `target`. Полностью команда будет выглядеть так: `git push -u target main`.

**В качестве результата пришлите ссылку на ваш репозиторий на GitHub.**

[ССЫЛКА НА 3 задание](https://github.com/Destian1995/new_repo)
#### Справка

При клонировании в локальный репозиторий клонируется только ветка `main`. Остальные ветки существуют только в удалённом репозитории. Просмотреть все ветки можно командой `git branch -a`. Красным подсвечены удалённые ветки, в начале их имени стоит `remotes/` (в командах оно не нужно), означающий, что ветка находится в удалённом репо, а далее - `origin/`, указывая на то, в каком репозитории они находятся.

Для слияния не нужно клонировать удалённые ветки в локальный репозиторий. Можно выполнить команду `git merge` указав полное имя удалённой ветки (`origin/earlyorder`).

