from rules_python.python.runfiles import runfiles as bazel_runfiles


def test_resources_directory() -> str:
    r = bazel_runfiles.Create()

    return r.Rlocation("gscan\\resources\\test")


def image_resources_directory() -> str:
    return _from_runfiles("gscan\\resources\\images")


def config_directory() -> str:
    return _from_runfiles("gscan\\config")


def staging_area() -> str:
    r = bazel_runfiles.Create()

    return r.Rlocation("gscan\\resources\\staging")


def runfile_path(path: str, workspace_root: str = "gscan"):
    return _from_runfiles(workspace_root + "\\" + path)


def _from_runfiles(file_path: str):
    return bazel_runfiles.Create().Rlocation(file_path)
