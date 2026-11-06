
from visitor import *
import pydot
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz/bin/'



class Node:
    def __init__(self):
        pass
    def accept(self, vis:Visitor):
        pass

class compUnit(Node):
   def __init__(self, childnodes, ID, linen, childMethod):
       self.children = []
       self.id = ID
       self.lineNum = linen
       self.childNo = 0
       for node in childnodes:
           if node is not None:
               self.children.append(node)
       self.children.append(childMethod)

   def accept(self, vis:Visitor):
       self.childNo = 0
       vis.pre_visitCompUnit(self)
       for child in self.children:
           child.accept(vis)
           self.childNo += 1

       vis.visitCompUnit(self)
#different accept method for the STVisitor since we have a function main void type scope it defines within its rule
   def STaccept(self, vis:Visitor):
       
       for child in range(len(self.children)-1):
           self.children[child].accept(vis)
           
    #this allows me to create the scope ST for main in the previsit and push it onto the stack before calling the methodbody child
    #previsit we create a function scope and also put the symbol into the global scope.
       vis.pre_visitCompUnit(self)
       #access the last child or methodbody child
       self.children[-1].accept(vis)
       vis.visitCompUnit(self)


   def FINALaccept(self, vis:Visitor):      
        vis.pre_visitCompUnit(self)
        #need to call the last child first and accept in the reverse order 
        for child in range(1,len(self.children)+1):
            self.children[-child].accept(vis)
            
    #this allows me to create the scope ST for main in the previsit and push it onto the stack before calling the methodbody child
    #previsit we create a function scope and also put the symbol into the global scope.
        
        
        vis.visitCompUnit(self)
  
class classDef(Node):
   
   def __init__(self, ID, linen, childnodes):
       self.dataChildren = []
       self.methodChildren = []
       self.id = ID
       self.lineNum = linen
       self.childNo = 0
       #lineNum is line number of id 
       for node in childnodes:
           if node is not None:
               if type(node) is dataMemDecl:
                   self.dataChildren.append(node)
               else:
                   self.methodChildren.append(node)
               
       
   def accept(self, vis:Visitor):
       self.childNo = 0
       vis.pre_visitClassDef(self)

       for child in self.dataChildren:
           child.accept(vis)
           self.childNo += 1
       for child in self.methodChildren:
           child.accept(vis)
           self.childNo += 1

       vis.visitClassDef(self)
       
class typeN(Node):
   def __init__(self, val, lineN):
       self.valType = val
       self.lineNum = lineN
             
   def accept(self, vis:Visitor):
       vis.visitTypeN(self)

class modifierN(Node):
   def __init__(self, val, lineN):
       #currently self.value will hold the value of the keyword 
       self.value = val
       self.lineNum = lineN
       
   def accept(self, vis:Visitor):
       vis.visitModifierN(self)       
      
class classMemDef(Node):
   def __init__(self, childN):
       self.child = childN
       self.childNo = 0
       
   def accept(self, vis:Visitor):
       self.childNo = 0
       vis.pre_visitClassMemDef(self)
       self.child.accept(vis)
       self.childNo += 1

       vis.visitClassMemDef(self)
        
   
class dataMemDecl(Node):
   def __init__(self, childN1, childN2):
       self.child1 = childN1
       self.child2 = childN2
       self.childNo = 0
       self.prepChildren = []
       
   def accept(self, vis:Visitor):
       self.childNo = 0
       vis.pre_visitDataMemDecl(self)
       for prechild in self.prepChildren:
            prechild.accept(vis)
            self.childNo += 1
       self.child1.accept(vis)
       self.childNo += 1
       self.child2.accept(vis)
       self.childNo += 1
       vis.visitDataMemDecl(self)

class methodDecl(Node):
   def __init__(self, child1, child2, brack, ID, linen, child3):
       self.childN1 = child1
       self.childN2 = child2
       self.childN3 = child3
       self.isBrack = brack
       self.id = ID
       self.lineNum = linen
       self.childNo = 0
       
   def accept(self, vis:Visitor):
       self.childNo = 0
       vis.pre_visitMethodDecl(self)
       self.childN1.accept(vis)
       self.childNo += 1
       self.childN2.accept(vis)
       self.childNo += 1
       self.childN3.accept(vis)
       self.childNo += 1
       vis.visitMethodDecl(self)      
   
class constructorDecl(Node):
   def __init__(self, ID, linen, child2):
       self.id = ID
       self.lineNum = linen
       self.childN2 = child2
       self.childNo = 0
         
   def accept(self, vis:Visitor):
       self.childNo = 0
       vis.pre_visitConstructorDecl(self)
       self.childN2.accept(vis)
       self.childNo += 1
       vis.visitConstructorDecl(self)
        
