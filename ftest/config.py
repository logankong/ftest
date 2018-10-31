import sys
import importlib
import os

IMPLICITLY_WAIT = 3
WAIT = 4

app_path = os.path.realpath(sys._getframe(1).f_code.co_filename).split('<')[0]
if app_path.split(os.sep)[-2] == 'action':
    module = app_path.split(os.sep)[-3] + '.' + 'config'
    app_path = app_path[0:-7]
else:
    module = app_path.split(os.sep)[-2] + '.' + 'config'
sys.path.append(app_path)

configModule = importlib.import_module('config')
hasWait = hasattr(configModule, "WAIT")
if hasWait:
    WAIT = getattr(configModule, "WAIT")

hasImplicitlyWait = hasattr(configModule, "IMPLICITLY_WAIT")
if hasImplicitlyWait:
    IMPLICITLY_WAIT = getattr(configModule, "IMPLICITLY_WAIT")

hasDbHost = hasattr(configModule, "DB_HOST")
if hasDbHost:
    DB_HOST = getattr(configModule, "DB_HOST")
hasDbPort = hasattr(configModule, "DB_PORT")
if hasDbPort:
    DB_PORT = getattr(configModule, "DB_PORT")
hasDbUser = hasattr(configModule, "DB_USER")
if hasDbUser:
    DB_USER = getattr(configModule, "DB_USER")
hasDbPwd = hasattr(configModule, "DB_PWD")
if hasDbPwd:
    DB_PWD = getattr(configModule, "DB_PWD")
hasDbName = hasattr(configModule, "DB_NAME")
if hasDbName:
    DB_NAME = getattr(configModule, "DB_NAME")

hasTunnel = hasattr(configModule, "TUNNEL_FLAG")
if hasTunnel:
    TUNNEL_FLAG = getattr(configModule, "TUNNEL_FLAG")
hasSshHost = hasattr(configModule, "SSH_FORWARDER_HOST")
if hasSshHost:
    SSH_FORWARDER_HOST = getattr(configModule, "SSH_FORWARDER_HOST")
hasSshPort = hasattr(configModule, "SSH_FORWARDER_PORT")
if hasSshPort:
    SSH_FORWARDER_PORT = getattr(configModule, "SSH_FORWARDER_PORT")
hasSshUser = hasattr(configModule, "SSH_FORWARDER_USER")
if hasSshUser:
    SSH_FORWARDER_USER = getattr(configModule, "SSH_FORWARDER_USER")
hasSshPwd = hasattr(configModule, "SSH_FORWARDER_PWD")
if hasSshPwd:
    SSH_FORWARDER_PWD = getattr(configModule, "SSH_FORWARDER_PWD")
