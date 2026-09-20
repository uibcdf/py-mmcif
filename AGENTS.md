# AGENTS Guide

This repository is a fork of https://github.com/rcsb/py-mmcif.
Its purpose is to provide portable, functionally tested conda packaging for consumers
that require the upstream `mmcif` Python API. The uibcdf channel is used as the
distribution channel. Parser or API defects that are not packaging-specific should be
reported upstream.

## Key paths

- `devtools/conda-build/`: conda recipe (`meta.yaml`), build script (`build.sh`), and manual upload notes (`README.md`).
- `devtools/conda-envs/build_env.yaml`: build environment for CI (micromamba).
- `.github/workflows/build_and_upload_conda_packages.yaml`: CI build and upload workflow.

## Conda packaging notes

- Runtime dependency for msgpack is `msgpack-python` in the conda recipe (matches prior successful builds).
- The conda package is `noarch: python` and deliberately installs the upstream
  pure-Python CIF and BCIF readers. Do not add a compiler dependency to this recipe.
- Native acceleration remains available in upstream builds on supported platforms. The
  `MMCIF_BUILD_EXTENSION` environment variable controls whether a source build includes
  it; Windows defaults to the portable backend.
- The recipe version is read from `mmcif/__init__.py` and must agree with the release tag.

## CI workflow behavior

- Triggers: GitHub Releases (`released`/`prereleased`) and manual `workflow_dispatch`.
- Builds one candidate, then tests that exact artifact on x86-64 and ARM64 Linux, Intel
  and ARM macOS, and x86-64 Windows with every supported MolSysSuite Python version.
  Python 3.14 is also exercised prospectively; this does not change the suite-wide
  support declaration.
- Manual runs do not publish unless `publish` is explicitly enabled. Release runs upload
  only after the complete test matrix passes.
- Uploads to Anaconda using `ANACONDA_UIBCDF_TOKEN` and the `uibcdf` user.
- Channels for dependencies: `conda-forge` and `defaults` only.

## README expectations

- Keep the fork/purpose disclaimer at the top of `README.md`, separated from upstream
  content by a horizontal rule.
