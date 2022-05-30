#!/bin/bash
sudo apt install python3 git -y
python -m pip3 install --upgrade pip
pip3 install pyspectator datetime
cd $HOME
git clone https://github.com/ablancoze/pi-temp-exporter.git 
cd pi-temp-exporter
python3 read-temp.py
*/5 * * * * python3 $HOME/pi-temp-exporter/read-temp.py start
