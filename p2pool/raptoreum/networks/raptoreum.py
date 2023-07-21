import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = '72746d2e'.decode('hex')
P2P_PORT = 10226
ADDRESS_VERSION = 60
SCRIPT_ADDRESS_VERSION = 16
RPC_PORT = 10225
RPC_CHECK = defer.inlineCallbacks(lambda raptoreumd: defer.returnValue(
            (yield helper.check_block_header(raptoreumd, '5c7aad59fd281029fba98b04a362d84843e579590e367f9cb0bbb3f9b6ee062b')) and
            (yield raptoreumd.rpc_getblockchaininfo())['chain'] == 'main'
        ))
BLOCKHASH_FUNC = lambda data: pack.IntType(256).unpack(__import__('raptoreum_hash').getPoWHash(data))
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('raptoreum_hash').getPoWHash(data))
BLOCK_PERIOD = 150 # s
SYMBOL = 'RTM'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'DashCore') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/DashCore/') if platform.system() == 'Darwin' else os.path.expanduser('~/.raptoreumcore'), 'raptoreum.conf')
BLOCK_EXPLORER_URL_PREFIX = 'https://explorer.raptoreum.com/block/?'
ADDRESS_EXPLORER_URL_PREFIX = 'https://explorer.raptoreum.com/address/?'
TX_EXPLORER_URL_PREFIX = 'https://explorer.raptoreum.com/tx/?'
SANE_TARGET_RANGE = (2**256//2**32//1000000 - 1, 2**256//2**32 - 1)
DUST_THRESHOLD = 0.001e8
