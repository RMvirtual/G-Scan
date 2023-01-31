@ECHO OFF
CLS
bazel run --build_python_zip=false --enable_runfiles=true //src/main/app/launchers:installer