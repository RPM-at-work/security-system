import typer
from rich import print

from server.api.backend.interface import ServerAPI
from server.security_server.config import BackendConfig

app = typer.Typer()
bc = BackendConfig(
    **{
        "host": "localhost",
        "port": 50051,
    }
)

api = ServerAPI(**bc.model_dump())


@app.command()
def add_db(name: str, email: str):
    api.say_hello(name=name, email=email)


@app.command()
def hello(name: str):
    print(f"Hello {name}")


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")


if __name__ == "__main__":
    app()
