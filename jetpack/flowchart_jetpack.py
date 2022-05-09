from pyflowchart import Flowchart

with open("jetpack/main.py") as f:
    code = f.read()

fc = Flowchart.from_code(code)
print(fc.flowchart())
