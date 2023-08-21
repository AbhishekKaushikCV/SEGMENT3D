## Environment bonnetal2 python = 3.7
- ### torch==1.1.0
```
conda install pytorch==1.1.0 torchvision==0.3.0 cudatoolkit=10.0 -c pytorch
```
- ### numpy== 1.19.2 (installing with torch by itself)

- ### scipy==0.19.1

```
was giving error with: pip install scipy==0.19.1,
so I installed it with pip install scipy

```
- ### vispy==0.5.3
```
installed with this command: pip install vispy==0.5.3
```

- ### tensorflow==1.13.1
```
installed with this command: pip install tensorflow==1.13.1.
getting error with this version: PROTOBUF ERROR

SOLVED BY UPGRADING TENSORFLOW:
Using this command: pip3 install --upgrade tensorflow

```

- ### opencv-contrib-python==4.1.0.25
```
installed with this command: pip install opencv-contrib-python==4.1.0.25
```
- ###  matplotlib==2.2.3
```
installed with this command: pip install matplotlib==2.2.3
```

- ### opencv-python==4.1.0.25
```
pip install opencv-python==4.1.0.25
```

- 
```
conda list cudnn
# packages in environment at /home/abhishek/anaconda3/envs/bonnetal2:
#
# Name                    Version                   Build  Channel
cudnn                     7.6.5                cuda10.0_0 
```

-


```
conda list cudatoolkit
# packages in environment at /home/abhishek/anaconda3/envs/bonnetal2:
#
# Name                    Version                   Build  Channel
cudatoolkit               10.0.130                      0 
```


##  Conda Commands:

```
conda env export -f environment.yml
conda create -n bonnetal --file environment.yml

conda --freeze-installed : To prevent existing packages from being updating when using the conda install command

```