# Blog-App
A blog application created using Django.
Users with different level of authorisations can log in, write posts, update profile information and many  more features.


## **Table of Contents**

### 1. Setup
    - Setup virtual enviroment named myenv and activate
    - Install dependancies - Django
    - Setup Django project give it a name , web_app
    - Start application name blog_app   

    My guide to [setting up](https://realpython.com/django-setup/).

### 2. Routing applications.

Views are used used to return responses, our app folder contains this python file with neccesesary functions. I will write a simple function that will return a simple statement when a user goes to the homepage. 

```python
def home(request):
    return HttpResponse("<h1>Blog Home Page</h1>")
``` 

The above function needs to be mapped to a url path for it to be executed via a call. This is achieved by simply creating a url python file inside the blog application, this is specific to the blog application.

The above must also be routed in the root directory url file, import include and add a path that references url file in the blog_app application. 

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





### 4. User Authentication and Authorisation. 
