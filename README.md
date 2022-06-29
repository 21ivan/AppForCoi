# AppForCoi

Django REST Api

Technologies used:

Django Rest Framework

Postgresql

venv

Python 3.8

If you wish to run your own build, first ensure you have python globally installed in your computer. 

After doing this, confirm that you have installed virtualenv globally as well. If not, run this:

    $ pip install virtualenv
Then, Git clone this repo to your PC

    $ git clone https://https://github.com/21ivan/AppForCoi.git

Dependencies

Cd into your the cloned repo as such:
    
$ cd AppForCoi

Create and fire up your virtual environment:

    $ virtualenv  venv -p python3
    $ source venv/bin/activate

Install the dependencies needed to run the app:
   
    $ pip install -r requirements.txt

Make those migrations work
    
    $ python manage.py makemigrations
    $ python manage.py migrate

Run It

Fire up the server using this one simple command:

    $ python manage.py runserver

You can now access the file api service on your browser by using

    http://localhost:8000/

List of Api-endpoints:

1. "api/directions" - return directions list
2. "api/doctors" - return doctors list
3. "api/doctors/<str:id>" - return doctor detail by 'id'

