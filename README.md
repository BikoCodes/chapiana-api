## Badges
[![Pipeline Status](https://gitlab.com/bikocodes/chapiana-api/badges/dev/pipeline.svg)](https://gitlab.com/bikocodes/chapiana-api/-/commits/dev)
[![Coverage Report](https://gitlab.com/bikocodes/chapiana-api/badges/dev/coverage.svg)](https://gitlab.com/bikocodes/chapiana-api/-/commits/dev)
[![Latest Release](https://gitlab.com/bikocodes/chapiana-api/-/badges/release.svg)](https://gitlab.com/bikocodes/chapiana-api/-/releases)
[![Lines of Code](https://img.shields.io/tokei/lines/gitlab/BikoCodes/chapiana-api)](https://gitlab.com/bikocodes/chapiana-api)
[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://gitlab.com/bikocodes/chapiana-api/-/blob/dev/LICENSE)


## Table of contents

* [About](#about)

* [Acknowledgements](#acknowledgements)

* [API Reference](#api-reference)

* [Features](#features)

* [Tech Stack](#tech-stack)

* [Local Development](#local-development)

* [Running Tests](#running-tests)

* [Demo](#demo)

* [Lessons Learned](#lessons-learned)

* [Feedback](#feedback)

* [License](#license)

# About

**Version 1.0.0**

This is a RESTFUL API that manages personal contacts of the user and maps every single contact to its owner with their specific images respectively.

## Acknowledgements

I am blessed to be surrounded by many extraordinary people in my life.Without them, it would not be possible for me to do what I do and advance in my mission of being an apristine Software Craftsman. I am deeply grateful.

I must offer special thanks to: 

- **Engineer** [Josephat Macharia](https://gitlab.com/joemash) 

Whom I count on in so very many ways and whose enthusiasm for software development always inspires me.


## API Reference

#### Get all contacts

```http://localhost:8000/
  GET contacts/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `auth_token` | `string` | **Required**. Your Authentication credentials. |

#### Get one contact

```http
  GET /contacts/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `integer` | **Required**. Id of the contact to fetch |


## Features

- [x] Login
- [x] Authorize Token Verification
- [x] Auth Token is generates a token once supplied with appropriate user details.
- [x] Create user(s) with UUID and auth-token(s)
- [x] Create contact mapped to a specific user via the autogenerated UUID
- [x] Returns a **refresh** and **access** JSON web token pair based on the served set of user credentials to prove their authentication.
- [x] Takes a **refresh** JSON web token and returns an **access** type JSON web token if the *refresh* token is **valid**.
- [x] Token **verify** takes a token and indicates if it is valid.It doesn't provide additional information about a token's fitness for a narrowed down use.  

## Architecture

This project impliments the follwing **layers**:

#### 1. Presentation Layer

This represents logic that consume the user logic from the `Usecase Layer`
and renders to the view. Here you can choose to render the view in either `swagger` or `redoc`

#### 2. Application Layer

The application specific logic lives here, this includes  interfaces, views, serializers, models etc.

## Patterns Used

- #### 12 Factor App

The project has been structured as a 12 factor app. For detailed exploration check the link 
https://12factor.net/

- #### Unit of Work Pattern

This pattern coordinates the writing out of changes made to objects using the repository pattern. 

For more details se e https://dotnettutorials.net/lesson/unit-of-work-csharp-mvc/#:~:text=The%20Unit%20of%20Work%20pattern,or%20fail%20as%20one%20unit.

# Local Development

1. Create and activate a virtual environment:

  ```bash
   $ python3 -m venv venv && source venv/bin/activate
  ```

2. Clone the chapiana-api project

  ```bash
    git clone https://github.com/BikoCodes/tests.git
  ```

3. Navigate to the chapiana-api directory

  ```bash
    cd src
  ```

4. Install the requirements:

  ```bash
   (venv)$ pip install -r requirements/dev.txt
  ```

5. Configure the specified environment variables below in an env.sh file:

  ```bash
    export  DATABASE_URL=postgresql://<user>:<pass>@localhost/<database>
    export  TEST_DATABASE_URL=sqlite:////tmp/dev.db
    export  SECRET_KEY=not-so-secret

    export GOOGLE_CLIENT_ID= provided by Google
    export GOOGLE_CLIENT_SECRET= provided by Google
  ```

6. Source the environment variables.

  ```bash
    (venv)$ source env.sh
  ```

7. Stage the database migrations.
  ```bash
    (venv)$ python3 manage.py makemigrations
  ```
  
8. Apply the database migrations.

  ```bash
    (venv)$ python3 manage.py migrate
  ```

9. Start the server
  ```bash
    (venv)$ $ python3 manage.py runserver 
  ```

10. Register and login. Navigate to: 
  ```bash
    http://localhost:8000
  ```

## Tech Stack

- Python 3.8.10
- Django 4.0.1
- Django Rest Framework 3.13.1
- Django Unittesting
- Selenium 4.1.0
- Docker
- Ansible

## Running Tests

To run tests, run the following command from the projects root:

```bash
  (venv)$ coverage run manage.py test
```

## Deployment

The application has been deployed to [Heroku](https://devcenter.heroku.com/).

The deployment has been set and scaled via CI/CD.

##### Steps
- The deployment is defined in `.gitlab-ci.yml`.
- It has 8 jobs which include `install_dependencies`,`build-client`, `migrations`, `connect` `code-test`, `deploy-to-staging`, `deploy-to-production`, and `deploy-to-release`.
- The repository has three branches `dev`, `prod` and `release`.
- Feature branches are merged into `dev`  which points to the `prod` branch.
- The deployment has six stages `prepare` , `build`, `test`, `develop`, `deploy` and `confidence-check`.
- The application is built from the Docker image and pushed to [Heroku](https://devcenter.heroku.com/)
- The codebase tests under the `test` stage are run and if there is a failure then the next stage will not be executed.
- There are two jobs that run under the `deploy` stage, the first one runs on `prod` branch and deploys the code to a production-A environment, the second one runs on `release` branch and deploys the code to a production-B environment.  

## Todo
- [ ] Ensure GitLab Pipepilnes are working
- [ ] Solve the bug issues arising int the CI/CD.
- [ ] Ensure tests are running appropriately.
- [ ] Deploy `Chapiana-api` on the stated environments.

## Demo

Want to see the contactapi application in action?.

[Register and Login](https://github.com/BikoCodes/tests.git)

## Lessons Learned

Developing RESTFUL API's integrated with unittesting test and functional testing.

## Packagerized Project

You can find the chapiana-api as a package on Python Package Index testing plaftorm.Use the following link to download:

 * [Download](https://test.pypi.org/project/contactsapi/#files)

 You can also use the following commands:
  ```bash
  pip install -i https://test.pypi.org/simple/contactsapi
  ```

## License

[MIT](https://choosealicense.com/licenses/mit/)