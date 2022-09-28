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

