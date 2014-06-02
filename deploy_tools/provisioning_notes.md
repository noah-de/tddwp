Provisioning a new site
========================

## Required packages:

* nginx
* Python 3
* Git
* pip
* virtualenv

on Fedora 20:

    sudo yum install nginx git python3 python3-pip
    sudo pip3 install virtualenv

## Nginx Virtual Host Config

* nginx.template.conf
* replace SITENAME with staging.my-domain.com

## Systemd

* see gunicorn-systemd
* replace SITENAME with staging.my-domain.com

## Folder structure:
Assume that we have a user account at /home/username

/home/username
└── sites
     └── SITENAME
	  ├── database
	  ├── source
	  ├── static
          └── virtualenv
