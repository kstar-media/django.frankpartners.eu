21.04.2021
Server default installed python2.7 and 3.8

Installed python 3.9 via apt
https://linuxhostsupport.com/blog/how-to-install-python-3-9-on-ubuntu-20-04/

Switch Python to version:
sudo update-alternatives --config python
https://linuxconfig.org/ubuntu-20-04-python-version-switch-manager

added 3.9 as alternative:
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.9 3

Now option switches on 3.9