# PythonWebCalculator

This is a project to demonstrate my abilities in Docker. 

The goal is to be able to access a web-based calculator on your localhost after running docker-compose up in your terminal.

The skills required to finalise this project are:

- How to install and setup docker and associated tools
- Use the CLI, Bash on a terminal on macOS
- Write a Dockerfile using DSL
- Understand a third-party app written in Python in such a way that I can map the necessary Docker commands and Dockerfile specifications to run the web server in Django.
- Using git for source control
- Deliver a ready-to-use app and documentation that allows first-time users to quickly setup the app. 

## Prerequisites

This application is only tested on macOS Mojave Version 10.14.6, but it should work on Linux and Windows (using PowerShell).

If the app does not run on your client, please issue a ticket or contact me directly. 

Make sure you have the following dependencies installed on your local environment:

- docker and docker-compose
- python (version 2)
- django
- psycopg2

## How to Use the App

1. Download the repository

`git clone https://github.com/byteknacker/PythonWebCalculator.git`

2. Change directory to the project directory

cd PythonWebCalculator

3. Run docker-compose

`docker-compose up`

4. Open a web browser such as Chrome and go to the site: http://localhost:8000

You should be able to see a web calculator. 
