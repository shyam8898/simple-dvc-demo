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

git init
dvc init
dvc add -R data_given
