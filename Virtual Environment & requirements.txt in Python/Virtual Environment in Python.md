cond promt command:
conda create -n helmet python=3.9 -y

conda activate helmet

conda env list

conda remove --name helmet --all


terminal command:
conda create --prefix .\helmet python=3.9 -y

conda activate .\helmet

Requirements file install:
pip install -r requirements.txt