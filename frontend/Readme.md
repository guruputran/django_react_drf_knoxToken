# About this project

Builds a Rest API with Django, using know Token authorization. This project has a specialty: We used custom user and override Django user. We set user types and default user Types. We used the drf special url, in the project level url to get the server serve for login and logout (readymade one), a cool feature of drf:
```bash
Raj Kumar: Penang Teams: gpsmartcodes@gmail.com
```
```bash
path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
```
## Uses DRF, knox, swagger, object level permissions

## Installation

Use pipenv first

```bash
pipenv shell
```
```bash
pipenv install etc etc
```
```bash
python manage.py runserver
```
```bash
exit
```
## To see clearly defined api routes go to these:
```bash
http://localhost:8000/swagger and http://localhost:8000/redoc
```
## Refer to requirements.txt to install all packages using pipenv

```python
pipenv lock -r > requirements.txt

# To install the requirements.txt
pipenv install -r path/to/requirements. txt

# make migrations
python manage.py makemigrations / python manage.py makemigrations appname

# migrate to database
python manage.py migrate

# make a superuser
winpty python manage.py createsuperuser
```
```python
The challenges that were faced and overcome, I will list here:
1) The knox expects us to send a header like:
Authorization: Token 6464ec7522913ce52d10fee9512f82a104ed0836fa5ee17c9f3113cd45c95958
with body as No body. Got fuzzy here a bit as documentation not clearly
tells about it. It is embedded somewhere.

2) There is logout and logoutall. The main difference here is that, the auth Tokens
for the user in question is deleted one if logout is used. If logoutall is used, all
the auth Tokens will get deleted simultaneously (which is a cool feature).
But again, we must send a header with format as (1) above for logout and logoutall.

3) For simple websites or applications, knox is a lightweight Token autorization in
comparison with JWT.

4) Documentation of knox says that expiry of Token is 10 hrs by default.

5) In this project, during registration and login, new auth tokens will be generated and 
thrown back as response for front end to pick up and update.
```
```python
There are basically two apps called 'users' and 'posts' here. The project is named 'core'
which is a cool name.
In both users and posts, have implemented RestAPI for getting posts list as an example
The api routes will be : http://localhost:8000/api/v1/ (posts app)
and http://localhost:8000/mypost (users app). Both these routes will throw back same
json data. Both the views have isAuthenticated gates. To understand better can play around it.
```
## Contributing
Pull requests are welcome.



## License
[MIT](https://choosealicense.com/licenses/mit/)