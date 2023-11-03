# task_for_PLT
Тестовое задание для компании "Надежные Лояльные Технологии"

### Стек:
![Python](https://img.shields.io/badge/Python-171515?style=flat-square&logo=Python)![3.11](https://img.shields.io/badge/3.11-blue?style=flat-square&logo=3.11)
![Aiogram](https://img.shields.io/badge/Aiogram-171515?style=flat-square&logo=Aiogram)![3.1.1](https://img.shields.io/badge/3.1.1-blue?style=flat-square&logo=3.1.1)
![MongoDB](https://img.shields.io/badge/PostgreSQL-171515?style=flat-square&logo=MongoDB)
![Pydantic](https://img.shields.io/badge/Pydantic-171515?style=flat-square&logo=Pydantic)

![Docker-compose](https://img.shields.io/badge/Docker--compose-171515?style=flat-square&logo=Docker)
![GitHub](https://img.shields.io/badge/GitHub-171515?style=flat-square&logo=GitHub)


### Запуск проекта
Клонируем репозиторий и переходим в него:
```bash
git clone https://github.com/PivnoyFei/task_for_PLT.git
cd task_for_PLT
```

#### Создаем и активируем виртуальное окружение:
```bash
python3 -m venv venv
source venv/bin/activate
```

#### Обновиляем pip и ставим зависимости из req.txt:
```bash
python -m pip install --upgrade pip && pip install -r requirements.txt
```


### Перед запуском сервера, в папке infra-rlt необходимо создать `.env` на основе `.env.template` файл со своими данными.
#### Переходим в папку с файлом docker-compose.yaml:
```bash
cd infra-rlt
```

### Запуск базы данных
```bash
docker-compose up -d --build
```

#### Останавливаем контейнеры:
```bash
docker-compose down -v
```

#### Запускаем проект оз основной папки:
```bash
cd ..
python3 application/main.py
```

#### Автор
[Смелов Илья](https://github.com/PivnoyFei)

