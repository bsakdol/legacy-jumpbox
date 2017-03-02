#Jumpbox

Jumpbox is a simple command line based interface that allows centralized management of Telnet/SSH device access. Currently, it is designed to work with Netbox to build a list of devices having a management IP address assigned to them.


| Release | License | Master Build | Development Build |
|:-------:|:-------:|:------------:|:-----------------:|
| [![Release](https://img.shields.io/github/release/bradical987/jumpbox.svg)](https://github.com/bradical987/jumpbox/releases) | [![License](https://img.shields.io/badge/license-GPLv3-blue.svg)](https://github.com/bradical987/jumpbox/blob/master/LICENSE) | [![Master Build](https://travis-ci.org/bradical987/jumpbox.svg?branch=master)](http://travis-ci.org/bradical987/jumpbox) | [![Development Build](https://travis-ci.org/bradical987/jumpbox.svg?branch=develop)](http://travis-ci.org/bradical987/jumpbox) |


###Installation
Install Required Packages:
```bash
  # apt-get install -y git python2.7 python-dev python-pip libpq-dev
```

Install Jumpbox libraries:
```bash
    # mkdir -p /opt/jumpbox/ && cd /opt/jumpbox/
    # git clone -b master https://github.com/bradical987/jumpbox.git .
```

Install Python requirements:
```bash
    # cd /opt/jumpbox
    # sudo pip install -r requirements.txt
```

Update the PSQL connection parameters in `jumpbox/database.py`
```bash
	# cp /opt/jumpbox/jumpbox/database.example.py /opt/jumpbox/jumpbox/database.py
```
Change `username` and `127.0.0.1` to be the username and IP address of your PSQL host
```python
	# Line 65
	conn = psycopg2.connect("user = 'username' host = '127.0.0.1'")
```

Create Jumpbox User:
```bash
    # useradd -m -s /opt/jumpbox/jumpbox.py jumpbox
    # passwd jumpbox
```

###Run Jumpbox
SSH to the Jumpbox server, logging in the with credentials for the `jumpbox` user.
