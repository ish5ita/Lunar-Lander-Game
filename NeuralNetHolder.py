import math
class NeuralNetHolder:

    def __init__(self):
        super().__init__()
        l1=[5.375858474504515, 5.528924050311718]  
        l2=[5.924327476257799, 6.5949875164755305]
        l3=[22.08371751258704, 20.814984073370663]
        l4=[22.324123174624706, 21.399628802313014]
        bw=[40.61295059995353, 40.10483219480512]

        

    
    def predict(self, input_row):
        # WRITE CODE TO PROCESS INPUT ROW AND PREDICT X_Velocity and Y_Velocit
        x1,y1=input_row.split(',')
        x1=float(x1)
        y1=float(y1)
        l1=[5.375858474504515, 5.528924050311718]  
        l2=[5.924327476257799, 6.5949875164755305]
        l3=[22.08371751258704, 20.814984073370663]
        l4=[22.324123174624706, 21.399628802313014]
        bw=[40.61295059995353, 40.10483219480512]
        maxx1=616.286097
        minx1=-615.5545614
        maxy1=822.1557098
        miny1=65.15550651
        maxx2=7.978620027
        minx2=-5.525213636
        maxy2=6.071713323
        miny2=-6.49977737
        lamda=0.05

        x1=x1-(minx1)/maxx1-minx1
        y1=y1-(miny1)/maxy1-miny1
        v1=x1*l1[0]+y1*l2[0]
        v2=x1*l1[1]+y1*l2[1]
        h1=1/(1+(math.pow(math.e,(-lamda*v1))))
        h2=1/(1+(math.pow(math.e,(-lamda*v2))))
        vh1=h1*l3[0]+h2*l4[0]+bw[0]
        vh2=h1*l3[1]+h2*l4[1]+bw[1]
        x2=1/1+(math.pow(math.e,(-lamda*vh1)))
        y2=1/1+(math.pow(math.e,(-lamda*vh2)))
        X_Velocity=(x2*(maxx2-minx2)+minx2)
        Y_Velocity=(y2*(maxy2-miny2)+miny2)
        return Y_Velocity,X_Velocity
        pass
