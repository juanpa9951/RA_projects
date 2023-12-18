from Classifier import ClassifierFunction
import time
PathSource=r"C:\Users\Maria del Carmen\OneDrive - Rewair A S\Inspección - Fotos\000. Original"
PathDestination=r"C:\Users\Maria del Carmen\OneDrive - Rewair A S\Inspección - Fotos"
PathLost=r"C:\Users\Maria del Carmen\OneDrive - Rewair A S\Inspección - Fotos\005. Lost"
start = time.time()
Locations=ClassifierFunction(PathSource,PathDestination,PathLost)
end = time.time()
ElapsedTime=end-start
print(" Execution time was ",ElapsedTime," seconds")