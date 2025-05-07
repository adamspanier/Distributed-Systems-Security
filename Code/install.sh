#!/bin/bash

    echo -e "\n ***** Updating! ***** \n"
    sudo apt update

    echo -e "\n ***** Installing GIT! ***** \n"
    sudo apt install git

    echo -e "\n ***** Installing PIP! ***** \n"
    sudo apt install python3-pip

    echo -e "\n ***** Installing Docker! ***** \n"
    sudo apt-get install ca-certificates curl

    # Credit docs.docker.com
    sudo install -m 0755 -d /etc/apt/keyrings
    sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
    sudo chmod a+r /etc/apt/keyrings/docker.asc
    echo \
      "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
      $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
      sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    sudo apt-get update

    sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
    sudo apt install docker-compose

    echo -e "\n ***** Running Docker! ***** \n"
    systemctl start docker
    docker login

    echo -e "\n ***** Installing OpenPLC 3! ***** \n"
    git clone https://github.com/thiagoralves/OpenPLC_v3.git
    cd OpenPLC_v3
    docker build -t openplc:v3 .
    cd ..

    echo -e "\n ***** Running Test Systems! ***** \n"
    echo -e "\n ***** Cloning Repository! ***** \n"
    git clone https://github.com/adamspanier/Distributed-Systems-Security.git
    
    echo -e "\n ***** Moving into the working directory ***** \n"
    cd Distributed-Systems-Security
    cd Code
    cd DockerTestNets
    sudo chmod 777 deploy.sh
    ./deploy.sh    



    
