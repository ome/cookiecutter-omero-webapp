OMERO.{{cookiecutter.webapp_name}}
=======================

This repository contains a
[cookiecutter](https://cookiecutter.readthedocs.io/) generated example
of a minimal OMERO.web app, derived from [cookiecutter-omero-webapp](https://github.com/ome/cookiecutter-omero-webapp).

This repository contains a minimal OMERO.web app (no JavaScript dependencies or build steps).


We will run the simplest example app below. This is called
`{{cookiecutter.repo_name}}`.


Installation
============

You can install and run the `omero-web` server in a Python virtual
environment or via Docker.


Run your app with locally-installed OMERO.web
---------------------------------------------

If you have installed OMERO.web locally in a virtual environment as
[recommended
here](https://docs.openmicroscopy.org/latest/omero/developers/Web/Deployment.html),
you can `pip install` this app as follows:

    # within your python venv:
    $ cd {{cookiecutter.repo_name}}
    $ pip install -e .

You also need to add your app to the `omero.web.apps`{.interpreted-text
role="property"} setting:

N.B. Here we use single quotes around double quotes.

    $ omero config append omero.web.apps '"{{cookiecutter.webapp_name}}"'

Now restart your `omero-web` server and go to
<http://localhost:4080/{{cookiecutter.webapp_name}}/> in your browser.

Run your app with OMERO.web in a Docker container
-------------------------------------------------

The following walk-through uses
[omero-web-docker](https://github.com/ome/omero-web-docker/) to run the
app. Here we add `{{cookiecutter.webapp_name}}` to the installed apps and map the app
directory to the `site-packages` directory in the Docker instance so
that python can import the `{{cookiecutter.webapp_name}}` module.

    # You need to be in the project directory for this to work.
    # cd {{cookiecutter.repo_name}}/

    # The OMERO server we want to connect to.
    $ host=demo.openmicroscopy.org

    # Path to the Python module for the app.
    $ appdir=$(pwd)/{{cookiecutter.webapp_name}}

    # Location within Docker instance we want to link the app, so it can be imported.
    $ docker_appdir=/opt/omero/web/venv3/lib/python3.6/site-packages/{{cookiecutter.webapp_name}}

    # This example config file installs "{{cookiecutter.webapp_name}}". See the file for more details.
    $ config=$(pwd)/config.omero

    # Location within Docker instance we want to mount the config.
    $ docker_config=/opt/omero/web/config/config.omero

    # Run Docker container.
    $ docker run -it --rm -e OMEROHOST=$host -p 4080:4080 -v $appdir:$docker_appdir -v $config:$docker_config openmicroscopy/omero-web-standalone:5.6.0-m4

This will run Docker in the foreground, showing the output in your
terminal and allowing you to kill the container with Ctrl-C. You should
see the following lines in the output, indicating that OMERO.web is
starting and the static files from your app are being included.

    ...
    Copying '/opt/omero/web/venv3/lib/python3.6/site-packages/{{cookiecutter.webapp_name}}/static/{{cookiecutter.webapp_name}}/app.css'
    Copying '/opt/omero/web/venv3/lib/python3.6/site-packages/{{cookiecutter.webapp_name}}/static/{{cookiecutter.webapp_name}}/app.js'
    ...
    Starting OMERO.web...

Now go to <http://localhost:4080/{{cookiecutter.webapp_name}}/> in your browser.

Further Info
============

For more documentation on deployment see:

1.  [Deployment](https://docs.openmicroscopy.org/latest/omero/developers/Web/Deployment.html)
