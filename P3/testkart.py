# -*- coding: utf-8 -*-
from netCDF4 import Dataset
import numpy as np

norkyst_file = '/users/julie/Downloads/Norkyst-800m.nc'
fh = Dataset(norkyst_file, mode='r')
print(fh)
fh.close()

print("hei")