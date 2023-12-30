# # Використовуйте базовий образ Python
# FROM python

# # Встановіть робочий каталог в контейнері
# WORKDIR /app

# # Копіюйте файл requirements.txt
# COPY requirements.txt /app/

# # Встановіть залежності
# RUN pip install --no-cache-dir -r requirements.txt

# # Скопіюйте файли в контейнер
# COPY . /app

# # Встановіть Gunicorn
# RUN pip install gunicorn

# # Відкрийте порт, який буде використовуватися Django
# EXPOSE 8000

# # Запустіть сервер Gunicorn для Django
# CMD ["gunicorn", "-b", "0.0.0.0:8000", "myproject.wsgi:application"]


# Використовуйте базовий образ Python
# FROM python

# # Встановіть робочий каталог в контейнері
# WORKDIR /app

# # Копіюйте файл requirements.txt
# COPY requirements.txt /app/

# # Встановіть залежності
# RUN pip install --no-cache-dir -r requirements.txt

# # Скопіюйте файли в контейнер
# COPY . /app

# # Відкрийте порт, який буде використовуватися Django
# EXPOSE 8000

# # Запустіть сервер для Django
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


# Використовуйте офіційний образ Python з підтримкою Django
FROM python:3.9

# Встановіть робочий каталог в контейнері
WORKDIR /app

# Копіюйте файли в контейнер
COPY . /app

# Встановіть залежності
RUN pip install --no-cache-dir -r /app/requirements.txt

# Відкрийте порт, який буде використовуватися Django
EXPOSE 8000

# Запустіть сервер для Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


