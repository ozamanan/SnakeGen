import matplotlib.pyplot as plt
import random as rn, numpy as np
import NeuralNet as NN
initPop, mutRate, numGen, solLen, numWin = 100, 0.05, 250, 3, 10
curPop = np.random.choice(np.arange(-15,15,step=0.01),size=(initPop,solLen),replace=False)
nextPop = np.zeros((curPop.shape[0], curPop.shape[1]))
fitVec = np.zeros((initPop, 2))
for i in range(numGen):
    fitVec = np.array([np.array([x, np.sum(NN.costFunction(NN.X, NN.y, curPop[x].T))]) for x in range(initPop)])
    print("(Gen: #%s) Total error: %s\n" % (i, np.sum(fitVec[:,1])))
    plt.scatter(i,np.sum(fitVec[:,1]))
    winners = np.zeros((numWin, solLen))
    for n in range(len(winners)):
        selected = np.random.choice(range(len(fitVec)), numWin/2, replace=False)
        wnr = np.argmin(fitVec[selected,1])
        winners[n] = curPop[int(fitVec[selected[wnr]][0])]
    nextPop[:len(winners)] = winners
    duplicWin = np.zeros((((initPop - len(winners))),winners.shape[1]))
    for x in range(winners.shape[1]):
        numDups = ((initPop - len(winners))/len(winners))
        duplicWin[:, x] = np.repeat(winners[:, x], numDups, axis=0)
        duplicWin[:, x] = np.random.permutation(duplicWin[:, x])
    nextPop[len(winners):] = np.matrix(duplicWin)
    mutMatrix = [np.float(np.random.normal(0,2,1)) if rn.random() < mutRate else 1 for x in range(nextPop.size)]
    nextPop = np.multiply(nextPop, np.matrix(mutMatrix).reshape(nextPop.shape))
    curPop = nextPop
    best_soln = curPop[np.argmin(fitVec[:,1])]
    #if np.sum(NN.costFunction(NN.X, NN.y, best_soln.T))==0:
        #break
plt.ylabel('Total cost/err')
plt.xlabel('Generation #')
best_soln = curPop[np.argmin(fitVec[:,1])]
X = np.array([[0,1,1],[1,1,1],[0,0,1],[1,0,1]])
result = NN.runForward(X, best_soln.T)
print("Best Sol'n:\n%s\nCost:%s" % (best_soln,np.sum(NN.costFunction(NN.X, NN.y, best_soln.T))))
print("When X = \n%s \nhThetaX = \n%s" % (X, result,))
