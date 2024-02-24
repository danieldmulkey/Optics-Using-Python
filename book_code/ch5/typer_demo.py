import typer

from paraxial import materials

app = typer.Typer()

@app.command()
def index(glass: str, wavelength: float):
    glass_fct = getattr(materials, glass)
    typer.echo(glass_fct(wavelength))


if __name__ == "__main__":
    app()
