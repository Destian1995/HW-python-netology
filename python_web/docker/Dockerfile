FROM nginx:latest

# Удаляем старые файлы приветствия
RUN rm -rf /usr/share/nginx/html/*

# Копируем новые файлы в контейнер
COPY html/ /usr/share/nginx/html/

# Указываем рабочий порт
EXPOSE 80
