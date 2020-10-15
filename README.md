# Zhuoer (Annie) Wang
This repo is a clone of https://github.com/miguelgrinberg/flasky 

The Dockerfile is located in the main directory (ECE444-F2020-Lab3) of this repository. To build and run the container, install docker and run the following commands in the main directory.  

### To build the Dockerfile
`docker build -t <repository_name>:latest .`  

### To run the container on a particular port, (in this case 5000)
`docker run -it --name <repository_name> --rm -p 5000:5000 <repository_name>`

## Screenshot 1: Docker Run Command
<img src="https://github.com/wangwangaze/ECE444-F2020-Lab3/blob/lab4_Microservice_Experiment/docker-screenshots/start_container.png">

## Screenshot 2: Browser
<img src="https://github.com/wangwangaze/ECE444-F2020-Lab3/blob/lab4_Microservice_Experiment/docker-screenshots/app.png">

## Screenshot 3: Docker Image
<img src="https://github.com/wangwangaze/ECE444-F2020-Lab3/blob/lab4_Microservice_Experiment/docker-screenshots/docker_image.png">