class initializer(Node):
   def __init__(self, child):
       self.childN1 = child
       self.childNo = 0
       #childn1 is the expression
       
   def accept(self, vis:Visitor):
       self.childNo = 0
       vis.pre_visitInitializer(self)
       self.childN1.accept(vis)
       self.childNo += 1
       vis.visitInitializer(self)
        
class methodSuf(Node):
   def __init__(self, child1, child2):
       self.childN1 = child1
       self.childN2 = child2
       self.childNo = 0
        #childN1 could be None or a parameter list
       
   def accept(self, vis:Visitor):
       self.childNo = 0
       vis.pre_visitMethodSuf(self)
       if self.childN1 is not None:
           self.childN1.accept(vis)
           self.childNo += 1
       
       self.childN2.accept(vis)
       self.childNo += 1
       vis.visitMethodSuf(self)
        
class methodBody(Node):
   def __init__(self, childnodes):
       #methodrest returns a list of 0(empty) or more statements so need to check for it
       self.children = []
       self.childNo = 0
       for node in childnodes:          
           if node is not None:
               self.children.append(node)
       
   def accept(self, vis:Visitor):
    self.childNo = 0
    vis.pre_visitMethodBody(self)
    for child in self.children:
        child.accept(vis)
        self.childNo += 1

    vis.visitMethodBody(self)

class parameterList(Node):
   def __init__(self, child1, childnodes):
       #parameterlrest returns a list of empty or more statements so need to check for it
       self.children = []
       self.childNo = 0
       self.children.append(child1)
       for node in childnodes:
           if node is not None:
               self.children.append(node)
       
   def accept(self, vis:Visitor):
       self.childNo = 0
       vis.pre_visitParameterList(self)
       for child in self.children:  
            child.accept(vis)
            self.childNo += 1
       vis.visitParameterList(self)  
   
class parameter(Node):
   def __init__(self, child1, brack, ID, linen):
       self.childN1 = child1
       self.isBrack = brack
       self.id = ID
       self.lineNum = linen
       self.childNo = 0
               
   def accept(self, vis:Visitor):
       self.childNo = 0
       vis.pre_visitParameter(self)
       self.childN1.accept(vis)
       self.childNo += 1
       vis.visitParameter(self)     
   
class varDecl(Node):
   def __init__(self, child1, brack, ID, linen, initial):
       self.childN1 = child1
       self.isBrack = brack
       self.id = ID
       #changed lineNum from idLineN
       self.lineNum = linen
       self.initializer = initial
       self.childNo = 0
       #isbrack is true or false if [] exists or not in the vardecl
       #initializer has None if no initial value was given at some point default to zero
       #child1 is type     
       
   def accept(self, vis:Visitor):
       self.childNo = 0
       vis.pre_visitVarDecl(self)
       self.childN1.accept(vis)
       self.childNo += 1 
       if self.initializer is not None:
           self.initializer.accept(vis)
           self.childNo += 1 
       vis.visitVarDecl(self)

#start of statement nodes 

class curlyBrackStatement(Node):
   def __init__(self, childNodes):
       self.prepChildren = []
       self.children = []
       self.childNo = 0
       for node in childNodes:
           if node is not None:
               self.children.append(node)

   def accept(self, vis:Visitor):
       self.childNo = 0
       vis.pre_visitcurlyBrackStatement(self)
       for prechild in self.prepChildren:
            prechild.accept(vis)
            self.childNo += 1
       for child in self.children:
            child.accept(vis)
            self.childNo += 1
       vis.visitcurlyBrackStatement(self)
        
class expressionStatement(Node):
   def __init__(self, child1):
       self.childN1 = child1
       self.prepChildren = []
       self.childNo = 0

   def accept(self, vis:Visitor):
       self.childNo = 0
       vis.pre_visitexpressionStatement(self)
       #have to be called before the other children
       for prechild in self.prepChildren:
            prechild.accept(vis)
            self.childNo += 1
       self.childN1.accept(vis)
       self.childNo += 1
       vis.visitexpressionStatement(self)
        

class ifStatement(Node):
   def __init__(self, child1, child2, child3, linen):
       self.childN1 = child1
       self.childN2 = child2
       self.childN3 = child3
       self.prepChildren = []
       self.lineNum = linen
       self.childNo = 0
       self.whloop = False
       self.whlabel = ''
        #if child3 is None then we know there is no else statement
   def accept(self, vis:Visitor):
       self.childNo = 0
       vis.pre_visitifStatement(self)
       #have to be called before the other children
       for prechild in self.prepChildren:
            prechild.accept(vis)
            self.childNo += 1
       self.childN1.accept(vis)
       self.childNo += 1
       self.childN2.accept(vis)
       self.childNo += 1
       if self.childN3 is not None:
           self.childN3.accept(vis)
           self.childNo += 1
       vis.visitifStatement(self)
        

