Game-Club:
Компьютерый клуб точнее это инструмент администратора 

Администратор включает компьютер на оплаченное время. \

Список компьютеров, зелеными отмечаны свободные компьютеры,
занятые же компьютеры отмечены красным \

Страница general на этой странице находятся все компьютеры общего зала \
Страница  vip на этой странице находятся все компьютеры vip зала 


Клонирование: \
git remote add origin git@github.com:NurzhigitAtashbaev/Game-Club.git

Запуск: \
Ubuntu: python3 -m venv venv \
source venv/bin/activate 

python manage.py makemigrations \
python manage.py migrate \
python manage.py runserver
