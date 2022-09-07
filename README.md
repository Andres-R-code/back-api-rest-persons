## REST API administration registration system persons

### `Deployment`

## Purpose
The purpose of this repository is to demonstrate some of my technical skills in building a REST API using Django with Django Rest Framework.

## Explanation of the challenge solution. 
The solution to create this Rest api was to design a database, with an entity representing the persons.  

After having the database working we proceeded to create the serializers and build the endpoints according to the business logic of the challenge. 


## Installation

Requires [Django] v2.2.24+ to run.

Install the dependencies and devDependencies and start the server.

### Development
```sh
cd dministration_registration_system
python -m venv venv
.\venv\Scripts\Activate.bat
pip install -r requirements.txt
Create a database named Persons CREATE DATABASE administration;
Place credentials in database view
python manage.py migrate
python manage.py createsuperuser
python manage.py migrate
python manage.py runserver
Go to the REST api documentation: http://127.0.0.1:8000/swagger/
```

## Plugins

| Plugin | README |
| ------ | ------ |
| Django Rest Framework | [plugins/jsonwebtoken/README.md][PlJw] |
| Json Web Token | [plugins/jsonwebtoken/README.md][PlJw] |



## Docker

By default, the Docker will expose port 8000, so change this within the
Dockerfile if necessary. When ready, simply use the Dockerfile to
build the image.

```sh
cd api-node
docker build -t <youruser>/api-node .
```

This will create the class center image and pull in the necessary dependencies.


Once done, you need to create a file called **env.list**

```sh
touch env.list
```

write your env vars into the file **env.list**, you might copy them from .env.example 

Finally run the Docker image and map the port to whatever you wish on
your host. In this example, we simply map port 8000 of the host to
port 8000 of the Docker (or whatever port was exposed in the Dockerfile):

**Note:** You must run the following command where the env.list file is located

```sh
docker run -d -p 8000:8000 --env-file ./env.list --name=classcenter <youruser>/api-node
```

Verify the deployment by navigating to your server address in
your preferred browser.
