class Data:
    def __init__(self, v):
        self.w = v

    @staticmethod
    def control(obj, data):
        z = "".join(str(data).split("-"))
        if len(z) != 8:
            return f"\n*** Incorrect data entered: {z}"
        d, m, y = int(z[:2]), int(z[2:4]), int(z[4:8])
        if d <= 0 or d > 31:
            print(f"\n*** Incorrect day entered: {d}")
        if m <= 0 or d > 12:
            print(f"\n*** Incorrect month entered: {m}")
        if len(str(y)) != 4 or y == 0:
            print(f"\n*** Incorrect year entered: {y}")
        return f"\nDate check completed !"

    @classmethod
    def unfold(cls, data):
        try:
            v = "".join(str(data).split("-"))
            print(f"\nUnfolded data:\nday = {int(v[:2])}\nmonth = {int(v[2:4])}\nyear = {int(v[4:8])}")
        except:
            print("\n*** Input data format error ! ")


dat = "12-04-1961"
print("\nInput date:", dat)
My_Data = Data(dat)
print(Data.control(Data.unfold(dat), dat))