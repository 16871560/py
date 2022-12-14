# -*- coding: utf-8 -*-
import requests, time

url = "https://api.github.com/repos/AleoHQ/snarkOS"

class Autocheck_repos():
    def __init__(self, repos):
        self.repos = repos

    def get_newest(self):
        try:
            ret = requests.get(self.repos)
            if ret.status_code == 200:
                ret = ret.json()
            else:
                raise Exception("请求频率过高")
        except Exception as e:
            raise e
        update = ret['updated_at']
        # str="2022-12-13T01:11:16Z"
        tmp = time.strptime(update, "%Y-%m-%dT%H:%M:%S%z")
        update_time = time.mktime(tmp)
        return str(update_time)

    def op(self, new_version):
        if new_version:
            # print("需要更新")
            with open("./update.txt", "w") as f:
                f.write(new_version)
        else:
            print("已经是最新。。。。")
            pass

    def cmp_version(self, new_version: object) -> object:
        with open("./update.txt", "r") as f:
            tmp = f.readline().strip()
            if tmp != new_version:
                return new_version
            else:
                return 0


        # 实现更新逻辑

    def run(self):
        newest = self.get_newest()
        update = self.cmp_version(newest)
        if update:
            print("需要更新")
            self.op(newest)
        else:
            print("已经是最新版")

if __name__ == '__main__':
    aleo = Autocheck_repos(url)
    aleo.run()
