# Nimap_project
# Django Python Machine Test
# project structure

machine_test/

├── requirements.txt

├── manage.py

├── core

│   ├── __init__.py

│   ├── settings.py

│   ├── urls.py

│   └── wsgi.py
└── api/

    ├── __init__.py
    
    ├── models.py
    
    ├── serializers.py
    
    ├── views.py
    
    ├── urls.
    
    └── permissions.
    
## Overview

Welcome to the Django Python Machine Test! This project is all about creating a REST API application to manage three important entities: **Users**, **Clients**, and **Projects**. With this system, you can easily register clients, manage their information, and assign projects to users—all through a clean and intuitive interface.

## Features

Goals trying to complet :

- **Register a Client**: Easily add new clients to the system.
- **Fetch Client Information**: Retrieve detailed info about clients.
- **Edit and Delete Client Information**: Make changes or remove clients as needed.
- **Add Projects**: Create new projects for clients and assign users to those projects.
- **Retrieve Assigned Projects**: View the projects assigned to logged-in users.

## Requirements

To get started, make sure you have the following:

- Python 3.x
- Django
- Django REST Framework
- MySQL 

## Installation

Ready to dive in? Here’s how to set everything up:

1. **Clone the Repository**: First, grab the code by running:
   ```bash
   git clone <your-git-repo-link>
   cd <project-directory>
