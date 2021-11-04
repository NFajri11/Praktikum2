a=input("Masukan nilai a:")
b=input("Masukan nilai b:")
print("variable a=",a)
print("variable b=",b)
print("hasil penggabungan {1}&{0}=%s".format(a,b) %(a+b))

# Konvensi nilai variable 
a=int(a)
b=int(b)
print("hasil penjumlahan {1}&{0}%d".format(a,b) %(a+b))
print("hasil pembagian {1}/{0}%f".format(a,b) %(a/b))