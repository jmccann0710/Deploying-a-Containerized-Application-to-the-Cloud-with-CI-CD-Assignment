# Module 13 - Automated Installation of a Node.js Web Application with Ansible

## Overview
This project automates the deployment of a simple Node.js web application on an Ubuntu EC2 instance using Ansible. The application is managed with PM2.

## Files Included
- app.js
- package.json
- deploy.yml
- rollback.yml
- test.sh
- README.md

## Prerequisites
- Ubuntu EC2 instance
- SSH key pair (.pem)
- Ansible installed
- Port 3000 open in the EC2 security group

## How to Run the Deployment
```bash
ansible-playbook deploy.yml