class whileStatement(Node):
   def __init__(self, child1, child2, linen):
       self.childN1 = child1 #expression
       self.childN2 = child2 #statement
       self.prepChildren = []
       self.lineNum = linen
       self.childNo = 0

   def accept(self, vis:Visitor):
       self.childNo = 0
       vis.pre_visitwhileStatement(self)
       for prechild in self.prepChildren:
            prechild.accept(vis)
            self.childNo += 1
       self.childN1.accept(vis)
       self.childNo += 1
       self.childN2.accept(vis)
       self.childNo += 1
       vis.visitwhileStatement(self)

class returnStatement(Node):
   def __init__(self, child1, linen):
       self.childN1 = child1
       self.childNo = 0
       self.lineNum = linen
       self.prepChildren = []
       #if child1 is None then we have no expression which is fine it could or could not have an expression

   def accept(self, vis:Visitor):
       self.childNo = 0
       vis.pre_visitreturnStatement(self)
       for prechild in self.prepChildren:
            prechild.accept(vis)
            self.childNo += 1
       if self.childN1 is not None:
           self.childN1.accept(vis)
           self.childNo += 1
      
       vis.visitreturnStatement(self)
        
   
class coutStatement(Node):
   def __init__(self, child1):
       self.childN1 = child1
       self.childNo = 0
       self.prepChildren = []

   def accept(self, vis:Visitor):
       self.childNo = 0
       vis.pre_visitcoutStatement(self)
       #have to be called before the other children
       for prechild in self.prepChildren:
            prechild.accept(vis)
            self.childNo += 1
       self.childN1.accept(vis)
       self.childNo += 1
      
       vis.visitcoutStatement(self)
        

class cinStatement(Node):
   def __init__(self, child1, linen):
       self.childN1 = child1
       self.lineNum = linen
       self.childNo = 0
       self.prepChildren = []

   def accept(self, vis:Visitor):
       self.childNo = 0
       vis.pre_visitcinStatement(self)
       #have to be called before the other children
       for prechild in self.prepChildren:
            prechild.accept(vis)
            self.childNo += 1
       self.childN1.accept(vis)
       self.childNo += 1
      
       vis.visitcinStatement(self)
        

class switchStatement(Node):
   def __init__(self, child1, child2, linen):
       self.childN1 = child1 #expression
       self.childN2 = child2 #caseblock
       self.lineNum = linen
       self.childNo = 0
       self.prepChildren = []

   def accept(self, vis:Visitor):
       self.childNo = 0
       vis.pre_visitswitchStatement(self)
       #have to be called before the other children
       for prechild in self.prepChildren:
            prechild.accept(vis)
            self.childNo += 1
       self.childN1.accept(vis)
       self.childNo += 1
       self.childN2.accept(vis)
       self.childNo += 1
       vis.visitswitchStatement(self)
        

class breakStatement(Node):
   def __init__(self, linen):
        self.lineNum = linen
       #doesnt hold any nodes its just break;
        

   def accept(self, vis:Visitor):
       vis.visitbreakStatement(self)
        
   
class varDeclStatement(Node):
   def __init__(self, child1):
       self.childN1 = child1
       self.childNo = 0
       self.prepChildren = []

   def accept(self, vis:Visitor):
       self.childNo = 0
       vis.pre_visitvarDeclStatement(self)
       #have to be called before the other children
       for prechild in self.prepChildren:
            prechild.accept(vis)
            self.childNo += 1
       self.childN1.accept(vis)
       self.childNo += 1
       vis.visitvarDeclStatement(self)
        

#end of statement nodes

#should i make a defaultstatements node?
class caseBlock(Node):
   def __init__(self, childNodeCases, childNodeStatements):
       self.caseChildren = []
       self.defaultStmtChildren = []
       self.childNo = 0

       for node in childNodeCases:
           if node is not None:
               self.caseChildren.append(node)
    
       for node in childNodeStatements:
           if node is not None:
               self.defaultStmtChildren.append(node)

   def accept(self, vis:Visitor):
       self.childNo = 0
       vis.pre_visitCaseBlock(self)
       for child in self.caseChildren:
            child.accept(vis)
            self.childNo += 1
       for child in self.defaultStmtChildren:
            child.accept(vis)
            self.childNo += 1
       vis.visitCaseBlock(self)
        
   
class case(Node):
   def __init__(self, val, valT, linen, childnodes):
       self.value = val #value
       self.valType = valT #values type
       self.lineNum = linen
       self.statementChildren = []
       self.childNo = 0
       #there could be zero or more children in statementChildren
       for node in childnodes:
           
           if node is not None:
               self.statementChildren.append(node)
       
   def accept(self, vis:Visitor):
       self.childNo = 0
       vis.pre_visitCase(self)
       for child in self.statementChildren:
            child.accept(vis)
            self.childNo += 1
       
       vis.visitCase(self)
        

