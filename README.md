create env

```bash
conda create -n wineq python=3.7 -y
```
activate env

```bash
conda activate wineq
```

created a req file
install the req

```bash
pip install -r requirements.txt
```

Create template.py for the template AND Run it.

```bash
python template.py
```
download the data from
https://drive.google.com/drive/folders/18zqQiCJVgF7uzXgfbIJ-04zgz1ItNfF5?usp=sharing

Create data_given folder for incoming data source from remote location and copy the data from above drive link

```bash
mkdir data_given
```

```bash
git init
```

```bash
dvc init
```
If getting error in python 3.7 after above command i.e dvc init then perform below steps
ImportError: cannot import name 'fsspec_loop' from 'fsspec.asyn'

```bash
pip uninstall fsspec
pip install fsspec==2022.7.1
```

```bash
dvc add data_given/winequality.csv
```

```bash
git add .
```

```bash
git commit -m "first commit"
```
oneliner updates for readme

```bash
git add . && git commit -m "update Readme.md"
```

```bash
git remote add origin https://github.com/shyam8898/simple-dvc-demo.git
git branch -M main
git push origin main
```

DVC Reproduce

```bash
dvc repro
```
To show metrics using DVC command

```bash
dvc metrics show
```
To show metrics differences between old and new using DVC command

```bash
dvc metrics diff
```

tox command -

```bash
tox
```

tox command for creating/initialization

```bash
touch tox.ini
```

for rebuilding -

```bash
tox -r
```
pytest command

```bash
pytest -v
```
setup commands -

```bash
pip install -e .
```
build your own package commands-

```bash
python setup.py sdist bdist_wheel
```