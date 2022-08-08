# Not every thing is declared
# Only what was needed or what we though we needed at some point
from enum import IntEnum
class Mechanism(IntEnum):
    PCA2_DERIVE_CRX = 0x00000804
    PCA4_DERIVE_MASTER_KEY = 0x00000805
    SAVE_RESTORE_KEY = 0x00000806
    PCA4_DERIVE_VPNC = 0x00000807
    PCA4_DERIVE_VPNC_AES = 0x00000808
    AES_CMAC_DERIVE = 0x00000810
    VERIFY_SHA512_ECC512 = 0x0000080B
    ECDSA_SHA256 = 0x00001000
    ECDSA_SHA384 = 0x00001001
    ECDSA_SHA512 = 0x00001002
    ECKCDSA_KEY_PAIR_GEN = 0x00001010
    ECKCDSA = 0x00001020
    SOFTWARE_SIGN = 0x00001030


class KeyType(IntEnum):
    ECC_KCDSA = 0x00001000