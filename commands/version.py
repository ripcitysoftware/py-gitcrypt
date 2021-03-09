import os
from pathlib import Path

import click


@click.group()
def cli():
    pass


def setup_python(version: str, file: str):
    print(f"In python_setup, version is {version}")
    
    version_path = Path.cwd() / file
    with open(version_path, "w+") as out:
        out.write(f"VERSION = \"{version}\"")
        out.write("\n")


#  cm-toolkit version --language python --version "$(cat VERSION_INFO)"
@click.command()
@click.option("-l", '--language',
              type=click.Choice(['python', 'angular'], case_sensitive=False), required=True)
@click.option("-v", "--version", required=True)
@click.option("-f", "--file", required=True, help="Path to file relative to the project root directory.")
def set_version(language: str, version: str, file: str):
    print(f"{language=}, {version=}")
    if "python" == language:
        setup_python(version, file)


cli.add_command(set_version)
