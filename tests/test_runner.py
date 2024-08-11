import argparse
import sys

import pytest

from pathlib import Path


def main(specific_tests: list[str]) -> None:
    current_directory = Path(f"{__file__}").parent
    sys.path.append((str(current_directory.joinpath("../src"))))

    retcode = pytest.main(specific_tests)
    print("Test run", "failed." if retcode else "successful.")



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
    parser.add_argument(
        "specific", nargs="*", help="Specific test paths or names to run")
    
    args = parser.parse_args()
    main(args.specific)
