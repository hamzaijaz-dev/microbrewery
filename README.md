# Microbrewery
This project is structured around three distinct microservices that are developed using Django: warehouse, sales, and accounting. 

For seamless asynchronous communication between these microservices, RabbitMQ has been employed. Each microservice has been encapsulated within its own Docker container. Furthermore, Docker has been utilized to host the MySQL database.

In addition to the core microservices, a mini-service has been developed using FastAPI to facilitate internal API calls to the microservices.


<code><img height="900" src="https://github.com/hamzaijaz-dev/microbrewery/blob/main/assets/micobrewery.png"></code>

## How to set up for local development
### Prerequisite: Docker Installation
Before you can use this project, you need to have Docker installed on your system. Docker allows you to containerize and run applications in isolated environments. If you haven't already installed Docker, follow the instructions below based on your operating system:

#### Installing Docker on Linux
Set up Docker's Apt repository:
* ``sudo apt-get update``
* ``sudo apt-get install ca-certificates curl gnupg``
* ``sudo install -m 0755 -d /etc/apt/keyrings``
* ``curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg``
* ``sudo chmod a+r /etc/apt/keyrings/docker.gpg``
* ``echo "deb [signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null``
* ``sudo apt-get update``

Install the Docker packages:
* ``sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin``

Start the Docker service and enable it to start on boot:
* ``sudo systemctl start docker``
* ``sudo systemctl enable docker``

Find out more on: https://docs.docker.com/engine/install/ubuntu/

#### Installing Docker desktop on macOS/Windows
* Download and install Docker Desktop 
* Follow the installation instructions provided on the website. 
* After installation, open Docker Desktop and ensure it's running.

You can find the docker desktop from: https://www.docker.com/products/docker-desktop/

### Run warehouse-microservice:
* ``cp warehouse/warehouse/template.env warehouse/warehouse/.env``
* Add details for host such as RABBIT_MQ_USER, RABBIT_MQ_PASSRABBIT_MQ_HOST in the .env file, Next run this command:
* ``cd warehouse && docker-compose up``
* Admin URL: http://0.0.0.0:8001/admin
* API documentations: http://0.0.0.0:8001/api/v1/docs

### Run accounting-microservice:
* ``cp accounting/accounting/template.env accounting/accounting/.env``
* Add details for host such as RABBIT_MQ_USER, RABBIT_MQ_PASSRABBIT_MQ_HOST in the .env file, Next run this command:
* ``cd accounting && docker-compose up``
* Admin URL: http://0.0.0.0:8002/admin
* API documentations: http://0.0.0.0:8002/api/v1/docs

### Run sales-microservice:
* ``cp sales/sales/template.env sales/sales/.env``
* Add details for host such as RABBIT_MQ_USER, RABBIT_MQ_PASSRABBIT_MQ_HOST in the .env file, Next run this command:
* ``cd sales && docker-compose up``
* Admin URL: http://0.0.0.0:8003/admin
* API documentations: http://0.0.0.0:8003/api/v1/docs

### Run main-service:
* Add the microservices URLs as environment variables in the docker-compose.yaml file located in the main directory with the following names: WAREHOUSE_URL, SALES_URL, and ACCOUNTING_URL.
* ``cd main && docker-compose up``
* API documentations: http://0.0.0.0:8000/docs

### Useful commands:
* Run ``docker-compose exec <image-name> sh`` to execute a shell within a running container that is managed by Docker Compose
* Run ``python manage.py migrate`` to run the migrations of the microservice
* Run ``python manage.py createsuper`` to create a super-user to access the admin dashboard
* Run ``docker exec -it <volume-name> mysql -u root -p`` to access a MySQL database within a running in Docker container
* Run ``python -u consumer.py`` to verify the RabbitMQ connection in terminal managed by Docker compose

Sometimes, we need a tool that creates a secure, publicly accessible tunnel URL to an application that's running on localhost. Especially, when we are implementing multiple microservices in same environment (localhost).
* Use ngrok for tunneling the URLs: https://ngrok.com
