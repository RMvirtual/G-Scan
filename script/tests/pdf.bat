cls
@echo off

bazel test --test_output=all --test_summary=detailed //src/test/pdf/...

@echo on