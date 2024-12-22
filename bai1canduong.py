s = int(input())
giay = s
ngay = giay // 86400
giay =  giay % 86400
gio = giay // 3600
giay = giay % 3600
phut = giay // 60
giay = giay%60

print(s," giay thi co ",ngay," ngay", gio," gio ",phut," phut ",giay," giay")