#beginning of expression nodes


class assignmentExpression(Node):
   def __init__(self, child1, child2, linen):
       self.childN1 = child1
       self.childN2 = child2
       self.lineNum = linen
       self.rNeedLoad = False
       #print(self.childN2, self.lineNum)
       self.childNo = 0

   def accept(self, vis:Visitor):
       self.childNo = 0
       vis.pre_visitassignmentExpression(self)
       self.childN1.accept(vis)
       self.childNo += 1
       self.childN2.accept(vis)
       self.childNo += 1
       vis.visitassignmentExpression(self)
        
   
class addAssignmentExpression(Node):
   def __init__(self, child1, child2, linen):
       self.childN1 = child1
       self.childN2 = child2
       self.lineNum = linen
       self.childNo = 0

   def accept(self, vis:Visitor):
       self.childNo = 0
       vis.pre_visitaddAssignmentExpression(self)
       self.childN1.accept(vis)
       self.childNo += 1
       self.childN2.accept(vis)
       self.childNo += 1
       vis.visitaddAssignmentExpression(self)
        

class subAssignmentExpression(Node):
   def __init__(self, child1, child2, linen):
       self.childN1 = child1
       self.childN2 = child2
       self.lineNum = linen
       self.childNo = 0

   def accept(self, vis:Visitor):
       self.childNo = 0
       vis.pre_visitsubAssignmentExpression(self)
       self.childN1.accept(vis)
       self.childNo += 1
       self.childN2.accept(vis)
       self.childNo += 1
       vis.visitsubAssignmentExpression(self)
        
   
class multAssignmentExpression(Node):
   def __init__(self, child1, child2, linen):
       self.childN1 = child1
       self.childN2 = child2
       self.lineNum = linen
       self.childNo = 0

   def accept(self, vis:Visitor):
       self.childNo = 0
       vis.pre_visitmultAssignmentExpression(self)
       self.childN1.accept(vis)
       self.childNo += 1
       self.childN2.accept(vis)
       self.childNo += 1
       vis.visitmultAssignmentExpression(self)
        
   
class divAssignmentExpression(Node):
   def __init__(self, child1, child2, linen):
       self.childN1 = child1
       self.childN2 = child2
       self.lineNum = linen
       self.childNo = 0

   def accept(self, vis:Visitor):
       self.childNo = 0
       vis.pre_visitdivAssignmentExpression(self)
       self.childN1.accept(vis)
       self.childNo += 1
       self.childN2.accept(vis)
       self.childNo += 1
       vis.visitdivAssignmentExpression(self)
        
 
class plusExpression(Node):
   def __init__(self, child1, child2, linen):
       self.childN1 = child1
       self.childN2 = child2
       self.lineNum = linen
       self.childNo = 0

   def accept(self, vis:Visitor):
       self.childNo = 0
       vis.pre_visitplusExpression(self)
       self.childN1.accept(vis)
       self.childNo += 1
       self.childN2.accept(vis)
       self.childNo += 1
       vis.visitplusExpression(self)
        
   
class minusExpression(Node):
   def __init__(self, child1, child2, linen):
       self.childN1 = child1
       self.childN2 = child2
       self.lineNum = linen
       self.childNo = 0

   def accept(self, vis:Visitor):
       self.childNo = 0
       vis.pre_visitminusExpression(self)
       self.childN1.accept(vis)
       self.childNo += 1
       self.childN2.accept(vis)
       self.childNo += 1
       vis.visitminusExpression(self)
        
   
class multExpression(Node):
   def __init__(self, child1, child2, linen):
       self.childN1 = child1
       self.childN2 = child2
       self.lineNum = linen
       self.childNo = 0

   def accept(self, vis:Visitor):
       self.childNo = 0
       vis.pre_visitmultExpression(self)
       self.childN1.accept(vis)
       self.childNo += 1
       self.childN2.accept(vis)
       self.childNo += 1
       vis.visitmultExpression(self)
        
   
class divExpression(Node):
   def __init__(self, child1, child2, linen):
       self.childN1 = child1
       self.childN2 = child2
       self.lineNum = linen
       self.childNo = 0

   def accept(self, vis:Visitor):
       self.childNo = 0
       vis.pre_visitdivExpression(self)
       self.childN1.accept(vis)
       self.childNo += 1
       self.childN2.accept(vis)
       self.childNo += 1
       vis.visitdivExpression(self)
        
   
class equalityExpression(Node):
   def __init__(self, child1, child2, linen):
       self.childN1 = child1
       self.childN2 = child2
       self.lineNum = linen
       self.childNo = 0

   def accept(self, vis:Visitor):
       self.childNo = 0
       vis.pre_visitequalityExpression(self)
       self.childN1.accept(vis)
       self.childNo += 1
       self.childN2.accept(vis)
       self.childNo += 1
       vis.visitequalityExpression(self)
        

