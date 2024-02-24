# Blog-App
A blog application created using Django.
Users with different level of authorisations can log in, write posts, update profile information and many  more features.


## **Table of Contents**

### 1. Setup
    - Setup virtual enviroment named myenv and activate
    - Install dependancies - Django
    - Setup Django project give it a name , web_app
    - Start application name blog_app
    - set postgres database   

My guide to [setting up](https://realpython.com/django-setup/).

Always activate the virtual when reopening the appliaction. 

### 2. Routing applications.

Views are used used to return responses, our app folder contains this python file with neccesesary functions. I will write a simple function that will return a simple statement when a user goes to the homepage. 

```python
def home(request):
    return HttpResponse("<h1>Blog Home Page</h1>")
``` 

The above function needs to be mapped to a url path for it to be executed via a call. This is achieved by simply creating a url python file inside the blog application, this is specific to the blog application.

This function is to be routed in the root directory url file by importing include and then adding a path that references url file in the blog_app application. 

```python
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog_app.urls')),
]
```
Run server and add path to blog in the address bar ,  http://127.0.0.1:8000/blog/
![Test Home Page](./images/1.bloghomepage.png)


### 3. Templates.
HTML files are created using templates, they must be located inside a templates folder in our application with a subdirectory with the same name as application. We need two html files, one to direct users to our home page and another to about page. 

Django must be notified of the new app, housing templates, by adding it inside the settings.py file in the installed app list. 

To load the templates created, we need to point blog_app views to use them. I would rather the home view display a html file than a simple html tag. Activate the changes by making the view return and render our static home html file. Run server again to view the changes. 

```python
def home(request):
    return render(request, 'blog_app/home.html', )
```
#### 3.1 Base Templates.
In our two templates, home and about, there are alot of redundant code. Code repeats in multiple locations making it less efficient. Multiple sections such as header, title, and footer can be placed in another base template then inherited by other templates. So the home and about html file will extend this template and add only code that is unique to them. 

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />

    <!-- my css -->
    <link rel="stylesheet" type="text/css" href="{% static 'blog/main.css' %}">
    <!-- Title  -->
    {% if title %}
        <title>BLOG - {{ title }}</title>
    {% else %}
        <title>Title</title>
    {% endif %}
</head>
<body>
    {%block content%} 
    {%endblock content%}
</body>
</html>
```

#### 3.2 Static files.
JavaScript, css and image files used in templates are stores in static folder inside the project directory. Django accesses these files by loading the static folder in the base template. 

#### 3.3 Boostrap.
Boostrap is a power, feature rich toolkit used to build responsive websites using pre built components. This module was access through a CDN link and used to make beautify the header, rooter and content of our templates. 


### 4. Database Management. 
Django works with relational databases such as SQlite(in-built) or Postgres. All database systems supported by Django use the language SQL to create, read, update and delete data in a relational database. SQL is also used to create, change, and delete the database tables themselves. An admin site is used to manage models in the database.  

#### 4.1 Admin page
Admin application is used to manage data through CRUD operations and view registered models in the backend making production efficient. Admin page configurations are automatically created when a user creates a project, all we need now is creating a super user and pass credentials at the command line. User information will be stored in auth_user table stored in the database after applying migrations. 

```bash
py manage.py createsuperuser
```
Admin page.
![Test Home Page](./images/2.adminpage.png)

To view our model in the admin page we need to import and register it in the admin python file inside the app directory.
Registered model.
![Registed model](./images/7.model_in_admin.png)

#### 4.2 Django ORM.
Django's Object Relational Mapper makes life easier by abstracting complex SQL queries. It allows users to easily manipulate data form the database using object oriented programming. 
- We need to only defeine a model class in a python file and apply migartions to effect changes in the database, no data definition query knowledge is needed. 
- Repetition is greatly reduced by migrations because one creates a model but does not write an SQL query again to create a table. 
- Migrations apply changes in the databese dynamically, the need to create a complex data manipulation sql query is avoided. 

#### 4.3 Define a model. 
A model is a single deifitive source of information about data. In order to access user data for each post they make, a model Post is defined, its attributes are stored in fields in models python file. In Python models are classes with tables while attributes map into a column in the database. 

Django has a standard model that is used to manage user accounts in the Authentication package. A user is the author of a post, we therefore need to import User model, a separate table having one to many relationship with Post table associated using a foreign key. 

Sample Post model.
```python
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    # Foreign key
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
```
Make migrations from the shell.

Post model in the database.
![Post model](./images/3.Postmodelindatabase.png)

Users model in database.
![User model](./images/4.user_table_in_database.png)

Foreign key in Post table referencing User table.
![Foreign key](./images/5.Post_model_foreign_key_to_user_model.png)


#### 4.4 Query database model.
ORM provides us with a way to interact with models in the database. Run shell command 

```shell
py manage.py shell
```
Query users by retrieving all objects. 
```shell
>>> from blog_app.models import Post
>>> from django.contrib.auth.models import User
>>> User.objects.all()
<QuerySet [<User: collins>]>
```

Filter data.

```shell
>>> User.objects.first()
<User: collins>
>>> User.objects.filter(username='collins')
<QuerySet [<User: collins>]>
>>> User.objects.filter(username='collins').first()
<User: collins>
```

Store filtered query.

```shell
>>> u1 = User.objects.filter(username='collins').first()
>>> u1
<User: collins>
```

User attributes.
```shell
>>> u1.id
1
>>> u1.pk
1
>>> u1.last_login
datetime.datetime(2024, 2, 23, 7, 31, 57, 175213, tzinfo=datetime.timezone.utc)
```

Get user by attribute.
```shell
>>> user = User.objects.get(id=1)
>>> user
<User: collins>
```

Create posts using different methods.

```shell
>>> post_1 = Post(title='Spatia Data Science',content='This is a new field that keeps growing',author=user)
>>> post_1.save()
>>> Post.objects.all()
<QuerySet [<Post: Spatia Data Science>]>
>>> post_3 = Post(title='Remote sensing and GIS',content='Used in spatial analysis like Land cover mapping', author_id=user.id)
>>> post_3.save()
>>> Post.objects.all()
<QuerySet [<Post: Spatia Data Science>, <Post: Enhance Spatial Engineering>, <Post: Remote sensing and GIS>]>
```

Get attributes of Post model.
```shell
>>> post_3.author
<User: collins>
>>> post_3.content
'Used in spatial analysis like Land cover mapping'
```

Fetch User model(parent table) data from Post model(child) using foreign key, get author email.
```shell
>>> post_3.author.email
'collins@gmail.com'
```

Fetch all the posts written by a user without performing a join analysis, use sets. Add related tablename_set.
```shell
>>> user_1 = User.objects.get(id=1)
>>> user_1
<User: collins>
>>> user_1.post_set
<django.db.models.fields.related_descriptors.create_reverse_many_to_one_manager.<locals>.RelatedManager object at 0x00000238A99065A0>
>>> user_1.post_set.all()
<QuerySet [<Post: Spatia Data Science>, <Post: Enhance Spatial Engineering>, <Post: Remote sensing and GIS>]>
```

Create a post directly using set, then query post table.
```shell
>>> user_1.post_set.create(title='AI in GIS',content='There are many algorithms suck KNN in GIS')
<Post: AI in GIS>
>>> Post.objects.all()
<QuerySet [<Post: Spatia Data Science>, <Post: Enhance Spatial Engineering>, <Post: Remote sensing and GIS>, <Post: AI in GIS>]>
```
Note that we did not specify the author of the post nor save the post like previously done. 

#### 4.5 Add queried data to views.
We can now acces queried information formthe database and display this information in our views. Import the Post class from the same directory file model.py and grab data into a dictionary. 

```python
from django.shortcuts import render
from .models import Post

def home(request):
    # grab data into a dictionary
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'blog_app/home.html', context)
```

Run server and go to home page. 
![Fetched data](./images/6.data_from_view_in_server.png)

### 5. User Registration and Authentication.
We are going to create an application that allows users to login from the front end by creating accounts and signing in with their own credentials. 

A logically separate application needs to be created to manage users. This user application will have its own form, routes and other features that are independent. Since users cannot use the admin page to sign in, we need to design a registration page that contains a form as the first step. A form is used to pass in informations from front end to backend python. It will verify user details such matching password, email vaidation, field validation, and rendering error messages as well as old values. 

Django does much of the heavy lifting i.e validation by simply automating tasks using pre built forms. Depending on user needs, this framework is extremely flexible as programmers can customize these forms when they need to scale up.

#### 5.1 Create User Application. 
In the project directory, we will create a new class to model user application. This app will handle all the functionalities related to users sign up.

```sh
py manage.py startapp users
```

Add application to installed apps variable in setting python file.

```python
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog_app',    # first app
    'users',      # second appp
]
```

#### 5.2 Design form.
A registration form has to be rendered by a function registration defined in `views.py` file in users application. A new user is created by creating an instance of a built in user form. The `UserCreationForm` is a class that will provide us with a html form in which users fill in. 

```python
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# define function that instatiate a form
def registration(request):
    form = UserCreationForm()  # Instance with blank form
    return render(request, 'users/register.html', {'form': form})
