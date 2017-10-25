# Setups
### Matplotlib in pyenv
Open python shell

```
import matplotlib
print(matplotlib.matplotlib_fname())
```
Close python shell

```
vi path/to/matplotlibrc
```
Find backend

```
backend      : macosx
```
Replace backend

```
backend      : Tkagg
```
### Ipython shell for pyspark
Create script path and file

```
mkdir /path/to/.scripts
vi ipyspark.sh
```
Save below

```
#!/bin/bash
export PYSPARK_DRIVER_PYTHON=ipython

${SPARK_HOME}/bin/pyspark
```
Change permission

```
chmod 711 ipyspark.sh
```
Open bash_profile

```
export PATH=$PATH:/path/to/.scripts
alias ipyspark="bash /path/to/.scripts/ipyspark.sh"
```
