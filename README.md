<h1 align="center">
  django-user-tel
</h1>

<p align="center">
  <a href="https://github.com/khasbilegt/django-user-tel/">
    <img src="https://img.shields.io/github/workflow/status/khasbilegt/django-user-tel/test?label=CI&logo=github&style=for-the-badge" alt="ci status">
  </a>
  <a href="https://pypi.org/project/django-user-tel/">
    <img src="https://img.shields.io/pypi/v/django-user-tel?style=for-the-badge" alt="pypi link">
  </a>
  <a href="https://codecov.io/github/khasbilegt/django-user-tel">
    <img src="https://img.shields.io/codecov/c/github/khasbilegt/django-user-tel?logo=codecov&style=for-the-badge" alt="codecov">
  </a>
  <br>
  <a>
    <img src="https://img.shields.io/pypi/pyversions/django-user-tel?logo=python&style=for-the-badge" alt="supported python versions">
  </a>
  <a>
    <img src="https://img.shields.io/pypi/djversions/django-user-tel?logo=django&style=for-the-badge" alt="supported django versions">
  </a>
</p>

<p align="center">
  <a href="#installation">Installation</a> •
  <a href="#contributing">Contributing</a> •
  <a href="#license">License</a>
</p>

<p align="center">Custom, simple Django User model with phone number as username</p>

## Installation

1. Use your preferred package manager ([pip](https://pip.pypa.io/en/stable/), [poetry](https://pypi.org/project/poetry/), [pipenv](https://pypi.org/project/pipenv/)) to install the package. For example:

```bash
$ poetry add django-user-tel
```

2. Then register 'user_tel', in the 'INSTALLED_APPS' section of your project's settings.

```python
# settings.py
...

INSTALLED_APPS = (
    ...
    'user_tel',
)

...
```

3. Set AUTH_USER_MODEL - Since it's a custom User model Django needs to know the path of the model

```bash
# settings.py
...

AUTH_USER_MODEL = 'user_tel.User'

...
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT License](https://choosealicense.com/licenses/mit/)
