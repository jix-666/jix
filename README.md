# JiX
[![Build Status](https://travis-ci.com/jix-666/jix.svg?branch=master)](https://travis-ci.com/jix-666/jix)
[![codecov](https://codecov.io/gh/jix-666/jix/branch/master/graph/badge.svg)](https://codecov.io/gh/jix-666/jix)

JiX web application is a web forum for finding friends and people who have mutually-interested events. The activities are categorized into categories including Hangout, Meeting, Study, Entertainment, Travel, etc. Users can select the interesting category of activity on the Explore page. Moreover, they can find or post about any activity or event on the Feed page. The feed and explore page is visible to everyone on the internet (doesn’t have to log in), but web visitors have to login before post and participate in any event. The intended users are various from teenagers to working adults.

## Getting Started

|    Name    | Required version(s) |
| :--------: | :-----------------: |
|   Python   |   3.7 or higher     |
|   Django   |   3.1 or higher     |

1. Clone this repository to your computer.
    ```
    git clone https://github.com/jix-666/jix.git
    ```
2. Change directory to the repository.
    ```
    cd jix
    ```
3. Install virtualenv to your computer.
    ```
    pip install virtualenv
    ```
4. Create virtual environment.
    ```
    virtualenv jix_env
    ```
5. Activate virtualenv by using this command.

    for Mac OS / Linux
    ```
    source jix_env/bin/activate
    ```
    for Windows
    ```
    jix_env\Scripts\activate
    ```
6. Run this command to install all require packages.
    ``` 
    pip install -r requirements.txt
    ```
7. Create .env file inside jix (same level as settings.py) and added:
    ```
    DEBUG=True
    ```
8. Run this command to migrate the database.
    ```
    python manage.py migrate
    ```
9. Start running the server by this command.
    ```
    python manage.py runserver
    ```
For MAC and OSX users may not be able to install psycopg2    
Follow these steps

1. Install brew by typing this on terminal
    ```
    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)
    ```
2. Install postgreSQL and openssl using homebrew
    ```
    brew install postgresql
    brew install openssl
    ```
3. export these variable in terminal
    ```
    export LDFLAGS="-L/usr/local/opt/openssl/lib"
    export CPPFLAGS="-I/usr/local/opt/openssl/include"
    ```
4. install psycopg2 
    ```
    pip3 install psycopg2 
    ```
    or 
    ```
    sudo pip3 install psycopg2
    ```
  

 

## Project Documents

- [Project proposal](https://docs.google.com/document/d/1xFfaPgIMUXFGIeDvwk4D-pv7skU7g_7FcfdE7mvHmDA/edit)
- [Vision Statement](../../wiki/Vision%20Statement)
- [Requirements](../../wiki/Requirements)
- [Code Review Procedure](../../wiki/Code%20Procedure)
- [Code Checklist](../../wiki/Code%20Checklist)
### Iteration Plan
- [Iteration 1 Plan](../../wiki/Iteration%201%20Plan)
- [Iteration 2 Plan](../../wiki/Iteration%202%20Plan)
- [Iteration 3 Plan](../../wiki/Iteration%203%20Plan)
- [Iteration 4 Plan](../../wiki/Iteration%204%20Plan)
- [Iteration 5 Plan](../../wiki/Iteration%205%20Plan)
- [Iteration 6 Plan](../../wiki/Iteration%206%20Plan)
- [Iteration 7 Plan](../../wiki/Iteration%207%20Plan)