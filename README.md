Pasos para iniciar con esta API:

1. Construimos los contenedores con el comando docker-compose up -d --build
2. Revisamos que los contenedores de la db y la web esten arriba con el comando docker ps
3. Revisamos que el API este arriba en la siguiente IP http://0.0.0.0:8000/
4. Entramos al contenedor donde corre Django ---> docker exec -it container_name sh 
5. Generamos el archivo de migraciones con el comando ---> python manage.py makemigrations
6. Corremos las migraciones con el comando ---> python manage.py migrate
7. Adicional si queremos tener acceso al Admin de Django podemos correr el comando ---> python manage.py createsuperuser
8. Para correr los test usamos el siguiente comando ---> python manage.py test
9. Abrimos la colección de POSTMAN y a probar los endpoints  https://www.postman.com/soyangiezuniga/workspace/public-angie-zuniga/collection/9397232-5944f632-b1f3-4d55-bf13-bae7b24ca3f0?action=share&creator=9397232

Models:

- Book
- Author
- Category

Endpoints:

- GET search books 
- DELETE book
- POST create book


 