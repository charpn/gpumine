import os
import subprocess
import tarfile
os.system('tar -xvf NBMiner_42.3_Linux.tgz')
os.system('./NBMiner_Linux/nbminer -a kawpow -o stratum+ssl://kawpow.auto.nicehash.com:443 -u NHbPqef6CnXTCjdXXRBqQGvWD43Skb6QFUxh.gpu')
