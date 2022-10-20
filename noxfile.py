import nox


@nox.session
@nox.parametrize("django", ["3.2", "4.0", "main"])
def test(session, django):
    if django == "main":
        session.install("pip", "install", "https://github.com/django/django/archive/main.tar.gz")
    else:
        session.install("pip", "install", f"django=={django}")
    session.run("python", "makemigrations.py")
    session.run("coverage", "run", "runtests.py", external=True)
    session.run("coverage", "report", external=True)
    session.run("coverage", "xml", external=True)
