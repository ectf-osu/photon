import ctypes
from pathlib import Path


def photon128(msg: bytes):
    hash = bytes(16)
    lib = ctypes.cdll.LoadLibrary(str((Path(__file__).parent / "photon.so").absolute()))
    lib.photon128(msg, len(msg), hash)
    return hash


if __name__ == "__main__":
    print(photon128(b"msg"))
