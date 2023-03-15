import nox


@nox.session
@nox.parametrize("django", ["3.2", "4.0", "4.2b1", "main"])
def test(session, django):
    if django == "main":
        session.run("pip", "install", "https://github.com/django/django/archive/main.tar.gz")
    else:
        session.run("pip", "install", f"django=={django}")
    session.run("python", "makemigrations.py")
    session.run("coverage", "run", "runtests.py", external=True)
    session.run("coverage", "report", external=True)
    session.run("coverage", "xml", external=True)
