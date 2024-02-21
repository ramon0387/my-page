import math

pH = float(input("pH = "))
ka = float(input("Ka = "))
A = float(input("[A-] = "))
HA = float(input("[HA] = "))
m_A = float(input("Molec mass of A- = "))
m_HA = float(input("Molec mass of HA = "))
vol = float(input("Volume = "))            # vol [=] L
assay_A = float(input("Assay of A- = "))   # Expressed in fraction
assay_HA = float(input("Assay of HA = "))   # Expressed in fraction


pka = -math.log10(ka)
y = pH - pka
rel = 10**y
mass_A = (rel * A * m_A * vol)/(assay_A)
mass_HA = (A * m_HA * vol)/(assay_HA)

print(f'----------------------------')
print(f'[A-/HA] = {rel:.4f} moles')
print(f'----------------------------')
print(f'mass of A- = {mass_A:.4f} g')
print(f'mass of HA = {mass_HA:.4f} g')
