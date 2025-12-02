This is an example package to learn how to create **Python packages**.

First, let's create these files:
``` bash
    -src/ft_package/__init__.py
    -src/ft_package/ft_package.py
    -tests/
    -LICENCE
    -pyproject.toml
    -README.md
```

Having added the metadata to pyproject.toml and filled MIT Licence, let's run these commands:

``` bash
sudo apt install python3-build (local env)
```
OR
``` bash
python3 -m pip install --upgrade build (venv)
```

Then:
``` bash
python3 -m build
```

It creates the `dist/` directory, with two files added : `ft_package-0.0.1.tar.gz` and `ft_package-0.0.1-py3-none-any.whl`.

Some other files such as `PKG-INFO`, `dependency_links.txt`, `SOURCES.txt` and `top_level.txt` are created.

Then let's run:
``` bash
pip install ./dist/ft_package-0.0.1.tar.gz
```
OR
``` bash
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

The package will be installed and can be imported in scripts.
