# Ввод данных
n = int(input("Введите номер студента: "))
α = int(input("Введите α: "))
β = int(input("Введите β: "))
γ = int(input("Введите γ: "))
δ = int(input("Введите δ: "))

m = int((n + δ)/2) + 1
l = int((α + β + γ + δ)/5) + 1

LenVec_a = m+1
LenVec_b = l+1

Vec_c = f"{m-5}a + {(-1)**n}b"
Vec_d = f"{l+(-1)**n+2}a + b"

# Пункт a
ScalarProduct = 0
ScalarProductStroka = f"{(m-5)*(l+(-1)**n+2)}a*a + {(m-5)}a*b + {(-1)**n*(l+(-1)**n+2)}b*a + {(-1)**n}b*b"

print(f"c = {Vec_c}")
print(f"d = {Vec_d}")
print(f"c*d = {ScalarProductStroka}")

ScalarProductStroka = ScalarProductStroka.replace("a*a", f"*{LenVec_a**2}").replace("b*b", f"*{LenVec_b**2}").replace("b*a", "a*b").replace("a*b", f"*{LenVec_a*LenVec_b/2}")
ScalarProductList = ScalarProductStroka.split(" + ")
print(f"= {ScalarProductStroka}")

for i in ScalarProductList:
    i = i.split("*")
    ScalarProduct += float(i[0])*float(i[1])

print(f"= {ScalarProduct}")

# Пункт b