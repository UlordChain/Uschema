import os

#I change version, but I dont knonw where is used. 
#This can have an impact if you make some judgments about the version.--lqp
__version__ = "0.0.1rc1"

BLOCKCHAIN_NAME_ENVVAR = "unetSCHEMA_BLOCKCHAIN_NAME"
if BLOCKCHAIN_NAME_ENVVAR in os.environ:
    if os.environ[BLOCKCHAIN_NAME_ENVVAR] in ['unet_main', 'unet_regtest',
                                              'unet_testnet']:
        BLOCKCHAIN_NAME = os.environ[BLOCKCHAIN_NAME_ENVVAR]
    else:
        raise OSError("invalid blockchain name: %s" % os.environ[BLOCKCHAIN_NAME_ENVVAR])
else:
    BLOCKCHAIN_NAME = "unet_main"
