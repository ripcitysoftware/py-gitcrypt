#!/usr/bin/env python

import os
from pathlib import Path

import click

COMMANDS_DIR = "/opt/cloudmanager"
if not os.path.exists(COMMANDS_DIR):
    COMMANDS_DIR = Path.cwd()

plugin_folder = os.path.join(COMMANDS_DIR, "commands")

class CloudManagerCLI(click.MultiCommand):
    def list_commands(self, ctx):
        rv = []
        for filename in os.listdir(plugin_folder):
            if filename.endswith(".py"):
                rv.append(filename[:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        ns = {}
        fn = os.path.join(plugin_folder, name + ".py")
        with open(fn) as f:
            code = compile(f.read(), fn, "exec")
            eval(code, ns, ns)
        return ns["cli"]


def main():
    cli = CloudManagerCLI(
        help="CloudManager subcommands are loaded from the plugin folder dynamically."
    )

    cli()


if __name__ == "__main__":
    main()
