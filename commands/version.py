import os
from pathlib import Path

import click


@click.group()
def cli():
    pass


def setup_python(version: str):
    print(f"In python_setup, version is {version}")
    
    version_path = Path.cwd() / "app" / "version.py"
    with open(version_path, "w+") as out:
        out.write(f"VERSION = \"{version}\"")
        out.write("\n")


#  cm-toolkit version --language python --version "$(cat VERSION_INFO)"
@click.command()
@click.option("-l", '--language',
              type=click.Choice(['python'], case_sensitive=False), required=True)
@click.option("-v", "--version", required=True)
def set_version(language: str, version: str):
    print(f"{language=}, {version=}")
    if "python" == language:
        setup_python(version)


cli.add_command(set_version)
