Cookiecutter to create OMERO.web apps
=====================================

[![Actions Status](https://github.com/ome/cookiecutter-omero-webapp/workflows/Build/badge.svg)](https://github.com/ome/cookiecutter-omero-webapp/actions)


[Cookiecutter](https://cookiecutter.readthedocs.io) allows creation of a project from a predefined template,
taking care of all the boilerplate code and filling in the relevant information from user's input.

This repository offers a template to start an OMERO.web app using a project skeleton.

Usage
=====
Install cookiecutter and use it with this repository's URL:

```sh
pip install cookiecutter
cookiecutter https://github.com/ome/cookiecutter-omero-webapp.git
```

You will be asked to fill in various values.
Here are some helpful tips for some of them:

  - **webapp_name**: This is the python package name for your app (no spaces or dashes), e.g. `omero_foo`.
  - **repo_name** The repository name, e.g. on `GitHub`. e.g. `omero-foo`. Use the same name as the app name replacing underscores by dashes
  - **webapp_title** A title for the app home page and for the link from webclient.
  - **description**: A description of your app, added to the README and used in `setup.py`.
  - **copyright_holder**: The holder of the copyright. This value will be added to the files' header.


Then you can install the app for development in your local `omero-web` environment.
Use the values you just entered in place of `repo_name` and `webapp_name` as follows:

```sh
$ cd repo_name
$ pip install -e .

$ omero config append omero.web.apps '"webapp_name"'
```

Then you can restart your `omero-web` server and see your app at `<your-server>/webapp_name/`.

For more details, please see the README of your newly created app.

License and Copyright
=====================

All projects that depend on the AGPL-licensed `omero-web` must also be licensed as AGPL.
A LICENSE file is included accordingly.

GitHub action
=============

The created repository contains two github actions:
* ``omero_plugin.yml``: This action tests the installation of the application as an omero-web app and runs some code checking/formatting like ``flake8`` or ``black``.
* ``publish_pypi.yml``: This action will build and push the application to [PyPi](https://pypi.org/). You must you access password as a secret ``PYPI_PASSWORD`` in order to connect to PyPi.
Modify the actions according to your requirements.
