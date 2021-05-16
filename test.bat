: Windows script to run the driver for G-Scan.
cls
@echo off
cd G-Scan\test
python -m unittest

cd ..\..
@echo on