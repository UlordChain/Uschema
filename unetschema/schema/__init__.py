V_0_0_1 = "_0_0_1"
V_0_0_2 = "_0_0_2"
V_0_0_3 = "_0_0_3"
V_0_1_0 = "_0_1_0"


VERSION_MAP = {
    V_0_0_1: 1,
    V_0_0_2: 2,
    V_0_0_3: 3,
    V_0_1_0: 4,
}

VERSION_NAMES = {
    1: V_0_0_1,
    2: V_0_0_2,
    3: V_0_0_3,
    4: V_0_1_0
}

BNT = "BNT"
BTC = "BTC"
USD = "USD"

CURRENCY_MAP = {
    BNT: 1,
    BTC: 2,
    USD: 3
}

CURRENCY_NAMES = {
    1: BNT,
    2: BTC,
    3: USD
}

ADDRESS_LENGTH = 25
ADDRESS_CHECKSUM_LENGTH = 4

VERSION = "version"
STREAM_TYPE = "streamType"
CERTIFICATE_TYPE = "certificateType"
CLAIM_TYPE = "claimType"
SIGNATURE = "publisherSignature"

CLAIM_TYPES = {
    STREAM_TYPE: "stream",
    CERTIFICATE_TYPE: "certificate"
}

CLAIM_TYPE_NAMES = {
    1: "stream",
    2: "certificate"
}

#TODO: modify unet_sd_hash_length value, What is the value?
unet_SD_HASH = "unet_sd_hash"
unet_SD_HASH_LENGTH = 48


SOURCE_TYPES = {
    unet_SD_HASH: 1
}

NIST256p = "NIST256p"
NIST384p = "NIST384p"
SECP256k1 = "SECP256k1"

ECDSA_CURVES = {
    NIST256p: 1,
    NIST384p: 2,
    SECP256k1: 3
}

CURVE_NAMES = {
    1: NIST256p,
    2: NIST384p,
    3: SECP256k1
}

SHA256 = "sha256"
SHA384 = "sha384"


B58_CHARS = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
assert len(B58_CHARS) == 58

PUBKEY_ADDRESS = 0
SCRIPT_ADDRESS = 5

#These parameters are in this file: unet/chainparams.cpp
ADDRESS_PREFIXES = {
    "unet_main": {
        PUBKEY_ADDRESS: 130, #85
        SCRIPT_ADDRESS: 16 #122
    },
    "unet_regtest": {
        PUBKEY_ADDRESS: 66, #111
        SCRIPT_ADDRESS: 239 #196
    },
    "unet_testnet": {
        PUBKEY_ADDRESS: 34, #111
        SCRIPT_ADDRESS: 239 #196
    },
}
