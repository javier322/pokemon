#!/bin/bash

sudo docker stop ctr_desafio-pokemon
sudo docker rm ctr_desafio-pokemon
sudo docker rmi img_desafio-pokemon

sudo mkdir output
sudo chmod 777 output
sudo docker build -t img_desafio-pokemon:latest .




