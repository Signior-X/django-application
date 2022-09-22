### Application Portal



### How I setup


#### My personal steps I followed
```
conda create --name aviate
conda activate aviate
conda install pip
pip install django
django-admin startproject aviate
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

