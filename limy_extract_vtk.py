import vtk
import numpy as np
import os
import glob
import math
import vtk
datapaths = glob.glob(os.path.expanduser("~")+'/src/negtrainsamples/*/')


#vtkpath = glob.glob('../DATA/Case  033/NRRD/Manual_CY/manual*.vtk')

def extract(filename):
    reader = vtk.vtkPolyDataReader()
    reader.SetFileName(filename)
    reader.Update()
    polydata = reader.GetOutput()
    temp = []
    m=polydata.GetNumberOfCells()
    print("cellnum:" + repr(m))
    for i in range(m):
        pts = polydata.GetCell(i).GetPoints()
        n=pts.GetNumberOfPoints()
        print("pointnum:"+ repr(n))
        num = 0
        for j in range(n):
            num += 1
            if num <= 100:
                temp.append(pts.GetPoint(j))
    temp = np.array(temp)
    print(temp.shape)
    return temp

#res = np.load('path.save')
for datapath in datapaths:
    vtkpath = glob.glob(datapath+'*.vtk')
    if not vtkpath:
        continue
    savename='case'+datapath[-4:-1]+'vtk-neg.save'
    final = []
    for filename in vtkpath:
        print(filename)
        final.append(extract(filename))
    print(np.shape(final))
    f = open(savename, 'wb')
    np.save(f, final)
    f.close


# i = 0
# res = glob.glob('../DATA/**/manual*.vtk', recursive=True)
# for filename in res:
#     print(filename)
#     # extract(filename)
#     i += 1
# print(i)
# f = open('path.save', 'wb')
# np.save(f, res)
# f.close

