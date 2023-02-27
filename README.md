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
