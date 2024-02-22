# Blog-App
A blog application created using Django.
Users with different level of authorisations can log in, write posts, update profile information and many  more features.


## **Table of Contents**

1. Setup
    - Setup virtual enviroment named myenv and activate
    - Install dependancies - Django
    - Setup Django project give it a name , web_app
    - Start application name blog_app   

    My guide to [setting up](https://realpython.com/django-setup/).

2. Routing applications.

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
Run server and add path to blog http://127.0.0.1:8000/blog/
![Test Home Page](./images/1.bloghomepage.png)

![Test Home Page](<img src="./images/1.bloghomepage.png" alt="blog app home page" width="500" height="400">)

