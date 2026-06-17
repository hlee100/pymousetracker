
[![pymousetracker.png](https://i.postimg.cc/zBMCsTmM/pymousetracker.png)](https://postimg.cc/62r4R2pL)
---

[![Static Badge](https://img.shields.io/badge/pypi-v1.2.1-blue)
](https://pypi.org/project/pymousetracker/) ![Static Badge](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13%20%7C%203.14-blue) [![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

A simple mouse tracking, color picking, and macro generation utility that can either be run via the CLI or in an IDE.


## 🚀 Quick Start

#### Installation

```bash
pip install pymousetracker
```

**Requirements:** Python >= 3.10

#### CLI Command
```bash
cursor-toolbox
```


#### 🖱️ Mouse Position Tracker

Tracks the x and y position of your cursor on a monitor of any size and accuratly retuns the positional values. 

```python
from pymousetracker import CursorToolbox

mouse = CursorToolbox()

mouse.mousePositionTracker() 
```

#### 🖌️ Mouse Color Picker

Idenifites colors on your montior depending on where you position your cursor over and returning back the color values via RGB and HEX.

```python
from pymousetracker import CursorToolbox

mouse = CursorToolbox()

mouse.mouseColorPicker()
```

#### 🤖 Mouse Automation Builder

Lets you record a sequence of mouse clicks and automatically generate a ready-to-run Python macro script from them.

```python
from pymousetracker import CursorToolbox

mouse = CursorToolbox()

mouse.mouseAutomationBuilder()
```
    
## 📄 License

pymousetracker code is open-sourced under the [MIT](https://choosealicense.com/licenses/mit/) license.

