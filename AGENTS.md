# AGENTS Guide

This repository is a fork of https://github.com/rcsb/py-mmcif.
Its sole purpose is to enable installation via conda, since no conda packages are available for this library.
The uibcdf channel is used as our distribution channel to address this gap.

## Key paths

- `devtools/conda-build/`: conda recipe (`meta.yaml`), build script (`build.sh`), and manual upload notes (`README.md`).
- `devtools/conda-envs/build_env.yaml`: build environment for CI (micromamba).
- `.github/workflows/build_and_upload_conda_packages.yaml`: CI build and upload workflow.

## Conda packaging notes

- Runtime dependency for msgpack is `msgpack-python` in the conda recipe (matches prior successful builds).
- Build requires `cmake`, `bison`, `flex`, and C/C++ compilers (CMakeLists.txt uses flex/bison).
- Recipe version is `{{ environ['GIT_DESCRIBE_TAG'] }}`; ensure releases/tags are created before CI runs.

## CI workflow behavior

- Triggers: GitHub Releases (`released`/`prereleased`) and manual `workflow_dispatch`.
- Uses micromamba to create a build env from `devtools/conda-envs/build_env.yaml`.
- Uploads to Anaconda using `ANACONDA_UIBCDF_TOKEN` secret and `uibcdf` user.
- Channels for dependencies: `conda-forge` and `defaults` only.

## README expectations

- Keep the fork/purpose disclaimer at the top of `README.md`, separated from upstream content by a horizontal rule.
