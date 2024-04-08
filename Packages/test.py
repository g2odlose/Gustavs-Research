import sys
sys.path.insert(0, '../ArtifactCalculate')
from ArtifactCalculate import ArtifactCalculator as ac

a01 = ac.ArtifactObject(0, 2, "Магнитные волны", False, 101)
a11 = ac.ArtifactObject(1, 1, "Магнитные волны", False, 111)
a12 = ac.ArtifactObject(1, 3, "Магнитные волны", False, 112)
a21 = ac.ArtifactObject(2, 1, "Магнитные волны", False, 121)
a22 = ac.ArtifactObject(2, 1, "Магнитные волны", False, 122)

a = ac.Artifact(1)

a.addObject(a01)
a.addObject(a11)

print(a.depend)
print("\n")

a01.info()
a11.info()
a12.info()
a21.info()
a22.info()

a.info()
