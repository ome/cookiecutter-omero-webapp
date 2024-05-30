
[![Actions Status]({{ cookiecutter.github_repository_url }}/workflows/OMERO/badge.svg)]({{ cookiecutter.github_repository_url }}/actions)


OMERO.{{cookiecutter.webapp_name}}
==================================

{{cookiecutter.description}}.

Installation
============

This section assumes that an OMERO.web is already installed. See [OMERO.web installation instructions]<https://github.com/ome/omero-web/blob/master/README.rst> for more details.

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

    # within your python venv:
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

