# 0x02. i18n

## Description
This project focuses on internationalization (i18n) within a Flask application. You'll learn how to manage multiple languages in your web application by parametrizing templates, inferring locales, and localizing timestamps.

## Learning Objectives
By the end of this project, you should be able to:
- Parametrize Flask templates to display content in different languages.
- Infer the correct locale based on URL parameters, user settings, or request headers.
- Localize timestamps using appropriate time zones.

## Resources
To help you complete this project, make sure to read or watch the following:

- [Flask-Babel ](https://web.archive.org/web/20201111174034/https://flask-babel.tkte.ch/)

- [Flask i18n tutorial ](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiii-i18n-and-l10n)

- [pytz ](https://pypi.org/project/pytz/)


## Learning Objectives
Learn how to parametrize Flask templates to display different languages
Learn how to infer the correct locale based on URL parameters, user settings or request headers
Learn how to localize timestamps

## Project Structure
```plaintext
.
├── 0-main.py
├── babel.cfg
├── myapp/
│   ├── __init__.py
│   ├── app.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   ├── translations/
│   │   ├── en/
│   │   ├── fr/
│   └── ...
└── README.md
