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
Proc-Type: 4,ENCRYPTED
DEK-Info: AES-128-CBC,DA58202EA242203DF89BB1D8A06B128E

ufEBGR7SLJXkkuniiq/03qOQAeMCuAd2Ihu5DaDSLYFtRszpupDELeuMP8GOxb36
jGGfJGf7EyruLrbR6hJErB6J6z/+rReGZ5IWZiPMUjbGFQmZvSsgGUdqqBmOXyvH
QaVDAZHcSqE5UW9jJSH3JcMX/AR08aD/ImGqpNmMsrx50R2LZJ67WP3T4yYsmwc0
6XZgkxMWRtYb9M7llNuHBaklfUpIbnxE7irJNr1MpoxINONvYkR35LcrdGGLYjdM
0WssmgkGnCbMHSmOVvBWWqgd/dx2RmEfpGm6ZLPHkoYAgKLeviRKFf55pKbs2BA6
lWIJ3wQ50UpR00AxDnnG89oRdASe5xldfD6LVNx5aj+LzDKjaLM7gNOPpx2Zfwg9
scGcE+wdazLbg4owOgNn/bBB9t6kEvWftzQfNWOYRVL/dP2ohp18RmeQOFqmLhVW
FrH/NJ9T7YJQq0VCs6qlTeWZ7SR24MZGEFWYxTDd2Ho8HJpRV3nAk7njCoVGAAb0
86qaprydkitbwVnjFcbC8njjP9jW3G6qtWy/42z6PLEb+vbTdt8S+WB2roKZfF8b
Lmz/1+p6vnW8Ps8SXg2rnoY2OIzYrazMqE27AvdTd4ctVu3PI7E8d3YmWFrk9rZk
0bZ6eXz0jy8pKPbJGhfT5tZOVdbaqewpb+HEdFyQFSO4+Uw5IxuVBxlVdHFLVSgZ
xBXUhtNw4nDe0EOOOax9eaVnANQsvB/xjr+xzdiFXWJLL0GKXJBrmrbwOr2j/WHM
auxnuG1x1y7M02b+4icxCqfTm7pFJkwcYrrYJu47/QE/pH5Q6Fcjnh1Dj/qMnoz5
UgyYEzlFFBtKl1uRPptX7xJOVaJpMuDRrZkWSKE5vRh1e3fJ03P9pnlDQJILrHkn
ZSlAE/k27zp8yL3ceHMIKy0QpK8s38sMv23Pqsncc+ac9SOEOkLtN9exiqAwwIM9
H0m+yzWQv6s7njCRfmcB4o1Yqa7UVSPb2CJjI//ajYnf41Rtlvo1QaCob6Ioi3CT
Tg3KCNvra/ONmr/kAjRKQv/kJuZSOBhvpbCqpCUuOKBtoxgDpwmEAFKk6bRNz/zj
R36kBzBxn4OfPygo3lg2hYE0hK1If8Amm6vTMG1/tX0hAkiCLhl7lz3kQ9rfGlSq
nN+28oW5XIlyXyFQldoszueINlvpGzhQEat44EWJ53P4lN6I3OeIXgwStB+N8B1x
NZDffkg2CJVvWawLMZwCzr7XgV6t/s/RSBPIVxzB9/xzXV9WNo+YBJ80+9/7JSpN
/AwfQ+eqelnXBLzZ+qmYM/JNLGGjO1cSIP1/gYNB6OVrd36CXhb6n+UTNHbwpqnB
JDkzllyEZvoT+qeUGGCTa8SYJEWJ8Cl7M5KE2S6Vc7d7p50TmqwpRE7pQUDjDCXA
9c0Dis8oXL4uT2XYu0UizhzTOsil12zOKRk1g4ddFtoG89Q7W/QzsUyEGk9GTEnj
Jgvqrgh1FpmlPP1rA0Drt0ejactgZZD0pWjdrHCqX84D2WDD1tVBPQoSwDkR7voS
P+ZseJsOCEpoxn+/kSYvnmbvseQWYFLSVUx7ewMURqhYwmPVx+KgxYHHDnY7Dz4t
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
