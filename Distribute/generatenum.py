class GenerateOrder(object):
    normal_number = 0   #类变量
    vip_number = 0  # 类变量

    @classmethod
    def getnormalorder(cls,length,header):
        if cls.normal_number == 10**length-1:
            cls.normal_number=0
        else:
            cls.normal_number += 1

        snum = str(cls.normal_number)
        while len(snum) < length:
            snum = '0' + snum

        return header + snum

    @classmethod
    def getviporder(cls,length,header):
        if cls.vip_number == 10**length-1:
            cls.vip_number=0
        else:
            cls.vip_number += 1

        snum = str(cls.vip_number)
        while len(snum) < length:
            snum = '0' + snum

        return header + snum
