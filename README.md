# ffa-cdr-admin

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