```
Create template folder in user folder structure, add a subfolder with the name user and place a new file ,`register.html`

Folder structure.
```
├── web_app
│   ├── users
│   │   ├── templates
│   │   │   ├── users
│   │   │   │   ├── register.html
```

This html file will extend from base html file. 

```html
<div class="content-section">
        <form method="POST">
            {% csrf_token %}
            <fieldset class="form-group">
                <legend class="border-bottom mb-4">Join Today</legend>
                {{ form.as_p }}
            </fieldset>
            <div class="form-group">
                <button class="btn btn-outline-info" type="submit">Sign Up</button>
            </div>
        </form>
        <div class="border-top pt-3">
            <small class="text-muted">
                Already Have An Account? <a class="ml-2" href="#">Sign In</a>
            </small>
        </div>
    </div>
```
Finally, to shoe the form we need to add a url pattern that utlizes our registration view. Import the view directly to the projects folder url file. 

```python
from django.contrib import admin
from django.urls import path, include
from users import views as users_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog_app.urls')),
    path('register/', users_view.registration, name='register'),
]
```

Run server and go to register page , http://127.0.0.1:8000/register/

![Register](./images/8.Register%20page.png)


#### 5.3 Collect data from form.
In our form we did not specify the location to store data collected, thus after user entered details, we were redirected to the same page with an empty form. 

When you send data to a server, POST request are used, otherwise if you expect data a GET method is preffered. Both are HTTTP protocol used for data exchange. POST method is also designed to transfer data with secret information from the server to backend i.e passwords. They are also best suited for submitting data especially ones with multiple fields such as those in forms. 

We need to verify the POST method then validate the data inside message body else(GET request) display a blank form. A valid form contains the correct python data types, converted to json formart. Backend user has to be notified that data was successfully submited and user redirected to the home page. For this reason we need to capture username field and display a success message. 

```python
# import redirect and message functions
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserRegisterForm
from django.contrib import messages


def register(request):
    # validate method 
    if request.method == 'POST':
        # Get data 
        form = UserRegisterForm(request.POST)
        # Validate form
        if form.is_valid():
            form.save()    # save infor

            # Success message
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            
            # Redirect to home page 
            return redirect('blog-home')
        
    # GET method
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
```

The base template needs to be updated to display the flash messages just above the content block. 

```html
<div class="col-md-8">
    # <!-- Success message. -->
    {% if messages %}
        {% for message in messages %}
        <div class="alert alert-{{ message.tags }}">
            {{ message }}
        </div>
        {% endfor %}
    {% endif %}
    {% block content %}{% endblock %}
</div>
```

#### 5.4 Customize the form.
Our currect form does not contain an email field, we need to add this attribute so as to collect it. 






