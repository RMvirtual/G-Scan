: Windows script to run the driver for G-Scan.
cls
@echo off
cd G-Scan\src\python
python Driver.py

cd ..\..\..
@echo on