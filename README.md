# Zhuoer (Annie) Wang
This repo is a clone of https://github.com/miguelgrinberg/flasky 

# Docker
The Dockerfile is located in the main directory (ECE444-F2020-Lab3) of this repository. To build and run the container, install docker and run the following commands in the main directory.  

### To build the Dockerfile
`docker build -t <repository_name>:latest .`  

### To run the container on a particular port, (in this case 5000)
`docker run -it --name <repository_name> --rm -p 5000:5000 <repository_name>`

# Screenshots

### Docker Run Command
<img src="https://github.com/wangwangaze/ECE444-F2020-Lab3/blob/lab4_Microservice_Experiment/docker-screenshots/start_container.png">

### Browser
<img src="https://github.com/wangwangaze/ECE444-F2020-Lab3/blob/lab4_Microservice_Experiment/docker-screenshots/app.png">

### Docker Image
<img src="https://github.com/wangwangaze/ECE444-F2020-Lab3/blob/lab4_Microservice_Experiment/docker-screenshots/docker_image.png">

# Docker vs Virtual Machine

A Docker container image is a stand-alone executable package containing all the software required to run it, while a virtual machine is an entire operating system.This means that multiple Docker images can be run on the same virtual machine. 

Virtual machines are much heavier since it has its own set of resources allocated to it. On the otherhand, Docker containers are lightweight, because they only contain ressources specified as requirements, so you could run perhaps thousands of containers on a single host.

Furthermore, Docker containers require less time to start, as smaller containers only require seconds to start. On the other hand a fully virtualized system usually takes minutes to start.



