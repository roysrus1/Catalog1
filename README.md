# Catalog Application - catalog.py
Code for catalog project assignment

#New section for LightSail documentation

#Server & App info:
IP address: 54.236.38.136
SSH Port: 2200
URL: http://54.236.38.136/

#Summary of Software Installed:

1. apache2
2. libapache2-mod-wsgi
3. postgresql
4. git
5. psycopg2 sqlalchemy
6. python-pip python-dev build-essential
7. pip install --upgrade pip
8. pip install --upgrade virtualenv

#Graders SSH key and passphrase:

passphrase: grader

key:

-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEA3qmLojL+QMaNRfZFgH8oAvb90/hTYj80Krj4T9Bqt/Qfq1vG
CbTJCSp8SOehcRIjQriKRRPnmdgudVmkse02HgT6Mmr3Fk4Sw7gFDBzSORK+Z0NI
QbjCP/DUPjErIsDExt6TARY5v5/RWNijqfPVFGO+eOPuQbpktR4wohtG3HG2c3hj
FIdW53k5ng5G95gjnWC2DrzVtQVQcDFjlcfByCVz1/FUVvF6z77FsoYw7ig7slH/
YZT+9IJrns62t/hedegiRMqUYuRRAPef6XXWXYjWQRScmKfAYyH4WKptstTm357l
IoBbdj2fj9jKELi0VRtXKWHul+vGJ8XW0mKZuwIDAQABAoIBAHC+KJXYfCUQZDgo
msiVmgzmQ2AxPQdiOWfogNLpFSBP3DlIHt6LS7/4YzYHExfNt0zxZBHWIk8jx2Jk
IaB2HBDXNFiTEMmafqXbZ7LaZRfBBegDiXK9up3ls5JKEy1lrj2ENas3NcZxhe8W
wsgrTpkkaC2OO/XMC3Ip9zYd2aOEfi+IgFSiz/g6ID0kKdMUybCtRFZylo/u92ZA
oz2r1qHHYOC3JyjLufkzbAPv9KlQxXemvr8Yz3NwF3q1vL6TcWVDwY9HnffE39t7
3mVLq+yR1/z+R7ja2c6V932yA1CTheJ7RcesXSVmr3HN+jS7Ky3Prw56gJPFuN5s
Wakn4wECgYEA/wCAjJOQNLvRqWesr80+L4nkmsIx0fQ5M4XJYXfWTk5SUX3F8BJO
ZhgrCMqbUV5jSO9c+zQsoFaIT6O/x8vz8XKwUxhqfmSrj4hqcp8XX1FGFNOwV0qO
mJb7G2LsG8iXcy08UCw01Ils+ZWDXRewdGz61lP8cPSdJA0BWrPEZ0UCgYEA34ik
ByiQJ6PM5fE5i2InXu1KUw/iTgpSGsbrRIl13IklUe9WiE+ZrbxpPJovjyKc14qT
00C6drcpLS2QW2LhvctDW/yozyWyxao0WjYMX2ibGTJ3PjbffeGB6OeZSERqs7ZT
dZZe/gY2cXQO+emPx50ejXAbj8u+nONt5V2OjP8CgYB9xX2h2FZT7B8o8t2ViCGX
yOdb/VQdPdvIsb/1tumYjcDEOMib9Ct+54SyPVwF8gv+OTEfJUitfICW5yj8Hngf
KnYVRgGgfX6wuJPoHNemR6vNMevT4g4a7LzFcTELMxCf2jvZPzR/b5i0MS4tiDWb
9vRxKdNk0wF+enukhO3mEQKBgCk9cV2suyPFEZlersorWq4lwy+d35ecSdeM2Xz0
i10bpFoAeQt+/BBUkWnP3HRg42TUuT8hUwVx91PRcy+ZB6LXbF79Nzu4bcoQA8ac
8B1uFCdK6zr8LrFvuGL6z4nIrZLoUW+BRZdCGCtISTcMQy2FrExV4Y/e/BS/1Neb
MiCLAoGAGb9eNHdOm3vAFENofWgQ04VxcgHAg/xWmqRbTQR7L/6M7UD6JCcztbBn
B3B8HIldts3yp61wjVR7giDZxnlL4DDfSs726ChJ66L58l3FEAQUqFHjc3Hkg6tL
T7U+rEyXWQXY4SWfvcSc/Dzu1LNMCRYuryCjq/9MlweQC8RyzVw=
-----END RSA PRIVATE KEY-----




