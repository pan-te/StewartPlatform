# coding=utf-8
# Testowe GUI do biblioteki stewart.py

from tkinter import *
from tkinter import ttk
import stewart as mt


def inverseCalculate(*args):
	jawsLengthInputF = [None] * 6
	for i in range(6):
		jawsLengthInputF[i] = float(jawsLengthInput[i].get())
	resultPlane = mt.inverseTransform(mt.Base(baseA, baseB), mt.Platform(platformA, platformB, thickness), jawsLengthInputF, 10, 10)
	planeCoordinatesOutput.set((resultPlane.position.x, resultPlane.position.y, resultPlane.position.z, resultPlane.rotation.x, resultPlane.rotation.y, resultPlane.rotation.z))


baseA = 2000.0
baseB = 100.0
platformA = 1600.0
platformB = 100.0
thickness = 100.0

root = Tk()

jawsLengthInput = [StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar()]
jawsLengthOutput = [StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar()]
planeCoordinatesInput = [[StringVar(), StringVar(), StringVar()], [StringVar(), StringVar(), StringVar()]]
planeCoordinatesOutput = StringVar()

root.title("Stewart GUI")
mainframe = ttk.Frame(root, padding = "3 3 12 12")
mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

jackEntry0 = ttk.Entry(mainframe, width = 32, textvariable = jawsLengthInput[0]).grid(column = 1, row = 2)
jackEntry1 = ttk.Entry(mainframe, width = 32, textvariable = jawsLengthInput[1]).grid(column = 1, row = 3)
jackEntry2 = ttk.Entry(mainframe, width = 32, textvariable = jawsLengthInput[2]).grid(column = 1, row = 4)
jackEntry3 = ttk.Entry(mainframe, width = 32, textvariable = jawsLengthInput[3]).grid(column = 1, row = 5)
jackEntry4 = ttk.Entry(mainframe, width = 32, textvariable = jawsLengthInput[4]).grid(column = 1, row = 6)
jackEntry5 = ttk.Entry(mainframe, width = 32, textvariable = jawsLengthInput[5]).grid(column = 1, row = 7)

planeOutput = ttk.Label(mainframe, textvariable = planeCoordinatesOutput)
planeOutput.grid(column = 1, row = 8)

inverseCalculateButton = ttk.Button(mainframe, text = "Calculate", command = inverseCalculate)
inverseCalculateButton.grid(column = 1, row = 9)

jackOutput = ttk.Label(mainframe, textvariable = jawsLengthOutput)
jackOutput.grid(column = 2, row = 3)

root.mainloop()