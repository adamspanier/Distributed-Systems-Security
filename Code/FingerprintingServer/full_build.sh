#!/bin/bash

  cd server
  echo -e "\n########## Building Server! ##########\n"
  ./build.sh
  cd ../client
  echo -e "\n########## Building Client! ##########\n"
  pwd
  ./build.sh
  cd ..
  docker compose up
