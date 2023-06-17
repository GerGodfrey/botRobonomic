
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
import os
import ipfshttpclient2
from robonomicsinterface import Account, Launch
from robonomicsinterface.utils import ipfs_qm_hash_to_32_bytes, web_3_auth
from substrateinterface import Keypair, KeypairType


