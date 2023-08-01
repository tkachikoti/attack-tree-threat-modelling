# Attack Tree Threat Modelling

This repository contains an assignment of a Computer Science MSc module at the University of Essex.

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
Attack tree threat modelling is a method used in computer and information security to describe the security of systems, based on varying attacks. Essentially, it's a tree structure, a graphical representation of attacks that can be used against a system, showing how an asset or target might be attacked.

In an attack tree model:

- The root of the tree is the ultimate goal of the attacker.
- Each level of the tree explores how the goal could be achieved.
- Each node in the tree represents a condition that the attacker must conquer to achieve the goal.
- Child nodes are conditions that lead up to the parent node being conquered.
- Leaf nodes (those at the end of branches) represent attack vectors, or paths, that the attacker could take.

### DREAD

DREAD is a risk assessment model used to quantify and prioritize the potential risks of identified vulnerabilities in a system. It stands for Damage, Reproducibility, Exploitability, Affected Users, and Discoverability — each representing a category to evaluate the risk of a vulnerability.

Here's a brief description of each category:

Damage: How severe would an attack be?
Reproducibility: How easy is it to reproduce the attack?
Exploitability: How easy is it to launch the attack?
Affected Users: How many users would be impacted if an attack were to occur?
Discoverability: How easy is it for an attacker to discover the vulnerability?
For each category, a score from 0 (low risk) to 10 (high risk) is assigned. The combined score provides an overall measure of risk, with a higher score indicating greater risk.

A DREAD score calculator is a tool that helps calculate the DREAD score of a vulnerability. By inputting the ratings for each category, the tool calculates the overall DREAD score, which can help in prioritizing security efforts and resources.

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

- Install Python (version 3.9.7 or greater) via: https://www.python.org/
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
$ python app.py
```

5. On the menu bar, click on the downward pointing chevron to open the preview menu. Please ensure that the 'Box URL' and the 'New Browser Tab' options are selected.

![The configuration that is required for the BTS app to run on Codio](https://tkachikoti-cloud-object-storage.ams3.digitaloceanspaces.com/images/github/bug-tracking-system/codio_config_1.png)

6. Click the 'Box URL' button to open a browser tab running the app.

![The button the must be clicked to open a web browser that can display the app](https://tkachikoti-cloud-object-storage.ams3.digitaloceanspaces.com/images/github/bug-tracking-system/codio_config_2.png)

Please refer to Codio's documentation to resolve any issues:
https://docs.codio.com/common/develop/ide/editing/preview.html

### Windows and macOS

1. Download and install Python: https://www.python.org/downloads/

2. Clone the repository:

```
$ git clone https://github.com/tkachikoti/bug_tracking_system.git
```

3. Change directory:

```
$ cd bug_tracking_system
```

4. Configure the environment and install dependencies:

```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -U flask
$ pip install -U Flask-WTF
$ pip install -U pytest
$ pip install -U numpy
```

5. Run the app:

```
$ python app.py
```

6. Open [http://192.168.1.12:3000/](http://192.168.1.12:3000/) in a browser.

## Testing the app

1. After following the relevant installation process, tests are executed from the root directory by entering:

```
$ pytest
```

## Functionality overview


### 1. Create/Update Ticket

Users can create or update a ticket by interacting with the form and clicking the button labelled 'CREATE/UPDATE TICKET'. The form includes front end validation to ensure all fields contain data.

![A demonstration of a user creating a ticket](https://tkachikoti-cloud-object-storage.ams3.digitaloceanspaces.com/images/github/bug-tracking-system/bts_create_page.gif)

Pseudo-code:

- Check if the form contains a key labelled 'component-name'
- Validate form data
- If form data is valid persist data in storage otherwise return to index page


### 2. View/Delete Ticket

Users can view or delete a ticket by referencing the unique identification number (uid) that is assigned to each ticket upon creation. A prompted appears on screen requesting users to confirm the deletion of a ticket prior to the execution of the command. This safeguards against the accidental deletion of a ticket.

![A demonstration of a user deleting a ticket](https://tkachikoti-cloud-object-storage.ams3.digitaloceanspaces.com/images/github/bug-tracking-system/bts_delete_page.gif)

Pseudo-code:

- Check if the form contains a key labelled 'uid'
- Retrieve all data about tickets from persistent storage
- Find ticket data with a 'uid' that matches the one received via GET/POST request form
- Return ticket data

### 3. Search Ticket

Users can search for a ticket by filling a form on the search page. The search algorithm uses cosine similarity to find the ticket(s) which closely resemble the string that is received via search form. (Budiman et al, 2017)

![A demonstration of a user searching for a ticket](https://tkachikoti-cloud-object-storage.ams3.digitaloceanspaces.com/images/github/bug-tracking-system/bts_search_page.gif)

Pseudo-code:

- Check if the form contains a key labelled 'search_value'
- Retrieve all data about tickets from persistent storage
- Iterate through the list of tickets checking the cosine similarity between the ticket data and the 'search_value'
- If the cosine similarity is greater than zero the ticket data is appended to the 'search_results' list
- 'search_results' list is sorted in descending order (with respects to the similarity score)
- 'search results' are returned

## References


Budiman, M., Gunawan, D. & Sembiring, C. (2017) 'The Implementation of Cosine Similarity to Calculate Text Relevance between Two Documents', *Journal of Physics: Conference Series*. Medan, Indonesia, 28–30 November. Medan: IOP Publishing Ltd.