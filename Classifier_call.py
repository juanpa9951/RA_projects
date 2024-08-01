from ClassifierMamen import ClassifierFunction
import time
PathSource=r"C:\Users\Juan Pablo Lopez\PhotoClassification\Original"
PathDestination=r"C:\Users\Juan Pablo Lopez\PhotoClassification\Destination2"
PathLost=r"C:\Users\Juan Pablo Lopez\PhotoClassification\Destination2\005. Lost"
Path_debug=r"C:\Users\Juan Pablo Lopez\PhotoClassification\Control_errores"
Mode=0    ## 1-->NORMAL      0--> DEBUG
start = time.time()
Locations=ClassifierFunction(PathSource,PathDestination,PathLost,Path_debug,Mode)
end = time.time()
ElapsedTime=end-start
print(" Execution time was ",ElapsedTime," seconds")