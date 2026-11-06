from nodes import *
from visitor import *


def semanticVisitorRunner(result, STvis):
    #symboltable creation visitor
    
    #print(result)
    #undeclared variables
    unvis = UndeclaredVisitor(STvis.globalST, STvis.classSTS, STvis.functionSTS)
    result.STaccept(unvis)
    if unvis.errorCounter > 0:
        print('Total errors detected:', unvis.errorCounter)
        return
    

    #check if type nodes are a valid type, 
    vtV = ValidTypeVisitor(STvis.globalST, STvis.classSTS, STvis.functionSTS)
    result.STaccept(vtV)
    if vtV.errorCounter > 0:
        print('Total errors detected:', vtV.errorCounter)
        return
    

    writeVis = ValidWriteVisitor(STvis.globalST, STvis.classSTS, STvis.functionSTS)
    result.STaccept(writeVis)
    if writeVis.errorCounter > 0:
        print('Total errors detected:', writeVis.errorCounter)
        return
    

    typecheckvis = TypeCheckingVisitor(STvis.globalST, STvis.classSTS, STvis.functionSTS)
    result.STaccept(typecheckvis)
    if typecheckvis.errorCounter > 0:
        print('Total errors detected:', typecheckvis.errorCounter)
        return
    

    indexevalvis = IndexEvalVisitor(STvis.globalST, STvis.classSTS, STvis.functionSTS)
    result.STaccept(indexevalvis)
    if indexevalvis.errorCounter > 0:
        print('Total errors detected:', indexevalvis.errorCounter)
        return
    
    
    functionevalvis = FunctionCallVisitor(STvis.globalST, STvis.classSTS, STvis.functionSTS)
    result.STaccept(functionevalvis)
    if functionevalvis.errorCounter > 0:
        print('Total errors detected:', functionevalvis.errorCounter)
        return
    

    ifwhilevis = IfWhileCondVisitor(STvis.globalST, STvis.classSTS, STvis.functionSTS)
    result.STaccept(ifwhilevis)
    if ifwhilevis.errorCounter > 0:
        print('Total errors detected:', ifwhilevis.errorCounter)
        return
    

    paramvis = ParameterCheckingVisitor(STvis.globalST, STvis.classSTS, STvis.functionSTS)
    result.STaccept(paramvis)
    if paramvis.errorCounter > 0:
        print('Total errors detected:', paramvis.errorCounter)
        return
    

    switchvis = SwitchCaseVisitor(STvis.globalST, STvis.classSTS, STvis.functionSTS)
    result.STaccept(switchvis)
    if switchvis.errorCounter > 0:
        print('Total errors detected:', switchvis.errorCounter)
        return
    

    returnvis = FunctionReturnVisitor(STvis.globalST, STvis.classSTS, STvis.functionSTS)
    result.STaccept(returnvis)
    if returnvis.errorCounter > 0:
        print('Total errors detected:', returnvis.errorCounter)
        return
    

    visbreak = BreakVisitor(STvis.globalST, STvis.classSTS, STvis.functionSTS)
    result.STaccept(visbreak)
    if visbreak.errorCounter > 0:
        print('Total errors detected:', visbreak.errorCounter)
        return