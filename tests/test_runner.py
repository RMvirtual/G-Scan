import sys
import pytest

from pathlib import Path


def main() -> None:
    binaries = Path(f"{__file__}/../release/gscan/bin")
    sys.path.append((str(binaries)))

    arguments = ["--ignore=test_runner.py"]
    retcode = pytest.main(arguments)

    print("Test run", "failed." if retcode else "successful.")

    

if __name__ == "__main__":
    main()
