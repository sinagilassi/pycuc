# 🧪 PyCUC

[![PyPI Downloads](https://static.pepy.tech/personalized-badge/pycuc?period=monthly&units=INTERNATIONAL_SYSTEM&left_color=GREY&right_color=GREEN&left_text=downloads%2Fmonth)](https://pepy.tech/projects/pycuc)
![PyPI](https://img.shields.io/pypi/v/PyCUC)
![Python Version](https://img.shields.io/pypi/pyversions/PyCUC.svg)
![License](https://img.shields.io/pypi/l/PyCUC)

PyCUC is a Python unit-conversion package for chemical and process engineering.

| Use case | API | Best for |
| --- | --- | --- |
| General dimensional conversion | `pycuc.from_to()` | Equation outputs and compound engineering units |
| Fixed-reference conversion | `pycuc.convert_from_to()` / `pycuc.to()` | Legacy categories and absolute temperature |
| Custom conversion tables | `pycuc.go()` | Project-specific YAML unit tables |

## 🚀 Start here

```python
import pycuc

pycuc.from_to(1, "kg.m/s^2", "N")              # 1.0
pycuc.from_to(1, "kJ/(mol.K)", "J/(mol.K)")    # 1000.0
pycuc.convert_from_to(25, "C", "K")             # 298.15
```

Use [Quick start](quickstart.md) to choose an API.  Then see
[Dimensional conversion](dimensional-conversion.md),
[Legacy conversion](legacy-conversion.md), or [Custom units](custom-units.md)
for the appropriate workflow.
