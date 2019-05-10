# Backend

## Packages

This just a quick overview of how to setup the backend

**Package dependencies**
- kivy : [DL & install guide](https://kivy.org/#download)
- [python-dotenv](https://pypi.org/project/python-dotenv/) - ```pip install python-dotenv```
- [requests](https://pypi.org/project/requests/) - ```pip install requests```

If your frontend you like won't need to read any further.

## DotEnv
The dotenv file is a way to append to your system's enviorments with out have to hard code or upload sensitive data to the repo.

why? [12factor](https://12factor.net/)

to use rename `example.env` -> `.env` please do not add your details directly to `example.env`

```
# RapidApi details
X-RAPIDAPI-HOST="found at Api's profile page"
X-RAPIDAPI-KEY="found at rapidApi dash"
# database stuff are placeholders
DB_PORT=""
DB_HOST=""
DB_USER=""
DB_PWD=""
DB_DBNAME=""
```

I've already set env files to not be uploaded to the repo

## Api

The Api we're using at the moment is [spoonacular](https://rapidapi.com/spoonacular/api/recipe-food-nutrition). you'll need a RapidApi account
to get a Application key, also you'll need to choose at minimum the free subscription with [spoonacular payment plan](https://rapidapi.com/spoonacular/api/recipe-food-nutrition/pricing).

_keep in mind your limited to 50 requests a day with the free plan._ 

Once you have a RapidApi account you'll need to goto the [dashboard](https://dashboard.rapidapi.com) and then either use the default or create an app. Click on the name of the app in the sidebar and then goto the security. You'll be taken to a new page there a key spacific will need to be copy into a `.env` file.

example of .env should kind of look like RAPID-HOST is correct below but is found on the spoonacular API page
```
X-RAPIDAPI-HOST="spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
X-RAPIDAPI-KEY="fsdf6a8dfj34279134325udhfka"
...
```

## Usage : python-dotenv
_Taken from Pypi page_

The easiest and most common usage consists on calling load_dotenv when the application starts, which will load environment variables from a file named .env in the current directory or any of its parents or from the path specificied; after that, you can just call the environment-related method you need as provided by os.getenv.

.env looks like this:
```python
# a comment and that will be ignored.
REDIS_ADDRESS=localhost:6379
MEANING_OF_LIFE=42
MULTILINE_VAR="hello\nworld"
```

You can optionally prefix each line with the word export, which will conveniently allow you to source the whole file on your shell.

.env can interpolate variables using POSIX variable expansion, variables are replaced from the environment first or from other values in the .env file if the variable is not present in the environment. (Note: Default Value Expansion is not supported as of yet, see #30.)

```python
CONFIG_PATH=${HOME}/.config/foo
DOMAIN=example.org
EMAIL=admin@${DOMAIN}
```