*********************** OLD INFO BELOW ON RUNNING SAME APP IN VAGARANT *********************************




#Prerequisites
# Installing the Vagrant VM for ud330 - Authentication & Authorization

**Note: If you already have a vagrant machine installed from previous Udacity courses skip to the 'Fetch the Source Code and VM Configuration' section**

In Lessons 2,3 and 4 of this course, you'll use a virtual machine (VM) to run a web server and a web app that uses it. The VM is a Linux system that runs on top of your own machine.  You can share files easily between your computer and the VM.

We're using the Vagrant software to configure and manage the VM. Here are the tools you'll need to install to get it running:

### Git

If you don't already have Git installed, [download Git from git-scm.com.](http://git-scm.com/downloads) Install the version for your operating system.

On Windows, Git will provide you with a Unix-style terminal and shell (Git Bash).
(On Mac or Linux systems you can use the regular terminal program.)

You will need Git to install the configuration for the VM. If you'd like to learn more about Git, [take a look at our course about Git and Github](http://www.udacity.com/course/ud775).

### VirtualBox

VirtualBox is the software that actually runs the VM. [You can download it from virtualbox.org, here.](https://www.virtualbox.org/wiki/Downloads)  Install the *platform package* for your operating system.  You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it.

**Ubuntu 14.04 Note:** If you are running Ubuntu 14.04, install VirtualBox using the Ubuntu Software Center, not the virtualbox.org web site. Due to a [reported bug](http://ubuntuforums.org/showthread.php?t=2227131), installing VirtualBox from the site may uninstall other software you need.

### Vagrant

Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem.  [You can download it from vagrantup.com.](https://www.vagrantup.com/downloads) Install the version for your operating system.

**Windows Note:** The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.

## Fetch the Source Code and VM Configuration

**Windows:** Use the Git Bash program (installed with Git) to get a Unix-style terminal.
**Other systems:** Use your favorite terminal program.

From the terminal, run:

    git clone https://github.com/udacity/OAuth2.0 oauth

This will give you a directory named **oauth** complete with the source code for the flask application, a vagrantfile, and a bootstrap.sh file for installing all of the necessary tools.

## Run the virtual machine!

Using the terminal, change directory to oauth (**cd oauth**), then type **vagrant up** to launch your virtual machine.


## Running the Catalog Menu App
Once it is up and running, type **vagrant ssh**. This will log your terminal into the virtual machine, and you'll get a Linux shell prompt. When you want to log out, type **exit** at the shell prompt.  To turn the virtual machine off (without deleting anything), type **vagrant halt**. If you do this, you'll need to run **vagrant up** again before you can log into it.


Now that you have Vagrant up and running type **vagrant ssh** to log into your VM.  change to the /vagrant directory by typing **cd /vagrant**. This will take you to the shared folder between your virtual machine and host machine.

## Running the Catalog Application

Type **ls** to ensure that you are inside the directory that contains catalog.py, catalog_setup.py, lotsosstudents.py and two directories named 'templates' and 'static'

Now type **python catalog_setup.py** to initialize the database.

Type **python lotsofstudents.py** to populate the database with students and prizes.

Type **python catalog.py** to run the Flask web server. In your browser visit **http://localhost:5000** to view the student menu app.

If you are not logged on, you can view the students and prizes populated via the lotsofstudents.py (initially).

If you choose to log on, you will be redirected to a google authentication process.  Once logged on, you should be able to view, add, edit, and delete students and prize items.
