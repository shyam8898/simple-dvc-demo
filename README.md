create env 

```bash
conda create -n wineq python=3.7 -y
```
activate env
```bash
conda activate wineq
```
create requirements.txt file
install the requirements.txt file
```bash 
pip install -r requirements.txt
```
download the dataset from 
https://drive.google.com/drive/folders/18zqQiCJVgF7uzXgfbIJ-04zgz1ItNfF5

```bash 
git init
```
```bash 
dvc init
```

```bash 
dvc add -R data_given
```

```bash 
git add .
```

```bash 
git commit -m "first Commit" 
```

```bash 
git add . && git commit -m "update Readme.md"
```

```bash 
git remote add origin https://github.com/shyam8898/simple-dvc-demo.git
```

```bash 
git branch -M main
```

```bash 
git push -u origin main
```

tox command -
```bash
tox
```

for rebuilding -
``` bash
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
python setup.py sdist bdist wheel
```

Open jupyter lab
```bash
jupyter-lab notebooks/
```