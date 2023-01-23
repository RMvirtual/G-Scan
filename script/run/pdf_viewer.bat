@ECHO OFF
CLS
bazel run --build_python_zip=false --enable_runfiles=true //src/main/app/pdf_viewer ^
    -- "C:\Users\ryanm\Documents\GitHub\G-Scan\resources\images\g-scan_logo.png"