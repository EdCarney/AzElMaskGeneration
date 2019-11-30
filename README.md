# Overview
This script creates azimuth-elevation mask files for clamshell-stype encolsures. The mask files are based on AGI's STK *.aem format.

# Setup
## Prerequisites
This tool is written in Python 2.7 and published on GitHub as a private repository. As such, both Python 2.7 and Git are required to access and run the tool. The latest official Python 2.7 version can be downloaded from [here](https://www.python.org/downloads/release/python-2717/ "Python"); most Windows machines will use the `Windows x86 MSI installer` download. The latest Git version can be downloaded from [here](https://git-scm.com/downloads "Git"). The default install instructions can be used for both installations.

MATLABs Python library is used to support plotting the azimuth-elevation values (primarily for debugging). Execute the following commands in a PowerShell terminal to install this Python library.
```
pip install matplotlib
```

## Cloning the Repo
Execute the following command in a powershell terminal to clone the git repository containing the necessary scripts.
```
git clone https://github.com/EdCarney/AzElMaskGeneration.git
```

# Using the Script
## Configuration
The script is configured via the `config.xml` file located in the `conf` directory. This file is used to set the following parameters:
* **Pivot Azimuth**: The orienation of the clamshell roof shutter hinge. This is measured in degrees clockwise from North.
* **Right Shutter Elevation**: The elevation of the right shutter measured in degrees. 'Right' is defined as the eastern shutter for a pivot azimuth of zero. An elevation of zero corresponds to the shutter being completely open; an elevation of 90 degrees corresponds to the shutter beign completely closed (i.e. vertical).
* **Left Shutter Elevation**: The elevation of the left shutter measured in degrees. 'Left' is defined as the western shutter for a pivot azimuth of zero. An elevation of zero corresponds to the shutter being completely open; an elevation of 90 degrees corresponds to the shutter beign completely closed (i.e. vertical).
* **Output File Name**: The name of the azimuth-elevation file that will be created by the script.

The below example demonstrates the right and left shutter elevations for a pivot azimuth of zero. 

![Zero Pivot Angle Example -thumbnail][zero_pivot_angle]

The below example demonstrates a nonzero pivot azimuth case. 

![Non-Zero Pivot Angle Example][nonzero_pivot_angle]

## Use
To execute the script, run the `createMask` Batch file. The azimuth-elevation file will be created in the top-level directory for the repository.


[zero_pivot_angle]: images\zero_pivot_angle.png#thumbnail "Zero Pivot Angle"
[nonzero_pivot_angle]: images\nonzero_pivot_angle.png "Non-Zero Pivot Angle"