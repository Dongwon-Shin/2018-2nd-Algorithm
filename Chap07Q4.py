import re


data = """
kim,fail,fail
shin,pass,fail
"""
pat = re.compile("(\w{3}[,]\w{4})[,]\w{4}")
print(pat.sub("\g<1>,pass", data))