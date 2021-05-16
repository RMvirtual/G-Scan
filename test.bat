: Windows script to run the driver for G-Scan.
cls
@echo off
cd G-Scan\test\
python tests.py -v

cd ..\..
@echo on