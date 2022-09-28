### Application Portal
The portal to check and review job applications created using Django Rest Framework. It allows applicants to create new applications, and reviewers to check the applications and change the status of application.


### Installation and Setup
Install Python and Django, create a new virtual environment for this particular project.

```
pip install -r requirements.txt
```

Now to run the server, simply do migrate and run
```
python manage.py migrate
python manage.py runserver
```

The server will run on `localhost:8000`

### Features and Screenshots
##### Create an application
![image](https://user-images.githubusercontent.com/56730716/192770314-cebcacdf-ab37-4a68-bc54-14ed20079345.png)

#### View user profile
![image](https://user-images.githubusercontent.com/56730716/192770606-01cc5767-005c-496b-92fa-bc89606ccc0b.png)
![image](https://user-images.githubusercontent.com/56730716/192770560-ad9354df-12a7-499b-82f5-e1a093f6de89.png)

#### Update user Profile, update status of application
![image](https://user-images.githubusercontent.com/56730716/192770754-c2183fd7-1983-4146-ad14-0d26fd3d907d.png)

#### Pagination and Filtering
![image](https://user-images.githubusercontent.com/56730716/192770934-757e8182-1187-42fd-a419-4a6ca5ed6578.png)
![image](https://user-images.githubusercontent.com/56730716/192771321-1ed040ca-9aba-46ce-b490-62263da82e29.png)


#### Swagger API documentation
![image](https://user-images.githubusercontent.com/56730716/192771104-4bf9920b-6419-4faf-b42b-382386a6df05.png)


#### My personal steps I followed
```
conda create --name aviate
conda activate aviate
conda install pip
pip install django
django-admin startproject AppPortal
cd AppPortal
python manage.py startapp portal
```

To run the server
```
python manage.py runserver
python manage.py migrate
```

Add portal app in the project and after creating some models.

#### Making changes into Models
Change your models (in models.py).
Run `python manage.py makemigrations` to create migrations for those changes
Run `python manage.py migrate` to apply those changes to the database.

```
python manage.py makemigrations portal
```


#### Created super user
```
python manage.py createsuperuser
```

- priyam
- 1234

