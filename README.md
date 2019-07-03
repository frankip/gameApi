# GameApi
GameApi is RESTful API created using django that can perform CRUD (Create, Read, Update, and Delete)
on postgres Database. It can track Games under a game category, Playes who have played a certain games, The score and users.

### Technologies Used
- Python
- Django
- Pipenv
- Djangorestframework

## How to Set Up

- clone the repo to your local machine 
    `git clone https://github.com/frankip/gameApi.git`
- Setup a virtual enviroment and install the dependendencies
    `pip install -r requirements.txt` or `pipenv install requirements.txt`

- in the settings file under Databases, change the name user and passwor to your desired credentials

- Set up migrations
    `python manage.py makemigrations`

- Migrate to create tables
    `python manage.py migrate`

- start the development server
    ``python manage.py runserver`

    
| HTTP verb | Scope | Semantics |
|----------:|-------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GET | Collection of game categories | Retrieve all the stored game categories in the collection, sorted by their name in ascending order. Each game category must include a list of URLs for each game resource that belongs to the category. |
| GET | Game category | Retrieve a single game category. The game category must include a list of URLs for each game resource that belongs to the category. |
| POST | Collection of game categories | Create a new game category in the collection. |
| Put | Game category | Update an existing game category. |
| PATCH | Game category | Update one or more fields of an existing game category. |
| DELETE | Game category | Delete an existing game category. |
| GET | Collection of games | Retrieve all the stored games in the collection, sorted by their name in ascending order. Each game must include its game category description. |
| GET | Game | Retrieve a single game. The game must include its game category description. |
| POST | Collection of games | Create a new game in the collection. |
| PUT | Game category | Update an existing game. |
| PATCH | Game category | Update one or more fields of an existing game. |
| DELETE | Game category | Delete an existing game. |
| GET | Collection of players | Retrieve all the stored players in the collection, sorted by their name in ascending order. Each player must include a list of the registered scores, sorted by score in descending order. The list must include all the details for the score achieved by the player and its related game. |
| GET | Player | Retrieve a single player. The player must include a list of the registered scores, sorted by score in descending order. The list must include all the details for the score achieved by the player and its related game. |
| POST | Collection of players | Create a new player in the collection. |
| PUT | Player | Update an existing player. |
| PATCH | Player | Update one or more fields of an existing player. |
| DELETE | Player | Delete an existing player. |
| GET | Collection of scores | Retrieve all the stored scores in the collection, sorted by score in descending order. Each score must include the player's name that achieved the score and the game's name. |
| GET | Score | Retrieve a single score. The score must include the player's name that achieved the score and the game's name. |
| POST | Collection of scores | Create a new score in the collection. The score must be related to an existing player and an existing game. |
| PUT | Score | Update an existing score. |
| PATCH | Score | Update one or more fields of an existing score. |
| DELETE | Score | Delete an existing score. |

