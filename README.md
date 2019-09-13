driving_round_town
conda install -c anaconda pyserial

## WSL
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
https://github.com/cezuni/usbip-win TODO
sudo apt-get install socat
