
[![Actions Status]({{ cookiecutter.github_repository_url }}/workflows/OMERO/badge.svg)]({{ cookiecutter.github_repository_url }}/actions)


OMERO.{{cookiecutter.webapp_name}}
==================================

{{cookiecutter.description}}.

Installation
============

Before installing the web app, you will need to install OMERO.web.
We recommend installing ``omero-web`` in a Python virtual environment.
You can create one using for example ``venv``, ``conda`` or ``mamba``.

Before installing ``omero-web``, we recommend to install the [ZeroC IcePy 3.6](https://zeroc.com/downloads/ice/3.6) Python bindings.
Our commercial partner [Glencoe Software](<https://www.glencoesoftware.com/blog/2023/12/08/ice-binaries-for-omero.html>) has produced several Python wheels to install the Ice-Python bindings depending on the desired Python version and the operating system. Please visit [OMERO Python language bindings](https://omero.readthedocs.io/en/stable/developers/Python.html) for a list of supported platforms and Python versions.


When the wheel is installed, activate the virtual environment and install ``omero-web`` from [PyPI](<https://pypi.org/>).

::

    $ pip install -U omero-web


Installing from Pypi
--------------------

Install the app using [pip](<https://pip.pypa.io/en/stable/>) .

Ensure that you are running ``pip`` from the Python environment
where ``omero-web`` is installed. Depending on your install, you may need to
call ``pip`` with, for example: ``/path/to_web_venv/venv/bin/pip install ...``

::

    $ pip install -U {{cookiecutter.repo_name}}


Development mode
----------------

Install `{{cookiecutter.repo_name}}` in development mode as follows:

    # within your Python virtual environment:
    $ cd {{cookiecutter.repo_name}}
    $ pip install -e .

After installation either from [Pypi](https://pypi.org/) or in development mode, you need to configure the application.
To add the application to the `omero.web.apps` settings, run the following command:

Note the usage of single quotes around double quotes:

    $ omero config append omero.web.apps '"{{cookiecutter.webapp_name}}"'

Optionally, add a link "{{cookiecutter.webapp_title}}" at the top of the webclient to
open the index page of this app:

    $ omero config append omero.web.ui.top_links '["{{cookiecutter.webapp_title}}", "{{cookiecutter.webapp_name}}_index", {"title": "Open {{cookiecutter.webapp_title}} in new tab", "target": "_blank"}]'


Now restart your `omero-web` server and go to
<http://localhost:4080/{{cookiecutter.webapp_name}}/> in your browser.


Further Info
============

1. This app was derived from [cookiecutter-omero-webapp](https://github.com/ome/cookiecutter-omero-webapp).
2. For further info on deployment, see [Deployment](https://docs.openmicroscopy.org/latest/omero/developers/Web/Deployment.html)


License
=======

This project, similar to many Open Microscopy Environment (OME) projects, is
licensed under the terms of the AGPL v3.


Copyright
=========

{% now 'utc', '%Y' %} {{ cookiecutter.copyright_holder }}

