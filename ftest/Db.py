import pymysql
from sshtunnel import SSHTunnelForwarder
from ftest.config import *


class DB():
    def __init__(self):
        self.db_host = DB_HOST
        self.db_port = DB_PORT
        self.db_user = DB_USER
        self.db_pwd = DB_PWD
        self.db_name = DB_NAME

        if TUNNEL_FLAG == 1:
            try:
                SSH_FORWARDER_CONFIG = {
                    'ssh_address_or_host': (SSH_FORWARDER_HOST, SSH_FORWARDER_PORT),
                    'ssh_password': SSH_FORWARDER_PWD,
                    'ssh_username': SSH_FORWARDER_USER,
                    'remote_bind_address': (DB_HOST, DB_PORT)
                }

                self.ssh = SSHTunnelForwarder(**SSH_FORWARDER_CONFIG)
                self.ssh.start()
                self.db_host = '127.0.0.1'
                self.db_port = self.ssh.local_bind_port
            except:
                import traceback
                traceback.print_exc()
                print('SSHTunnelForwarder connect mysql error. ')

        SQL_Config = {
            'host': self.db_host,
            'port': self.db_port,
            'user': self.db_user,
            'passwd': self.db_pwd,
            'db': self.db_name,
            'charset': 'utf8',
            'cursorclass': pymysql.cursors.DictCursor,
        }

        try:
            self.conn = pymysql.Connect(**SQL_Config)
            self.cursor = self.conn.cursor()
        except:
            print('connect mysql error.')

    def insert(self, sqlString, *args):
        try:
            self.cursor.execute(sqlString, *args)
        except:
            print("insert failed.")

    def getOne(self, sqlString, *args):
        try:
            self.cursor.execute(sqlString, *args)
            data = self.cursor.fetchone()
            return data
        except:
            import traceback
            traceback.print_exc()
            print(sqlString + ' execute failed.')

    def getAll(self, sqlString, *args):
        try:
            self.cursor.execute(sqlString, *args)
            data = self.cursor.fetchall()
            return data
        except:
            import traceback
            traceback.print_exc()
            print(sqlString + ' execute failed.')

    def update(self, sqlString, *args):
        try:
            self.cursor.execute(sqlString, *args)
            self.conn.commit()
        except:
            print(sqlString + ' update failed.')

    def close(self):
        self.cursor.close()
        self.conn.close()
        if TUNNEL_FLAG:
            self.ssh.close()

    def __del__(self):
        self.close()


if __name__ == "__main__":
    db = DB('127.0.0.1', 3306, 'root', '123456', 'world')
    print(db.query("show tables;"))
