[![Build home page](https://github.com/openfedem/openfedem.org/actions/workflows/build-website.yml/badge.svg)](https://github.com/openfedem/openfedem.org/actions/workflows/build-website.yml)

[<img alt="Deployed with FTP Deploy Action" src="https://img.shields.io/badge/Deployed With-FTP DEPLOY ACTION-%3CCOLOR%3E?style=for-the-badge&color=2b9348">](https://github.com/SamKirkland/FTP-Deploy-Action)

# Open FEDEM Website

Welcome to the repository for the OpenFEDEM Website.
This repository contains the source files (Markdown) and content
for the [OpenFEDEM website](https://openfedem.org/).

## Introduction

OpenFEDEM (Open Finite Element Dynamics in Elastic Mechanisms) is an open source software package
developed to provide comprehensive solutions in active nonlinear structural dynamics and adjacent engineering fields.
The GUI part of this package can be found at [openfedem/fedem-gui](https://github.com/openfedem/fedem-gui)
whereas the solvers can be fond at [openfedem/fedem-solvers](https://github.com/openfedem/fedem-solvers).

This repository is dedicated to the development and maintenance of OpenFEDEM's official website,
built using [MkDocs](https://www.mkdocs.org/) from the Markdown source files.

## Installation

To set up a local version of the web site for development purposes, you will need to install `MkDocs`.
Follow these steps:

1. Clone this repository:

       git clone https://github.com/openfedem/openfedem.org.git

2. Install MkDocs:

       pip install mkdocs mkdocs-material pymdown-extensions

   See the [MkDocs Installation Guide](https://www.mkdocs.org/#installation) for further instructions.

3. Navigate to the cloned directory `openfedem.org` and run the command

       mkdocs serve

   This will start a local web-server and you can view the results by visiting the address
   `http://127.0.0.1:8000` in your web browser.

## Usage

After setting up the local environment:

- Edit the Markdown files to update the website content locally.
  The changes will be visible immediately in the local web server when using `mkdocs serve`.

- Once all changes are finalized, they can be built into static files by running the command

      mkdocs build

## Conversions

The first line holds the title of the subpage and shall have Markdown heading level 1, typically `#<title>`

The Markdown heading level 2, e.g., `##<section heading>`, represents the first section level, and so on.

## Contributing

Contributions to improve this website are welcome. Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make your changes and test them locally.
4. Submit a pull request with a clear description of the changes.

## Administration

All raw files used by `MkDocs` to make the static website shall be located under the [docs](docs) directory
and adequately linked into the `nav` section of the [mkdocs.yml](mkdocs.yml) file.

## Publish

Publishing new website content can only be performed using the OpenFEDEM website admin user.

Build a local static version with `mkdocs build`.
This will create or update a `site` directory where all the files to be pushed to the web server are located.
This can be done manually from [one.com](https://www.one.com)'s file browser, alternatively using FTP.
Visit one.com's [User guide](https://help.one.com/hc/en-us/categories/360002171437-Hosting) for more information.

The github action [Build home page](https://github.com/openfedem/openfedem.org/actions/workflows/build-website.yml)
will do this automatically whenever an update is pushed to the main branch of this repository.

## Contact

For questions or suggestions regarding OpenFEDEM,
please contact a `Maintainer` listed [here](https://openfedem.org/developer_area).

---

This README is a guide to help users and contributors understand and participate in the development of the OpenFEDEM **_website_**.
For more information on the OpenFEDEM software's source code, please visit
the [fedem-gui](https://github.com/openfedem/fedem-gui) and/or
the [fedem-solvers](https://github.com/openfedem/fedem-solvers) repositories.
