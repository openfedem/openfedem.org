OpenFEDEM Homepage
==================

Welcome to the repository for the OpenFEDEM homepage, a part of the Open Source Finite Element package designed active nonlinear flexible dynamics problems. This repository contains the source code and content for the [OpenFEDEM website](https://www.openfedem.org).

## Introduction

OpenFEDEM (Open Finite Element Dynamics of Elastic Mechanisms) is an open-source software package developed to provide comprehensive solutions in active nonlinear structural dynamics and adjacent engineering fields. The GUI version of this package can be found at [SAP/fedem-gui](https://github.com/SAP/fedem-gui) whereas the solvers can be fond at [SAP/fedem-solvers](https://github.com/SAP/fedem-solvers). 

This repository is dedicated to the development and maintenance of OpenFEDEM's official website, built using Markdown and MkDocs.

## Installation

To set up a local version of the website for development purposes, you will need to install MkDocs. Follow these steps:

1. Clone the repository: `git clone https://github.com/openfedem/openfedem.org.git`
2. Install MkDocs: Instructions can be found at [MkDocs Installation Guide](https://www.mkdocs.org/#installation)
3. Navigate to the cloned directory and run `mkdocs serve` to start a local server. 

## Usage

After setting up the local environment:

- Edit the Markdown files to update the website content.
- Use `mkdocs serve` to preview changes locally.
- Once changes are finalized, they can be built into static files using `mkdocs build`.

## Conversions
The first line holds the title of the subpage and shall have Markdown heading level 1, typically _# < title>_

The Markdown heading level 2 e.g. _## <section heading>_, represents the first section level and so on.


## Contributing

Contributions to improve the website are welcome. Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make your changes and test them locally.
4. Submit a pull request with a clear description of the changes.

For more detailed instructions, see [CONTRIBUTING.md](CONTRIBUTING.md).

## Administration 
All raw files used by `mkdocs` to make the static website shall be located under the `docs` directory and adequately 
linked into the `nav` section of the `mkdocs.yml` file. 

### Publish
Publishing of the website can only be executed using the OpenFEDEM website admin user. 

Build a local static version with `mkdocs build`. This will create or update a `site` directory where all the files
to be pushed to the web server. This can be done from http://one.com's file browser, alternatively using SFTP. 
Visit one.com's user guide for more information. 

## License

This project is licensed under the [MIT License](LICENSE).???

## Contact

For questions or suggestions regarding OpenFEDEM, please contact [Your Contact Information]. ???

---

This README is a guide to help users and contributors understand and participate in the development of the OpenFEDEM **_website_**. For more information on the OpenFEDEM software's source code, visit [fedem-gui repository](https://github.com/SAP/fedem-gui) and/or [fedem-solvers repository](https://github.com/SAP/fedem-solvers).

