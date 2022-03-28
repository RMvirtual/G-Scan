: Windows script to run the driver for G-Scan.
cls
@echo off
cd ..\..\G-Scan\src
python Driver.py

cd ..\..\script\manual
@echo on