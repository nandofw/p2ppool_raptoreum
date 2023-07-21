from p2pool.raptoreum import networks

PARENT = networks.nets['raptoreum']
SHARE_PERIOD = 20 # seconds
CHAIN_LENGTH = 24*60*60//20 # shares
REAL_CHAIN_LENGTH = 24*60*60//20 # shares
TARGET_LOOKBEHIND = 100 # shares  //with that the pools share diff is adjusting faster, important if huge hashing power comes to the pool
SPREAD = 10 # blocks
IDENTIFIER = '7242ef345e1bed6b'.decode('hex')
PREFIX = '3b3e1286f446b891'.decode('hex')
COINBASEEXT = '2f5032506f6f6c2d524150544f5245554d2f'.decode('hex')
P2P_PORT = 10226
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 7777
BOOTSTRAP_ADDRS = ''.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-raptoreum'
VERSION_CHECK = lambda v: v >= 180000
