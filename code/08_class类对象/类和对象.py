class clock:
    id = None
    price = None

    def sound(self):
        import winsound
        winsound.Beep(2000, 3000)

clo1 = clock()
clo1.id = 200210
clo1.price = "200$"

print(f"闹钟1的id为：{clo1.id},价格为:{clo1.price}")

# --------------------------------------------------------------
clo2 = clock()
clo2.id= 200211
clo2.price = "250$"
print(f"闹钟2的id为：{clo2.id},它的价格为：{clo2.price}")
print("响一声")
# clo1.sound()