class notEqualExpression(Node):
   def __init__(self, child1, child2, linen):
       self.childN1 = child1
       self.childN2 = child2
       self.lineNum = linen
       self.childNo = 0

   def accept(self, vis:Visitor):
       self.childNo = 0
       vis.pre_visitnotEqualExpression(self)
       self.childN1.accept(vis)
       self.childNo += 1
       self.childN2.accept(vis)
       self.childNo += 1
       vis.visitnotEqualExpression(self)
        

class lessThanExpression(Node):
   def __init__(self, child1, child2, linen):
       self.childN1 = child1
       self.childN2 = child2
       self.lineNum = linen
       self.childNo = 0

   def accept(self, vis:Visitor):
       self.childNo = 0
       vis.pre_visitlessThanExpression(self)
       self.childN1.accept(vis)
       self.childNo += 1
       self.childN2.accept(vis)
       self.childNo += 1
       vis.visitlessThanExpression(self)
        

class greaterThanExpression(Node):
   def __init__(self, child1, child2, linen):
       self.childN1 = child1
       self.childN2 = child2
       self.lineNum = linen
       self.childNo = 0

   def accept(self, vis:Visitor):
       self.childNo = 0
       vis.pre_visitgreaterThanExpression(self)
       self.childN1.accept(vis)
       self.childNo += 1
       self.childN2.accept(vis)
       self.childNo += 1
       vis.visitgreaterThanExpression(self)
        
   
class LTEqualsExpression(Node):
   def __init__(self, child1, child2, linen):
       self.childN1 = child1
       self.childN2 = child2
       self.lineNum = linen
       self.childNo = 0

   def accept(self, vis:Visitor):
       self.childNo = 0
       vis.pre_visitLTEqualsExpression(self)
       self.childN1.accept(vis)
       self.childNo += 1
       self.childN2.accept(vis)
       self.childNo += 1
       vis.visitLTEqualsExpression(self)
        

class GTEqualsExpression(Node):
   def __init__(self, child1, child2, linen):
       self.childN1 = child1
       self.childN2 = child2
       self.lineNum = linen
       self.childNo = 0

   def accept(self, vis:Visitor):
       self.childNo = 0
       vis.pre_visitGTEqualsExpression(self)
       self.childN1.accept(vis)
       self.childNo += 1
       self.childN2.accept(vis)
       self.childNo += 1
       vis.visitGTEqualsExpression(self)
        
   
class andExpression(Node):
   def __init__(self, child1, child2, linen):
       self.childN1 = child1
       self.childN2 = child2
       self.lineNum = linen
       self.childNo = 0

   def accept(self, vis:Visitor):
       self.childNo = 0
       vis.pre_visitandExpression(self)
       self.childN1.accept(vis)
       self.childNo += 1
       self.childN2.accept(vis)
       self.childNo += 1
       vis.visitandExpression(self)
        

class orExpression(Node):
   def __init__(self, child1, child2, linen):
       self.childN1 = child1
       self.childN2 = child2
       self.lineNum = linen
       self.childNo = 0

   def accept(self, vis:Visitor):
       self.childNo = 0
       vis.pre_visitorExpression(self)
       self.childN1.accept(vis)
       self.childNo += 1
       self.childN2.accept(vis)
       self.childNo += 1
       vis.visitorExpression(self)
        
       
class notExpression(Node):
   def __init__(self, child1, linen):
       self.childN1 = child1
       self.lineNum = linen
       self.childNo = 0

   def accept(self, vis:Visitor):
       self.childNo = 0
       vis.pre_visitnotExpression(self)
       self.childN1.accept(vis)
       self.childNo += 1
       vis.visitnotExpression(self)
        

class unaryPlusExpression(Node):
   def __init__(self, child1, linen):
       self.childN1 = child1
       self.lineNum = linen
       self.childNo = 0
       
   def accept(self, vis:Visitor):
       self.childNo = 0
       vis.pre_visitunaryPlusExpression(self)
       self.childN1.accept(vis)
       self.childNo += 1
       vis.visitunaryPlusExpression(self)
        

class unaryMinusExpression(Node):
   def __init__(self, child1, linen):
       self.childN1 = child1
       self.lineNum = linen
       self.childNo = 0
       

   def accept(self, vis:Visitor):
       self.childNo = 0
       vis.pre_visitunaryMinusExpression(self)
       self.childN1.accept(vis)
       self.childNo += 1
       vis.visitunaryMinusExpression(self)
        

class literalIntExpression(Node):
   def __init__(self, val, linen):
       self.value = int(val)
       self.lineNum = linen
    
   def accept(self, vis:Visitor):
       vis.visitliteralIntExpression(self)
        

