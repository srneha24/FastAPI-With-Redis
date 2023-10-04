# Using Redis With FastAPI

This project was made on WSL2.

### USED TOOLS AND TECHNOLOGIES

- FastAPI - _As an HTTP server_
- Redis - _As a cache service, message broker and schedular backend_
- Redisinsight - _To visualise Redis data on a GUI_
- Celery - _As a scheduler_
- Celery Beat - _To automate the scheduling_

### Build
- Create an envionment file, titled `.env`, with the follwing variables
    - **DOCKER_CONTAINER_IP:** The IP address of the redis-stack image inside the container
    - **FASTAPI_IP:** The IP address of the fastapi_app image inside the container


- To build the project, run the following command on your console of choice

    ```
    docker-compose build
    ```

### RUN
To run this project, run the following command on your console of choice

```
docker-compose up
```
