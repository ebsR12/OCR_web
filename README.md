[![CircleCI](https://circleci.com/gh/fabinhojorge/OCR_web.svg?style=svg)](https://circleci.com/gh/fabinhojorge/OCR_web)

# OCR web
This project is an OCR (tesseract) web interface to upload images. 
The idea of this project is to study technologies like Python, Django, Tesseract(OCR), Continuous Integration, Celery, etc...


## How to install and Run
After activate your Python Virtual Environment (_venv_) run the below command:

```
pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```

So you can access in the local URL: _[localhost:8000](localhost:8000/)_


## How to use
1. _TBD_


## Libraries
* Django
* Pillow
* Bootstrap
* JQuery
* Tesseract
* Celery


## To Do
* [X] Create an initial project
* [X] Add the continuous integration build and test (Circleci)
* [ ] Create the upload media system: models, forms, templates, media url, etc... 
* [ ] Call the OCR to process the image
* [ ] After the core is working, enhance the BE with Celery.
