# Deploying to Heroku

## 1. Create Heroku App

## 2. Connect Git remote

## 3. Add 'requirements.txt''

## 4. Add 'Procfile'

### Deployed website: https://thorin-flask-app-joao-906bc6a0ef47.herokuapp.com/

### Terminal commands Heroku CLI

*npm install -g heroku* to install Heroku CLI

*heroku login -i* to login to Heroku account (use KEY instead of password)

*heroku apps* to display applications in Heroku

*git remote add heroku + heroku url* to add remote

*git push -u heroku main* to push code to Heroku

*pip3 freeze —local . requirements.txt* to create requirements doc

*echo web: python run.py > Procfile* to create Procfile that tells Heroku how to run the app