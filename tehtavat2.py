print("hei, maailma!")
print('"hei!", sanoi Ville')
print("hyvää")
print("huomenta")
print("hyvää\nhuomenta")
kayttaja = input('anna nimesi:')
print("hauska tavata", kayttaja+"!")
print(kayttaja)

eka=-9
toka=12_456_123_180
kolmas=4.973
neljäs=-4+2j
print(eka)
print(toka)
print(kolmas)
print(neljäs)
print(neljäs.real)
print(neljäs.imag)

fahrenheit_str=input("anna lämpötila fahrenheit-asteina:")
fahrenheit=float(fahrenheit_str)
celsius=(fahrenheit-32)*5/9
print("lämpötila celsius-asteina:"+str((celsius)))

print(f"lämpötila celsius-asteina:{celsius:6.2f}")
print(f"lämpötila celsius-asteina:{celsius}")
import math
print(f"{'pii':12s}:{math.pi:10.5f}")
print(f"{'neeperin luku':12s}:{math.e:10.5f}")
