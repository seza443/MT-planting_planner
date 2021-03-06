[![Maintainability](https://api.codeclimate.com/v1/badges/25cf8913fbec3dfd4d1e/maintainability)](https://codeclimate.com/github/ZelieM/MT-planting_planner/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/25cf8913fbec3dfd4d1e/test_coverage)](https://codeclimate.com/github/ZelieM/MT-planting_planner/test_coverage)
[![Build Status](https://travis-ci.org/ZelieM/MT-planting_planner.svg?branch=master)](https://travis-ci.org/ZelieM/MT-planting_planner)

# Description

Todo small description of the project and the architecture

## Architecture

Todo use [ASCII flow](http://asciiflow.com/) to draw an architecture schema or include the nice draw

# Installation

### Requirements
- Install [python3](https://www.python.org/)
- Install [PostgreSQL](https://www.postgresql.org)
- (pip should be installed along with python3 but if is not the case, install it as well)
- Install required dependencies with `pip install -r requirements.txt`
- Create  Postgre database named `planting_planner_db`
- Create a Postgre database named `vegetable_library_db`
- Create a Postgre user named `postgres` with password `azerty` and grant him full access to both databases

### Migrations
Execute the migrations on the databases with the following commands:
- `python manage.py migrate`
- `python manage.py migrate --database=db_vegetables_library`

### Secrets
Some secret values are used when running the project.
Those values are not versionned in git and you must create them manually on each machine.
There are located in [planting_planner/settings/secrets/secrets.json](planting_planner/settings/secrets/secrets.json).

Follow those steps to create your secrets:

- Create the file [planting_planner/settings/secrets/secrets.json](planting_planner/settings/secrets/secrets.json)
- Copy the content of [planting_planner/settings/secrets/secrets.json.template](planting_planner/settings/secrets/secrets.json.template)
- Change the values with your secrets

# Development

To develop this project locally, install the requirements (see above).

Then start the project locally with

```
python manage.py runserver
```

## Icons
We use [Fontawesome5](https://fontawesome.com) to insert icons in our HTML templates.
This tool provide nice free [searchable icons](https://fontawesome.com/icons?m=free).

To use an icon, simply insert the following tag and replace `fa-user` by the icon you want

```html
<i class="fas fa-fw fa-user"></i>
```

- `fas` is the *solid* type of icon, Fontawesome provides Solid, Regular, Light and Brand
- `fa-fw` forces the icons to have all the same size

# Tests
To run the unit tests with code coverage, execute

```
coverage run --source='.' manage.py test planner --settings=planting_planner.settings.tests
```

# Production
- Clone the repository
- Ensure that python3 is installed
- Install all requirements (with pip3)
- Install Apache and mod_wsgi
- Migrations: `python3 manage.py migrate --settings=planting_planner.settings.production`
- After each migration, restart apache (`service apache2 restart`)

## Apache configuration
Apache config file (`/etc/apache2/sites-available/lauzeplan.conf`)

````
# Path to WSGI file (generated by django)
WSGIScriptAlias / /home/zmulders/MT-planting_planner/planting_planner/wsgi.py
# Home path of the project (make it available to import for django)
WSGIPythonPath /home/zmulders/MT-planting_planner
Alias /static /home/zmulders/MT-planting_planner/planner/static

# Serve static resources
<Directory /home/zmulders/MT-planting_planner/planner/static>
    Require all granted
</Directory>

# Serve Django application
<Directory /home/zmulders/MT-planting_planner/planting_planner>
    <Files wsgi.py>
        Require all granted
    </Files>
</Directory>
````

##Automatic deployment
This project is automatically updated on the server thanks to a CGI script written in Perl.
However, the migrations are not run automatically.


Dump of the vegetable library database, from production server:
 `pg_dump lauzeplan_library -h pgsql.uclouvain.be -p 5440 --username=lauzeplan -f test_dump_db.txt`
