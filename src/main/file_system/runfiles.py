from rules_python.python.runfiles import runfiles


def test_resources_directory() -> str:
    r = runfiles.Create()

    return r.Rlocation("gscan/resources/test")


def image_resources_directory() -> str:
    return _from_runfiles("gscan\\resources\\images")

    r = runfiles.Create()

    return r.Rlocation("gscan/resources/images")


def data_directory() -> str:
    r = runfiles.Create()

    return r.Rlocation("data/user_settings.dat")


def user_settings_data_path() -> str:
    r = runfiles.Create()

    return r.Rlocation("data/user_settings.dat")


def temp_directory() -> str:
    r = runfiles.Create()

    return r.Rlocation("gscan/data/temp")


def staging_area() -> str:
    r = runfiles.Create()

    return r.Rlocation("gscan/resources/staging")


def _from_runfiles(file_path: str):
    return runfiles.Create().Rlocation(file_path)
