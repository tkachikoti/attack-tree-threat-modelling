# Attack Tree Threat Modelling




This repository contains an assignment of a Computer Science MSc module at the University of Essex. This application helps with Threat Modelling using Attack Trees and DREAD Scoring (Zhang et al, 2021). It offers functionality to calculate the average DREAD score based on user input and also allows for the uploading of a JSON file containing attack tree data.

![A demonstration of the JSON file structure](https://tkachikoti-cloud-object-storage.ams3.digitaloceanspaces.com/images/github/attack-tree-threat-modelling/json_structure.png)

## Table of contents


- [Description](#description)
- [Installing and running the app](#installing-and-running-the-app)
- [Testing the app](#testing-the-app)
- [Functionality overview](#functionality-overview)
- [References](#references)

## Description


This repository contains a minimum viable product of a [Flask](https://github.com/pallets/flask) based DREAD score calculator.
- The front end interface was built using [Bootstrap](https://github.com/twbs/bootstrap), [Jinja](https://github.com/pallets/jinja) and [d3](https://github.com/d3/d3)
- The testing functionality was implemented using [pytest](https://github.com/pytest-dev/pytest)

### Attack tree threat modelling
Attack tree threat modelling is a method used in computer and information security to describe the security of systems, based on varying attacks (Alhebaishi & Singhal, 2019). Essentially, it's a tree structure, a graphical representation of attacks that can be used against a system, showing how an asset or target might be attacked (Alhebaishi & Singhal, 2019).

In an attack tree model:

- The root of the tree is the ultimate goal of the attacker (Shostack, 2014).
- Each level of the tree explores how the goal could be achieved (Shostack, 2014).
- Each node in the tree represents a condition that the attacker must conquer to achieve the goal (Shostack, 2014).
- Child nodes are conditions that lead up to the parent node being conquered (Shostack, 2014).
- Leaf nodes (those at the end of branches) represent attack vectors, or paths, that the attacker could take (Shostack, 2014).

### DREAD

DREAD is a risk assessment model used to quantify and prioritize the potential risks of identified vulnerabilities in a system (Zhang et al, 2021). It stands for Damage, Reproducibility, Exploitability, Affected Users, and Discoverability — each representing a category to evaluate the risk of a vulnerability (Zhang et al, 2021).

Here's a brief description of each category:

Damage: How severe would an attack be? (Zhang et al, 2021)
Reproducibility: How easy is it to reproduce the attack? (Zhang et al, 2021)
Exploitability: How easy is it to launch the attack? (Zhang et al, 2021)
Affected Users: How many users would be impacted if an attack were to occur? (Zhang et al, 2021)
Discoverability: How easy is it for an attacker to discover the vulnerability? (Zhang et al, 2021)
For each category, a score from 0 (low risk) to 10 (high risk) is assigned. The combined score provides an overall measure of risk, with a higher score indicating greater risk (Zhang et al, 2021).

A DREAD score calculator is a tool that helps calculate the DREAD score of a vulnerability (Zhang et al, 2021). By inputting the ratings for each category, the tool calculates the overall DREAD score, which can help in prioritizing security efforts and resources (Zhang et al, 2021).

## Installing and running the app


1. Clone the repository:

```
$ git clone https://github.com/tkachikoti/attack-tree-threat-modelling
```

2. Change directory:

```
$ cd attack-tree-threat-modelling
```

3. Configure the environment and install dependencies:

- Install Python (version 3.9.7 or newer) via: https://www.python.org/
- Install pip via: https://pip.pypa.io/en/stable/installation/
- Execute the following commands via terminal:
```
$ python -m venv env
$ source env/bin/activate  # on Linux or macOS
$ source env/Scripts/activate     # on Windows
$ pip install -r requirements.txt
```

4. Run the app:

```
$ flask run
```

5. Open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in a browser.

## Testing the app

1. After following the relevant installation process, tests are executed from the root directory by entering:

```
$ pytest
```
![A demonstration of a completed test](https://tkachikoti-cloud-object-storage.ams3.digitaloceanspaces.com/images/github/attack-tree-threat-modelling/upload_screen.png)

## Functionality overview


### Usage

The application offers the following endpoints:

- ```/```: The index page of the application.
- ```/calculate```: Calculates the average DREAD score based on the form data received.
- ```/upload```: Handles the uploading of a JSON file, extracts attack tree data and DREAD score data from it.


### Home Page

On the home page, you can view the existing data and use the form to input new DREAD scores.

![A demonstration of the app in action](https://tkachikoti-cloud-object-storage.ams3.digitaloceanspaces.com/images/github/attack-tree-threat-modelling/app_demo.gif)

### Uploading a JSON File
To upload a JSON file with attack tree data and DREAD scores:

- Click on the Choose File button in the Upload JSON File section.
- Select your JSON file from your file system and click Open.
- Click on the Upload button. The page will refresh and display the attack tree data and DREAD scores from the file.

![upload example](https://tkachikoti-cloud-object-storage.ams3.digitaloceanspaces.com/images/github/attack-tree-threat-modelling/upload_screen.png)

### Calculating DREAD Scores

To calculate DREAD scores:

- Fill out the form fields on the home page with the appropriate scores.
- Click on the Calculate button. The page will refresh and display the average scores for each DREAD category.

![A demonstration of an attack tree](https://tkachikoti-cloud-object-storage.ams3.digitaloceanspaces.com/images/github/attack-tree-threat-modelling/attack_tree.png)

![A demonstration of a DREAD calculator form](https://tkachikoti-cloud-object-storage.ams3.digitaloceanspaces.com/images/github/attack-tree-threat-modelling/dread_calc_form.png)

![A demonstration of an average DREAD calculator score](https://tkachikoti-cloud-object-storage.ams3.digitaloceanspaces.com/images/github/attack-tree-threat-modelling/avg_score.png)

## References

Alhebaishi, Wang, L., & Singhal, A. (2019). Threat Modeling for Cloud Infrastructures. EAI Endorsed Transactions on Security and Safety, 5(17), 156246–. https://doi.org/10.4108/eai.10-1-2019.156246

Shostack, A. (2014). Threat modeling: Designing for security. John Wiley & Sons.

Zhang, L., Taal, A., Cushing, R., de Laat, C., & Grosso, P. (2021). A risk-level assessment system based on the STRIDE/DREAD model for digital data marketplaces. International Journal of Information Security, 1-17.