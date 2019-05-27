#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Power by HPCM 2019-05-17 20:26:34
# Filename 01-get_io_count.py
import requests

url = "https://passport.baidu.com/v2/api/?login"

data = {
    "staticpage": "http://i.baidu.com/v3Jump.html",
    "charset": "UTF-8",
    "token": "705d2cbdcfd61a84afe108d537c242f4",
    "tpl": "uc",
    "subpro": "",
    "apiver": "v3",
    "tt": "1558097572985",
    "codestring": "",
    "safeflg": "0",
    "u": "http://i.baidu.com",
    "isPhone": "false",
    "detect": "1",
    "gid": "34A3FD2-ADE6-4025-B1BF-083DBEDA1B7D",
    "quick_user": "0",
    "logintype": "dialogLogin",
    "logLoginType": "pc_loginDialog",
    "idc": "",
    "loginmerge": "true",
    "splogin": "rate",
    "username": "565956231@qq.com",
    "password": "lfXm/H0k5HSwVFHLkJdXczAmBu239Bck1HSq4d7meln7VTv7hpHWiP6miZX0U1Qu/OXFNLkgWh7M6sjClMG2cIx5vnlQGoHUWCN6jEsVDENsFdFTUnF0SdJsFgyArz1UIluH6nbIvkalhsZO6P3mh0EvYgaXpn4nbjO7++gKmoI=",
    "mem_pass": "on",
    "rsakey": "0pEcElZX3JsuFH9ACexUfV3cbEVFR8rR",
    "crypttype": "12",
    "ppui_logintime": "33301",
    "countrycode": "",
    "fp_uid": "",
    "fp_info": "",
    "ds": "VpIrvEovmRLQJnpm3HM3CyUrwHi9Pi9bBQ3ZJ6ePZXmp4HRtdow+B9/rFUVStw5lEEVHqP3B3fqR6AwB5vTcBLMPCubcK/l08DBtUZE3l00f14Sz4eUO+g3WZi4NfOnU4SQjaiHWntgvlKDpG7e9Zs6k++sQ8B7Exd8lq1BmWBODWsGEDhvYvO6shdS/bJfqIQiYajALSBeqaGlmjrCcD21+fGZxm68hTs3AZ+GnDRJ6wRlsyAj2Uelqf09FSQhe7doacFFEy8Eb2mPwVyecAsPojlbe4iFSLNIsJfr0R17ubjLI0Lou30dzql3ggPSxvS3j7+Bgnm+lIuYuKsbxklzTkjt7QiwBhvRRviJqguJLDuoJ5iMnxo5hHAEypqiKga6OTQT+2kdfA/+rQEdUXwK8NyVs5i8n23generrMMVXb+lDUA3jUkmxwaVDuQokLpNQsrIxUKrmAiNCQ+D4SG08RQiUen0xmlF+CSrNlbECOI81/pmzuRgxE7CULFvGmJNHlun5daiz+WlJfetlC4Z/77ep56ZkBt+aYJ6RHEPhpgd4HuckOwYALSTpt1ZeSl2LcvbXt4FQFTIq331H5d1jcTAI8EZSShF3TNAnc5Rei/LhRqc5b86has375ovlq2YZl6/1/V0FJQhw8eZB9RbU5HA3ROyRblgZJkPDGvOKkNGjpWxsXk9j9IBU3htthRWKVJHtJXg7Kh/ey5yiLvGBsVI0Dzl22TGWo31Bh9LjXdEcUxB9qIGM1gou+3HbGOhvNSpJc1rlZzyLmy4Kh67zQeN1x030oDrjtGjOqArinaMHq1GhkS6MigbyE3NQ",
    "tk": "8035wFzzGVROwJ+YqFpPavRfLn8JJw5HggJId9M1zP5LVw9Ay0I68zH2vnHnvAqHva5Q",
    "dv": "tk0.36947188778395181558097539928@oom0wkAkqYMUHYMmgy8OGaAkqYHpsBrynhEHdoIsC6JzpgJydg2JCzPZdRGmgz8Etgoq__qm0hzBE6~Ak6gCRgVCEpyAsrhE3P96IyoJyhEIsaV8sdoFvszFxPiF5raBE8RAk8~Bmgl8E3eAsrhE3P96IyoJyhEIsaV8sdoFvszFxPiF5raBk8xAk6lC9gy8k6~AsrhE3P96IyoJyhEIsaV8sdoG5dRMJg~CO8Y8z2ZAkI~8ztYHpsBrynhEHdoIsC6JzpgJydyFZHRE5sfGJgZCEFYCE2VAktlCzI~A0g_zkkDIkukbKxFhumh89gRAkFl-mrPvYgAO8ZBE6x8ENeCzFe8z3y8ENVCEIe8k3xCE8~BEtehmvD0rlFkXiAZ3j25sQG0Ij2ZdfAxPSMvCiMLIiA0HjGvH5DL~SGq__xmv8mggAkpeBEIY8E6lCRgVBEtgAkpgBkqY8E3R8mgVBEtgAkpgCkq_",
    "extrajson": "",
    "traceid": "3C7DB001",
    "callback": "parent.bd__pcbs__k6t0nh"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
    "Host": "passport.baidu.com",
    "Origin": "http://i.baidu.com",
    "Referer": "http://i.baidu.com/welcome/",
    "Content-Type": "application/x-www-form-urlencoded",
    "Content-Length": "2248",
    "Cookie": "BAIDUID=4296046C002606DDB6DED01A5ADB4182:FG=1; BIDUPSID=4296046C002606DDB6DED01A5ADB4182; PSTM=1550713766; MCITY=-340%3A; HOSUPPORT=1; UBI=fi_PncwhpxZ%7ETaJc6tARV41j-0xl98W2VVSobwQRe1%7EZtXPy6PUN6uq26ugrWh98CQQF0c4piUhh%7Eu7H9hX; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=1467_28804_21079_18559_29064_28519_28768_28720_28964_28832_28584_26350_22158; delPer=0; PSINO=7; ZD_ENTRY=baidu; USERNAMETYPE=2; SAVEUSERID=e9c2ae6818c96037e33768b842dda99f526904d8; HISTORY=7856ebdb9b0beac3768b46157eea4156157033ea3a89f57001a8553ef9a001da5088a1eae1c1; pplogid=8035wFzzGVROwJ%2BYqFpPavRfLn8JJw5HggJId9M1zP5LVw9Ay0I68zH2vnHnvAqHva5Q"
}

session = requests.Session()
req = session.post(url, headers=headers, data=data)
print(req.status_code)
print(req.content.decode("utf8"))
print(session.get("http://www.baidu.com").content.decode("utf8"))