class literalCharExpression(Node):
   def __init__(self, val, linen):
       self.value = val
       self.lineNum = linen
    
   def accept(self, vis:Visitor):
       vis.visitliteralCharExpression(self)
       
        
   
class literalStringExpression(Node):
   def __init__(self, val, linen):
       self.value = val
       self.lineNum = linen
    
   def accept(self, vis:Visitor):
       vis.visitliteralStringExpression(self)
        

class trueExpression(Node):
   def __init__(self, val, linen):
       self.value = val
       self.lineNum = linen
    
   def accept(self, vis:Visitor):
       vis.visittrueExpression(self)
        

class falseExpression(Node):
   def __init__(self, val, linen):
       self.value = val
       self.lineNum = linen
    
   def accept(self, vis:Visitor):
       vis.visitfalseExpression(self)
        
   
class nullExpression(Node):
   def __init__(self, val, linen):
       self.value = val
       self.lineNum = linen
    
   def accept(self, vis:Visitor):
       vis.visitnullExpression(self)
        
   
class identifierExpression(Node):
   def __init__(self, val, linen):
       self.value = val
       self.lineNum = linen
    
   def accept(self, vis:Visitor):
       vis.visitidentifierExpression(self)
       
   
class thisExpression(Node):
   def __init__(self, val, linen):
       self.value = val
       self.lineNum = linen
    
   def accept(self, vis:Visitor):
       vis.visitthisExpression(self)
        

class callExpression(Node):
   def __init__(self, child1, child2):
       self.childN1 = child1
       self.childN2 = child2
       self.childNo = 0
       self.funName = ''
       self.RT = ''
       self.parentClass = ''
    
   def accept(self, vis:Visitor):
       self.childNo = 0
       vis.pre_visitcallExpression(self)
       self.childN1.accept(vis)
       self.childNo += 1
       self.childN2.accept(vis)
       self.childNo += 1
       vis.visitcallExpression(self)
    

class arrayExpression(Node):
   def __init__(self, child1, child2):
       self.childN1 = child1
       self.childN2 = child2
       self.childNo = 0
    
   def accept(self, vis:Visitor):
       self.childNo = 0
       vis.pre_visitarrayExpression(self)
       self.childN1.accept(vis)
       self.childNo += 1
       self.childN2.accept(vis)
       self.childNo += 1
       vis.visitarrayExpression(self)
        

class periodExpression(Node):
   def __init__(self, child1, ID, linen):
       #childN1 will be the expression part and id will just be id
       self.childN1 = child1
       self.id = ID
       self.idLineN = linen
       self.childNo = 0
    
   def accept(self, vis:Visitor):
       self.childNo = 0
       vis.pre_visitperiodExpression(self)
       self.childN1.accept(vis)
       self.childNo += 1
       vis.visitperiodExpression(self)
        

class newExpression(Node):
   def __init__(self, child1, child2, linen):
       self.childN1 = child1
       self.childN2 = child2
       self.lineNum = linen
       self.childNo = 0
    
   def accept(self, vis:Visitor):
       self.childNo = 0
       vis.pre_visitnewExpression(self)
       self.childN1.accept(vis)
       self.childNo += 1
       self.childN2.accept(vis)
       self.childNo += 1
       vis.visitnewExpression(self)
        
   
class parenExpression(Node):
   def __init__(self, child1):
       self.childN1 = child1
       self.childNo = 0
    
   def accept(self, vis:Visitor):
       self.childNo = 0
       vis.pre_visitparenExpression(self)
       self.childN1.accept(vis)
       self.childNo += 1
       
       vis.visitparenExpression(self)
        

#end of expression nodes


class arguments(Node):
   def __init__(self, child1, linen):
       self.childN1 = child1
       self.lineNum = linen
       self.childNo = 0
        #childN1 could be an argument list or be None 
       
   def accept(self, vis:Visitor):
       self.childNo = 0
       vis.pre_visitArguments(self)
       if self.childN1 is not None:
           self.childN1.accept(vis)
           self.childNo += 1
       
       vis.visitArguments(self)
        
   
class argumentList(Node):
   def __init__(self, child1, childnodes):
       self.children = []
       self.children.append(child1)
       self.childNo = 0

       for node in childnodes: 
           if node is not None:
               self.children.append(node)
       
   def accept(self, vis:Visitor):
       self.childNo = 0
       vis.pre_visitArgumentList(self)
       for child in self.children:
            child.accept(vis)
            self.childNo += 1
       
       vis.visitArgumentList(self)
        
   
