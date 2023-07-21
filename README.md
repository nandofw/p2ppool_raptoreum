Requirements:
-------------------------
Generic:

* Raptoreumd >=0.17.0.0
* Python >=2.7
* Twisted >=13.0.0
* Zope.interface >=3.8.0
* pycrypto >= 2.6.1

Linux:

    sudo apt-get install python2 python2-dev python2-twisted python2-pip-whl python2-setuptools-whl
    sudo apt-get install gcc g++

Install Python modules:
-------------------------
Download the required submodules:

    git submodule init
    git submodule update

Raptoreum_hash:

    cd raptoreum_hash
    python setup.py install --user

Running P2Pool:
-------------------------
To use P2Pool, you must be running your own local raptoreumd. For standard
configurations, using P2Pool should be as simple as:

    python run_p2pool.py

Then run your miner program, connecting to 127.0.0.1 on port 7703 with any
username and password.

If you are behind a NAT, you should enable TCP port forwarding on your
router. Forward port 7777 to the host running P2Pool.

Run for additional options.

    python run_p2pool.py --help

Official wiki :
-------------------------
https://en.bitcoin.it/wiki/P2Pool

Alternate web front end :
-------------------------
* https://github.com/hardcpp/P2PoolExtendedFrontEnd
* https://github.com/johndoe75/p2pool-node-status
* https://github.com/justino/p2pool-ui-punchy

Sponsors:
-------------------------

Thanks to:
* The Bitcoin Foundation for its generous support of P2Pool
* The Litecoin Project for its generous donations to P2Pool
* The Vertcoin Community for its great contribution to P2Pool
* jakehaas, vertoe, chaeplin, dstorm, poiuty, elbereth  and mr.slaveg from the Darkcoin/Dash Community
