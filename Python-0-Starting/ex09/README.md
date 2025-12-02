This is an example package to learn how to create Python packages.

After creating these files:
    -src/ft_package/__init__.py
    -src/ft_package/ft_package.py
    -tests/
    -LICENCE
    -pyproject.toml
    -README.md

Having added the metadata to pyproject.toml and filled MIT Licence, write these commands:

sudo apt install python3-build (local env)
OR
python3 -m pip install --upgrade build (venv)

Then:
python3 -m build

It creates a venv in which the dist/ directory is created, with two files added : ft_package-0.0.1.tar.gz and ft_package-0.0.1-py3-none-any.whl.

Some other files such as PKG-INFO, dependency_links.txt, SOURCES.txt and top_level.txt are created.

In the venv, run the command
pip install ./dist/ft_package-0.0.1.tar.gz
OR
pip install ./dist/ft_package-0.0.1-py3-none-any.whl

The package will be installed and can be imported in scripts