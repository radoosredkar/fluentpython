from vectorV3 import Vector3d
import sentry_sdk
sentry_sdk.init("https://302785b4cd2a4d8191b6d136ad403db8@sentry.io/2550028")

vector = Vector3d([x for x in range(10)])
print(vector)
print(-vector)

vector1 = Vector3d([x for x in range(12)])
print(vector + vector1)
print(vector + (1, 2, 3))
print((1, 2, 3) + vector)
# print(1 + vector) # throws error, see implementation
print(vector1 * 22)
print(20 * vector)
# print("x" * vector) # throws error, see implementation

# Comparisons
print()
print()
print()
print()
print()
print()
print("COMPARISONS OF VECTORS")
va = Vector3d([1.0, 2.0, 3.0])
vb = Vector3d(range(1, 4))
print(va, vb)
vc = (1, 2, 3)

print(va==vb)
print(va==vc)
