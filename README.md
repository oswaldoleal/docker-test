# **To-Do Web Service**

### **Docker Deployment**
General docker commands
```sh
$ [clone this repo]
$ cd docker-test
$ docker image build -t <image_name>:<image_version> .
$ docker container run --publish <host_port>:<container_port> [--detach] --name <build_name> <image_name>:<image_version>
```
Assingment specific commands. Maps the port 8500 in the host to the port 5000 of the container
```sh
$ git clone https://github.com/oswaldoleal/docker-test.git
$ cd docker-test
$ docker image build -t OL_LC:1.0 .
$ docker container run --publish 8500:5000 --name OL_LC OL_LC:1.0
```

### **Documentation**

##### **Endpoints**

###### Authentication
*  `POST` ***/auth/login***
    * Allows users to log into their accounts 
        * Request body:
           ```json
               {
                  "username": "admin",
                  "password": "real_secure"
               }
           ```
        * Return data:
           ```json
               {
                   "apikey": "555555555555555",
                   "message": "Successful login",
                   "status": 200
               }
           ```
*  `POST` ***/auth/logout***
    * Allows for a users to log out their accounts
       * Request body:
           ```json
            {
               "username": "admin"
            }
           ```
       * Return data:
           ```json
            {
               "message": "Successful logout",
               "status": 200
            }
           ```
###### Users
*  `POST` ***/user/register***
    * Endpoint to register a new user account
       * Request body:
           ```json
            {
               "username": "admin",
               "password": "real_secure"
            }
           ```
       * Return data:
           ```json
            {
               "message": "Successful register",
               "status": 200
            }
           ```
*  `POST` ***/user/delete***
    * Endpoint to delete an existing user account
       * Request body:
           ```json
            {
               "username": "admin"
            }
           ```
       * Return data:
           ```json
            {
               "message": "Successful deletion",
               "status": 200
            }
           ```
###### Tasks
*  `POST` ***/task***
    * Endpoint to list all the user's tasks
       * Request body:
           ```json
            {
               "username": "admin",
               "apikey": "555555555555555"
            }
           ```
       * Return data:
           ```json
            {
               "status": 200,
               "tasks": [
                  {
                     "date": "12/13/2019, 14:26:26",
                     "detail": "the docker assignment",
                     "id": "6085992141384171",
                     "status": "NOT DONE",
                     "title": "finish the sd assignment"
                  },
                  {
                     "date": "12/13/2019, 14:38:20",
                     "detail": "the docker assignment",
                     "id": "8876548629708302",
                     "status": "NOT DONE",
                     "title": "finish the sd assignment"
                  },
                  {
                     "date": "12/16/2019, 07:48:00",
                     "detail": "the docker assignment",
                     "id": "24601123105822653",
                     "status": "NOT DONE",
                     "title": "finish the sd assignment"
                  }
               ]
            }
           ```
*  `POST` ***/task/<task_id>***
    * Endpoint to get an specific user's task
       * Request body:
           ```json
            {
               "username": "admin",
               "apikey": "555555555555555"
            }
           ```
       * Return data:
           ```json
            {
               "status": 200,
               "task": [
                  {
                     "date": "12/13/2019, 14:38:20",
                     "detail": "the docker assignment",
                     "id": "8876548629708302",
                     "status": "NOT DONE",
                     "title": "finish the sd assignment"
                  }
               ]
            }
           ```
*  `POST` ***/task/add***
    * Allows users to add tasks to their accounts
       * Request body:
           ```json
            {
               "username": "admin",
               "title": "finish the sd assignment",
               "detail": "the docker assignment",
               "apikey": "555555555555555"
            }
           ```
       * Return data:
           ```json
            {
               "message": "Successful adding",
               "status": 200
            }
           ```
*  `POST` ***/task/delete***
    * Allows users to delete an specific task in their accounts
       * Request body:
           ```json
            {
               "username": "admin",
               "apikey": "555555555555555",
               "task_id": "6085992141384171"
            }
           ```
       * Return data:
           ```json
            {
               "message": "Successful delete",
               "status": 200
            }
           ```
*  `POST` ***/task/status/<task_id>***
    * Allows users to change a task status (DONE[1] / NOT DONE[0])
       * Request body:
           ```json
            {
               "username": "admin",
               "apikey": "555555555555555",
               "status": 1
            }
           ```
       * Return data:
           ```json
            {
               "message": "Successful status change",
               "status": 200
            }
           ```