class index(Node):
   def __init__(self, child1, linen):
       self.childN1 = child1
       self.lineNum = linen
       self.childNo = 0
       
       
   def accept(self, vis:Visitor):
       self.childNo = 0
       vis.pre_visitIndex(self)
       self.childN1.accept(vis)
       self.childNo += 1
       vis.visitIndex(self)
        
   

#labels can only be alphanumeric or underscore characters
#could just do post visit and call accept on the children and after each children check stack
#would also have to set a flag and and save back ups 
#still have to keep track of scope entering and exiting the same thiong we did for the other visitors. that way we know which scope to reference
#previsit save previous flag reset it to false, postvisit set flag to true and call accept on child then reassign child to child1.
#this is so we can keep track of which sub tree goes to which child
#we could set aside the sub tree and then combine it later, but the problem is is that we still dont know who our parent is 
#Desugaring to replace a node we need to know its parent so we can reasign its child variable to the new node 
class ASMnode(Node):
    def __init__(self, instruct, labelname = '', reg = -1, regsN = 0):
        #what data is this going to need
        #first print the label if any then space or tab and place the instruction on the same line 
        #make each node hold a parent variable, from there when we have assign our children or during accept we will go
        # in each node class, go through each child and do child.parent = self. since it is an object they should all contain a link to parent
        #but what if i change the parent how do i change the parent pointer for all the children? and change its own parent to change its child to me and get rid of the old one
        #self.parent = None 
        self.childNo = 0
        self.instruction = instruct
        self.label = labelname
        self.register = reg
        self.regsNeed = regsN
        #dont know which to have, child or chilren varaible   0-15
        #self.child = None

        self.children = []
        #just do one accept here so we can see the output in vistor dot without having to add a unique one to each asm node
    def accept(self, vis:Visitor):
        self.childNo = 0
        vis.pre_visitASMnode(self)
        for child in self.children:
            child.accept(vis)
            self.childNo += 1

        vis.visitASMnode(self)
        pass

    def __str__(self, file):
        #just print label space and instruction, it doesnt matter if it has a label or not 
        file.write(self.label+' '+self.instruction+'\n')
        #print(self.label, self.instruction)
        pass
#people on msteams said they used a stack to store the new nodes and then the parent in post visit would just attach it to itsstack??? or something?
#this is meant for 2 or more statements that are together, this is so we dont throw an error when we have to return two nodes to the parent instead we put it in the blockstatement and return that
#this could work for calculating offsets for the variable to find it and get it. it makes sense cause some nodes do create multiple nodes 
#that have to be in the same level and called in a specific order, so a block statement works really well for this

class BlockStatement(Node):
    def __init__(self, nodechildren, name = ''):
        self.childNo = 0
        self.children = []
        self.namec = name
        #just do one accept here so we can see the output in vistor dot without having to add a unique one to each asm node
        for child in nodechildren:

            if isinstance(child, list):
                for ch in child:
                    self.children.append(ch)
            else:

                self.children.append(child)

    def accept(self, vis:Visitor):
        self.childNo = 0
        vis.pre_visitBlocknode(self)
        for child in self.children:
            child.accept(vis)
            self.childNo += 1

        vis.visitBlocknode(self)
        pass

#ASMNODES
class ADDnode(ASMnode):
    def __init__(self, instruct, labelname = '', reg = -1, regsN = 0):
        ASMnode.__init__(self, instruct, labelname, reg, regsN)

    

class JMPnode(ASMnode):
    def __init__(self, instruct, labelname = '', reg = -1, regsN = 0):
        ASMnode.__init__(self, instruct, labelname, reg, regsN)
    
class JMRnode(ASMnode):
    def __init__(self, instruct, labelname = '', reg = -1, regsN = 0):
        ASMnode.__init__(self, instruct, labelname, reg, regsN)
    
class BNZnode(ASMnode):
    def __init__(self, instruct, labelname = '', reg = -1, regsN = 0):
        ASMnode.__init__(self, instruct, labelname, reg, regsN)
    
class BGTnode(ASMnode):
    def __init__(self, instruct, labelname = '', reg = -1, regsN = 0):
        ASMnode.__init__(self, instruct, labelname, reg, regsN)
    
class BLTnode(ASMnode):
    def __init__(self, instruct, labelname = '', reg = -1, regsN = 0):
        ASMnode.__init__(self, instruct, labelname, reg, regsN)
  
class BRZnode(ASMnode):
    def __init__(self, instruct, labelname = '', reg = -1, regsN = 0):
        ASMnode.__init__(self, instruct, labelname, reg, regsN)
  
class MOVnode(ASMnode):
    def __init__(self, instruct, labelname = '', reg = -1, regsN = 0):
        ASMnode.__init__(self, instruct, labelname, reg, regsN)
   
class LDAnode(ASMnode):
    def __init__(self, instruct, labelname = '', reg = -1, regsN = 0):
        ASMnode.__init__(self, instruct, labelname, reg, regsN)
   
