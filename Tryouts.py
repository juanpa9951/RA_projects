from ClassifierMamen import ClassifierFunction
import time
PathSource=r"C:\Users\Juan Pablo Lopez\PhotoClassification\Original"
PathDestination=r"C:\Users\Juan Pablo Lopez\PhotoClassification\Destination2"
PathLost=r"C:\Users\Juan Pablo Lopez\PhotoClassification\Destination2\005. Lost"
start = time.time()
Locations=ClassifierFunction(PathSource,PathDestination,PathLost)
end = time.time()
ElapsedTime=end-start
print(" Execution time was ",ElapsedTime," seconds")