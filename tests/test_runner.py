import sys
import pytest

from pathlib import Path


def main() -> None:
    binaries = Path(f"{__file__}/../../release/gscan/bin").resolve()
    sys.path.append((str(binaries)))

    for path in sys.path:
        print(path)

    arguments = ["--ignore=test_runner.py"]
    retcode = pytest.main(arguments)

    print("Test run", "failed." if retcode else "successful.")

    

if __name__ == "__main__":
    main()
