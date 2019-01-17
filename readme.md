# Heroku and Flask setup instructions

[View Heroku app](https://floating-river-14266.herokuapp.com)

## The Flask part
- Create a folder for your app. Don't call it "flask".
- Create a Python engine file to take care of the running (`app.py`).
- In this file give your app a name (line 3).
- Create folders for templates and static files
- Check to make sure your app/site works with Flask by running the engine file in terminal:
```
$ python app.py
```
- Make sure your app is a Git repository

## The Heroku part
- Log into your Heroku account
- Go to your app folder in terminal and do the following: 
```
$ heroku create
```
- Add the Python build pack to your project: 
```
$ heroku buildpacks:set heroku/python
```
- Create a requirements.txt file with the following things:
```
Flask
gunicorn
jinja2
```
- Create a `Procfile` with the following line:
```
web: gunicorn app:app
```
  The first app refers to the Python engine file (`app.py`), the second app refers to the app name in that file
- Add, commit and push your changes to GitHub
- Push your changes to Heroku as well: 
```
$ git push heroku master
```
- Prepare the viewing of your app with heroku: 
```
$ heroku ps:scale web=1
```
- And now view it: 
```
$ heroku open
```



