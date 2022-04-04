import matrixCreator
import bNb

initPTuple = matrixCreator.readFromFile()
initPTuple.printPuzzle()
bNb.checkIsSolvable(initPTuple)
bNb.moveTile(initPTuple, bNb.whereEmptyBlock(initPTuple), 'D').printPuzzle()