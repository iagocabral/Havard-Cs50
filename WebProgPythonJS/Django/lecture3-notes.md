### HTTP Status Codes
| number | mean |
|-----|--:|
| 200 | Ok| 
| 301 | Moved Permanently|
| 303 | Forbidden|
| 404 | Not Found|
| 500 | Internal Server Error|


### Install Django
> pip3 install Django

### Create Project
> django-admin startproject PROJECT-NAME

### Run Django
> python manage.py runserver

### Create a Django app
> python manage.py startapp APP-NAME

### Pastas do Django
manage.py - able to execute commands 
settings.py - contains important configurations settings
urls.py - table of contents of all urls

## Notes
- Every Django project consists of one or more django applications<br>
- after create django project, create a django app<br>
- views is something the user migth want to see<br>

## Class
- create project

- create an app

- Add Django app in project **settings.py INSTALLED_APPS**

- create an app view:<br>
    ```
    from django.http import HttpResponse
    def index(request):
    return HttpResponse("Hello, World!")
    ```

- create urls.py at the app:<br>
    ```
    from django.urls import path
    from . import views
    urlpatterns = [
        path("", views.index, name="index")
    ]
    ```

- Add in project urls.py:<br>
    ```
    import include
    path('hello/', include("hello.urls))
    ```

- Adicionando uma url que muda de acordo com a entrada **(ex: /iago)**:<br>
    - At hello views.py:<br>

    ```
        def greet(request, name):
            return HttpResponse(f"Hello, {name.capitalize()}!")
    ```

    - At hello urls.py:<br>
        ```
        path("<str:name>", views.greet, name="greet")**,
        ```

- Renderizando um Html nas views, at hello/views.py
    ```
        return render(request, "hello/index.html")
    ```


