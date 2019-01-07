#Logs Analysis

The objective of the Logs Analysis Project is to create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.


## Up & running 
**Step 1:** Download and install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org). We’ll need these tools to setup and manage the Virtual Machine (VM). 



**Step 2:** Download the database dump from the [downloads folder](downloads/)
Then, copy the database dump `newsdata.sql` to the `/log_analysis` folder .



**Step 3:**  move to the project path by `cd /path/log_analysis` , then run `vagrant up` which will install all dependencies over ubuntu image & seed the postgres db news , with the data that you moved in **step 2**

**Step 4:**
After the vagrant finish  installing , open up your terminal and type 

```
vagrant up
vagrant ssh #connects to vm
cd /vagrant 
python commandHandler.py

```

When you want to get out of the vm you can click `<Ctrl + D>` 
If you want to delete the vm

```
vagrant destroy
```

