import math

pH = float(input("pH = "))
ka = float(input("Ka = "))
m = float(input("ion molality = "))

z_cat = float(input("Cation charge number = ")) # cation charge of disociated conjugate base salt
z_ani = float(input("Anion charge number = ")) # cation charge of disociated conjugate base salt
z = float(input("A- charge number = ")) # Conjugated base charge 

pka = -math.log10(ka)
I = 0.5 ((m * z_ani**2) + (m * z_cat**2))
ifc = (0.509 * z**2)(1/I**-0.5)
y = pH - pka + ifc
rel = 10**y

print(f'----------------------------')
print(f'[A-]/[HA] = {rel:.4f} moles')
