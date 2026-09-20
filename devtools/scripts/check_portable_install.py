"""Checking the installed pure-Python CIF and BCIF readers."""

from __future__ import annotations

import argparse
import tempfile
from pathlib import Path

from mmcif.io import IoAdapter
from mmcif.io.BinaryCifReader import BinaryCifReader
from mmcif.io.IoAdapterPy import IoAdapterPy


def _check_container(container_list) -> None:
    assert len(container_list) == 1
    assert container_list[0].getName() == "1BNA"
    assert len(container_list[0].getObjNameList()) == 55


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("data_directory", type=Path)
    arguments = parser.parse_args()

    assert IoAdapter is IoAdapterPy, (
        "The portable package unexpectedly selected the native extension"
    )

    with tempfile.TemporaryDirectory(prefix="py-mmcif-check-") as output_directory:
        cif_containers = IoAdapter(raiseExceptions=True).readFile(
            arguments.data_directory / "1bna.cif",
            outDirPath=output_directory,
        )
    _check_container(cif_containers)

    bcif_containers = BinaryCifReader().deserialize(
        str(arguments.data_directory / "1bna.bcif.gz")
    )
    _check_container(bcif_containers)

    print("portable CIF and BCIF readers: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
