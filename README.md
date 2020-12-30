# microservices-example
Microservices event driven example using Django, Flask, MySql, RabbitMQ

## Architecture
## Event Bus
Rabbit mq is running in a local container and communicates with both admin and main service
</br>
## Admin Service
- Responsible to manage the create products for users
- Communicates with ```admin_db``` database
- Subscribed to a channel for updating likes for a particular product
- Produces messages for creating, updating, deleting a product
</br>
## Main Service
- Responsible to add likes to products and can retrieve the list of the products
- Communicates with ```main_db``` database
- Subscribed to channels for creating, updating, deleting a product
- Produces messages for liking a product

## Run the example
```make rabbit```
</br>
```make admin```
</br>
```make main```

## Useful commands
#### Admin container
```python manage.py makemigrations```
</br>
```python manage.py migrate```
</br>
</br>

#### Admin database
Create some users in the ```admin_db```
```
INSERT INTO products_user (id)
VALUES (1);
```

#### Main container
```python manager.py db init```
</br>
```python manager.py db migrate```
</br>
```python manager.py db upgrade```

## Endpoints
#### Admin Service
GET, POST
</br>
```http://localhost:8000/api/products```
</br>
PUT, DELETE
</br>
```http://localhost:8000/api/products/<str:id>```
</br>
</br>
#### Main Service
GET
</br>
```http://localhost:8001/api/products```
</br>
POST
</br>
```http://localhost:8001/api/products/<str:id>/like```
