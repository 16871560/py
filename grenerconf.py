# -*- coding: utf-8 -*-
import os

def  getfile(path,fname):

    with open(path+fname,"w") as f:

        with open("nginx.tpl","r") as tpl:

            ret=tpl.readlines()
            ret=''.join(ret)
            print(ret.format(port="80",servername="www.ben.com",
                             access_log="ben.log",
                             home="/ben",
                             proxy_port=8080))
            ret=ret.format(port="80",servername="www.ben.com",
                             access_log="ben.log",
                             home="/ben",
                             proxy_port=8080)
        f.write(ret)

if __name__ == '__main__':

    getfile(".","test.conf")


'''
server {{
    listen       {port};
    server_name  {servername};

    access_log  {access_log}  main;

    location / {{
        root   {home};
        index  index.html index.htm;
        proxy_pass http://127.0.0.1:{proxy_port};
    }}
}}
'''