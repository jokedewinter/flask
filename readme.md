#Heroku and Flask sitting in a tree...

#The Flask part
- Create a folder for your app. Don't call it "flask".
- Create a Python engine file to take care of the running.
- In this file give your app a name.
- Create folders for templates and static files
- Check to make sure your app/site works with Flask by running the engine file in terminal.
- If you haven't done this already make sure your app is a Git repository

#The Heroku part
- Login in at Heroku
- Go to your app folder in terminal and do the following: $ heroku create
- Add the Python build pack to your project: $ heroku buildpacks:set heroku/python
- Create a requirements.txt file with the following things:
  Flask==1.0.2
  gunicorn==19.9.0
- Create a Procfile with the following line:
  web: gunicorn app:app
  The first app refers to the Python engine file, the second app refers to the app name in that file
- Add, commit and push your changes to GitHub
- Push your changes to Heroku as well: $ git push heroku master
- Prepare the viewing of your masterpiece: $ heroku ps:scale web=1
- And now view it: $ heroku open


##Useful links:
https://stackoverflow.com/questions/52039991/flask-application-failing-on-heroku-no-module-named-app
