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
* Add your RABBIT_MQ_URL in the .env file, Next run this command:
* ``cd warehouse && docker-compose up``
* API documentations: http://0.0.0.0:8001/api/v1/docs

### Run accounting-microservice:
* ``cp accounting/accounting/template.env accounting/accounting/.env``
* Add your RABBIT_MQ_URL in the .env file, Next run this command:
* ``cd accounting && docker-compose up``
* API documentations: http://0.0.0.0:8002/api/v1/docs

### Run sales-microservice:
* ``cp sales/sales/template.env sales/sales/.env``
* Add your RABBIT_MQ_URL in the .env file, Next run this command:
* ``cd sales && docker-compose up``
* API documentations: http://0.0.0.0:8003/api/v1/docs

### Run main-service:
* Add the microservices URLs as environment variables in the docker-compose.yaml file located in the main directory with the following names: WAREHOUSE_URL, SALES_URL, and ACCOUNTING_URL.
* ``cd main && docker-compose up``
* API documentations: http://0.0.0.0:8000/docs