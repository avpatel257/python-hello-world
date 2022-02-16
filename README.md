Local Setup
---

Make sure you have `virtualenv` installed on your local.
If not run following command to install it:

```bash
pip install virtualenv
```

Where to store virtual environments?
---
While the tools allow you to put your virtual environments anywhere in the system, it is not a desirable thing to do. There are two options:

- Have one global place for them, like ~/virtualenvs.

- Store them in each project’s directory, like ~/git/foobar/.venv.

If you pick the global virtual environment store option, you can use the following short function (put it in .bashrc / .zshrc / your shell configuration file) to get a simple way to activate an environment (by running `workon foo`)

```bash
export WORKON_HOME=~/projects/python/virtualenvs

function workon {
    source "$WORKON_HOME/$1/bin/activate"
}
```


To create virtualenvironment:

```bash
python3 -m virtualenv $WORKON_HOME/python-hello-world
```

Activate virtualenv

```
workon python-hello-world
```

Any dependency you install going forward will be scoped to this environment.

```
pip install Flask

```

Generate requirements.txt

```
pip freeze --local > requirements.txt
```

Install from requirements.txt

```
pip install -r requirements.txt
```



