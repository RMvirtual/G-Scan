: Windows script to run the driver for G-Scan.
cls
@echo off
cd G-Scan\test\validation
python -m unittest -v

cd ..\..\..
@echo on