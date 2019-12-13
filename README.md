# **To-Do Web Service**

### **Docker Deployment**

```sh
$ [clone this repo]
$ cd docker-test
$ docker image build -t <image_name>:<image_version> .
$ docker container run --publish <host_port>:<container_port> [--detach] --name <build_name> <image_name>:<image_version>
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
*  `POST` ***/user/delete***
###### Tasks
*  `POST` ***/task***
*  `POST` ***/task/<task_id>***
*  `POST` ***/task/add***
*  `POST` ***/task/delete***
*  `POST` ***/task/status/<task_id>***
