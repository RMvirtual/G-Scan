cls
@echo off

bazel test --test_output=all --test_summary=detailed //src/test/barcodes/...

@echo on