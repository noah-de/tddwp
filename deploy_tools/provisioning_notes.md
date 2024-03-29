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
* replace SITENAME with appropriate value

## Systemd

* see gunicorn.service
* replace SITENAME and USERNAME with appropriate values

## Folder structure:
Assume that we have a user account at /home/username

<pre>
/home/username
└── sites
     └── SITENAME
	  ├── database
	  ├── source
	  ├── static
          └── virtualenv
</pre>
