: Windows script to run the driver for G-Scan.
cls
@echo off
cd G-Scan\test\
python gui_tests.py

cd ..\..
@echo on