driving_round_town
conda install -c anaconda pyserial

## Ubuntu 19.04
### Download and install
https://ubuntu.com/download/desktop
https://rufus.ie/

### Remove sudo password prompt
http://jonmoore.duckdns.org/index.php/linux-articles/58-remove-sudo-password-prompt

### Basic update
Set `Software Updater` to use best mirror
```bash
sudo apt update
sudo apt upgrade
sudo apt autoremove
```

### Fix time
https://www.howtogeek.com/323390/how-to-fix-windows-and-linux-showing-different-times-when-dual-booting/
https://stackoverflow.com/questions/41986507/unable-to-set-default-python-version-to-python3-in-ubuntu

### Set DNS servers and flush (optional)
https://1.1.1.1/dns/
```bash
sudo service networking restart
```

### Python3
```bash
sudo apt install python3 python3-pip python3-tk pkg-config libcairo2-dev linux-tools-common eog libgirepository1.0-dev  # linux-tools-common is for usbip
```
https://stackoverflow.com/questions/41986507/unable-to-set-default-python-version-to-python3-in-ubuntu

```bash
python -m pip install --upgrade pip setuptools wheel
sudo pip3 install pip-review rplidar numpy scipy matplotlib pandas Pillow testresources --upgrade
sudo pip-review --auto
```

#### PyRoboViz
```bash
cd
git clone https://github.com/simondlevy/PyRoboViz.git
cd PyRoboViz/
sudo python3 setup.py install
cd
```

## WSL (discarded)
https://docs.microsoft.com/en-us/windows/wsl/install-win10

https://www.microsoft.com/en-sg/p/ubuntu-1804-lts/9n9tngvndl3q

```bash
sudo apt update;
sudo apt upgrade;
sudo apt install python3 python3-pip pkg-config libcairo2-dev linux-tools-common;
# linux-tools-common is for usbip
cd
wget https://github.com/magmaOffenburg/RoboViz/releases/download/1.6.1/linux64.tar.gz
# https://github.com/magmaOffenburg/RoboViz/releases
sudo apt-get install eog
git clone https://github.com/simondlevy/PyRoboViz.git
cd
cd PyRoboViz/
sudo python3 setup.py install
cd
sudo pip3 install pip-review rplidar numpy scipy matplotlib pandas Pillow --upgrade
sudo apt-get install python3-tk
pip-review --auto
```
https://virtualizationreview.com/articles/2017/02/08/graphical-programs-on-windows-subsystem-on-linux.aspx
https://www.putty.org/
https://sourceforge.net/projects/xming/files/latest/download
http://laptops.eng.uci.edu/software-installation/using-linux/how-to-configure-xming-putty#TOC-Installation-Configuration-of-Xming
https://www.scivision.dev/usb-tty-windows-subsystem-for-linux/

On RPi
```bash
sudo apt update;
sudo apt upgrade;
sudo apt install usbip
sudo apt-get install socat
```
