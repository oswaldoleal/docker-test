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
            	"message": "Successful login",
            	"status": 200
            }
        ```
*  `POST` ***/auth/logout***
    * Allows for a users to log out their accounts
###### Users
*  `POST` ***/user/register***
    * Endpoint to register a new user account
*  `POST` ***/user/delete***
    * Endpoint to delete an existing user account
###### Tasks
*  `POST` ***/task***
    * Endpoint to list all the user's tasks
*  `POST` ***/task/<task_id>***
    * Endpoint to get an specific user's task
*  `POST` ***/task/add***
    * Allows users to add tasks to their accounts
*  `POST` ***/task/delete***
    * Allows users to delete an specific task in their accounts
*  `POST` ***/task/status/<task_id>***
    * Allows users to change a task status (DONE / NOT DONE)
