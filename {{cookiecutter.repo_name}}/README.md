OMERO.{{cookiecutter.webapp_name}}
=======================

{{cookiecutter.description}}.

Installation
============

Install `{{cookiecutter.webapp_name}}` in development mode as follows:

    # within your python venv:
    $ cd {{cookiecutter.repo_name}}
    $ pip install -e .

Add the app to the `omero.web.apps` setting:

N.B. Here we use single quotes around double quotes:

    $ omero config append omero.web.apps '"{{cookiecutter.webapp_name}}"'

Optionally, add a link "{{cookiecutter.webapp_title}}" at the top of the webclient to
open the index page of this app:

    $ omero config append omero.web.ui.top_links '["{{cookiecutter.webapp_title}}", "{{cookiecutter.webapp_name}}_index", {"title": "Open {{cookiecutter.webapp_title}} in new tab", "target": "_blank"}]'


Now restart your `omero-web` server and go to
<http://localhost:4080/{{cookiecutter.webapp_name}}/> in your browser.


Further Info
============

1.  This app was derived from [cookiecutter-omero-webapp](https://github.com/ome/cookiecutter-omero-webapp).
2.  For further info on depolyment, see [Deployment](https://docs.openmicroscopy.org/latest/omero/developers/Web/Deployment.html)
