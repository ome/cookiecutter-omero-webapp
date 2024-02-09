# Cookiecutter to create OMERO.web apps

[Cookiecutter](https://cookiecutter.readthedocs.io) allows creation of a project from a predefined template,
taking care of all the boilerplate code and filling in the relevant information from user's input.

This repository offers a template to start an OMERO.web app using a project skeleton.

# Usage
Install cookiecutter and use it with this repository's URL:

```sh
pip install cookiecutter
cookiecutter https://github.com/ome/cookiecutter-omero-webapp.git
```

You will be asked to fill in various values.
Here are some helpful tips for some of them:

  - **webapp_name**: This is the python package name for your app (no spaces or dashes), e.g. `omero_foo`.
  - **webapp_title** A label for the page ```<title>``` and for the link from webclient.
  - **description**: A description of your app, added to the README and used in `setup.py`.
  - **repo_name** The repository name, e.g. on `GitHub`. e.g. `omero-foo`.


Then you can install the app for development in your local `omero-web` environment:

```sh
$ cd repo_name
$ pip install -e .

$ omero config append omero.web.apps '"webapp_name"'
```

Then you can restart your `omero-web` server and see your app at `<your-server>/webapp_name/`.

For more details, please see the README of your newly created app.
