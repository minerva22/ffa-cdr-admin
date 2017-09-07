# ffa-cdr-admin
Django application to support ffa cdr monthly report (ffa-mfe/r-ffa/...)

# Installation

```
sudo apt-get install freetds-dev
pew new ffacdradmin
# for more info about pymssql check ffapb/ffa-blotter requirement.txt
pip install django progressbar33 git+https://github.com/pymssql/pymssql.git
```

# Import marketflow

- copy importMarketflow.sh.dist to importMarketflow.sh and set env vars for database connection
- copy manage.sh.dist to manage.sh and set debug variable
- `./importMarketflow.sh --debug`

# Create project
 - Run the following command in command line
  django-admin startproject ffa-cdr-admin

 - To create your app, make sure you’re in the same directory as manage.py and type this command:
   
  $ python manage.py startapp cdradmin
 
 - Create your firts view under your app (cdradmin/views.py)
 
 - Include the following code under cdradmin/urls.py
   
   urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    ] 
 - Under ffacdradmin/settings.py insert the following in order to point the root:
 
   urlpatterns = [
    url(r'^cdradmin/', include('cdradmin.urls')),
    url(r'^admin/', admin.site.urls),
   ]

 - Create the necessary models under cdradmin/models.py

 - Under ffacdradmin/settings in INSTALLED_APPS put:
   'cdradmin.apps.CdradminConfig',
 
 - Run the following commands in order to migrate the necessary changes did in the models:
  
  $ python manage.py makemigrations cdradmin
  $ python manage.py sqlmigrate cdradmin
   
 - Run migrate to create those model tables in your database:
 
   $ python manage.py migrate

 - Create an admin user
  
    $ python manage.py createsuperuser

 - Add the necessary views and index page

 - To get data from other system: 
     . Modify manage.py to be 
        os.environ['DJANGO_SETTINGS_MODULE'] = 'ffacdradmin.settings'

    . Create folders: management/command/ under the app folder
    . Create files : import_marketflow.py under folder command
# sample code in R to fetch this json data

```
url = "http://.../?asjson=true"
library(RCurl)
x = RCurl::getURL(url)
library(jsonlite)
y = jsonlite::fromJSON(x)
```
# LICENSE
MIT
