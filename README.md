<div align="center">

  <a href="">[![Pytest Testing Suite](https://github.com/flamapy/flamapy-fm-dist/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/flamapy/flamapy-fm-dist/actions/workflows/tests.yml)</a>
  <a href="">[![Commits Syntax Checker](https://github.com/flamapy/flamapy-fm-dist/actions/workflows/commits.yml/badge.svg?branch=main)](https://github.com/flamapy/flamapy-fm-dist/actions/workflows/commits.yml)</a>
  <a href="">![PyPI](https://img.shields.io/pypi/v/flamapy-fm-dist?label=pypi%20package)
  <a href="">![PyPI - Downloads](https://img.shields.io/pypi/dm/flamapy-fm-dist)
</div>

# 

<div id="top"></div>
<br />
<div align="center">

  <h3 align="center">FLAMAPY Feature model distribution</h3>

  <p align="center">
    A new and easy way to use FLAMA
    <br />
    <a href="https://github.com/flamapy/flamapy-fm-dist/issues">Report Bug</a>
    ·
    <a href="https://github.com/flamapy/flamapy-fm-dist/issues">Request Feature</a>
  </p>
</div>
<!-- ABOUT THE PROJECT -->

## About The Project

FLAMAPY Feature model distribution provides an easier way of using FLAMA when analysing feature models. It packs the most used plugins for analyis of feature models adding a layer of convenience to use the framework or integrate it. 

Feature Model Analysis has a crucial role in software product line engineering, enabling us to understand, design, and validate the complex relationships among features in a software product line. These feature models can often be complex and challenging to analyze due to their variability, making it difficult to identify conflicts, dead features, and potential optimizations. This is where this distribution comes in.

Please note: This is a living document and we will continue to update and improve it as we release new versions of the plugins and receive feedback from our users. If there's anything you don't understand or if you have any suggestions for improvement, don't hesitate to contact us. We're here to help!

Three main interfaces are provided:
* A command line interface (CLI): While Flama offers a basic CLI to interact with, this distribution provides a more user friendly CLI with more options and a more intuitive interface.
* A REST API: The REST API allows for easy integration with other tools and applications. It is also a more user friendly interface for those who are not familiar with the command line.
* A Python interface: The Python interface allows for easy integration with other tools and applications. It simplyfies the use of the framework, avoiding to understand all the conventions within the Flama ecosystem.


<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

* [Docker](https://www.docker.com/)
* [Flask](https://flask.palletsprojects.com/en/2.2.x/)
* [FLAMA](https://github.com/diverso-lab/core)
* [Flasgger](https://github.com/flasgger/flasgger)

<p align="right">(<a href="#top">back to top</a>)</p>

# Using the Python interface
This is simple, Flama FM dist in hosted in pypi, therefore simply add the package flama-fm-dist to your requirements file and call the API as follows:

```python
from flamapy.interfaces.python.FLAMAFeatureModel import FLAMAFeatureModel

fm = FLAMAFeatureModel("path/to/feature/model")
print(fm.valid())
```
Currently the operations provided by this distribution are: 
* atomic_sets: This operation is used to find the atomic sets in a model. It returns the atomic sets if they are found in the model. If the model does not follow the UVL specification, an         exception is raised and the operation returns False.
* average_branching_factor: This refers to the average number of child features that a parent feature has in a feature model. It's calculated by dividing the total number of child features by the total number of parent features. A high average branching factor indicates a complex       feature model with many options, while a low average branching factor indicates a simpler model.
* count_leafs: This operation counts the number of leaf features in a feature model. Leaf features are those that do not have any child features. They represent the most specific options in a product line.
* estimated_number_of_products: This is an estimate of the total number of different products that can be produced from a feature model. It's calculated by considering all possible combinations of  features. This can be a simple multiplication if all features are independent, but in most cases, constraints and dependencies between features need to be taken into account.
* feature_ancestors: These are the features that are directly or indirectly the parent of a given feature in a feature model. Ancestors of a feature are found by traversing up the feature hierarchy. This information can be useful to understand the context and dependencies of a feature.
* leaf_features: This operation is used to find leaf features in a model. It returns the leaf features if they are found in the model. If the model does not follow the UVL specification, an 
exception is raised and the operation returns False.   
* max_dept:  This operation is used to find the max depth of the tree in a model.It returns the max depth of the tree. 
* commonality: This is a measure of how often a feature appears in the products of a product line. It's usually expressed as a percentage. A feature with 100% commonality is a core feature, as it appears in all products.
* core_features: These are the features that are present in all products of a product line. In a feature model, they are the features that are mandatory and not optional. Core features define the commonality among all products in a product line. This call requires sat to be called, however, there is an implementation within flama that does not requires sat. please use the framework in case of needing it. 
* dead_features: These are features that, due to the constraints and dependencies in the feature model, cannot be included in any valid product. Dead features are usually a sign of an error in the feature model.
* error_detection: This refers to the process of identifying and locating errors in a feature model. Errors can include things like dead features, false optional features, or contradictions in the constraints.
* false_optional_features: These are features that appear to be optional in the feature model, but due to the constraints and dependencies, must be included in every valid product. Like dead features, false optional features are usually a sign of an error in the feature model.
* filter: This operation selects a subset of the products of a product line based on certain criteria. For example, you might filter the products to only include those that contain a certain feature.
* products number: This is the total number of different products that can be produced from a feature model.It's calculated by considering all possible combinations of features, taking into account the constraints and dependencies between features.
* products: This operation returns all the products of a product line. A product is a valid combination of features that can be produced from a feature model. The products are returned as a list of lists, where each inner list represents a product and contains the features that are included in that product.
* valid_configuration: This operation checks if a given configuration is valid in a feature model. A configuration is a list of features that are included in a product. The operation returns True if the configuration is valid, and False if it's not.
* valid_product: This operation checks if a given product (full configuration) is valid in a feature model. A product is a list of features that are included in a product. The operation returns True if the product is valid, and False if it's not.
* valid: This operation checks if a feature model is valid. A feature model is valid if it follows the UVL specification. The operation returns True if the feature model is valid, and False if it's not.


# Using the command line interface
The command line of this Flama distribution is implemented using [Fire](https://github.com/google/python-fire). When you install the pip package flama-fm-dist, you will find a new command in your pc called flama-fm-dist. Simply call it and follow the instructions. 

# Using the distribution REST API

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

First, you will need to install [Docker](https://docs.docker.com/desktop/).

### Instalation

1. Clone the repository

2. If you are running Windows, run
  ```sh
  $ cd flamapy-dm-dist
  $ ./start-server.cmd
  ```
  
3. If you are running Linux or MacOS, run
  ```sh
  $ cd flamapy-dm-dist
  $ ./start-server.sh
  ```
  
This script will build, install and deploy the API in http://localhost:8000, you can access all the endpoints through an application like [Postman](https://www.postman.com/)

<p align="right">(<a href="#top">back to top</a>)</p>

### API Documentation

All the documentation is registered with Swagger UI and OAS 3.0. It is accesible through /api/v1/docs. This documentation is generated dinamically by relyin gon flasgger. DO not forget to document your code in the route files!

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

Once you have successfully configured your local development environment, in the / folder you will find different methods that work on UVL:

If you want to add new operations, please start by adding a python interface action within the class FLAMAFeatureModel, this is a simple method that, relying on Flama, execute the operation. Later on, you edit the operations route file by calling the prevously created mehod. The command line interface is updated automatically. 

Use Flask Blueprint and import the path from app.py. This way, now the functionality will be accessible from the API in the new endpoint. Don't forget to fully document the method, the path. If the functionality is not properly documented, it will not be added to the main repository!

<p align="right">(<a href="#top">back to top</a>)</p>
