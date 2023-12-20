OpenFEDEM homepage
==================

The OpenFEDEM homepage, located at http://www.openfedem.org is hosted by one.com and build using the Mkdocs framework. 

## Raw text
The raw text is written in Markdown. 

The first line holds the title of the subpage and shall have Markdown heading level 1, typically _#< title>_

The Markdown heading level 2 e.g. _## <section heading>_, represents the first section level and so on.

## Files 
New files is put into the docs directory and added to the appropriate location in the nav section of the `mkdocs.yml` file 

## Running local web server for testing

At root level run:
> $ mkdocs serve

## Publish

Build a local static version with:
> $ mkdocs build
 
This will create a `site` directory with all the files to be copies to actual web server. This can be done from 
http://one.com's file browser with the OpenFEDEM admin user and a manual upload. Alternatively SFTP can be used. 

> $ scp -r /site/ admin@openfedem_oeg:/remote/directory/