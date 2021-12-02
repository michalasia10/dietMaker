import subprocess  # nosec

import click

from source.core.app import server


@click.group("Fast-api App manager")
def manage() -> None:
    pass


@manage.command(help="Run the web server")
def run_server() -> None:
    click.echo("-> Runnning the server")
    server.run()


@manage.group(help="Manage the database")
def database() -> None:
    # group to manage data base
    pass


@database.command(help="Make migration")
@click.option('-m', '--msg', default="autogenerate", help='Add a message, default=autogenerate')
def migration(msg: str) -> int:
    return subprocess.call(["alembic", "revision", "--autogenerate", "-m", f"{msg}"])  # nosec


@database.command(help="apply migration")
def migrate() -> int:
    return subprocess.call(["alembic", "upgrade", "head"])


if __name__ == "__main__":
    manage()
    database()