class STRLnode(ASMnode):
    def __init__(self, instruct, labelname = '', reg = -1, regsN = 0):
        ASMnode.__init__(self, instruct, labelname, reg, regsN)
   
class LDRLnode(ASMnode):
    def __init__(self, instruct, labelname = '', reg = -1, regsN = 0):
        ASMnode.__init__(self, instruct, labelname, reg, regsN)
    
class STBLnode(ASMnode):
    def __init__(self, instruct, labelname = '', reg = -1, regsN = 0):
        ASMnode.__init__(self, instruct, labelname, reg, regsN)

class LDBLnode(ASMnode):
    def __init__(self, instruct, labelname = '', reg = -1, regsN = 0):
        ASMnode.__init__(self, instruct, labelname, reg, regsN)
    
class ADInode(ASMnode):
    def __init__(self, instruct, labelname = '', reg = -1, regsN = 0):
        ASMnode.__init__(self, instruct, labelname, reg, regsN)
    
class SUBnode(ASMnode):
    def __init__(self, instruct, labelname = '', reg = -1, regsN = 0):
        ASMnode.__init__(self, instruct, labelname, reg, regsN)
    
class MULnode(ASMnode):
    def __init__(self, instruct, labelname = '', reg = -1, regsN = 0):
        ASMnode.__init__(self, instruct, labelname, reg, regsN)
    
class DIVnode(ASMnode):
    def __init__(self, instruct, labelname = '', reg = -1, regsN = 0):
        ASMnode.__init__(self, instruct, labelname, reg, regsN)
    
class CMPnode(ASMnode):
    def __init__(self, instruct, labelname = '', reg = -1, regsN = 0):
        ASMnode.__init__(self, instruct, labelname, reg, regsN)
    
class ANDnode(ASMnode):
    def __init__(self, instruct, labelname = '', reg = -1, regsN = 0):
        ASMnode.__init__(self, instruct, labelname, reg, regsN)
    
class ORnode(ASMnode):
    def __init__(self, instruct, labelname = '', reg = -1, regsN = 0):
        ASMnode.__init__(self, instruct, labelname, reg, regsN)
    
class TRPZEROnode(ASMnode):
    def __init__(self, instruct, labelname = '', reg = -1, regsN = 0):
        ASMnode.__init__(self, instruct, labelname, reg, regsN)
    
class TRPONEnode(ASMnode):
    def __init__(self, instruct, labelname = '', reg = -1, regsN = 0):
        ASMnode.__init__(self, instruct, labelname, reg, regsN)
    
class TRPTWOnode(ASMnode):
    def __init__(self, instruct, labelname = '', reg = -1, regsN = 0):
        ASMnode.__init__(self, instruct, labelname, reg, regsN)
    
class TRPTHREEnode(ASMnode):
    def __init__(self, instruct, labelname = '', reg = -1, regsN = 0):
        ASMnode.__init__(self, instruct, labelname, reg, regsN)
    
class TRPFOURnode(ASMnode):
    def __init__(self, instruct, labelname = '', reg = -1, regsN = 0):
        ASMnode.__init__(self, instruct, labelname, reg, regsN)
    
class STRRnode(ASMnode):
    def __init__(self, instruct, labelname = '', reg = -1, regsN = 0):
        ASMnode.__init__(self, instruct, labelname, reg, regsN)
    
class LDRRnode(ASMnode):
    def __init__(self, instruct, labelname = '', reg = -1, regsN = 0):
        ASMnode.__init__(self, instruct, labelname, reg, regsN)
    
class STBRnode(ASMnode):
    def __init__(self, instruct, labelname = '', reg = -1, regsN = 0):
        ASMnode.__init__(self, instruct, labelname, reg, regsN)
    
class LDBRnode(ASMnode):
    def __init__(self, instruct, labelname = '', reg = -1, regsN = 0):
        ASMnode.__init__(self, instruct, labelname, reg, regsN)
    
class ALLCIMMEDIATEnode(ASMnode):
    def __init__(self, instruct, labelname = '', reg = -1, regsN = 0):
        ASMnode.__init__(self, instruct, labelname, reg, regsN)
    
class ALLCLABELnode(ASMnode):
    def __init__(self, instruct, labelname = '', reg = -1, regsN = 0):
        ASMnode.__init__(self, instruct, labelname, reg, regsN)
    
class ALLCREGISTERnode(ASMnode):
    def __init__(self, instruct, labelname = '', reg = -1, regsN = 0):
        ASMnode.__init__(self, instruct, labelname, reg, regsN)
    
class DIRECTIVEnode(ASMnode):
    def __init__(self, instruct, labelname = '', reg = -1, regsN = 0):
        ASMnode.__init__(self, instruct, labelname, reg, regsN)
    