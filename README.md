<div align="center">

  <a href="">[![Pytest Testing Suite](https://github.com/joszamama/flamapy-api/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/joszamama/flamapy-api/actions/workflows/tests.yml)</a>
  <a href="">[![Commits Syntax Checker](https://github.com/joszamama/flamapy-api/actions/workflows/commits.yml/badge.svg?branch=main)](https://github.com/joszamama/flamapy-api/actions/workflows/commits.yml)</a>
  
</div>

# 

<div id="top"></div>
<br />
<div align="center">

  <h3 align="center">FLAMAPY API</h3>

  <p align="center">
    A new and easy way to use FLAMA
    <br />
    <a href="https://github.com/joszamama/flamapy-api/issues">Report Bug</a>
    ·
    <a href="https://github.com/joszamama/flamapy-api/issues">Request Feature</a>
  </p>
</div>
<!-- ABOUT THE PROJECT -->

## About The Project

FLAMAPY API provides an abstraction layer over FLAMA, so that it can be used from any environment through requests to this API. In this way, we eliminate project dependencies and standardize a way to consume it for other applications.

Intended workflow explained:
* User deploys the API with Docker (see Instalation)
* User access the API, reads /api/v1/docs
* User can now start using the API

There are a few known bugs that we acknowledge, described in the projects section. If you detect any other new bug, please consider reporting it!

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Docker](https://www.docker.com/)
* [Flask](https://flask.palletsprojects.com/en/2.2.x/)
* [FLAMA](https://github.com/diverso-lab/core)
* [Flasgger](https://github.com/flasgger/flasgger)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

First, you will need to install [Docker](https://docs.docker.com/desktop/).

### Instalation

1. Clone the repository

2. If you are running Windows, run
  ```sh
  $ cd flamapy-api
  $ ./start-server.cmd
  ```
  
3. If you are running Linux or MacOS, run
  ```sh
  $ cd flamapy-api
  $ ./start-server.sh
  ```
  
This script will build, install and deploy the API in http://localhost:5000, you can access all the endpoints through an application like [Postman](https://www.postman.com/)

<p align="right">(<a href="#top">back to top</a>)</p>

### API Documentation

All the documentation is registered with Swagger UI and OAS 3.0. It is accesible through /api/v1/docs.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Creating a new endpoint

Once you have successfully configured your local development environment, in the /operations folder you will find different methods that work on UVL:

```sh
Info: general information about components, such as plugins and operations.
Count: Count something given a model
Find: Find something given a model
Validate: validate something given a model
```

If these actions represent the functionality you want to add, write the code inside the file. Otherwise, create a new .py file with the verb of the action to be performed. (Example: I want to create and endpoint for modifying the UVL, then, I must create a modify.py file. In this file, create a generic and parameterized method that provides the new functionality. 

Now, from the /routes folder, add the endpoint to the corresponding path. (If you created a new file, also create a new path, as shown in the application).

Use Flask Blueprint and import the path from app.py. This way, now the functionality will be accessible from the API in the new endpoint. Don't forget to fully document the method, the path, and update the swagger.yml file in /static to support the new functionality. If the functionality is not properly documented, it will not be added to the main repository!

<p align="right">(<a href="#top">back to top</a>)</p>
