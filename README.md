# [TUT](https://www.youtube.com/watch?v=rfscVS0vtbw)


[CONDA CHEATSHEET](https://docs.conda.io/projects/conda/en/latest/_downloads/843d9e0198f2a193a3484886fa28163c/conda-cheatsheet.pdf)

```
conda create -n learn-python python=3.12

conda activate learn-python

conda list
conda search python

conda list -e > requirements.txt
conda install --file requirements.txt

conda remove -n learn-python --all
conda deactivate
```