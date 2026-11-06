import nodes
from symboltable import *
import pydot
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz/bin/'

#have to create a global counter just in case i have to use it in a later visitor that way i dont create past temp variables from other visitors
tempCounter = 0
whileCounter = 0
switchCounter = 0
ifCounter = 0
stringCounter = 0
intCounter = 0
charCounter = 0
compareCounter = 0
litLabelCounter = 0

class Visitor:
   def pre_visitCompUnit(self, node):
      pass
   def visitCompUnit(self, node):
      pass
   def pre_visitClassDef(self, node):
      pass
   def visitClassDef(self, node):
      pass
   def visitTypeN(self, node):
      pass
   def visitModifierN(self, node):
      pass
   def pre_visitClassMemDef(self, node):
      pass
   def visitClassMemDef(self, node):
      pass
   def pre_visitDataMemDecl(self, node):
      pass
   def visitDataMemDecl(self, node):
      pass
   def pre_visitMethodDecl(self, node):
      pass
   def visitMethodDecl(self, node):
      pass
   def pre_visitConstructorDecl(self, node):
      pass
   def visitConstructorDecl(self, node):
      pass
   def pre_visitInitializer(self, node):
      pass
   def visitInitializer(self, node):
      pass
   def pre_visitMethodSuf(self, node):
      pass
   def visitMethodSuf(self, node):
      pass
   def pre_visitMethodBody(self, node):
      pass
   def visitMethodBody(self, node):
      pass
   def pre_visitParameterList(self, node):
      pass
   def visitParameterList(self, node):
      pass
   def pre_visitParameter(self, node):
      pass
   def visitParameter(self, node):
      pass
   def pre_visitVarDecl(self, node):
      pass
   def visitVarDecl(self, node):
      pass
   def pre_visitcurlyBrackStatement(self, Node):
      pass
   def visitcurlyBrackStatement(self, Node):
      pass
   def pre_visitexpressionStatement(self, Node):
      pass

   def visitexpressionStatement(self, Node):
      pass

   def pre_visitifStatement(self, Node):
      pass
   def visitifStatement(self, Node):
      pass

   def pre_visitwhileStatement(self, Node):
      pass
   def visitwhileStatement(self, Node):
      pass

   def pre_visitreturnStatement(self, Node):
      pass
   def visitreturnStatement(self, Node):
      pass

   def pre_visitcoutStatement(self, Node):
      pass
   def visitcoutStatement(self, Node):
      pass

   def pre_visitcinStatement(self, Node):
      pass
   def visitcinStatement(self, Node):
      pass

   def pre_visitswitchStatement(self, Node):
      pass
   def visitswitchStatement(self, Node):
      pass

   def visitbreakStatement(self, Node):
      pass

   def pre_visitvarDeclStatement(self, Node):
      pass
   def visitvarDeclStatement(self, Node):
      pass

#end of statements
   def pre_visitCaseBlock(self, node):
      pass
   def visitCaseBlock(self, node):
      pass
   def pre_visitCase(self, node):
      pass
   def visitCase(self, node):
      pass


#    def visitExpression(node):

   def pre_visitassignmentExpression(self, Node):
      pass
   def visitassignmentExpression(self, Node):
      pass

   def pre_visitaddAssignmentExpression(self, Node):
      pass
   def visitaddAssignmentExpression(self, Node):
      pass

   def pre_visitsubAssignmentExpression(self, Node):
      pass
   def visitsubAssignmentExpression(self, Node):
      pass

   def pre_visitmultAssignmentExpression(self, Node):
      pass
   def visitmultAssignmentExpression(self, Node):
      pass
   

   def pre_visitdivAssignmentExpression(self, Node):
      pass
   def visitdivAssignmentExpression(self, Node):
      pass

   def pre_visitplusExpression(self, Node):
      pass
   def visitplusExpression(self, Node):
      pass

   def pre_visitminusExpression(self, Node):
      pass
   def visitminusExpression(self, Node):
      pass

   def pre_visitmultExpression(self, Node):
      pass
   def visitmultExpression(self, Node):
      pass

   def pre_visitdivExpression(self, Node):
      pass
   def visitdivExpression(self, Node):
      pass

   def pre_visitequalityExpression(self, Node):
      pass
   def visitequalityExpression(self, Node):
      pass

   def pre_visitnotEqualExpression(self, Node):
      pass
   def visitnotEqualExpression(self, Node):
      pass

   def pre_visitlessThanExpression(self, Node):
      pass
   def visitlessThanExpression(self, Node):
      pass

   def pre_visitgreaterThanExpression(self, Node):
      pass
   def visitgreaterThanExpression(self, Node):
      pass

   def pre_visitLTEqualsExpression(self, Node):
      pass
   def visitLTEqualsExpression(self, Node):
      pass

   def pre_visitGTEqualsExpression(self, Node):
      pass
   def visitGTEqualsExpression(self, Node):
      pass

   def pre_visitandExpression(self, Node):
      pass
   def visitandExpression(self, Node):
      pass

   def pre_visitorExpression(self, Node):
      pass
   def visitorExpression(self, Node):
      pass
      
   def pre_visitnotExpression(self, Node):
      pass
   def visitnotExpression(self, Node):
      pass

   def pre_visitunaryPlusExpression(self, Node):
      pass
   def visitunaryPlusExpression(self, Node):
      pass

   def pre_visitunaryMinusExpression(self, Node):
      pass
   def visitunaryMinusExpression(self, Node):
      pass

   def visitliteralIntExpression(self, Node):
      pass

   def visitliteralCharExpression(self, Node):
      pass

   def visitliteralStringExpression(self, Node):
      pass

   def visittrueExpression(self, Node):
      pass

   def visitfalseExpression(self, Node):
      pass

   def visitnullExpression(self, Node):
      pass

   def visitidentifierExpression(self, Node):
      pass

   def visitthisExpression(self, Node):
      pass

   def pre_visitcallExpression(self, Node):
      pass
   def visitcallExpression(self, Node):
      pass

   def pre_visitarrayExpression(self, Node):
      pass
   def visitarrayExpression(self, Node):
      pass

   def pre_visitperiodExpression(self, Node):
      pass
   def visitperiodExpression(self, Node):
      pass

   def pre_visitnewExpression(self, Node):
      pass
   def visitnewExpression(self, Node):
      pass

   def pre_visitparenExpression(self, Node):
      pass
   def visitparenExpression(self, Node):
      pass

#end of expressions

   def pre_visitArguments(self, node):
      pass
   def visitArguments(self, node):
      pass
   def pre_visitArgumentList(self, node):
      pass
   def visitArgumentList(self, node):
      pass
   def pre_visitIndex(self, node):
      pass
   def visitIndex(self, node):
      pass


   def pre_visitBlocknode(self, Node):
      pass
   def visitBlocknode(self, Node):
      pass
#ASMnode visits
   def visitJMPnode(self, Node):
      pass
   def visitJMRnode(self, Node):
      pass
   def visitBNZnode(self, Node):
      pass
   def visitBGTnode(self, Node):
      pass
   def visitBLTnode(self, Node):
      pass
   def visitBRZnode(self, Node):
      pass
   def visitMOVnode(self, Node):
      pass
   def visitLDAnode(self, Node):
      pass
   def visitSTRLnode(self, Node):
      pass
   def visitLDRLnode(self, Node):
      pass
   def visitSTBLnode(self, Node):
      pass
   def visitLDBLnode(self, Node):
      pass
   def visitADInode(self, Node):
      pass
   def visitSUBnode(self, Node):
      pass
   def visitMULnode(self, Node):
      pass
   def visitDIVnode(self, Node):
      pass
   def visitCMPnode(self, Node):
      pass
   def visitANDnode(self, Node):
      pass
   def visitORnode(self, Node):
      pass
   def visitTRPZEROnode(self, Node):
      pass
   def visitTRPONEnode(self, Node):
      pass
   def visitTRPTWOnode(self, Node):
      pass
   def visitTRPTHREEnode(self, Node):
      pass
   def visitTRPFOURnode(self, Node):
      pass
   def visitSTRRnode(self, Node):
      pass
   def visitLDRRnode(self, Node):
      pass
   def visitSTBRnode(self, Node):
      pass
   def visitLDBRnode(self, Node):
      pass
   def visitALLCIMMEDIATEnode(self, Node):
      pass
   def visitALLCLABELnode(self, Node):
      pass
   def visitALLCREGISTERnode(self, Node):
      pass
   def visitDIRECTIVEnode(self, Node):
      pass

   def pre_visitASMnode(self, Node):
      pass
   def visitASMnode(self, Node):
      pass

   #we can add previsits but im unsure as to why we would need them
   def pre_visitJMPnode(self, Node):
      pass
   def pre_visitJMRnode(self, Node):
      pass
   def pre_visitBNZnode(self, Node):
      pass
   def pre_visitBGTnode(self, Node):
      pass
   def pre_visitBLTnode(self, Node):
      pass
   def pre_visitBRZnode(self, Node):
      pass
   def pre_visitMOVnode(self, Node):
      pass
   def pre_visitLDAnode(self, Node):
      pass
   def pre_visitSTRLnode(self, Node):
      pass
   def pre_visitLDRLnode(self, Node):
      pass
   def pre_visitSTBLnode(self, Node):
      pass
   def pre_visitLDBLnode(self, Node):
      pass
   def pre_visitADInode(self, Node):
      pass
   def pre_visitSUBnode(self, Node):
      pass
   def pre_visitMULnode(self, Node):
      pass
   def pre_visitDIVnode(self, Node):
      pass
   def pre_visitCMPnode(self, Node):
      pass
   def pre_visitANDnode(self, Node):
      pass
   def pre_visitORnode(self, Node):
      pass
   def pre_visitTRPZEROnode(self, Node):
      pass
   def pre_visitTRPONEnode(self, Node):
      pass
   def pre_visitTRPTWOnode(self, Node):
      pass
   def pre_visitTRPTHREEnode(self, Node):
      pass
   def pre_visitTRPFOURnode(self, Node):
      pass
   def pre_visitSTRRnode(self, Node):
      pass
   def pre_visitLDRRnode(self, Node):
      pass
   def pre_visitSTBRnode(self, Node):
      pass
   def pre_visitLDBRnode(self, Node):
      pass
   def pre_visitALLCIMMEDIATEnode(self, Node):
      pass
   def pre_visitALLCLABELnode(self, Node):
      pass
   def pre_visitALLCREGISTERnode(self, Node):
      pass
   def pre_visitDIRECTIVEnode(self, Node):
      pass
   


class visitorDot(Visitor):
    def __init__(self):
        self.graph = pydot.Dot('AST', graph_type='digraph', bgcolor='white')
        self.graph.set_node_defaults(shape='record')
        self.nodeNum = 1
        self.childs = []
          
    def collectCH(self, numChilds):
       children = []
       for i in range(numChilds):
          children.append(self.childs.pop())
       children.sort(reverse=True)
       return children
    
    def pre_visitCompUnit(self, node):
        self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'compunit'))
        self.childs.append(self.nodeNum)
        self.nodeNum += 1
        
    
    def visitCompUnit(self, node):
        chs = self.collectCH(node.childNo)
        root = self.collectCH(1).pop()
        for child in chs:
           self.graph.add_edge(pydot.Edge(root, child, color='blue'))

        #self.childs.append(root)
        
        self.graph.write_png("output.png") 
          
    

    def pre_visitClassDef(self, node):
        self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'classdef: ' + node.id))
        self.childs.append(self.nodeNum)
        self.nodeNum += 1
        
    def visitClassDef(self, node):
        chs = self.collectCH(node.childNo)
        root = self.collectCH(1).pop()
        for child in chs:
           self.graph.add_edge(pydot.Edge(root, child, color='blue'))

        self.childs.append(root)
          
    def pre_visitASMnode(self, Node):
       self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'ASMnode: ' + Node.label + Node.instruction))
       self.childs.append(self.nodeNum)
       self.nodeNum += 1
       pass
    def visitASMnode(self, Node):
       chs = self.collectCH(Node.childNo)
       root = self.collectCH(1).pop()
       for child in chs:
          self.graph.add_edge(pydot.Edge(root, child, color='blue'))

       self.childs.append(root)
       pass
    
    def pre_visitBlocknode(self, Node):
       self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'BLOCKNODE numchildren: ' + str(len(Node.children))))
       self.childs.append(self.nodeNum)
       self.nodeNum += 1
       
    
    def visitBlocknode(self, Node):
       chs = self.collectCH(Node.childNo)
       root = self.collectCH(1).pop()
       for child in chs:
          self.graph.add_edge(pydot.Edge(root, child, color='blue'))

       self.childs.append(root)
       

    def visitTypeN(self, node):
        self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'type: ' + node.valType))
        self.childs.append(self.nodeNum)
        self.nodeNum += 1
        
        
    
    def visitModifierN(self, node):
        self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'modifier: ' + node.value))
        self.childs.append(self.nodeNum)
        self.nodeNum += 1
        
        
    def pre_visitClassMemDef(self, node):
        self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'ClassMemberDefinition'))
        self.childs.append(self.nodeNum)
        self.nodeNum += 1
          
    
    def visitClassMemDef(self, node):
        chs = self.collectCH(node.childNo)
        root = self.collectCH(1).pop()
        for child in chs:
           self.graph.add_edge(pydot.Edge(root, child, color='blue'))

        self.childs.append(root)
          

    def pre_visitDataMemDecl(self, node):
        self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'DataMemberDeclaration'))
        self.childs.append(self.nodeNum)
        self.nodeNum += 1
          
    def visitDataMemDecl(self, node):
        chs = self.collectCH(node.childNo)
        root = self.collectCH(1).pop()
        for child in chs:
           self.graph.add_edge(pydot.Edge(root, child, color='blue'))

        self.childs.append(root)
          
    

    def pre_visitMethodDecl(self, node):
        self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'MethodDeclaration: ' + node.id))
        self.childs.append(self.nodeNum)
        self.nodeNum += 1
          
    def visitMethodDecl(self, node):
        chs = self.collectCH(node.childNo)
        root = self.collectCH(1).pop()
        for child in chs:
           self.graph.add_edge(pydot.Edge(root, child, color='blue'))

        self.childs.append(root)
          
    

    def pre_visitConstructorDecl(self, node):
        self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'ConstructorDeclaration: ' + node.id))
        self.childs.append(self.nodeNum)
        self.nodeNum += 1
          
    def visitConstructorDecl(self, node):
        chs = self.collectCH(node.childNo)
        root = self.collectCH(1).pop()
        for child in chs:
           self.graph.add_edge(pydot.Edge(root, child, color='blue'))

        self.childs.append(root)
          
    
    def pre_visitInitializer(self, node):
        self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'Initializer'))
        self.childs.append(self.nodeNum)
        self.nodeNum += 1
          
    def visitInitializer(self, node):
        chs = self.collectCH(node.childNo)
        root = self.collectCH(1).pop()
        for child in chs:
           self.graph.add_edge(pydot.Edge(root, child, color='blue'))

        self.childs.append(root)
          

    def pre_visitMethodSuf(self, node):
        self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'MethodSuffix'))
        self.childs.append(self.nodeNum)
        self.nodeNum += 1
          
    def visitMethodSuf(self, node):
        chs = self.collectCH(node.childNo)
        root = self.collectCH(1).pop()
        for child in chs:
           self.graph.add_edge(pydot.Edge(root, child, color='blue'))

        self.childs.append(root)
          
    
    def pre_visitMethodBody(self, node):
        self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'methodbody'))
        self.childs.append(self.nodeNum)
        self.nodeNum += 1
        
          
    def visitMethodBody(self, node):
        chs = self.collectCH(node.childNo)
        root = self.collectCH(1).pop()
        for child in chs:
           self.graph.add_edge(pydot.Edge(root, child, color='blue'))

        self.childs.append(root)
        
    
    def pre_visitParameterList(self, node):
        self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'ParameterList'))
        self.childs.append(self.nodeNum)
        self.nodeNum += 1
          
    def visitParameterList(self, node):
        chs = self.collectCH(node.childNo)
        root = self.collectCH(1).pop()
        for child in chs:
           self.graph.add_edge(pydot.Edge(root, child, color='blue'))

        self.childs.append(root)
          

    def pre_visitParameter(self, node):
        self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'Parameter: ' + node.id))
        self.childs.append(self.nodeNum)
        self.nodeNum += 1
          
    def visitParameter(self, node):
        chs = self.collectCH(node.childNo)
        root = self.collectCH(1).pop()
        for child in chs:
           self.graph.add_edge(pydot.Edge(root, child, color='blue'))

        self.childs.append(root)
          
    
    def pre_visitVarDecl(self, node):
        self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'varDecl: ' + node.id))
        self.childs.append(self.nodeNum)
        self.nodeNum += 1
        
    
    def visitVarDecl(self, node):
        chs = self.collectCH(node.childNo)
        root = self.collectCH(1).pop()
        for child in chs:
           self.graph.add_edge(pydot.Edge(root, child, color='blue'))

        self.childs.append(root)



   # def visitStatement(node):
    #      

    
    def pre_visitcurlyBrackStatement(self, Node):
       self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'CurlyBrackStatement'))
       self.childs.append(self.nodeNum)
       self.nodeNum += 1
         
    def visitcurlyBrackStatement(self, Node):
       chs = self.collectCH(Node.childNo)
       root = self.collectCH(1).pop()
       for child in chs:
          self.graph.add_edge(pydot.Edge(root, child, color='blue'))

       self.childs.append(root)
         

    def pre_visitexpressionStatement(self, Node):
       self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'ExpressionStatement'))
       self.childs.append(self.nodeNum)
       self.nodeNum += 1
         
    def visitexpressionStatement(self, Node):
       chs = self.collectCH(Node.childNo)
       root = self.collectCH(1).pop()
       for child in chs:
          self.graph.add_edge(pydot.Edge(root, child, color='blue'))

       self.childs.append(root)
         

    def pre_visitifStatement(self, Node):
       self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'IfStatement'))
       self.childs.append(self.nodeNum)
       self.nodeNum += 1
         
    def visitifStatement(self, Node):
       chs = self.collectCH(Node.childNo)
       root = self.collectCH(1).pop()
       for child in chs:
          self.graph.add_edge(pydot.Edge(root, child, color='blue'))

       self.childs.append(root)
         

    def pre_visitwhileStatement(self, Node):
       self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'WhileStatement'))
       self.childs.append(self.nodeNum)
       self.nodeNum += 1
         
    def visitwhileStatement(self, Node):
       chs = self.collectCH(Node.childNo)
       root = self.collectCH(1).pop()
       for child in chs:
          self.graph.add_edge(pydot.Edge(root, child, color='blue'))

       self.childs.append(root)
         


    def pre_visitreturnStatement(self, Node):
       self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'ReturnStatement'))
       self.childs.append(self.nodeNum)
       self.nodeNum += 1
         
    def visitreturnStatement(self, Node):
       chs = self.collectCH(Node.childNo)
       root = self.collectCH(1).pop()
       for child in chs:
          self.graph.add_edge(pydot.Edge(root, child, color='blue'))

       self.childs.append(root)
       
         
   
    def pre_visitcoutStatement(self, Node):
       self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'CoutStatement'))
       self.childs.append(self.nodeNum)
       self.nodeNum += 1
         
    def visitcoutStatement(self, Node):
       chs = self.collectCH(Node.childNo)
       root = self.collectCH(1).pop()
       for child in chs:
          self.graph.add_edge(pydot.Edge(root, child, color='blue'))

       self.childs.append(root)
         

    def pre_visitcinStatement(self, Node):
       self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'CinStatement'))
       self.childs.append(self.nodeNum)
       self.nodeNum += 1
         
    def visitcinStatement(self, Node):
       chs = self.collectCH(Node.childNo)
       root = self.collectCH(1).pop()
       for child in chs:
          self.graph.add_edge(pydot.Edge(root, child, color='blue'))

       self.childs.append(root)
         

    def pre_visitswitchStatement(self, Node):
       self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'SwitchStatement'))
       self.childs.append(self.nodeNum)
       self.nodeNum += 1
         
    def visitswitchStatement(self, Node):
       chs = self.collectCH(Node.childNo)
       root = self.collectCH(1).pop()
       for child in chs:
          self.graph.add_edge(pydot.Edge(root, child, color='blue'))

       self.childs.append(root)
         

    def visitbreakStatement(self, Node):
       self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'BreakStatement'))
       self.childs.append(self.nodeNum)
       self.nodeNum += 1
         
   
    def pre_visitvarDeclStatement(self, Node):
       self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'VaraibleDeclarationStatement'))
       self.childs.append(self.nodeNum)
       self.nodeNum += 1
         
    def visitvarDeclStatement(self, Node):
       chs = self.collectCH(Node.childNo)
       root = self.collectCH(1).pop()
       for child in chs:
          self.graph.add_edge(pydot.Edge(root, child, color='blue'))

       self.childs.append(root)
         

#end of statements
    def pre_visitCaseBlock(self, node):
      self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'CaseBlock'))
      self.childs.append(self.nodeNum)
      self.nodeNum += 1
        
    def visitCaseBlock(self, node):
      chs = self.collectCH(node.childNo)
      root = self.collectCH(1).pop()
      for child in chs:
         self.graph.add_edge(pydot.Edge(root, child, color='blue'))

      self.childs.append(root)  

        
    
    def pre_visitCase(self, node):
      self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'Case: ' + str(node.value)))
      self.childs.append(self.nodeNum)
      self.nodeNum += 1
        
        
    def visitCase(self, node):
      chs = self.collectCH(node.childNo)
      root = self.collectCH(1).pop()
      for child in chs:
         self.graph.add_edge(pydot.Edge(root, child, color='blue'))

      self.childs.append(root)   
        

#    def visitExpression(node):         


    def pre_visitassignmentExpression(self, Node):
      self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'AssignmentExpression'))
      self.childs.append(self.nodeNum)
      self.nodeNum += 1 
        
    def visitassignmentExpression(self, Node):
      chs = self.collectCH(Node.childNo)
      root = self.collectCH(1).pop()
      for child in chs:
         self.graph.add_edge(pydot.Edge(root, child, color='blue'))

      self.childs.append(root) 
        
   

    def pre_visitaddAssignmentExpression(self, Node):
      self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'addAssignmentExpression'))
      self.childs.append(self.nodeNum)
      self.nodeNum += 1 
        
    def visitaddAssignmentExpression(self, Node):
      chs = self.collectCH(Node.childNo)
      root = self.collectCH(1).pop()
      for child in chs:
         self.graph.add_edge(pydot.Edge(root, child, color='blue'))

      self.childs.append(root) 
        

    def pre_visitsubAssignmentExpression(self, Node):
      self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'subAssignmentExpression'))
      self.childs.append(self.nodeNum)
      self.nodeNum += 1 
        
    def visitsubAssignmentExpression(self, Node):
      chs = self.collectCH(Node.childNo)
      root = self.collectCH(1).pop()
      for child in chs:
         self.graph.add_edge(pydot.Edge(root, child, color='blue'))

      self.childs.append(root) 
        
   
    def pre_visitmultAssignmentExpression(self, Node):
      self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'multAssignmentExpression'))
      self.childs.append(self.nodeNum)
      self.nodeNum += 1 
        
    def visitmultAssignmentExpression(self, Node):
      chs = self.collectCH(Node.childNo)
      root = self.collectCH(1).pop()
      for child in chs:
         self.graph.add_edge(pydot.Edge(root, child, color='blue'))

      self.childs.append(root) 
        
   
    def pre_visitdivAssignmentExpression(self, Node):
      self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'divAssignmentExpression'))
      self.childs.append(self.nodeNum)
      self.nodeNum += 1 
        
    def visitdivAssignmentExpression(self, Node):
      chs = self.collectCH(Node.childNo)
      root = self.collectCH(1).pop()
      for child in chs:
         self.graph.add_edge(pydot.Edge(root, child, color='blue'))

      self.childs.append(root) 
        
 
    def pre_visitplusExpression(self, Node):
      self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'PlusExpression'))
      self.childs.append(self.nodeNum)
      self.nodeNum += 1 
        
    def visitplusExpression(self, Node):
      chs = self.collectCH(Node.childNo)
      root = self.collectCH(1).pop()
      for child in chs:
         self.graph.add_edge(pydot.Edge(root, child, color='blue'))

      self.childs.append(root) 
        
   
    def pre_visitminusExpression(self, Node):
      self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'MinusExpression'))
      self.childs.append(self.nodeNum)
      self.nodeNum += 1 
        
    def visitminusExpression(self, Node):
      chs = self.collectCH(Node.childNo)
      root = self.collectCH(1).pop()
      for child in chs:
         self.graph.add_edge(pydot.Edge(root, child, color='blue'))

      self.childs.append(root) 
        
   
    def pre_visitmultExpression(self, Node):
      self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'MultExpression'))
      self.childs.append(self.nodeNum)
      self.nodeNum += 1 
        
    def visitmultExpression(self, Node):
      chs = self.collectCH(Node.childNo)
      root = self.collectCH(1).pop()
      for child in chs:
         self.graph.add_edge(pydot.Edge(root, child, color='blue'))

      self.childs.append(root) 
        
   
    def pre_visitdivExpression(self, Node):
      self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'DivExpression'))
      self.childs.append(self.nodeNum)
      self.nodeNum += 1 
        
    def visitdivExpression(self, Node):
      chs = self.collectCH(Node.childNo)
      root = self.collectCH(1).pop()
      for child in chs:
         self.graph.add_edge(pydot.Edge(root, child, color='blue'))

      self.childs.append(root) 
        
   
    def pre_visitequalityExpression(self, Node):
      self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'EqualityExpression'))
      self.childs.append(self.nodeNum)
      self.nodeNum += 1 
        
    def visitequalityExpression(self, Node):
      chs = self.collectCH(Node.childNo)
      root = self.collectCH(1).pop()
      for child in chs:
         self.graph.add_edge(pydot.Edge(root, child, color='blue'))

      self.childs.append(root) 
        

    def pre_visitnotEqualExpression(self, Node):
      self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'notEqualExpression'))
      self.childs.append(self.nodeNum)
      self.nodeNum += 1 
        
    def visitnotEqualExpression(self, Node):
      chs = self.collectCH(Node.childNo)
      root = self.collectCH(1).pop()
      for child in chs:
         self.graph.add_edge(pydot.Edge(root, child, color='blue'))

      self.childs.append(root) 
        

    def pre_visitlessThanExpression(self, Node):
      self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'lessThanExpression'))
      self.childs.append(self.nodeNum)
      self.nodeNum += 1 
        
    def visitlessThanExpression(self, Node):
      chs = self.collectCH(Node.childNo)
      root = self.collectCH(1).pop()
      for child in chs:
         self.graph.add_edge(pydot.Edge(root, child, color='blue'))

      self.childs.append(root) 
        

    def pre_visitgreaterThanExpression(self, Node):
      self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'greaterThanExpression'))
      self.childs.append(self.nodeNum)
      self.nodeNum += 1 
        
    def visitgreaterThanExpression(self, Node):
      chs = self.collectCH(Node.childNo)
      root = self.collectCH(1).pop()
      for child in chs:
         self.graph.add_edge(pydot.Edge(root, child, color='blue'))

      self.childs.append(root) 
        
   
    def pre_visitLTEqualsExpression(self, Node):
      self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'LTEqualsExpression'))
      self.childs.append(self.nodeNum)
      self.nodeNum += 1 
        
    def visitLTEqualsExpression(self, Node):
      chs = self.collectCH(Node.childNo)
      root = self.collectCH(1).pop()
      for child in chs:
         self.graph.add_edge(pydot.Edge(root, child, color='blue'))

      self.childs.append(root) 
        

    def pre_visitGTEqualsExpression(self, Node):
      self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'GTEqualsExpression'))
      self.childs.append(self.nodeNum)
      self.nodeNum += 1 
        
    def visitGTEqualsExpression(self, Node):
      chs = self.collectCH(Node.childNo)
      root = self.collectCH(1).pop()
      for child in chs:
         self.graph.add_edge(pydot.Edge(root, child, color='blue'))

      self.childs.append(root) 
        
   
    def pre_visitandExpression(self, Node):
      self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'andExpression'))
      self.childs.append(self.nodeNum)
      self.nodeNum += 1 
        
    def visitandExpression(self, Node):
      chs = self.collectCH(Node.childNo)
      root = self.collectCH(1).pop()
      for child in chs:
         self.graph.add_edge(pydot.Edge(root, child, color='blue'))

      self.childs.append(root) 
        

    def pre_visitorExpression(self, Node):
      self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'orExpression'))
      self.childs.append(self.nodeNum)
      self.nodeNum += 1 
        
    def visitorExpression(self, Node):
      chs = self.collectCH(Node.childNo)
      root = self.collectCH(1).pop()
      for child in chs:
         self.graph.add_edge(pydot.Edge(root, child, color='blue'))

      self.childs.append(root) 
        
       
    def pre_visitnotExpression(self, Node):
      self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'notExpression'))
      self.childs.append(self.nodeNum)
      self.nodeNum += 1 
        
    def visitnotExpression(self, Node):
      chs = self.collectCH(Node.childNo)
      root = self.collectCH(1).pop()
      for child in chs:
         self.graph.add_edge(pydot.Edge(root, child, color='blue'))

      self.childs.append(root)
        

    def pre_visitunaryPlusExpression(self, Node):
      self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'unaryPlusExpression'))
      self.childs.append(self.nodeNum)
      self.nodeNum += 1 
        
    def visitunaryPlusExpression(self, Node):
      chs = self.collectCH(Node.childNo)
      root = self.collectCH(1).pop()
      for child in chs:
         self.graph.add_edge(pydot.Edge(root, child, color='blue'))

      self.childs.append(root)
        

    def pre_visitunaryMinusExpression(self, Node):
      self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'unaryMinusExpression'))
      self.childs.append(self.nodeNum)
      self.nodeNum += 1 
        
    def visitunaryMinusExpression(self, Node):
      chs = self.collectCH(Node.childNo)
      root = self.collectCH(1).pop()
      for child in chs:
         self.graph.add_edge(pydot.Edge(root, child, color='blue'))

      self.childs.append(root)
        

    def visitliteralIntExpression(self, Node):
      self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'literalIntexpression: ' + str(Node.value)))
      self.childs.append(self.nodeNum)
      self.nodeNum += 1
   
        

    def visitliteralCharExpression(self, Node):
      self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'literalCharexpression: ' + Node.value))
      self.childs.append(self.nodeNum)
      self.nodeNum += 1
   
        
   
    def visitliteralStringExpression(self, Node):
      self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'literalStringexpression: ' + Node.value))
      self.childs.append(self.nodeNum)
      self.nodeNum += 1
        

    def visittrueExpression(self, Node):
      self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'trueexpression'))
      self.childs.append(self.nodeNum)
      self.nodeNum += 1
   
        

    def visitfalseExpression(self, Node):
      self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'falseexpression'))
      self.childs.append(self.nodeNum)
      self.nodeNum += 1
   
        
   
    def visitnullExpression(self, Node):
      self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'nullexpression'))
      self.childs.append(self.nodeNum)
      self.nodeNum += 1
   
        
   
    def visitidentifierExpression(self, Node):
      self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'identifierexp: ' + Node.value))
      self.childs.append(self.nodeNum)
      self.nodeNum += 1
      
   
        
   
    def visitthisExpression(self, Node):
      self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'thisExpression'))
      self.childs.append(self.nodeNum)
      self.nodeNum += 1
   
        

    def pre_visitcallExpression(self, Node):
      self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'callExpression'))
      self.childs.append(self.nodeNum)
      self.nodeNum += 1
   
        
    def visitcallExpression(self, Node):
      chs = self.collectCH(Node.childNo)
      root = self.collectCH(1).pop()
      for child in chs:
         self.graph.add_edge(pydot.Edge(root, child, color='blue'))

      self.childs.append(root) 
   
        

    def pre_visitarrayExpression(self, Node):
      self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'arrayExpression'))
      self.childs.append(self.nodeNum)
      self.nodeNum += 1
   
        
    def visitarrayExpression(self, Node):
      chs = self.collectCH(Node.childNo)
      root = self.collectCH(1).pop()
      for child in chs:
         self.graph.add_edge(pydot.Edge(root, child, color='blue'))

      self.childs.append(root) 
   
        

    def pre_visitperiodExpression(self, Node):
      self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'periodExpression: ' + Node.id))
      self.childs.append(self.nodeNum)
      self.nodeNum += 1
   
        
    def visitperiodExpression(self, Node):
      chs = self.collectCH(Node.childNo)
      root = self.collectCH(1).pop()
      for child in chs:
         self.graph.add_edge(pydot.Edge(root, child, color='blue'))

      self.childs.append(root) 
   
        

    def pre_visitnewExpression(self, Node):
      self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'newExpression'))
      self.childs.append(self.nodeNum)
      self.nodeNum += 1
   
        
    def visitnewExpression(self, Node):
      chs = self.collectCH(Node.childNo)
      root = self.collectCH(1).pop()
      for child in chs:
         self.graph.add_edge(pydot.Edge(root, child, color='blue'))

      self.childs.append(root) 
   
        
   
    def pre_visitparenExpression(self, Node):
      self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'parenExpression'))
      self.childs.append(self.nodeNum)
      self.nodeNum += 1
   
        
    def visitparenExpression(self, Node):
      chs = self.collectCH(Node.childNo)
      root = self.collectCH(1).pop()
      for child in chs:
         self.graph.add_edge(pydot.Edge(root, child, color='blue'))

      self.childs.append(root) 
   
        

#end of expressions




    def pre_visitArguments(self, node):
      self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'Arguments'))
      self.childs.append(self.nodeNum)
      self.nodeNum += 1
      
    def visitArguments(self, node):
      chs = self.collectCH(node.childNo)
      root = self.collectCH(1).pop()
      for child in chs:
         self.graph.add_edge(pydot.Edge(root, child, color='blue'))

      self.childs.append(root) 
    

    def pre_visitArgumentList(self, node):
      self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'ArgumentList'))
      self.childs.append(self.nodeNum)
      self.nodeNum += 1
    def visitArgumentList(self, node):
      chs = self.collectCH(node.childNo)
      root = self.collectCH(1).pop()
      for child in chs:
         self.graph.add_edge(pydot.Edge(root, child, color='blue'))

      self.childs.append(root) 
        
    

    def pre_visitIndex(self, node):
      self.graph.add_node(pydot.Node(self.nodeNum, shape='circle', label = 'Index'))
      self.childs.append(self.nodeNum)
      self.nodeNum += 1

    def visitIndex(self, node):
      chs = self.collectCH(node.childNo)
      root = self.collectCH(1).pop()
      for child in chs:
         self.graph.add_edge(pydot.Edge(root, child, color='blue'))

      self.childs.append(root) 
        




#only push and pop off the stack when we pre vist and post vist
#if we are checking a higher scope for declaration just refer to points in the stack instead of popping off
#when we post visit a classdef pop the stack and append it to self.classSTS and the same for functionandconstructor
#use $ in ids and temp vars i create to ensure that an id or varname in the tescase cant be the same
class STVisitor(Visitor):
   def __init__(self):
      self.globalST = SymbolTable('global')
      self.classSTS = []
      self.functionSTS = []
      self.stack = []
      self.current = 0 #max depth for stack will be index 2, to keep track of that place should we just use current as a index tracker????
      self.errorCounter = 0 #if double declared variables exist
      self.constrCounter = 0 #keeps track of how many constructors are within a class. #constructors must also have the same name as its parent, but do they need return statements?
      self.stack.append(self.globalST)

   def printError(self, id, lineno1):
      typeval,lineno2,isarr,modifier,isfun,ispar = self.stack[self.current].lookup(id)
      print('Error: Double declared variable detected within scope', self.stack[self.current].name, 'for variable id:', id, 'located on lines', str(lineno1), 'and', str(lineno2))
      self.errorCounter += 1

   def pre_visitCompUnit(self, node):
      #append a symbol for the main function to the global scope
      #check if main is already declared in the global scope
      if(self.stack[self.current].checkKey(node.id)):
         #print('double declared variable detected for variable name', node.id, 'locate on linenumber', node.lineno)
         self.printError(node.id, node.lineNum)
      #should we have the next two lines be in an else: or just stand alone as is since we need to continues and detect other errors
      #but one warning this could end up overwriting the current id within the symbol table
      self.stack[self.current].insert(node.id, 'void', node.lineNum, False, '', True)
      self.stack.append(SymbolTable(node.id, self.globalST.name))
      self.current +=1
      
   def visitCompUnit(self, node):
      #pop the main function scope off
      #also pop the global scope off the stack and either append it to classSTS or reassign it to self.globalST
      self.functionSTS.append(self.stack.pop())
      self.current -= 1
      self.globalST = self.stack.pop()
      self.current -= 1
      
   def pre_visitClassDef(self, node):
      self.constrCounter = 0
      if(self.stack[self.current].checkKey(node.id)):
         #print('double declared variable detected for variable name', node.id, 'locate on linenumber', node.lineno)
         self.printError(node.id, node.lineNum)
     
      self.stack[self.current].insert(node.id, node.id, node.lineNum)
      #classes can only be defined in the global scope
      self.stack.append(SymbolTable(node.id))
      self.current += 1
      
   def visitClassDef(self, node):
      self.classSTS.append(self.stack.pop())
      self.current -= 1
      #check to see if a constructor was declared
      #alduos says they could provide one or not but cant be more than 1 
      if self.constrCounter > 1:
         print('Error: A class cant have more than one constructor. Error detected within class', node.id, 'on line', node.lineNum)
         self.errorCounter += 1
      
   def visitTypeN(self, node):
      pass
   def visitModifierN(self, node):
      pass

   def pre_visitClassMemDef(self, node):
      pass
   def visitClassMemDef(self, node):
      pass
   def pre_visitDataMemDecl(self, node):
      pass
   def visitDataMemDecl(self, node):
      #still need to attach the modifier
      #need to get the variable declaration id
      typeval,lineno2,isarr,modifier,isfun,ispar = self.stack[self.current].lookup(node.child2.id)
     
      self.stack[self.current].insert(node.child2.id,typeval,lineno2,isarr,node.child1.value,isfun,ispar)
      
   def pre_visitMethodDecl(self, node):
      if(self.stack[self.current].checkKey(node.id)):
         #print('double declared variable detected for variable name', node.id, 'locate on linenumber', node.lineno)
         self.printError(node.id, node.lineNum)
     
      self.stack[self.current].insert(node.id, node.childN2.valType, node.lineNum, node.isBrack, node.childN1.value, True)
      self.stack.append(SymbolTable(node.id, self.stack[self.current].name))
      self.current += 1
      
   def visitMethodDecl(self, node):
      self.functionSTS.append(self.stack.pop())
      self.current -= 1

   
   def pre_visitConstructorDecl(self, node):
      self.constrCounter += 1
      if self.constrCounter > 1:
         print('Error: Declared too many constructors for the class',self.stack[self.current].name,'on line', node.lineNum)
         self.errorCounter += 1
      if(self.stack[self.current].checkKey(node.id)):
         #print('double declared variable detected for variable name', node.id, 'locate on linenumber', node.lineno)
         self.printError(node.id, node.lineNum)
      elif (self.stack[self.current].name != node.id):
         print('Error: constructor function does not match the name of the class, error found on line', node.lineNum)
         self.errorCounter += 1
     
      self.stack[self.current].insert(node.id, node.id, node.lineNum, False, '', True)
      self.stack.append(SymbolTable(node.id, self.stack[self.current].name))
      self.current += 1
      
   def visitConstructorDecl(self, node):
      self.functionSTS.append(self.stack.pop())
      self.current -= 1
      
   def pre_visitInitializer(self, node):
      pass
   def visitInitializer(self, node):
      pass
   def pre_visitMethodSuf(self, node):
      pass
   def visitMethodSuf(self, node):
      pass
   def pre_visitMethodBody(self, node):
      pass
   def visitMethodBody(self, node):
      pass
   def pre_visitParameterList(self, node):
      pass
   def visitParameterList(self, node):
      pass
   def pre_visitParameter(self, node):
      pass
   def visitParameter(self, node):
      if(self.stack[self.current].checkKey(node.id)):
         #print('double declared variable detected for variable name', node.id, 'locate on linenumber', node.lineno)
         self.printError(node.id, node.lineNum)
      if node.childN1.valType == 'void':
         print('Error: you cannot have a void type as a parameter. Error on line', node.lineNum)
         self.errorCounter +=1
      else:
         self.stack[self.current].insert(node.id, node.childN1.valType, node.lineNum, node.isBrack, '', False, True)
      
   def pre_visitVarDecl(self, node):
      pass
   def visitVarDecl(self, node):
      if(self.stack[self.current].checkKey(node.id)):
         #print('double declared variable detected for variable name', node.id, 'locate on linenumber', node.lineno)
         self.printError(node.id, node.lineNum)
      if node.childN1.valType == 'void':
         print('Error: you cannot declare a variable with a void type. Error on line', node.lineNum)
         self.errorCounter +=1
      else:
         self.stack[self.current].insert(node.id, node.childN1.valType, node.lineNum, node.isBrack, '', False, False)
     
      pass
   def pre_visitcurlyBrackStatement(self, Node):
      pass
   def visitcurlyBrackStatement(self, Node):
      pass
   def pre_visitexpressionStatement(self, Node):
      pass

   def visitexpressionStatement(self, Node):
      pass

   def pre_visitifStatement(self, Node):
      pass
   def visitifStatement(self, Node):
      pass

   def pre_visitwhileStatement(self, Node):
      pass
   def visitwhileStatement(self, Node):
      pass

   def pre_visitreturnStatement(self, Node):
      pass
   def visitreturnStatement(self, Node):
      pass

   def pre_visitcoutStatement(self, Node):
      pass
   def visitcoutStatement(self, Node):
      pass

   def pre_visitcinStatement(self, Node):
      pass
   def visitcinStatement(self, Node):
      pass

   def pre_visitswitchStatement(self, Node):
      pass
   def visitswitchStatement(self, Node):
      pass

   def visitbreakStatement(self, Node):
      pass

   def pre_visitvarDeclStatement(self, Node):
      pass
   def visitvarDeclStatement(self, Node):
      pass

#end of statements
   def pre_visitCaseBlock(self, node):
      pass
   def visitCaseBlock(self, node):
      pass
   def pre_visitCase(self, node):
      pass
   def visitCase(self, node):
      pass


#    def visitExpression(node):

   def pre_visitassignmentExpression(self, Node):
      pass
   def visitassignmentExpression(self, Node):
      pass

   def pre_visitaddAssignmentExpression(self, Node):
      pass
   def visitaddAssignmentExpression(self, Node):
      pass

   def pre_visitsubAssignmentExpression(self, Node):
      pass
   def visitsubAssignmentExpression(self, Node):
      pass

   def pre_visitmultAssignmentExpression(self, Node):
      pass
   def visitmultAssignmentExpression(self, Node):
      pass
   

   def pre_visitdivAssignmentExpression(self, Node):
      pass
   def visitdivAssignmentExpression(self, Node):
      pass

   def pre_visitplusExpression(self, Node):
      pass
   def visitplusExpression(self, Node):
      pass

   def pre_visitminusExpression(self, Node):
      pass
   def visitminusExpression(self, Node):
      pass

   def pre_visitmultExpression(self, Node):
      pass
   def visitmultExpression(self, Node):
      pass

   def pre_visitdivExpression(self, Node):
      pass
   def visitdivExpression(self, Node):
      pass

   def pre_visitequalityExpression(self, Node):
      pass
   def visitequalityExpression(self, Node):
      pass

   def pre_visitnotEqualExpression(self, Node):
      pass
   def visitnotEqualExpression(self, Node):
      pass

   def pre_visitlessThanExpression(self, Node):
      pass
   def visitlessThanExpression(self, Node):
      pass

   def pre_visitgreaterThanExpression(self, Node):
      pass
   def visitgreaterThanExpression(self, Node):
      pass

   def pre_visitLTEqualsExpression(self, Node):
      pass
   def visitLTEqualsExpression(self, Node):
      pass

   def pre_visitGTEqualsExpression(self, Node):
      pass
   def visitGTEqualsExpression(self, Node):
      pass

   def pre_visitandExpression(self, Node):
      pass
   def visitandExpression(self, Node):
      pass

   def pre_visitorExpression(self, Node):
      pass
   def visitorExpression(self, Node):
      pass
      
   def pre_visitnotExpression(self, Node):
      pass
   def visitnotExpression(self, Node):
      pass

   def pre_visitunaryPlusExpression(self, Node):
      pass
   def visitunaryPlusExpression(self, Node):
      pass

   def pre_visitunaryMinusExpression(self, Node):
      pass
   def visitunaryMinusExpression(self, Node):
      pass

   def visitliteralIntExpression(self, Node):
      pass

   def visitliteralCharExpression(self, Node):
      pass

   def visitliteralStringExpression(self, Node):
      pass

   def visittrueExpression(self, Node):
      pass

   def visitfalseExpression(self, Node):
      pass

   def visitnullExpression(self, Node):
      pass

   def visitidentifierExpression(self, Node):
      pass

   def visitthisExpression(self, Node):
      pass

   def pre_visitcallExpression(self, Node):
      pass
   def visitcallExpression(self, Node):
      pass

   def pre_visitarrayExpression(self, Node):
      pass
   def visitarrayExpression(self, Node):
      pass

   def pre_visitperiodExpression(self, Node):
      pass
   def visitperiodExpression(self, Node):
      pass

   def pre_visitnewExpression(self, Node):
      pass
   def visitnewExpression(self, Node):
      pass

   def pre_visitparenExpression(self, Node):
      pass
   def visitparenExpression(self, Node):
      pass

#end of expressions

   def pre_visitArguments(self, node):
      pass
   def visitArguments(self, node):
      pass
   def pre_visitArgumentList(self, node):
      pass
   def visitArgumentList(self, node):
      pass
   def pre_visitIndex(self, node):
      pass
   def visitIndex(self, node):
      pass

#check id expressions





#have a stack that has the value type of dot operator evaluations so its id type
#first check if stack is empty is so then we know we are the first dot operator to execute, then check if our child is a certain type
#if its an id then look it up in our scope and gets type value and look that up in the global scope for its class scope get it then look up if my id exists within that scope if so then 
#get my id type and put it on the stack(or only put it on the stack if its a type id not our already defined ones) also check if the varialbes modifier is public
#if stack wasnt empty then pop it off and check if it exists in the global scope and then get its scope, from there check if my id exists in the scope
#and if so then put my ids type onto the stack.
#might have to also make arrays and function calls put things on the stack, functions can return arrays of a type
#typecheck() or maybe have nodes return things or store in a stack or container for me to use later 

class UndeclaredVisitor(Visitor):
   def __init__(self, globalst, classsts, functionsts):
      self.globalST = globalst
      self.classSTS = classsts
      self.functionSTS = functionsts
      self.stack = []
      self.current = 0 #max depth for stack will be index 2, to keep track of that place should we just use current as a index tracker????
      self.errorCounter = 0 
      self.stack.append(self.globalST)
      self.typestack = [] #hold past types that were used and defined
      self.prevdots = []
      self.thisflag = False


   def findClassST(self,name):
      for st in self.classSTS:
         if st.name == name:
            return st
   
   def findFunctionST(self,name, parentN):
      for st in self.functionSTS:
         if st.name == name and st.parent == parentN:
            return st


   def pre_visitCompUnit(self, node):
      self.stack.append(self.findFunctionST(node.id, 'global'))
      self.current += 1
      
   def visitCompUnit(self, node):
      #pop the scope off
      self.stack.pop()
      self.current -= 1
      
   def pre_visitClassDef(self, node):
      self.stack.append(self.findClassST(node.id))
      self.current += 1
      
   def visitClassDef(self, node):
      #pop the scope off
      self.stack.pop()
      self.current -= 1

      
   def visitTypeN(self, node):
      pass
   def visitModifierN(self, node):
      pass
   def pre_visitClassMemDef(self, node):
      pass
   def visitClassMemDef(self, node):
      pass
   def pre_visitDataMemDecl(self, node):
      pass
   def visitDataMemDecl(self, node):
      pass
   def pre_visitMethodDecl(self, node):
      self.stack.append(self.findFunctionST(node.id, self.stack[self.current].name))
      self.current += 1
      
   def visitMethodDecl(self, node):
      #pop the scope off
      self.stack.pop()
      self.current -= 1
      
   def pre_visitConstructorDecl(self, node):
      self.stack.append(self.findFunctionST(node.id, self.stack[self.current].name))
      self.current += 1
      
   def visitConstructorDecl(self, node):
      #pop the scope off
      self.stack.pop()
      self.current -= 1
      
   def pre_visitInitializer(self, node):
      pass
   def visitInitializer(self, node):
      pass
   def pre_visitMethodSuf(self, node):
      pass
   def visitMethodSuf(self, node):
      pass
   def pre_visitMethodBody(self, node):
      pass
   def visitMethodBody(self, node):
      pass
   def pre_visitParameterList(self, node):
      pass
   def visitParameterList(self, node):
      pass
   def pre_visitParameter(self, node):
      pass
   def visitParameter(self, node):
      pass
   def pre_visitVarDecl(self, node):
      pass
   def visitVarDecl(self, node):
      pass
   def pre_visitcurlyBrackStatement(self, Node):
      pass
   def visitcurlyBrackStatement(self, Node):
      pass
   def pre_visitexpressionStatement(self, Node):
      pass

   def visitexpressionStatement(self, Node):
      pass

   def pre_visitifStatement(self, Node):
      pass
   def visitifStatement(self, Node):
      pass

   def pre_visitwhileStatement(self, Node):
      pass
   def visitwhileStatement(self, Node):
      pass

   def pre_visitreturnStatement(self, Node):
      pass
   def visitreturnStatement(self, Node):
      pass

   def pre_visitcoutStatement(self, Node):
      pass
   def visitcoutStatement(self, Node):
      pass

   def pre_visitcinStatement(self, Node):
      pass
   def visitcinStatement(self, Node):
      pass

   def pre_visitswitchStatement(self, Node):
      pass
   def visitswitchStatement(self, Node):
      pass

   def visitbreakStatement(self, Node):
      pass

   def pre_visitvarDeclStatement(self, Node):
      pass
   def visitvarDeclStatement(self, Node):
      pass

#end of statements
   def pre_visitCaseBlock(self, node):
      pass
   def visitCaseBlock(self, node):
      pass
   def pre_visitCase(self, node):
      pass
   def visitCase(self, node):
      pass


#    def visitExpression(node):

   def pre_visitassignmentExpression(self, Node):
      pass
   def visitassignmentExpression(self, Node):
      pass

   def pre_visitaddAssignmentExpression(self, Node):
      pass
   def visitaddAssignmentExpression(self, Node):
      pass

   def pre_visitsubAssignmentExpression(self, Node):
      pass
   def visitsubAssignmentExpression(self, Node):
      pass

   def pre_visitmultAssignmentExpression(self, Node):
      pass
   def visitmultAssignmentExpression(self, Node):
      pass
   

   def pre_visitdivAssignmentExpression(self, Node):
      pass
   def visitdivAssignmentExpression(self, Node):
      pass

   def pre_visitplusExpression(self, Node):
      pass
   def visitplusExpression(self, Node):
      pass

   def pre_visitminusExpression(self, Node):
      pass
   def visitminusExpression(self, Node):
      pass

   def pre_visitmultExpression(self, Node):
      pass
   def visitmultExpression(self, Node):
      pass

   def pre_visitdivExpression(self, Node):
      pass
   def visitdivExpression(self, Node):
      pass

   def pre_visitequalityExpression(self, Node):
      pass
   def visitequalityExpression(self, Node):
      pass

   def pre_visitnotEqualExpression(self, Node):
      pass
   def visitnotEqualExpression(self, Node):
      pass

   def pre_visitlessThanExpression(self, Node):
      pass
   def visitlessThanExpression(self, Node):
      pass

   def pre_visitgreaterThanExpression(self, Node):
      pass
   def visitgreaterThanExpression(self, Node):
      pass

   def pre_visitLTEqualsExpression(self, Node):
      pass
   def visitLTEqualsExpression(self, Node):
      pass

   def pre_visitGTEqualsExpression(self, Node):
      pass
   def visitGTEqualsExpression(self, Node):
      pass

   def pre_visitandExpression(self, Node):
      pass
   def visitandExpression(self, Node):
      pass

   def pre_visitorExpression(self, Node):
      pass
   def visitorExpression(self, Node):
      pass
      
   def pre_visitnotExpression(self, Node):
      pass
   def visitnotExpression(self, Node):
      pass

   def pre_visitunaryPlusExpression(self, Node):
      pass
   def visitunaryPlusExpression(self, Node):
      pass

   def pre_visitunaryMinusExpression(self, Node):
      pass
   def visitunaryMinusExpression(self, Node):
      pass

   def visitliteralIntExpression(self, Node):
      pass

   def visitliteralCharExpression(self, Node):
      pass

   def visitliteralStringExpression(self, Node):
      pass

   def visittrueExpression(self, Node):
      pass

   def visitfalseExpression(self, Node):
      pass

   def visitnullExpression(self, Node):
      pass

   def visitidentifierExpression(self, Node):
      for scope in reversed(range(len(self.stack))):
         if self.stack[scope].checkKey(Node.value):
            #break out of the loop
            typeval, lineno, isarray, modifier, isfunction, isparameter = self.stack[scope].lookup(Node.value)
            if isarray:
               self.typestack.append(typeval+'$reference')
            else:
               self.typestack.append(typeval)

            
            break
         elif scope == 1:
            print('Error: variable', Node.value, 'is undeclared, located on line', Node.lineNum)
            self.errorCounter += 1



      

   def visitthisExpression(self, Node):
      if self.current == 2:
         self.typestack.append(self.stack[self.current].parent)
         self.thisflag = True
      else:
         print('Error: this can only be used within the function/method scope of a class, Error: located on line', Node.lineNum)
         self.errorCounter += 1
      pass

   def pre_visitcallExpression(self, Node):
      #self.prevdots.append(self.typestack)
      pass
   def visitcallExpression(self, Node):
      #self.typestack = self.prevdots.pop()
      pass

   def pre_visitarrayExpression(self, Node):
      pass

   def visitarrayExpression(self, Node):
      value = self.typestack.pop()
      #strip reference off since we know that we have an index to go along with it 
      lengthstr = len(value)
      lengthstr -= 10
      value = value[:lengthstr]
      #value = value[.strip('$reference')]
      self.typestack.append(value)

   def pre_visitperiodExpression(self, Node):
      #if there is anything on the stack get rid of it 
      if len(self.typestack) > 0:
         self.typestack.clear()
      
   def visitperiodExpression(self, Node):

      if len(self.typestack) == 0:
         print('expected an identifier, function call, or an array of a class type at the beginning of the dot expression on line:', Node.idLineN)
         self.errorCounter += 1
         #this only works for id allow for things like function or array on left side, maybe by adding to stack in those vissit nodes
         
      else:
         value = self.typestack.pop()

         #search the value in the global scope
         if self.stack[0].checkKey(value):
            
            for st in self.classSTS:
               if st.name == value:
                  cscope = st
                  break
            if cscope.checkKey(Node.id):
               #check if modifier is private
               typeval, lineno, isarray, modifier, isfunction, isparameter = cscope.lookup(Node.id)
               #can make a quick change here just make this set a flag in the visitor and then check it here if its on if so turn it off and dont output error
               if modifier == 'private' and (self.current != 2 or ((self.stack[self.current].parent == cscope.name and (not self.thisflag)) or self.stack[self.current].parent != cscope.name )):
                  print('Error: cannot access a data member or method in the class', cscope.name, 'that is private. Tried accessing from line', Node.idLineN)
                  self.errorCounter += 1
               else:
                  self.thisflag = False
                  if isarray:
                     self.typestack.append(typeval+'$reference')
                  else:
                     self.typestack.append(typeval)
                  
            else:
               print('Error: the class', cscope.name, 'does not contain a data member or function with the id', Node.id, 'which you tried accessing on line', Node.idLineN)
               self.errorCounter += 1
         else:
            if value in ['int', 'void', 'char','bool','string']:
               print('Error: can only access members or functions of class types, cannot access members of type', value, 'Error found on line', Node.idLineN)
               self.errorCounter += 1
            else:
               if '$reference' in value:
                  print('Error: tried accessing a reference, if its an array make sure it has an index to an object. Value was', value,'--Tried accessing from line', Node.idLineN)
                  self.errorCounter += 1
               else:
                  print('Error: tried accessing a data member or function of the class', value,'which does not exist. Tried accessing from line', Node.idLineN)
                  self.errorCounter += 1



      

   def pre_visitnewExpression(self, Node):
      pass
   def visitnewExpression(self, Node):
      pass

   def pre_visitparenExpression(self, Node):
      pass
   def visitparenExpression(self, Node):
      pass

#end of expressions
   #important if we dont set empty list to type stack then whatever changes i make to type stack replicate to prevdots elements
   def pre_visitArguments(self, node):
      self.prevdots.append(self.typestack)
      self.typestack = []
      pass
   def visitArguments(self, node):
      self.typestack = self.prevdots.pop()
      pass
   def pre_visitArgumentList(self, node):
      pass
   def visitArgumentList(self, node):
      pass
   def pre_visitIndex(self, node):
      self.prevdots.append(self.typestack)
      self.typestack = []
      
   def visitIndex(self, node):
      self.typestack = self.prevdots.pop()
      




class ValidWriteVisitor(Visitor):
   def __init__(self, globalst, classsts, functionsts):
      self.globalST = globalst
      self.classSTS = classsts
      self.functionSTS = functionsts
      self.stack = []
      self.current = 0 #max depth for stack will be index 2, to keep track of that place should we just use current as a index tracker????
      self.errorCounter = 0 
      self.stack.append(self.globalST)
      self.leftflag = False
      self.prevflags = []
      self.prevTypes = []
      self.thisflag = False

   def simpleCheck(self, Node):
      if isinstance(Node, nodes.plusExpression):
         print('Error: A plus expression cannot be written to, invalid write found on line', Node.lineNum)
         self.errorCounter += 1
         return False
      elif isinstance(Node, nodes.minusExpression):
         print('Error: A minus expression cannot be written to, invalid write found on line', Node.lineNum)
         self.errorCounter += 1
         return False
      elif isinstance(Node, nodes.multExpression):
         print('Error: A multiply expression cannot be written to, invalid write found on line', Node.lineNum)
         self.errorCounter += 1
         return False
      elif isinstance(Node, nodes.divExpression):
         print('Error: A division expression cannot be written to, invalid write found on line', Node.lineNum)
         self.errorCounter += 1
         return False
      elif isinstance(Node, nodes.equalityExpression):
         print('Error: An equality expression cannot be written to, invalid write found on line', Node.lineNum)
         self.errorCounter += 1
         return False
      elif isinstance(Node, nodes.notEqualExpression):
         print('Error: A not equal expression cannot be written to, invalid write found on line', Node.lineNum)
         self.errorCounter += 1
         return False
      elif isinstance(Node, nodes.lessThanExpression):
         print('Error: A less than expression cannot be written to, invalid write found on line', Node.lineNum)
         self.errorCounter += 1
         return False
      elif isinstance(Node, nodes.greaterThanExpression):
         print('Error: A greater than expression cannot be written to, invalid write found on line', Node.lineNum)
         self.errorCounter += 1
         return False
      elif isinstance(Node, nodes.LTEqualsExpression):
         print('Error: A less than or equals to expression cannot be written to, invalid write found on line', Node.lineNum)
         self.errorCounter += 1
         return False
      elif isinstance(Node, nodes.GTEqualsExpression):
         print('Error: A greater than or equals to expression cannot be written to, invalid write found on line', Node.lineNum)
         self.errorCounter += 1
         return False
      elif isinstance(Node, nodes.andExpression):
         print('Error: An and expression cannot be written to, invalid write found on line', Node.lineNum)
         self.errorCounter += 1
         return False
      elif isinstance(Node, nodes.orExpression):
         print('Error: An or expression cannot be written to, invalid write found on line', Node.lineNum)
         self.errorCounter += 1
         return False
      elif isinstance(Node, nodes.notExpression):
         print('Error: A not expression cannot be written to, invalid write found on line', Node.lineNum)
         self.errorCounter += 1
         return False
      elif isinstance(Node, nodes.literalIntExpression):
         print('Error: A literal integer cannot be written to, invalid write found on line', Node.lineNum)
         self.errorCounter += 1
         return False
      elif isinstance(Node, nodes.literalCharExpression):
         print('Error: A literal char cannot be written to, invalid write found on line', Node.lineNum)
         self.errorCounter += 1
         return False
      elif isinstance(Node, nodes.literalStringExpression):
         print('Error: A literal string cannot be written to, invalid write found on line', Node.lineNum)
         self.errorCounter += 1
         return False
      elif isinstance(Node, nodes.trueExpression):
         print('Error: A true expression cannot be written to, invalid write found on line', Node.lineNum)
         self.errorCounter += 1
         return False
      elif isinstance(Node, nodes.falseExpression):
         print('Error: A false expression cannot be written to, invalid write found on line', Node.lineNum)
         self.errorCounter += 1
         return False
      elif isinstance(Node, nodes.nullExpression):
         print('Error: A null expression cannot be written to, invalid write found on line', Node.lineNum)
         self.errorCounter += 1
         return False
      elif isinstance(Node, nodes.identifierExpression):
         #check if its a function
         for scope in reversed(range(len(self.stack))):
            if self.stack[scope].checkKey(Node.value):
               #we know for a fact that its declared because we ran our undeclared visitor
               typeval, lineno, isarray, modifier, isfunction, isparameter = self.stack[scope].lookup(Node.value)
               if isfunction:
                  print('Error: Functions cannot be written/assigned to, invalid write found on line', Node.lineNum)
                  self.errorCounter += 1
                  return False
               break
            
         return False
      elif isinstance(Node, nodes.thisExpression):
         print('Error: A this expression cannot be written to, invalid write found on line', Node.lineNum)
         self.errorCounter += 1
         return False
      elif isinstance(Node, nodes.callExpression):
         print('Error: A call expression cannot be written to, invalid write found on line', Node.childN2.lineNum)
         self.errorCounter += 1
         return False
      elif isinstance(Node, nodes.newExpression):
         print('Error: A new expression cannot be written to, invalid write found on line', Node.lineNum)
         self.errorCounter += 1
         return False
      else:
         return True


   def findClassST(self,name):
      for st in self.classSTS:
         if st.name == name:
            return st
   
   def findFunctionST(self,name, parentN):
      for st in self.functionSTS:
         if st.name == name and st.parent == parentN:
            return st


   def pre_visitCompUnit(self, node):
      self.stack.append(self.findFunctionST(node.id, 'global'))
      self.current += 1
      
   def visitCompUnit(self, node):
      #pop the scope off
      self.stack.pop()
      self.current -= 1
      
   def pre_visitClassDef(self, node):
      self.stack.append(self.findClassST(node.id))
      self.current += 1
      
   def visitClassDef(self, node):
      #pop the scope off
      self.stack.pop()
      self.current -= 1

      
   def visitTypeN(self, node):
      pass
   def visitModifierN(self, node):
      pass
   def pre_visitClassMemDef(self, node):
      pass
   def visitClassMemDef(self, node):
      pass
   def pre_visitDataMemDecl(self, node):
      pass
   def visitDataMemDecl(self, node):
      pass
   def pre_visitMethodDecl(self, node):
      self.stack.append(self.findFunctionST(node.id, self.stack[self.current].name))
      self.current += 1
      
   def visitMethodDecl(self, node):
      #pop the scope off
      self.stack.pop()
      self.current -= 1
      
   def pre_visitConstructorDecl(self, node):
      self.stack.append(self.findFunctionST(node.id, self.stack[self.current].name))
      self.current += 1
      
   def visitConstructorDecl(self, node):
      #pop the scope off
      self.stack.pop()
      self.current -= 1
   def pre_visitInitializer(self, node):
      pass
   def visitInitializer(self, node):
      pass
   def pre_visitMethodSuf(self, node):
      pass
   def visitMethodSuf(self, node):
      pass
   def pre_visitMethodBody(self, node):
      pass
   def visitMethodBody(self, node):
      pass
   def pre_visitParameterList(self, node):
      pass
   def visitParameterList(self, node):
      pass
   def pre_visitParameter(self, node):
      pass
   def visitParameter(self, node):
      pass
   def pre_visitVarDecl(self, node):
      pass
   def visitVarDecl(self, node):
      pass
   def pre_visitcurlyBrackStatement(self, Node):
      pass
   def visitcurlyBrackStatement(self, Node):
      pass
   def pre_visitexpressionStatement(self, Node):
      pass

   def visitexpressionStatement(self, Node):
      pass

   def pre_visitifStatement(self, Node):
      pass
   def visitifStatement(self, Node):
      pass

   def pre_visitwhileStatement(self, Node):
      pass
   def visitwhileStatement(self, Node):
      pass

   def pre_visitreturnStatement(self, Node):
      pass
   def visitreturnStatement(self, Node):
      pass

   def pre_visitcoutStatement(self, Node):
      pass
   def visitcoutStatement(self, Node):
      pass



   def pre_visitcinStatement(self, Node):
      pass
   def visitcinStatement(self, Node):

      #have to make some changes cause things like cin >> var += 2; should give an error , same with just =??????
      self.leftflag = self.simpleCheck(Node.childN1)

      if self.leftflag:
         Node.childN1.accept(self)
         self.leftflag = False
         if len(self.prevTypes) > 0:
            val, isfunction = self.prevTypes.pop()
            #if its a function throw an error otherwise we know its just a data member which can be written to
            if isfunction:
               print('Error: Functions cannot be written/assigned to, invalid write to found on line', Node.lineNum)
               self.errorCounter += 1
      

   def pre_visitswitchStatement(self, Node):
      pass
   def visitswitchStatement(self, Node):
      pass

   def visitbreakStatement(self, Node):
      pass

   def pre_visitvarDeclStatement(self, Node):
      pass
   def visitvarDeclStatement(self, Node):
      pass

#end of statements
   def pre_visitCaseBlock(self, node):
      pass
   def visitCaseBlock(self, node):
      pass
   def pre_visitCase(self, node):
      pass
   def visitCase(self, node):
      pass


#    def visitExpression(node):

   def pre_visitassignmentExpression(self, Node):
      #also check if the id of the left side is for a function
      #if isinstance(Node.childN1, nodes.plusExpression):
      #set a flag and call accept on childN1 then after accept is called set the flag back to 0 or false
      #if  flag is already set we are already in a left side so dont do anything just continue 
      pass
      
   def visitassignmentExpression(self, Node):
      #problem we are currently double reporting errors if its like this a.b(c()=5+5) = 5/8
      
      self.leftflag = self.simpleCheck(Node.childN1)

      if self.leftflag:
         Node.childN1.accept(self)
         self.leftflag = False
         if len(self.prevTypes) > 0:
            val, isfunction = self.prevTypes.pop()
            #if its a function throw an error otherwise we know its just a data member which can be written to
            if isfunction:
               print('Error: Functions cannot be written/assigned to, invalid write to found on line', Node.lineNum)
               self.errorCounter += 1

   def pre_visitaddAssignmentExpression(self, Node):
      pass
   def visitaddAssignmentExpression(self, Node):
      self.leftflag = self.simpleCheck(Node.childN1)

      if self.leftflag:
         Node.childN1.accept(self)
         self.leftflag = False
         if len(self.prevTypes) > 0:
            val, isfunction = self.prevTypes.pop()
            #if its a function throw an error otherwise we know its just a data member which can be written to
            if isfunction:
               print('Error: Functions cannot be written/assigned to, invalid write to found on line', Node.lineNum)
               self.errorCounter += 1

   def pre_visitsubAssignmentExpression(self, Node):
      pass
   def visitsubAssignmentExpression(self, Node):
      self.leftflag = self.simpleCheck(Node.childN1)

      if self.leftflag:
         Node.childN1.accept(self)
         self.leftflag = False
         if len(self.prevTypes) > 0:
            val, isfunction = self.prevTypes.pop()
            #if its a function throw an error otherwise we know its just a data member which can be written to
            if isfunction:
               print('Error: Functions cannot be written/assigned to, invalid write to found on line', Node.lineNum)
               self.errorCounter += 1

   def pre_visitmultAssignmentExpression(self, Node):
      pass
   def visitmultAssignmentExpression(self, Node):
      self.leftflag = self.simpleCheck(Node.childN1)

      if self.leftflag:
         Node.childN1.accept(self)
         self.leftflag = False
         if len(self.prevTypes) > 0:
            val, isfunction = self.prevTypes.pop()
            #if its a function throw an error otherwise we know its just a data member which can be written to
            if isfunction:
               print('Error: Functions cannot be written/assigned to, invalid write to found on line', Node.lineNum)
               self.errorCounter += 1
   

   def pre_visitdivAssignmentExpression(self, Node):
      pass
   def visitdivAssignmentExpression(self, Node):
      self.leftflag = self.simpleCheck(Node.childN1)

      if self.leftflag:
         Node.childN1.accept(self)
         self.leftflag = False
         if len(self.prevTypes) > 0:
            val, isfunction = self.prevTypes.pop()
            #if its a function throw an error otherwise we know its just a data member which can be written to
            if isfunction:
               print('Error: Functions cannot be written/assigned to, invalid write to found on line', Node.lineNum)
               self.errorCounter += 1

   def pre_visitplusExpression(self, Node):
      pass
   def visitplusExpression(self, Node):
      pass

   def pre_visitminusExpression(self, Node):
      pass
   def visitminusExpression(self, Node):
      pass

   def pre_visitmultExpression(self, Node):
      pass
   def visitmultExpression(self, Node):
      pass

   def pre_visitdivExpression(self, Node):
      pass
   def visitdivExpression(self, Node):
      pass

   def pre_visitequalityExpression(self, Node):
      pass
   def visitequalityExpression(self, Node):
      pass

   def pre_visitnotEqualExpression(self, Node):
      pass
   def visitnotEqualExpression(self, Node):
      pass

   def pre_visitlessThanExpression(self, Node):
      pass
   def visitlessThanExpression(self, Node):
      pass

   def pre_visitgreaterThanExpression(self, Node):
      pass
   def visitgreaterThanExpression(self, Node):
      pass

   def pre_visitLTEqualsExpression(self, Node):
      pass
   def visitLTEqualsExpression(self, Node):
      pass

   def pre_visitGTEqualsExpression(self, Node):
      pass
   def visitGTEqualsExpression(self, Node):
      pass

   def pre_visitandExpression(self, Node):
      pass
   def visitandExpression(self, Node):
      pass

   def pre_visitorExpression(self, Node):
      pass
   def visitorExpression(self, Node):
      pass
      
   def pre_visitnotExpression(self, Node):
      pass
   def visitnotExpression(self, Node):
      pass

   def pre_visitunaryPlusExpression(self, Node):
      pass
   def visitunaryPlusExpression(self, Node):
      pass

   def pre_visitunaryMinusExpression(self, Node):
      pass
   def visitunaryMinusExpression(self, Node):
      pass

   def visitliteralIntExpression(self, Node):
      pass

   def visitliteralCharExpression(self, Node):
      pass

   def visitliteralStringExpression(self, Node):
      pass

   def visittrueExpression(self, Node):
      pass

   def visitfalseExpression(self, Node):
      pass

   def visitnullExpression(self, Node):
      pass

   def visitidentifierExpression(self, Node):
      if self.leftflag:
         #we know the varaible is already declared because we called our undeclvisitor before this
         for scope in reversed(range(len(self.stack))):
            if self.stack[scope].checkKey(Node.value):
               #break out of the loop
               typeval, lineno, isarray, modifier, isfunction, isparameter = self.stack[scope].lookup(Node.value)
               self.prevTypes.append((typeval, isfunction))
               break
            
      

   def visitthisExpression(self, Node):
      if self.current == 2:
         self.prevTypes.append((self.stack[self.current].parent, False))
      else:
         print('Error: this can only be used within the function/method scope of a class, Error: located on line', Node.lineNum)
         self.errorCounter += 1
      pass

   def pre_visitcallExpression(self, Node):
      pass
   def visitcallExpression(self, Node):
      pass

   def pre_visitarrayExpression(self, Node):
      if not isinstance(Node.childN1, nodes.identifierExpression) and not isinstance(Node.childN1, nodes.callExpression) and not isinstance(Node.childN1, nodes.thisExpression):
         if self.leftflag:
            self.leftflag = self.simpleCheck(Node.childN1)

      
   def visitarrayExpression(self, Node):
      pass

   def pre_visitperiodExpression(self, Node):
      if not isinstance(Node.childN1, nodes.identifierExpression) and not isinstance(Node.childN1, nodes.callExpression) and not isinstance(Node.childN1, nodes.thisExpression):
         if self.leftflag:
            self.leftflag = self.simpleCheck(Node.childN1)
      
   def visitperiodExpression(self, Node):
         
      if self.leftflag:
         value, isfunct = self.prevTypes.pop()

         #search the value in the global scope
         
            
         for st in self.classSTS:
            if st.name == value:
               cscope = st
               break
         
         #we already know it exists cause our undeclvisitor was executed before this and wouldve given errors
         typeval, lineno, isarray, modifier, isfunction, isparameter = cscope.lookup(Node.id)
         
         self.prevTypes.append((typeval, isfunction))
         
         
      

   def pre_visitnewExpression(self, Node):
      pass
   def visitnewExpression(self, Node):
      pass

   def pre_visitparenExpression(self, Node):
      
      if self.leftflag:
         self.leftflag = self.simpleCheck(Node.childN1)
   
   def visitparenExpression(self, Node):
      pass

#end of expressions

   def pre_visitArguments(self, node):
      self.prevflags.append(self.leftflag)
      self.leftflag = False
      
   def visitArguments(self, node):
      self.leftflag = self.prevflags.pop()
   def pre_visitArgumentList(self, node):
      pass
   def visitArgumentList(self, node):
      pass
   def pre_visitIndex(self, node):
      self.prevflags.append(self.leftflag)
      self.leftflag = False
      
   def visitIndex(self, node):
      self.leftflag = self.prevflags.pop()
      


#visitor to check while loops and if statements for bool
#visitor to check case type matches expression type of switch and that switch expression is char or an int
#visitor check for stand alone function without () i dont know where that is not allowed
#divide and conquer the error checking into seperate visitors 
#cin visitor that ensures cin isnt being stored in a string can only read integers and characters but first check if the right is writtable
#check for break statements occur inside while or switch statements-> have a counter when we post visit a while or switch
#if counter is zero keep it zero otherwise -1 from the counter, this ensures that wait.... if we have two break statemetns in one while loop 
#we would increment by two and cause an error even though technically that shouldnt be an error cause its in a while loop. 
#instead when we previsit a while loop, switch statemnt, or at the end of everything check if counter is greater than zero if so then a break statement
#occured outside of a valid statement print error. 
#have to type check parameters of functions and make sure that their parameters match are in order and are the same types as their parameter, also make sure we have the same amount of parameters


class TypeCheckingVisitor(Visitor):
   def __init__(self, globalst, classsts, functionsts):
      self.globalST = globalst
      self.classSTS = classsts
      self.functionSTS = functionsts
      self.stack = []
      self.current = 0 #max depth for stack will be index 2, to keep track of that place should we just use current as a index tracker????
      self.errorCounter = 0 
      self.stack.append(self.globalST)
      self.leftflag = False
      self.prevflags = []
      self.prevTypes = []
      self.childrenTypes = []
      

   def findClassST(self,name):
      for st in self.classSTS:
         if st.name == name:
            return st
   
   def findFunctionST(self,name, parentN):
      for st in self.functionSTS:
         if st.name == name and st.parent == parentN:
            return st


   def pre_visitCompUnit(self, node):
      self.stack.append(self.findFunctionST(node.id, 'global'))
      self.current += 1
      
   def visitCompUnit(self, node):
      #pop the scope off
      self.stack.pop()
      self.current -= 1
      
   def pre_visitClassDef(self, node):
      self.stack.append(self.findClassST(node.id))
      self.current += 1
      
   def visitClassDef(self, node):
      #pop the scope off
      self.stack.pop()
      self.current -= 1

      
   def visitTypeN(self, node):
      pass
   def visitModifierN(self, node):
      pass
   def pre_visitClassMemDef(self, node):
      pass
   def visitClassMemDef(self, node):
      pass
   def pre_visitDataMemDecl(self, node):
      pass
   def visitDataMemDecl(self, node):
      pass
   def pre_visitMethodDecl(self, node):
      self.stack.append(self.findFunctionST(node.id, self.stack[self.current].name))
      self.current += 1
      
   def visitMethodDecl(self, node):
      #pop the scope off
      self.stack.pop()
      self.current -= 1
      
   def pre_visitConstructorDecl(self, node):
      self.stack.append(self.findFunctionST(node.id, self.stack[self.current].name))
      self.current += 1
      
   def visitConstructorDecl(self, node):
      #pop the scope off
      self.stack.pop()
      self.current -= 1
      
   def pre_visitInitializer(self, node):
      pass
   def visitInitializer(self, node):
      pass
   def pre_visitMethodSuf(self, node):
      pass
   def visitMethodSuf(self, node):
      pass
   def pre_visitMethodBody(self, node):
      pass
   def visitMethodBody(self, node):
      pass
   def pre_visitParameterList(self, node):
      pass
   def visitParameterList(self, node):
      pass
   def pre_visitParameter(self, node):
      pass
   def visitParameter(self, node):
      pass
   def pre_visitVarDecl(self, node):
      pass
   def visitVarDecl(self, node):
      #childn1 is the type
      

      if node.initializer is not None:
         #can just look into the current scope and get the information using the var id
         typeval, lineno, isarray, modifier, isfunction, isparameter = self.stack[self.current].lookup(node.id)
         if isarray:
            typeval = typeval + '$reference'
         self.childrenTypes.append((typeval,lineno, isarray, isfunction, isparameter))
         if len(self.childrenTypes) < 2:
            print('visitor type checking, wasnt enough elements in self.childrenTypes to pop two things off')

         #had to switch the next two statements order to ensure the 1 gets the left side which is type while 2 gets the initializer
         valueT1, lineno1, isarr1, isfun1, ispara1 = self.childrenTypes.pop()
         valueT2, lineno2, isarr2, isfun2, ispara2 = self.childrenTypes.pop()

#we can allow the if statement below because you can assign a memory to a variable that is array
         if isinstance(node.initializer, nodes.newExpression) and (isarr1 != isarr2) and (valueT1 == valueT2):
            if isarr1:
               print('Error: Expected to be intialized with new', valueT1, '[index], instead you intialized to an instance of an object by doing a constructor call(). Error found in variable declaration on line', node.lineNum)
               self.errorCounter += 1
               self.childrenTypes.append((valueT1, node.lineNum, False, False, False))
            elif isarr2:
               print('Error: Expected to be intialized with new', valueT1, '(arguments), instead you intialized an allocation of memory[]. Error found in variable declaration on line', node.lineNum)
               self.errorCounter += 1
               self.childrenTypes.append((valueT1, node.lineNum, False, False, False))

         elif valueT1 == valueT2:
            #we already checked that the left side will be something we can write to.
            self.childrenTypes.append((valueT1, node.lineNum, False, False, False))
            
         else:
            #we will handle null and new assignments in the new Visitor for now just ignore it and move on, class type set to null is fine so is array to null in variable declaration but i dont know for assignment
            #check if a class type is being assigned null which is ok
            #if (valueT2 == 'null' and isarr1) or (valueT2 == 'null' and self.stack[0].checkKey(valueT1)) or (valueT2 == 'this' and self.stack[0].checkKey(valueT1)):
            if (valueT2 == 'null' and ('$reference' in valueT1)) or (valueT2 == 'null' and self.stack[0].checkKey(valueT1)) or (valueT2 == 'this' and self.stack[0].checkKey(valueT1)):
               
               self.childrenTypes.append((valueT1, node.lineNum, False, False, False))
               #gonna have to check if child on the right is instance of new and is array, because the only times we can do new with index is in variable declaration
               #if variable declaration is intializing an array of a type to just the call of the type we should give an error because the variable is expecting to get a pointer in memory not an object
            
            else:
               self.errorCounter += 1
               print('Error: The types on the left and right side of the variable declaration do not match. Error found in variable declaration on line', node.lineNum)
               self.childrenTypes.append((valueT1, node.lineNum, False, False, False))


      
         
   def pre_visitcurlyBrackStatement(self, Node):
      pass
   def visitcurlyBrackStatement(self, Node):
      pass
   def pre_visitexpressionStatement(self, Node):
      pass

   def visitexpressionStatement(self, Node):
      pass

   def pre_visitifStatement(self, Node):
      pass
   def visitifStatement(self, Node):
      pass

   def pre_visitwhileStatement(self, Node):
      pass
   def visitwhileStatement(self, Node):
      pass

   def pre_visitreturnStatement(self, Node):
      pass
   def visitreturnStatement(self, Node):
      pass

   def pre_visitcoutStatement(self, Node):
      pass
   def visitcoutStatement(self, Node):
      pass

   def pre_visitcinStatement(self, Node):
      pass
   def visitcinStatement(self, Node):
      #type check ensure that cin is only reading integers and characters no strings
      valueT1, lineno1, isarr1, isfun1, ispara1 = self.childrenTypes.pop()
      if valueT1 not in ['int', 'char']:
         print('Error: cin statement can only read in integers or characters, the expression evaluated to',valueT1,'which cannot be read into. Error found on line', Node.lineNum)
         self.errorCounter += 1

      pass

   def pre_visitswitchStatement(self, Node):
      pass
   def visitswitchStatement(self, Node):
      pass

   def visitbreakStatement(self, Node):
      pass

   def pre_visitvarDeclStatement(self, Node):
      pass
   def visitvarDeclStatement(self, Node):
      pass
      

#end of statements
   def pre_visitCaseBlock(self, node):
      pass
   def visitCaseBlock(self, node):
      pass
   def pre_visitCase(self, node):
      pass
   def visitCase(self, node):
      pass


#    def visitExpression(node):

   def pre_visitassignmentExpression(self, Node):
      pass
   def visitassignmentExpression(self, Node):
      #you can assign class type or even array to a null
      #it could just be a plain dot operator or id 
      #can still assign new to something
      #we ensured that the left side is something we can write to, we just type checking
      #val1 is the left side val2 is the right side of the operation 
      #also have to check in variable declaration cause we can possibly have an intializer
      #for class types checkkey in the global scope to see if it is indeed a class type
      #for arrays we need isarray
      #to see if type is class look up valueT1 in the class scopes classSTS and if found then we can assign it a null or new(do we have to make sure that if its a class type, that we assign it with a new constructor call with the same name or just null)
      if len(self.childrenTypes) < 2:
         print('visitor type checking, wasnt enough elements in self.childrenTypes to pop two things off')

      valueT2, lineno2, isarr2, isfun2, ispara2 = self.childrenTypes.pop()
      valueT1, lineno1, isarr1, isfun1, ispara1 = self.childrenTypes.pop()

      
      if isinstance(Node.childN2, nodes.newExpression) and (isarr1 != isarr2) and (valueT1 == valueT2):
         if isarr1:
            print('Error: Expected to be assigned with new', valueT1, '[index], instead you intialized to an instance of an object by doing a constructor call(). Error found in variable declaration on line', Node.lineNum)
            self.errorCounter += 1
            self.childrenTypes.append((valueT1, Node.lineNum, False, False, False))
         elif isarr2:
            print('Error: Expected to be assigned with new', valueT1, '(arguments), instead you intialized an allocation of memory[]. Error found in variable declaration on line', Node.lineNum)
            self.errorCounter += 1
            self.childrenTypes.append((valueT1, Node.lineNum, False, False, False))
      elif valueT1 == valueT2:
         #we already checked that the left side will be something we can write to.
         self.childrenTypes.append((valueT1, Node.lineNum, False, False, False))
         
      else:
         #we will handle null and new assignments in the new Visitor for now just ignore it and move on, class type set to null is fine so is array to null in variable declaration but i dont know for assignment
         #check if a class type is being assigned null which is ok
         #print(valueT1, valueT2)
         if (valueT2 == 'null' and ('$reference' in valueT1)) or (valueT2 == 'null' and self.stack[0].checkKey(valueT1)) or (valueT2 == 'this' and self.stack[0].checkKey(valueT1)):
            
            self.childrenTypes.append((valueT1, Node.lineNum, False, False, False))
            #gonna have to check if child on the right is instance of new and is array, because the only times we can do new with index is in variable declaration
            #if variable declaration is intializing an array of a type to just the call of the type we should give an error because the variable is expecting to get a pointer in memory not an object
         
         else:
            self.errorCounter += 1
            print('Error: The types on the left and right side of the assignment expression do not match. Error found in assignment expression on line', Node.lineNum)
            self.childrenTypes.append((valueT1, Node.lineNum, False, False, False))


   def pre_visitaddAssignmentExpression(self, Node):
      pass
   def visitaddAssignmentExpression(self, Node):
      valueT2, lineno2, isarr2, isfun2, ispara2 = self.childrenTypes.pop()
      valueT1, lineno1, isarr1, isfun1, ispara1 = self.childrenTypes.pop()
      if valueT1 == valueT2:
         if valueT1 == 'int':
            self.childrenTypes.append((valueT1, Node.lineNum, False, False, False))
         else:
            print('Error: Plus assignment expression can only be used on int types. Error found in plus assignment expression on line', Node.lineNum)
            self.errorCounter += 1
            self.childrenTypes.append((valueT1, Node.lineNum, False, False, False))
         
      else:
         self.errorCounter += 1
         print('Error: The types on the left and right side of the plus assignment expression do not match(both need to be an int type). Error found in plus assignment expression on line', Node.lineNum)
         self.childrenTypes.append((valueT1, Node.lineNum, False, False, False))

   def pre_visitsubAssignmentExpression(self, Node):
      pass
   def visitsubAssignmentExpression(self, Node):
      valueT2, lineno2, isarr2, isfun2, ispara2 = self.childrenTypes.pop()
      valueT1, lineno1, isarr1, isfun1, ispara1 = self.childrenTypes.pop()
      if valueT1 == valueT2:
         if valueT1 == 'int':
            self.childrenTypes.append((valueT1, Node.lineNum, False, False, False))
         else:
            print('Error: Minus assignment expression can only be used on int types. Error found in minus assignment expression on line', Node.lineNum)
            self.childrenTypes.append((valueT1, Node.lineNum, False, False, False))
            self.errorCounter += 1
         
      else:
         self.errorCounter += 1
         print('Error: The types on the left and right side of the minus assignment expression do not match(both need to be an int type). Error found in minus assignment expression on line', Node.lineNum)
         self.childrenTypes.append((valueT1, Node.lineNum, False, False, False))


   def pre_visitmultAssignmentExpression(self, Node):
      pass
   def visitmultAssignmentExpression(self, Node):
      valueT2, lineno2, isarr2, isfun2, ispara2 = self.childrenTypes.pop()
      valueT1, lineno1, isarr1, isfun1, ispara1 = self.childrenTypes.pop()
      if valueT1 == valueT2:
         if valueT1 == 'int':
            self.childrenTypes.append((valueT1, Node.lineNum, False, False, False))
         else:
            print('Error: Multiply assignment expression can only be used on int types. Error found in multiply assignment expression on line', Node.lineNum)
            self.errorCounter += 1
            self.childrenTypes.append((valueT1, Node.lineNum, False, False, False))
         
      else:
         self.errorCounter += 1
         print('Error: The types on the left and right side of the multiply assignment expression do not match(both need to be an int type). Error found in multiply assignment expression on line', Node.lineNum)
         self.childrenTypes.append((valueT1, Node.lineNum, False, False, False))
   

   def pre_visitdivAssignmentExpression(self, Node):
      pass
   def visitdivAssignmentExpression(self, Node):
      #we are still doing a binary operation so we still require int types
      valueT2, lineno2, isarr2, isfun2, ispara2 = self.childrenTypes.pop()
      valueT1, lineno1, isarr1, isfun1, ispara1 = self.childrenTypes.pop()
      if valueT1 == valueT2:
         if valueT1 == 'int':
            self.childrenTypes.append((valueT1, Node.lineNum, False, False, False))
         else:
            print('Error: Divide assignment expression can only be used on int types. Error found in divide assignment expression on line', Node.lineNum)
            self.errorCounter += 1
            self.childrenTypes.append((valueT1, Node.lineNum, False, False, False))
         
      else:
         self.errorCounter += 1
         print('Error: The types on the left and right side of the divide assignment expression do not match(both need to be an int type). Error found in divide assignment expression on line', Node.lineNum)
         self.childrenTypes.append((valueT1, Node.lineNum, False, False, False))

   def pre_visitplusExpression(self, Node):
      pass
   def visitplusExpression(self, Node):
      valueT2, lineno2, isarr2, isfun2, ispara2 = self.childrenTypes.pop()
      valueT1, lineno1, isarr1, isfun1, ispara1 = self.childrenTypes.pop()
      if valueT1 == valueT2:
         if valueT1 == 'int':
            self.childrenTypes.append((valueT1, Node.lineNum, False, False, False))
         else:
            print('Error: Plus expression can only be used on int types. Error found in plus expression on line', Node.lineNum)
            self.errorCounter += 1
            self.childrenTypes.append((valueT2, Node.lineNum, False, False, False))
         
      else:
         self.errorCounter += 1
         print('Error: The types on the left and right side of the plus expression do not match(both need to be an int type). Error found in plus expression on line', Node.lineNum)
         self.childrenTypes.append((valueT2, Node.lineNum, False, False, False))

   def pre_visitminusExpression(self, Node):
      pass
   def visitminusExpression(self, Node):
      valueT2, lineno2, isarr2, isfun2, ispara2 = self.childrenTypes.pop()
      valueT1, lineno1, isarr1, isfun1, ispara1 = self.childrenTypes.pop()
      if valueT1 == valueT2:
         if valueT1 == 'int':
            self.childrenTypes.append((valueT1, Node.lineNum, False, False, False))
         else:
            print('Error: Minus expression can only be used on int types. Error found in minus expression on line', Node.lineNum)
            self.errorCounter += 1
            self.childrenTypes.append((valueT2, Node.lineNum, False, False, False))
         
      else:
         self.errorCounter += 1
         print('Error: The types on the left and right side of the minus expression do not match(both need to be an int type). Error found in minus expression on line', Node.lineNum)
         self.childrenTypes.append((valueT2, Node.lineNum, False, False, False))

   def pre_visitmultExpression(self, Node):
      pass
   def visitmultExpression(self, Node):
      valueT2, lineno2, isarr2, isfun2, ispara2 = self.childrenTypes.pop()
      valueT1, lineno1, isarr1, isfun1, ispara1 = self.childrenTypes.pop()
      if valueT1 == valueT2:
         if valueT1 == 'int':
            self.childrenTypes.append((valueT1, Node.lineNum, False, False, False))
         else:
            print('Error: Multiplication expression can only be used on int types. Error found in multiplication expression on line', Node.lineNum)
            self.errorCounter += 1
            self.childrenTypes.append((valueT2, Node.lineNum, False, False, False))
         
      else:
         self.errorCounter += 1
         print('Error: The types on the left and right side of the multiplication expression do not match(both need to be an int type). Error found in multiplication expression on line', Node.lineNum)
         self.childrenTypes.append((valueT2, Node.lineNum, False, False, False))

   def pre_visitdivExpression(self, Node):
      pass
   def visitdivExpression(self, Node):

      valueT2, lineno2, isarr2, isfun2, ispara2 = self.childrenTypes.pop()
      valueT1, lineno1, isarr1, isfun1, ispara1 = self.childrenTypes.pop()
      if valueT1 == valueT2:
         if valueT1 == 'int':
            self.childrenTypes.append((valueT1, Node.lineNum, False, False, False))
         else:
            print('Error: Division expression can only be used on int types. Error found in division expression on line', Node.lineNum)
            self.errorCounter += 1
            self.childrenTypes.append((valueT2, Node.lineNum, False, False, False))
         
      else:
         self.errorCounter += 1
         print('Error: The types on the left and right side of the division expression do not match(both need to be an int type). Error found in division expression on line', Node.lineNum)
         self.childrenTypes.append((valueT2, Node.lineNum, False, False, False))


   def pre_visitequalityExpression(self, Node):
      pass
   def visitequalityExpression(self, Node):
      valueT2, lineno2, isarr2, isfun2, ispara2 = self.childrenTypes.pop()
      valueT1, lineno1, isarr1, isfun1, ispara1 = self.childrenTypes.pop()
      if valueT1 == valueT2:
         if valueT1 == 'char' or valueT1 == 'int' or valueT1 == 'bool' or valueT1 == 'string':
            #im unsure if it can be performed on ints and bools or only bools
            #has to put bool back onto the stack
            self.childrenTypes.append(('bool', Node.lineNum, False, False, False))
         else:
            print('Error: Equality expression can only be used on char, int, bool, or string types. Error found in equality expression on line', Node.lineNum)
            self.errorCounter += 1
            self.childrenTypes.append((valueT2, Node.lineNum, False, False, False))
         
      else:
         self.errorCounter += 1
         print('Error: The types on the left and right side of the equality expression do not match(both need to be a char type or int type or bool or a string type). Error found in equality expression on line', Node.lineNum)
         self.childrenTypes.append((valueT2, Node.lineNum, False, False, False))
      

   def pre_visitnotEqualExpression(self, Node):
      pass
   def visitnotEqualExpression(self, Node):
      valueT2, lineno2, isarr2, isfun2, ispara2 = self.childrenTypes.pop()
      valueT1, lineno1, isarr1, isfun1, ispara1 = self.childrenTypes.pop()
      if valueT1 == valueT2:
         if valueT1 == 'char' or valueT1 == 'int' or valueT1 == 'bool' or valueT1 == 'string':
            #im unsure if it can be performed on ints and bools or only bools
            #has to put bool back onto the stack
            self.childrenTypes.append(('bool', Node.lineNum, False, False, False))
         else:
            print('Error: Not equal to expression can only be used on char, int, bool, or string types types. Error found in not equal to expression on line', Node.lineNum)
            self.errorCounter += 1
            self.childrenTypes.append((valueT2, Node.lineNum, False, False, False))
         
      else:
         self.errorCounter += 1
         print('Error: The types on the left and right side of the not equal to expression do not match(both need to be a char type or int type or bool or a string type type). Error found in not equal to expression on line', Node.lineNum)
         self.childrenTypes.append((valueT2, Node.lineNum, False, False, False))
      

   def pre_visitlessThanExpression(self, Node):
      pass
   def visitlessThanExpression(self, Node):
      valueT2, lineno2, isarr2, isfun2, ispara2 = self.childrenTypes.pop()
      valueT1, lineno1, isarr1, isfun1, ispara1 = self.childrenTypes.pop()
      if valueT1 == valueT2:
         if valueT1 == 'char' or valueT1 == 'int':
            #im unsure if it can be performed on ints and bools or only bools
            #has to put bool back onto the stack
            self.childrenTypes.append(('bool', Node.lineNum, False, False, False))
         else:
            print('Error: Less than expression can only be used on char or int types. Error found in less than expression on line', Node.lineNum)
            self.errorCounter += 1
            self.childrenTypes.append((valueT2, Node.lineNum, False, False, False))
         
      else:
         self.errorCounter += 1
         print('Error: The types on the left and right side of the less than expression do not match(both need to be a char type or int type). Error found in less than expression on line', Node.lineNum)
         self.childrenTypes.append((valueT2, Node.lineNum, False, False, False))
      

   def pre_visitgreaterThanExpression(self, Node):
      pass
   def visitgreaterThanExpression(self, Node):
      valueT2, lineno2, isarr2, isfun2, ispara2 = self.childrenTypes.pop()
      valueT1, lineno1, isarr1, isfun1, ispara1 = self.childrenTypes.pop()
      if valueT1 == valueT2:
         if valueT1 == 'char' or valueT1 == 'int':
            #im unsure if it can be performed on ints and bools or only bools
            #has to put bool back onto the stack
            self.childrenTypes.append(('bool', Node.lineNum, False, False, False))
         else:
            print('Error: Greater than expression can only be used on char or int types. Error found in Greater than expression on line', Node.lineNum)
            self.errorCounter += 1
            self.childrenTypes.append((valueT2, Node.lineNum, False, False, False))
         
      else:
         self.errorCounter += 1
         print('Error: The types on the left and right side of the Greater than expression do not match(both need to be a char type or int type). Error found in Greater than expression on line', Node.lineNum)
         self.childrenTypes.append((valueT2, Node.lineNum, False, False, False))
      

   def pre_visitLTEqualsExpression(self, Node):
      pass
   def visitLTEqualsExpression(self, Node):
      valueT2, lineno2, isarr2, isfun2, ispara2 = self.childrenTypes.pop()
      valueT1, lineno1, isarr1, isfun1, ispara1 = self.childrenTypes.pop()
      if valueT1 == valueT2:
         if valueT1 == 'char' or valueT1 == 'int':
            #im unsure if it can be performed on ints and bools or only bools
            self.childrenTypes.append(('bool', Node.lineNum, False, False, False))
         else:
            print('Error: Less than or equals to expression can only be used on char or int types. Error found in Less than or equals to expression on line', Node.lineNum)
            self.errorCounter += 1
            self.childrenTypes.append((valueT2, Node.lineNum, False, False, False))
         
      else:
         self.errorCounter += 1
         print('Error: The types on the left and right side of the Less than or equals to expression do not match(both need to be a char type or int type). Error found in Less than or equals to expression on line', Node.lineNum)
         self.childrenTypes.append((valueT2, Node.lineNum, False, False, False))
      

   def pre_visitGTEqualsExpression(self, Node):
      pass
   def visitGTEqualsExpression(self, Node):
      valueT2, lineno2, isarr2, isfun2, ispara2 = self.childrenTypes.pop()
      valueT1, lineno1, isarr1, isfun1, ispara1 = self.childrenTypes.pop()
      if valueT1 == valueT2:
         if valueT1 == 'char' or valueT1 == 'int':
            #im unsure if it can be performed on ints and bools or only bools
            self.childrenTypes.append(('bool', Node.lineNum, False, False, False))
         else:
            print('Error: Greater than or equals to expression can only be used on char or int types. Error found in Greater than or equals to expression on line', Node.lineNum)
            self.errorCounter += 1
            self.childrenTypes.append((valueT2, Node.lineNum, False, False, False))
         
      else:
         self.errorCounter += 1
         print('Error: The types on the left and right side of the Greater than or equals to expression do not match(both need to be a char type or int type). Error found in Greater than or equals to expression on line', Node.lineNum)
         self.childrenTypes.append((valueT2, Node.lineNum, False, False, False))
      

   def pre_visitandExpression(self, Node):
      pass
   def visitandExpression(self, Node):
      valueT2, lineno2, isarr2, isfun2, ispara2 = self.childrenTypes.pop()
      valueT1, lineno1, isarr1, isfun1, ispara1 = self.childrenTypes.pop()
      if valueT1 == valueT2:
         if valueT1 == 'bool':
            #im unsure if it can be performed on ints and bools or only bools
            self.childrenTypes.append(('bool', Node.lineNum, False, False, False))
         else:
            print('Error: and expression can only be used on bool types. Error found in and expression on line', Node.lineNum)
            self.errorCounter += 1
            self.childrenTypes.append((valueT2, Node.lineNum, False, False, False))
      else:
         self.errorCounter += 1
         print('Error: The types on the left and right side of the and expression do not match(both need to be a bool type). Error found in and expression on line', Node.lineNum)
         self.childrenTypes.append((valueT2, Node.lineNum, False, False, False))
      

   def pre_visitorExpression(self, Node):
      pass
   def visitorExpression(self, Node):
      valueT2, lineno2, isarr2, isfun2, ispara2 = self.childrenTypes.pop()
      valueT1, lineno1, isarr1, isfun1, ispara1 = self.childrenTypes.pop()
      if valueT1 == valueT2:
         if valueT1 == 'bool':
            #im unsure if it can be performed on ints and bools or only bools
            self.childrenTypes.append(('bool', Node.lineNum, False, False, False))
         else:
            print('Error: or expression can only be used on bool types. Error found in or expression on line', Node.lineNum)
            self.errorCounter += 1
            self.childrenTypes.append((valueT2, Node.lineNum, False, False, False))
      else:
         self.errorCounter += 1
         print('Error: The types on the left and right side of the or expression do not match(both need to be a bool type). Error found in or expression on line', Node.lineNum)
         self.childrenTypes.append((valueT2, Node.lineNum, False, False, False))
      
      
   def pre_visitnotExpression(self, Node):
      pass
   def visitnotExpression(self, Node):
      
      valueT1, lineno1, isarr1, isfun1, ispara1 = self.childrenTypes.pop()
      if valueT1 == 'bool':
         #im unsure if it can be performed on ints and bools or only bools
         self.childrenTypes.append((valueT1, Node.lineNum, False, False, False))
      else:
         self.errorCounter += 1
         print('Error: Unary not can only be performed on bool types. Error found in unary not expression on line', Node.lineNum)
         self.childrenTypes.append((valueT1, Node.lineNum, False, False, False))
      

   def pre_visitunaryPlusExpression(self, Node):
      pass
   def visitunaryPlusExpression(self, Node):
      valueT1, lineno1, isarr1, isfun1, ispara1 = self.childrenTypes.pop()
      if valueT1 == 'int':
         #has to be an int
         self.childrenTypes.append((valueT1, Node.lineNum, False, False, False))
      else:
         self.errorCounter += 1
         print('Error: binary operations can only be performed on int types. Error found in unary plus expression on line', Node.lineNum)
         self.childrenTypes.append((valueT1, Node.lineNum, False, False, False))

   def pre_visitunaryMinusExpression(self, Node):
      pass
   def visitunaryMinusExpression(self, Node):
      valueT1, lineno1, isarr1, isfun1, ispara1 = self.childrenTypes.pop()
      if valueT1 == 'int':
         #has to be an int
         self.childrenTypes.append((valueT1, Node.lineNum, False, False, False))
      else:
         self.errorCounter += 1
         print('Error: binary operations can only be performed on int types. Error found in unary minus expression on line', Node.lineNum)
         self.childrenTypes.append((valueT1, Node.lineNum, False, False, False))

   def visitliteralIntExpression(self, Node):
      self.childrenTypes.append(('int', Node.lineNum, False, False, False))

   def visitliteralCharExpression(self, Node):
      self.childrenTypes.append(('char', Node.lineNum, False, False, False))

   def visitliteralStringExpression(self, Node):
      self.childrenTypes.append(('string', Node.lineNum, False, False, False))

   def visittrueExpression(self, Node):
      self.childrenTypes.append(('bool', Node.lineNum, False, False, False))

   def visitfalseExpression(self, Node):
      self.childrenTypes.append(('bool', Node.lineNum, False, False, False))

   def visitnullExpression(self, Node):
      self.childrenTypes.append(('null', Node.lineNum, False, False, False))
      

   def visitidentifierExpression(self, Node):
      
         #we know the varaible is already declared because we called our undeclvisitor before this
      for scope in reversed(range(len(self.stack))):
         if self.stack[scope].checkKey(Node.value):
            #break out of the loop
            typeval, lineno, isarray, modifier, isfunction, isparameter = self.stack[scope].lookup(Node.value)
            
            if isarray:
               
               #this will help to make sure we are not just using reference to an array in binary operators but rather its elements in its memory
               self.childrenTypes.append((typeval+'$reference',lineno, isarray, isfunction, isparameter))
            else:
               self.childrenTypes.append((typeval,lineno, isarray, isfunction, isparameter))
            break
      

   def visitthisExpression(self, Node):
      # do we need to check for this? and how?
      #cannot be stand alone?
      if self.current == 2:
         self.childrenTypes.append((self.stack[self.current].parent, Node.lineNum, False, False, False))
      else:
         print('Error: this can only be used within the function/method scope of a class, Error: located on line', Node.lineNum)
         self.errorCounter += 1
      

   def pre_visitcallExpression(self, Node):
      pass
   def visitcallExpression(self, Node):
      pass

   def pre_visitarrayExpression(self, Node):
      pass
      
         
      
   def visitarrayExpression(self, Node):
      valueT1, lineno1, isarr1, isfun1, ispara1 = self.childrenTypes.pop()
      #strip reference off since we know that we have an index to go along with it 
      lengthstr = len(valueT1)
      lengthstr -= 10
      valueT1 = valueT1[:lengthstr]
      self.childrenTypes.append((valueT1, lineno1, False, isfun1, ispara1))
      pass

   def pre_visitperiodExpression(self, Node):
      pass
   def visitperiodExpression(self, Node):
      #error occurs when we have something like a(a.b).c.a the inner function call will keep its value on the stack which can be picked up by other types

      valueT1, lineno1, isarr1, isfun1, ispara1 = self.childrenTypes.pop()
      #we already checked that the period expressions are declared
      #search the value in the global scope
      cscope = None
      for st in self.classSTS:
         if st.name == valueT1:
            cscope = st
            break
      if cscope == None:
         print('error in period expression wasnt able to find the apropriate scope even though we have already ensured that the scope exists, cscope is None')
      else:
         #we already know it exists cause our undeclvisitor was executed before this and wouldve given errors
         typeval, lineno, isarray, modifier, isfunction, isparameter = cscope.lookup(Node.id)
         #in another visitor we will pass the function instead of lineno
         if isarray:
            #this will help to make sure we are not just using reference to an array in binary operators but rather its elements in its memory
            self.childrenTypes.append((typeval+'$reference',lineno, isarray, isfunction, isparameter))
         else:
            self.childrenTypes.append((typeval,lineno, isarray, isfunction, isparameter))
        
      

   def pre_visitnewExpression(self, Node):
      pass
   def visitnewExpression(self, Node):
      #childn1 is a type node
      #even if its a certain type i dont think we can perform normal operations on it can we?
      #in another visitor we will bechecking if its going to an array or object
      
      #self.childrenTypes.append(('new', Node.childN1.lineNum, False, False, False))
      #the type could be static or an id
      if Node.childN1.valType in ['void','int', 'char', 'bool', 'string']:
         if isinstance(Node.childN2, nodes.arguments):
            print('Error: In the New expression you cannot pass cannot pass arguments to the types: void,int,char,bool,string. Error found on line', Node.lineNum)
            self.errorCounter += 1
            #so we can continue with errorchecking
            self.childrenTypes.append((Node.childN1.valType, Node.childN1.lineNum, False, False, False))
         else:
            #this means its childN2 is an index which is fine.... can you apply new to a void type??
            if Node.childN1.valType == 'void':
               print('Error: In the New expression you cannot allocate memory for type void. Error found on line', Node.lineNum)
               self.errorCounter += 1
            else:
               self.childrenTypes.append((Node.childN1.valType+'$reference', Node.childN1.lineNum, True, False, False))
      else:
         #new can only call constructor functions
         #check global scope if class even exists with its name the same as the type
         if self.stack[0].checkKey(Node.childN1.valType):
            #break out of the loop
            #check if its an instance of arguments
            if isinstance(Node.childN2, nodes.arguments):
               #constrfunct = self.findFunctionST(Node.childN1.valType, Node.childN1.valType)
               #typeval, lineno, isarray, modifier, isfunction, isparameter = self.stack[0].lookup(Node.childN1.valType)
               #self.childrenTypes.append((typeval,lineno, isarray, isfunction, isparameter))
               self.childrenTypes.append((Node.childN1.valType, Node.childN1.lineNum, False, False, False))
            else:
               #its an index for its childN2
               self.childrenTypes.append((Node.childN1.valType+'$reference', Node.childN1.lineNum, True, False, False))

         else:
            print('Error: In the New expression could not find the class that type', Node.childN1.valType,'was reffering to, ensure that a valid type is provided. Error found on line', Node.lineNum)
            self.errorCounter += 1
            #even if its an error append something so that the rest of our error checking can be completed
            self.childrenTypes.append((Node.childN1.valType, Node.childN1.lineNum, False, False, False))

   def pre_visitparenExpression(self, Node):
      pass
   def visitparenExpression(self, Node):
      pass

#end of expressions

   def pre_visitArguments(self, node):
      pass
   def visitArguments(self, node):
      pass
   def pre_visitArgumentList(self, node):
      pass
   def visitArgumentList(self, node):
      #after we evaluate one argument by type checking we pop one off the stack so its not misread by its outer parent call
      #before we just self.chilredntypes.pop() no for len
      for i in range(len(node.children)):
         self.childrenTypes.pop()
      
   def pre_visitIndex(self, node):
      pass
   def visitIndex(self, node):
      #after we evaluate the expression we want to pop it off so it doesnt get misread by its outer parent call
      self.childrenTypes.pop()


#checks that the left expression of an array is an array type and that the index evaluates to an int
#we also check for stand alone array variables that arent being indexed
class IndexEvalVisitor(TypeCheckingVisitor):
   def __init__(self, globalst, classsts, functionsts):
      TypeCheckingVisitor.__init__(self, globalst, classsts, functionsts)
      self.orphanArrays = []

   def pre_visitCompUnit(self, node):
      self.stack.append(self.findFunctionST(node.id, 'global'))
      self.current += 1
      
   def visitCompUnit(self, node):
      #pop the scope off
      self.stack.pop()
      self.current -= 1
      #for id, lineno in self.orphanArrays:
         #since it runs Typecheckingvisitor functions it could increment errorcounter if it has any issues so we cant really run this before typechecking visitor, we could use a unique error counter. but it should
         #be fine to run this visitor after type check
      #   self.errorCounter += 1
      #   print('Error: Array variable', id, 'did not have an index [int] to the right of it, can only read into array variables. Error found on line', lineno)

   
   def pre_visitperiodExpression(self, Node):
      pass
   def visitperiodExpression(self, Node):
      
      valueT1, lineno1, isarr1, isfun1, ispara1 = self.childrenTypes.pop()
      #we already checked that the period expressions are declared
      #search the value in the global scope
      cscope = None
      for st in self.classSTS:
         if st.name == valueT1:
            cscope = st
            break
      if cscope == None:
         print('error in period expression wasnt able to find the apropriate scope even though we have already ensured that the scope exists, cscope is None')
      else:
         #we already know it exists cause our undeclvisitor was executed before this and wouldve given errors
         typeval, lineno, isarray, modifier, isfunction, isparameter = cscope.lookup(Node.id)
         #in another visitor we will pass the function instead of lineno
         if isarray:
            #this will help to make sure we are not just using reference to an array in binary operators but rather its elements in its memory
            self.childrenTypes.append((typeval+'$reference',lineno, isarray, isfunction, isparameter))
         else:
            self.childrenTypes.append((typeval,lineno, isarray, isfunction, isparameter))


   def visitidentifierExpression(self, Node):

      for scope in reversed(range(len(self.stack))):
         if self.stack[scope].checkKey(Node.value):
            #break out of the loop
            typeval, lineno, isarray, modifier, isfunction, isparameter = self.stack[scope].lookup(Node.value)
            
            if isarray:
               
               #this will help to make sure we are not just using reference to an array in binary operators but rather its elements in its memory
               self.childrenTypes.append((typeval+'$reference',lineno, isarray, isfunction, isparameter))
            else:
               self.childrenTypes.append((typeval,lineno, isarray, isfunction, isparameter))
            break

   def pre_visitIndex(self, node):
      pass


      
   def visitIndex(self, node):
      #after we evaluate if expression resulted to an int, dont put it back on stack because we are exiting the index so we dont want that interfering with the parent evaluations
      valueT1, lineno1, isarr1, isfun1, ispara1 = self.childrenTypes.pop()
      if valueT1 != 'int':
         print('Error: The expression within the index did not evaluate to an int type. Error found on line', node.lineNum)
         self.errorCounter +=1



   def pre_visitarrayExpression(self, Node):
      pass
   def visitarrayExpression(self, Node):
      #ensure that the expression to the left of us is an array type otherwise we cannot use index on it
      #valueT2, lineno2, isarr2, isfun2, ispara2 = self.childrenTypes.pop() dont need it cause post visit index will get rid of itselfs type from the stack so all thats left is the left expression type evaluation
      #valueT1, lineno1, isarr1, isfun1, ispara1 = self.childrenTypes.pop()
      #if isarr1:
         #it is an array so put it back... we will do the same for functions to make sure we are function calling a function 
      #   self.childrenTypes.append((valueT1, lineno1, isarr1, isfun1, ispara1))
      #else:
      #   print('Error: the expression to left of the index is not an array, can only index arrays. Error found on line', Node.childN2.lineNum)
      #   self.errorCounter +=1
      #ensure that the expression to the left of us is an array type otherwise we cannot use index on it
      #index is also used by new, need to place the code here so we dont cause issues with new keywords
      valueT1, lineno1, isarr1, isfun1, ispara1 = self.childrenTypes.pop()
      if isarr1:
         #valueT1, lineno1, isarr1, isfun1, ispara1 = self.childrenTypes.pop()
         #strip reference off since we know that we have an index to go along with it 
         lengthstr = len(valueT1)
         lengthstr -= 10
         valueT1 = valueT1[:lengthstr]
         self.childrenTypes.append((valueT1, lineno1, False, isfun1, ispara1))
   
      else:
         print('Error: the expression to left of the index is not an array, can only index arrays. Error found on line', Node.childN2.lineNum)
         self.errorCounter +=1
         self.childrenTypes.append((valueT1, lineno1, isarr1, isfun1, ispara1))
      

   
            



#checks that the left expression of a function call is a function type
#we also check for stand alone function variables that arent being indexed
class FunctionCallVisitor(TypeCheckingVisitor):
   def __init__(self, globalst, classsts, functionsts):
      TypeCheckingVisitor.__init__(self, globalst, classsts, functionsts)
      self.orphanFunctions = []
      #something added on for me to know which class a function belongs to
      self.classNames = []

   def pre_visitCompUnit(self, node):
      self.stack.append(self.findFunctionST(node.id, 'global'))
      self.current += 1
      
   def visitCompUnit(self, node):
      #pop the scope off
      self.stack.pop()
      self.current -= 1
      for id, lineno in self.orphanFunctions:
         #since it runs Typecheckingvisitor functions it could increment errorcounter if it has any issues so we cant really run this before typechecking visitor, we could use a unique error counter. but it should
         #be fine to run this visitor after type check
         self.errorCounter += 1
         print('Error: Function', id, 'was not called, requires a () to the right of it with the correct amount of arguments and types, functions need to be called. Error found on line', lineno)


   def pre_visitperiodExpression(self, Node):
      pass
   def visitperiodExpression(self, Node):

     
      valueT1, lineno1, isarr1, isfun1, ispara1 = self.childrenTypes.pop()
      #we already checked that the period expressions are declared
      #search the value in the global scope
      cscope = None
      for st in self.classSTS:
         if st.name == valueT1:
            cscope = st
            break
      if cscope == None:
         print('error in period expression wasnt able to find the apropriate scope even though we have already ensured that the scope exists, cscope is None')
      else:
         #we already know it exists cause our undeclvisitor was executed before this and wouldve given errors
         typeval, lineno, isarray, modifier, isfunction, isparameter = cscope.lookup(Node.id)
         #in another visitor we will pass the function instead of lineno
         if isarray:
            #this will help to make sure we are not just using reference to an array in binary operators but rather its elements in its memory
            if isfunction:
               self.orphanFunctions.append((Node.id, Node.idLineN))
               self.classNames.append(cscope.name)

            self.childrenTypes.append((typeval+'$reference',lineno, isarray, isfunction, isparameter))
         else:
            self.childrenTypes.append((typeval,lineno, isarray, isfunction, isparameter))
            if isfunction:
               self.orphanFunctions.append((Node.id, Node.idLineN))
               self.classNames.append(cscope.name)
         
         

   def visitidentifierExpression(self, Node):
         #we know the varaible is already declared because we called our undeclvisitor before thisfor scope in reversed(range(len(self.stack))):
         
      for scope in reversed(range(len(self.stack))):
         if self.stack[scope].checkKey(Node.value):
            #break out of the loop
            typeval, lineno, isarray, modifier, isfunction, isparameter = self.stack[scope].lookup(Node.value)
            
            if isarray:
               if isfunction:
                  self.orphanFunctions.append((Node.value, Node.lineNum))
                  self.classNames.append(self.stack[scope].name)
               #this will help to make sure we are not just using reference to an array in binary operators but rather its elements in its memory
               self.childrenTypes.append((typeval+'$reference',lineno, isarray, isfunction, isparameter))
            else:
               self.childrenTypes.append((typeval,lineno, isarray, isfunction, isparameter))
               if isfunction:
                  self.orphanFunctions.append((Node.value, Node.lineNum))
                  self.classNames.append(self.stack[scope].name)
            break


   def pre_visitcallExpression(self, Node):
      pass
   def visitcallExpression(self, Node):
      valueT1, lineno1, isarr1, isfun1, ispara1 = self.childrenTypes.pop()
      if isfun1:
         Node.RT = valueT1
         
         Node.parentClass = self.classNames.pop()
         self.childrenTypes.append((valueT1, lineno1, isarr1, isfun1, ispara1))
         
         self.orphanFunctions.pop()
      else:
         print('Error: the expression to left of the arguments is not a function, can only pass arguments to functions. Error found on line', Node.childN2.lineNum)
         self.errorCounter +=1
         self.childrenTypes.append((valueT1, lineno1, isarr1, isfun1, ispara1))



   #validate that the conditional expressions of if and while statements evaluate to 
class IfWhileCondVisitor(TypeCheckingVisitor):
   def __init__(self, globalst, classsts, functionsts):
      TypeCheckingVisitor.__init__(self, globalst, classsts, functionsts)
      

   def pre_visitifStatement(self, Node):
      pass
   def visitifStatement(self, Node):
      #we need to call accept on the first child again, so that the value on the stack is from the conditional expression evaluation
      Node.childN1.accept(self)
      valueT1, lineno1, isarr1, isfun1, ispara1 = self.childrenTypes.pop()
      #do we need to put it back onto the stack???
      #what if expression becomes a this or new
      if valueT1 != 'bool':
         print('Error: The conditional expression for the if statements must evaluate to a bool type. Error found on line', Node.lineNum)
         self.errorCounter += 1
         

      

   def pre_visitwhileStatement(self, Node):
      pass
   def visitwhileStatement(self, Node):
      Node.childN1.accept(self)
      valueT1, lineno1, isarr1, isfun1, ispara1 = self.childrenTypes.pop()
      #do we need to put it back onto the stack???
      #what if expression becomes a this or new
      if valueT1 != 'bool':
         print('Error: The conditional expression for the while statements must evaluate to a bool type. Error found on line', Node.lineNum)
         self.errorCounter += 1
      
   
#make sure this works recursively and on main
#ensure that the correct amount of arguments were passed into the function and that their types match with what was expected
class ParameterCheckingVisitor(TypeCheckingVisitor):
   def __init__(self, globalst, classsts, functionsts):
      TypeCheckingVisitor.__init__(self, globalst, classsts, functionsts)
      self.functionScopes = []
      self.currentparams = [] #holds tuples of (typeval, isarray) of parameters
      self.pastparams = [] #holds lists of past parameters
      self.currentargs = []
      self.pastargs = [] #holds a lists of past arguments
      
   #need to save past parameter saves in case the arguments themselves call another function with their own set of arguments
   #we already ensured that we are going into a function and is a valid function so in post visit use scope by self.stack[-1] then in post as we are
   #leaving pop the scope off
   

   def countParams(self, funscope):
      for typeval, lineno, isarray, modifier, isfunction, isparameter in funscope.data.values():
         #the index 0 will be the first parameter in the function
         if isparameter:
            if isarray:
               self.currentparams.append((typeval+'$reference', isarray))
            else:
               self.currentparams.append((typeval, isarray))


   def pre_visitArguments(self, node):
      #save the current list and call count params
      self.pastparams.append(self.currentparams)
      self.currentparams = []
      self.pastargs.append(self.currentargs)
      self.currentargs = []
      if self.functionScopes[0] is not None:
         self.countParams(self.functionScopes[-1])
      
      
   def visitArguments(self, node):
      if len(self.currentparams) > len(self.currentargs):
         print('Error: Not enough arguments passed into function call, expected',str(len(self.currentparams)), 'arguments but only got',str(len(self.currentargs)), 'for function',self.functionScopes[-1].name,'--Error found on line',node.lineNum)
         self.errorCounter += 1
      elif len(self.currentparams) < len(self.currentargs):
         print('Error: Too many arguments passed into function call, expected',str(len(self.currentparams)), 'arguments but got',str(len(self.currentargs)), 'for function',self.functionScopes[-1].name,'--Error found on line',node.lineNum)
         self.errorCounter += 1
      elif len(self.currentparams) == len(self.currentargs):
         for i in range(len(self.currentparams)):
            argT, argArr = self.currentargs[i]
            paramT, paramArr = self.currentparams[i]
            if argT == paramT:
               #we dont need to check array cause its included in Type with $reference
               pass

               #if argArr != paramArr:
                #  if argArr:
                 #    print('Error: Argument',str(i),'is an an array while the parameter is a non-array. Argument must match parameter type and if its an array, for function',self.functionScopes[-1].name,'Error found on line',node.lineNum)
                  #   self.errorCounter += 1
                  #   break
                  #elif paramArr:
                  #   print('Error: Argument',str(i),'is not an array while the parameter is an array. Argument must match parameter type and if its an array, for function',self.functionScopes[-1].name,'Error found on line',node.lineNum)
                  #   self.errorCounter += 1
                  #   break

                  
            else:
               if (argT == 'null' and ('$reference' in paramT)) or (argT == 'null' and self.stack[0].checkKey(paramT)):
                  pass
               else:
                  print('Error: Argument',str(i+1),'type:',argT,'does not match the parameter type:',paramT,'that was expected for the function',self.functionScopes[-1].name,'--Error found on line',node.lineNum)
                  self.errorCounter += 1
                  break



      #so if it has a parent arguments it can access the correct data 
      self.functionScopes.pop()
      self.currentparams = self.pastparams.pop()
      self.currentargs = self.pastargs.pop()
   def pre_visitArgumentList(self, node):
      pass
   def visitArgumentList(self, node):
      #after we evaluate one argument by type checking we pop one off the stack so its not misread by its outer parent call
      #before we just self.chilredntypes.pop() no for len
      #it will store these in reverse order so child3,child2type,child1type
      for i in range(len(node.children)):
         valueT, lineno, isarr, isfun, ispara = self.childrenTypes.pop()
         self.currentargs.insert(0,(valueT,isarr))
      #self.currentargs.sort(reverse=True)
      #now in order of child1type,child2type,child3type

      

   def pre_visitperiodExpression(self, Node):
      pass
   def visitperiodExpression(self, Node):

      valueT1, lineno1, isarr1, isfun1, ispara1 = self.childrenTypes.pop()
      #we already checked that the period expressions are declared
      #search the value in the global scope
      cscope = None
      for st in self.classSTS:
         if st.name == valueT1:
            cscope = st
            break
      if cscope == None:
         print('error in period expression wasnt able to find the apropriate scope even though we have already ensured that the scope exists, cscope is None\n\n')
      else:
         #we already know it exists cause our undeclvisitor was executed before this and wouldve given errors
         typeval, lineno, isarray, modifier, isfunction, isparameter = cscope.lookup(Node.id)
         
         if isfunction:
            funscope = self.findFunctionST(Node.id, cscope.name)
            self.functionScopes.append(funscope)
         #in another visitor we will pass the function instead of lineno
         if isarray:
            #this will help to make sure we are not just using reference to an array in binary operators but rather its elements in its memory
            self.childrenTypes.append((typeval+'$reference',lineno, isarray, isfunction, isparameter))
         else:
            self.childrenTypes.append((typeval,lineno, isarray, isfunction, isparameter))

   def visitidentifierExpression(self, Node):
         #we know the varaible is already declared because we called our undeclvisitor before this
         
      for scope in reversed(range(len(self.stack))):
         if self.stack[scope].checkKey(Node.value):
            #break out of the loop
            typeval, lineno, isarray, modifier, isfunction, isparameter = self.stack[scope].lookup(Node.value)
            if isfunction:
               funscope = self.findFunctionST(Node.value, self.stack[scope].name)
               self.functionScopes.append(funscope)

            if isarray:
            #this will help to make sure we are not just using reference to an array in binary operators but rather its elements in its memory
               self.childrenTypes.append((typeval+'$reference',lineno, isarray, isfunction, isparameter))
            else:
               self.childrenTypes.append((typeval,lineno, isarray, isfunction, isparameter))
            break


#have to do it in previsit before it calls its children
   def pre_visitnewExpression(self, Node):
       #check global scope if class even exists with its name the same as the type
      if self.stack[0].checkKey(Node.childN1.valType):
         #break out of the loop
         #check if its an instance of arguments
         if isinstance(Node.childN2, nodes.arguments):
            #we know that childN1 type must have a value of class name or in other words its constructor
            constrfunct = self.findFunctionST(Node.childN1.valType, Node.childN1.valType)
            #typeval, lineno, isarray, modifier, isfunction, isparameter = self.stack[0].lookup(Node.childN1.valType)
            #self.childrenTypes.append((typeval,lineno, isarray, isfunction, isparameter))
            self.functionScopes.append(constrfunct)
            
   

   


#i dont think we even need the New vistor because our typechecking visitor validates that we use new in the correct way and that it also exists
class NewVisitor(TypeCheckingVisitor):
   def __init__(self, globalst, classsts, functionsts):
      TypeCheckingVisitor.__init__(self, globalst, classsts, functionsts)
      self.orphanFunctions = []
   



#go through each type node and check to see if it is valid, for instance check if its one of the basic types or if its valType matches any of the class names in the global scope. 
#the only types allowed are the static ones and classes
#call this after undeclared checking, since types arent valid if they dont exist
class ValidTypeVisitor(TypeCheckingVisitor):
   def __init__(self, globalst, classsts, functionsts):
      TypeCheckingVisitor.__init__(self, globalst, classsts, functionsts)
      self.orphanFunctions = []
   def visitTypeN(self, node):
      if node.valType not in ['void','int','char','string','bool']:
         if not self.stack[0].checkKey(node.valType):
            print('Error: The type',node.valType,'inputed on line', node.lineNum,'is not a valid type, type must be either void, int, char, string, bool, or a classname')
            self.errorCounter += 1



#validate that the type of expression used in the switch is a char or int.
#validate that case children of switch have their types matched with its parent/switch expression
# call these visitors after typechecking visitor
class SwitchCaseVisitor(TypeCheckingVisitor):
   def __init__(self, globalst, classsts, functionsts):
      TypeCheckingVisitor.__init__(self, globalst, classsts, functionsts)
      self.prevSWTypes = []
      self.currentSWType = ''
   def pre_visitswitchStatement(self, Node):
      #evaluate the type for my expression and set it as a flag, maybe do the same thing save what we currently have away  when we enter another switch cause we could have another switch within a case statement
      self.prevSWTypes.append(self.currentSWType)
      self.currentSWType = ''
      Node.childN1.accept(self)
      valueT, lineno, isarr, isfun, ispara = self.childrenTypes.pop()
      if valueT not in ['int','char']:
         print('Error: Switch statement expression must evaluate to a char or int type', Node.lineNum)
         self.errorCounter += 1
         
      self.currentSWType = valueT

      
   def visitswitchStatement(self, Node):
      #pop of the prev stack and assign it to current
      self.currentSWType = self.prevSWTypes.pop()
      
   def pre_visitCaseBlock(self, node):
      pass
   def visitCaseBlock(self, node):
      pass
   def pre_visitCase(self, node):
      #can do either in per or post visit
      #check my case value and make sure it has the same type as my switch statement flag(our grammar ensures that case has a char literal or int literal)
      if self.currentSWType in ['int','char']:
         if self.currentSWType != node.valType:
            print('Error: Case value must be a',self.currentSWType,'literal, current case value type does not match its parents switch expression type. Error found on line', node.lineNum)
            self.errorCounter += 1
      #i could do an else and report an error but the error is reported earlier in the parent switch previsit

      
   def visitCase(self, node):
      pass
   




#validate that each function has return of their return type
#if return type is void it still needs a return but just return 0
#if the functions return type doesnt match with the statement return exp or if it doesnt return anything or if it doesnt even contain a return statement
#throw an error
#post visit function decl and constrdecl check if return counter is at least one and set it back to zero
#do constructors need a return statement
#does main require a return statement
class FunctionReturnVisitor(TypeCheckingVisitor):
   def __init__(self, globalst, classsts, functionsts):
      TypeCheckingVisitor.__init__(self, globalst, classsts, functionsts)
      self.retCounter = 0

   def pre_visitMethodDecl(self, node):
      self.stack.append(self.findFunctionST(node.id, self.stack[self.current].name))
      self.current += 1
      
      self.retCounter = 0
      
   def visitMethodDecl(self, node):
      #have to do this before we pop the scope off 
      #if self.retCounter == 0:
      #   print('Error: the method',node.id,'in class',self.stack[self.current].parent,'requires at least one return statement with the appropriate return type. Error found on line', node.lineNum)
      #   self.errorCounter += 1
      #pop the scope off
      self.stack.pop()
      self.current -= 1
      

      
   def pre_visitConstructorDecl(self, node):
      self.stack.append(self.findFunctionST(node.id, self.stack[self.current].name))
      self.current += 1
      self.retCounter = 0
      
   def visitConstructorDecl(self, node):
      #if self.retCounter == 0:
         #i dont think we need to have a return staement for constructors if so what return type do we need 
      #   print('Error: the constructor',node.id,'in class',self.stack[self.current].parent,'requires at least one return statement with the appropriate return type. Error found on line', node.lineNum)
      #   self.errorCounter += 1
      if self.retCounter > 0:
         #i dont think we need to have a return staement for constructors if so what return type do we need 
         print('Error: the constructor',node.id,'in class',self.stack[self.current].parent,' doesnt require a return statement, ill take care of it :). the linenum of the class that the error was found in is on', node.lineNum)
         self.errorCounter += 1
      #pop the scope off
      self.stack.pop()
      self.current -= 1

   def pre_visitreturnStatement(self, Node):
      self.retCounter += 1
      pass
   def visitreturnStatement(self, Node):
      #is it allowed in constructors and main?
      funame = self.stack[self.current].name
         #access its class 
      typeval, lineno, isarray, modifier, isfunction, isparameter = self.stack[self.current-1].lookup(funame)
      if isarray:
         typeval = typeval+'$reference'

      if Node.childN1 is None:
         
         if typeval != 'void':
            print('Error: return statement on line', Node.lineNum, 'needs to return a', typeval)
            self.errorCounter += 1
         else:
            #apparently its okay for void to have a return type as long as it returns nothing
            #print('Error: Functions with a return type of void, should not contain any return statements. Please omit the return statement on line', Node.lineNum)
            #self.errorCounter += 1
            pass
      else:
         valueT1, lineno1, isarr1, isfun1, ispara1 = self.childrenTypes.pop()
         if (typeval == 'void'):
            #print('Error: Functions with a return type of void, should not contain any return statements. Please omit the return statement on line', Node.lineNum)
            print('Error: Functions with a return type of void, should not return any values. Please omit the value you are returning in the return statement', Node.lineNum)
            self.errorCounter += 1
         elif valueT1 == typeval:

            #if isarr1 != isarray:
             #  if isarr1:
              #    print('Error: return statement on line', Node.lineNum, 'cannot return an array')
              #    self.errorCounter += 1
              # elif isarray:
              #    print('Error: return statement on line', Node.lineNum, 'needs to return an array')
              #    self.errorCounter += 1
              pass

         else:
            if (('$reference' in typeval) and (valueT1 == 'null')) or (self.stack[0].checkKey(typeval) and (valueT1 == 'null')):
               pass
            else:
               print('Error: return statement on line', Node.lineNum, 'does not match the return type', typeval, 'of the function')
               self.errorCounter += 1

   

   def visitClassDef(self, node):
      self.retCounter = 0
      #pop the scope off
      self.stack.pop()
      self.current -= 1
   #have to check return type for main as well??
   def pre_visitCompUnit(self, node):
      self.stack.append(self.findFunctionST(node.id, 'global'))
      self.current += 1
      self.retCounter = 0
      
   def visitCompUnit(self, node):
      #functions dont require return statements i manually input at least one regardless
      if self.retCounter > 0:
         #i dont think we need to have a return staement for constructors if so what return type do we need 
         print('Error: main is a void type, as such it doesnt require and return statements.')
         self.errorCounter += 1

      #pop the scope off
      self.stack.pop()
      self.current -= 1




#ensure that break statements are ONLY used within a while statements and switch statements
#previsit save the last break counter in a list and set it to zero, post visit check break counter is at least 1 if not output error message, also in post visit pop off the last break counter and set it to current
class BreakVisitor(TypeCheckingVisitor):
   def __init__(self, globalst, classsts, functionsts):
      TypeCheckingVisitor.__init__(self, globalst, classsts, functionsts)
      self.prevbreaks = []
      self.currentbreaks = []

   def pre_visitCompUnit(self, node):
      self.stack.append(self.findFunctionST(node.id, 'global'))
      self.current += 1
      
      
   def visitCompUnit(self, node):

      #pop the scope off
      self.stack.pop()
      self.current -= 1
      for lineno in self.currentbreaks:
         print('Error: Break statements can only occur within switch and while statements. Break statement on line', str(lineno), 'is not within a while or switch statement')
         self.errorCounter += 1

   
   def pre_visitswitchStatement(self, Node):
      self.prevbreaks.append(self.currentbreaks)
      self.currentbreaks = []
      

      
   def visitswitchStatement(self, Node):
      self.currentbreaks = self.prevbreaks.pop()
      

   def pre_visitwhileStatement(self, Node):
      self.prevbreaks.append(self.currentbreaks)
      self.currentbreaks = []
      
   def visitwhileStatement(self, Node):
      self.currentbreaks = self.prevbreaks.pop()
      
   def visitbreakStatement(self, Node):
      self.currentbreaks.append(Node.lineNum)




   

















#before desugaring make visitors that default initialize like he said 
#go through each symbol in the symbol table and default initialize it.
#what do i default initialize arrays? no they just allocate off heap and contain a pointer or reference to that spot in memory
#id expressions have to know where in memory it is also i cant just have it take a register but instead maybe take the next open one?
#since we are desugaring we know for a fact that everything is correct syntax wise and semantic wise.
#have to rewrite special assignments like d += 34 to d = d+45 same for *= and others, again like he said, take complex nodes and 
#turn them into simpler nodes that mean the same thing, this could also mean turning into ast nodes and asm nodes
#LDA loads address  shouldnt references be initialized to zero?  only need to support string literals sthey can be in static memory aka directive
# a = d+e +5+e+d
#15visitors average for everything 

#first simplify
#when do we default initialize?
#based off of what i read, first we have to simplify and make an intermediate format of my code. this means simplfiying for loops and while loops,
#as well as dot expressions and indexes. for example some people are doing a.b().c   -> temp1 = a.b();   temp2 = temp1.c
#from there we can start creating actual ASembly by also have a record or object that keeps track of what registers are being used and which ones are being used
#this helps us to create the right asm nodes with the correct registers. the book says something about how you will be able to keep track, function locals will be on the stack
#i have a note that says c.f(4) -> becomes f(c,4) which is just passing in of course this
#of local variables with something, im unsure check page 14 chp 11
#we can create activation records using the functions scope/ symbol table. this also allows us to know what local varaibles are also gonna be stored
#on the activation record/stack
#remember in the assembler class we had local variables in functions called temp can and should we assume that those local varaibles will be stored the
#same way in main since main is a function? --> i mean that makes sense if we are also gonna be making our own temporary variables in main 
#int values are the only values we can perform binary operations
#book says that global variables will become labels or directives, should we do the same for main or just treat it as a function and store variables
#as locals which would mean keeping a record and just accessing by offset/address in heap pointer or something , also by using the activation record
#which is the paramaters and size along with local variables size to accuratley compute offset and know how to obtain them using the offset and act recored

#chp 8 is about making intermediate code simplifying

#for now we assume local variables are also stored in main
#reduce while to a dummy token with a label and if statement

#gonna still need to keep track of scope stack in the comp constr and function nodes
class ReConnectVisitor(Visitor):
   def __init__(self, globalst, classsts, functionsts):
      self.globalST = globalst
      self.classSTS = classsts
      self.functionSTS = functionsts
      self.stack = []
      self.current = 0 #max depth for stack will be index 2, to keep track of that place should we just use current as a index tracker????
      
      self.stack.append(self.globalST)
      
      self.nodesStack = []

   def findClassST(self,name):
      for st in self.classSTS:
         if st.name == name:
            return st
   
   def findFunctionST(self,name, parentN):
      for st in self.functionSTS:
         if st.name == name and st.parent == parentN:
            return st
         
   def pre_visitCompUnit(self, node):
      self.stack.append(self.findFunctionST(node.id, 'global'))
      self.current += 1
      
   def visitCompUnit(self, node):
      #pop the scope off
      self.stack.pop()
      self.current -= 1
      #have to reverse sort afterwards
      numChildren = len(node.children)
      node.children = []
      for child in range(numChildren):
         node.children.insert(0,self.nodesStack.pop())
      #node.children.sort(reverse=True)

      
   def pre_visitClassDef(self, node):
      self.stack.append(self.findClassST(node.id))
      self.current += 1
      
   def visitClassDef(self, node):
      #pop the scope off
      self.stack.pop()
      self.current -= 1

      numChildren = len(node.methodChildren)
      node.methodChildren = []
      for child in range(numChildren):
         node.methodChildren.insert(0,self.nodesStack.pop())
      #node.methodChildren.sort(reverse=True)

      numChildren = len(node.dataChildren)
      node.dataChildren = []
      for child in range(numChildren):
         node.dataChildren.insert(0,self.nodesStack.pop())
      #node.dataChildren.sort(reverse=True)
      self.nodesStack.append(node)

      
   def visitTypeN(self, node):
      self.nodesStack.append(node)
      
   def visitModifierN(self, node):
      self.nodesStack.append(node)
      
   def pre_visitClassMemDef(self, node):
      pass
      
   def visitClassMemDef(self, node):
      node.child = self.nodesStack.pop()
      self.nodesStack.append(node)
      pass

   def pre_visitDataMemDecl(self, node):
      pass
   def visitDataMemDecl(self, node):
      #need to go in reverse be cuase the first pop will be the child N2
      node.child2 = self.nodesStack.pop()
      node.child1 = self.nodesStack.pop()
      numChildren = len(node.prepChildren)
      node.prepChildren = []
      for child in range(numChildren):
         node.prepChildren.insert(0,self.nodesStack.pop())
      self.nodesStack.append(node)
      

      
   def pre_visitMethodDecl(self, node):
      self.stack.append(self.findFunctionST(node.id, self.stack[self.current].name))
      self.current += 1
      
   def visitMethodDecl(self, node):
      #pop the scope off
      self.stack.pop()
      self.current -= 1

      node.childN3 = self.nodesStack.pop()
      node.childN2 = self.nodesStack.pop()
      node.childN1 = self.nodesStack.pop()
      self.nodesStack.append(node)
      
   def pre_visitConstructorDecl(self, node):
      self.stack.append(self.findFunctionST(node.id, self.stack[self.current].name))
      self.current += 1
      
   def visitConstructorDecl(self, node):
      #pop the scope off
      self.stack.pop()
      self.current -= 1
      node.childN2 = self.nodesStack.pop()
      self.nodesStack.append(node)
   
   def visitInitializer(self, node):
      node.childN1 = self.nodesStack.pop()
      self.nodesStack.append(node)
      
   
   def visitMethodSuf(self, node):
      if node.childN1 is None:
         node.childN2 = self.nodesStack.pop()
      else:
         node.childN2 = self.nodesStack.pop()
         node.childN1 = self.nodesStack.pop()
      self.nodesStack.append(node)
      
   
   def visitMethodBody(self, node):
      #have to reverse sort afterwards
      numChildren = len(node.children)
      node.children = []
      for child in range(numChildren):
         node.children.insert(0,self.nodesStack.pop())
      #node.children.sort(reverse=True)
      self.nodesStack.append(node)
      
   
   def visitParameterList(self, node):
      #have to reverse sort afterwards
      numChildren = len(node.children)
      node.children = []
      for child in range(numChildren):
         node.children.insert(0,self.nodesStack.pop())
      #node.children.sort(reverse=True)
      self.nodesStack.append(node)
      
   
   def visitParameter(self, node):
      node.childN1 = self.nodesStack.pop()
      self.nodesStack.append(node)
      
   
   def visitVarDecl(self, node):
      if node.initializer is None:
         node.childN1 = self.nodesStack.pop()
      else:
         node.initializer = self.nodesStack.pop()
         node.childN1 = self.nodesStack.pop()
      self.nodesStack.append(node)
      
   
   def visitcurlyBrackStatement(self, Node):
      #have to reverse sort afterwards
      numChildren = len(Node.children)
      Node.children = []
      for child in range(numChildren):
         Node.children.insert(0,self.nodesStack.pop())

      numChildren = len(Node.prepChildren)
      Node.prepChildren = []
      for child in range(numChildren):
         Node.prepChildren.insert(0,self.nodesStack.pop())
      #Node.children.sort(reverse=True)
      self.nodesStack.append(Node)
      
   

   def visitexpressionStatement(self, Node):
      Node.childN1 = self.nodesStack.pop()
      numChildren = len(Node.prepChildren)
      Node.prepChildren = []
      for child in range(numChildren):
         Node.prepChildren.insert(0,self.nodesStack.pop())
      self.nodesStack.append(Node)
      

   
   def visitifStatement(self, Node):
      if Node.childN3 is None:
         Node.childN2 = self.nodesStack.pop()
         Node.childN1 = self.nodesStack.pop()
         
      else:
         Node.childN3 = self.nodesStack.pop()
         Node.childN2 = self.nodesStack.pop()
         Node.childN1 = self.nodesStack.pop()

      numChildren = len(Node.prepChildren)
      Node.prepChildren = []
      for child in range(numChildren):
         Node.prepChildren.insert(0,self.nodesStack.pop())
      self.nodesStack.append(Node)
      

   
   def visitwhileStatement(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
      numChildren = len(Node.prepChildren)
      Node.prepChildren = []
      for child in range(numChildren):
         Node.prepChildren.insert(0,self.nodesStack.pop())
      self.nodesStack.append(Node)
      

   
   def visitreturnStatement(self, Node):
      if Node.childN1 is None:
         pass
         
      else:
         Node.childN1 = self.nodesStack.pop()
         

      numChildren = len(Node.prepChildren)
      Node.prepChildren = []
      for child in range(numChildren):
         Node.prepChildren.insert(0,self.nodesStack.pop())

   
      
      self.nodesStack.append(Node)
      

   
   def visitcoutStatement(self, Node):
      Node.childN1 = self.nodesStack.pop()
      numChildren = len(Node.prepChildren)
      Node.prepChildren = []
      for child in range(numChildren):
         Node.prepChildren.insert(0,self.nodesStack.pop())
      self.nodesStack.append(Node)
      

   
   def visitcinStatement(self, Node):
      Node.childN1 = self.nodesStack.pop()
      numChildren = len(Node.prepChildren)
      Node.prepChildren = []
      for child in range(numChildren):
         Node.prepChildren.insert(0,self.nodesStack.pop())
      self.nodesStack.append(Node)

  
   def visitswitchStatement(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
      numChildren = len(Node.prepChildren)
      Node.prepChildren = []
      for child in range(numChildren):
         Node.prepChildren.insert(0,self.nodesStack.pop())
      self.nodesStack.append(Node)
      

   def visitbreakStatement(self, Node):
      self.nodesStack.append(Node)
      

   
   def visitvarDeclStatement(self, Node):
      Node.childN1 = self.nodesStack.pop()
      numChildren = len(Node.prepChildren)
      Node.prepChildren = []
      for child in range(numChildren):
         Node.prepChildren.insert(0,self.nodesStack.pop())
      self.nodesStack.append(Node)
      

#end of statements
   
   def visitCaseBlock(self, node):
      numChildren = len(node.defaultStmtChildren)
      node.defaultStmtChildren = []
      for child in range(numChildren):
         node.defaultStmtChildren.insert(0,self.nodesStack.pop())
      #node.defaultStmtChildren.sort(reverse=True)

      numChildren = len(node.caseChildren)
      node.caseChildren = []
      for child in range(numChildren):
         node.caseChildren.insert(0,self.nodesStack.pop())
      #node.caseChildren.sort(reverse=True)
      self.nodesStack.append(node)
      
   
   def visitCase(self, node):
      numChildren = len(node.statementChildren)
      node.statementChildren = []
      for child in range(numChildren):
         node.statementChildren.insert(0,self.nodesStack.pop())
      #node.statementChildren.sort(reverse=True)
      self.nodesStack.append(node)
      


#    def visitExpression(node):

  
   def visitassignmentExpression(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
      self.nodesStack.append(Node)
      

  
   def visitaddAssignmentExpression(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
      self.nodesStack.append(Node)
      pass

   
   def visitsubAssignmentExpression(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
      self.nodesStack.append(Node)
      pass

  
   def visitmultAssignmentExpression(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
      self.nodesStack.append(Node)
      pass
   

   
   def visitdivAssignmentExpression(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
      self.nodesStack.append(Node)
      pass

   
   def visitplusExpression(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
      self.nodesStack.append(Node)
      pass

   
   def visitminusExpression(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
      self.nodesStack.append(Node)
      pass

   
   def visitmultExpression(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
      self.nodesStack.append(Node)
      pass

   
   def visitdivExpression(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
      self.nodesStack.append(Node)
      pass

   
   def visitequalityExpression(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
      self.nodesStack.append(Node)
      pass

   
   def visitnotEqualExpression(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
      self.nodesStack.append(Node)
      pass

   
   def visitlessThanExpression(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
      self.nodesStack.append(Node)
      pass

   
   def visitgreaterThanExpression(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
      self.nodesStack.append(Node)
      pass

   
   def visitLTEqualsExpression(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
      self.nodesStack.append(Node)
      pass

   
   def visitGTEqualsExpression(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
      self.nodesStack.append(Node)
      pass

   
   def visitandExpression(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
      self.nodesStack.append(Node)
      pass

   
   def visitorExpression(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
      self.nodesStack.append(Node)
      pass
      
  
   def visitnotExpression(self, Node):
      Node.childN1 = self.nodesStack.pop()
      self.nodesStack.append(Node)
      pass

   
   def visitunaryPlusExpression(self, Node):
      Node.childN1 = self.nodesStack.pop()
      self.nodesStack.append(Node)
      pass

   
   def visitunaryMinusExpression(self, Node):
      Node.childN1 = self.nodesStack.pop()
      self.nodesStack.append(Node)
      pass

   def visitliteralIntExpression(self, Node):
      self.nodesStack.append(Node)
      pass

   def visitliteralCharExpression(self, Node):
      self.nodesStack.append(Node)
      pass

   def visitliteralStringExpression(self, Node):
      self.nodesStack.append(Node)
      pass

   def visittrueExpression(self, Node):
      self.nodesStack.append(Node)
      pass

   def visitfalseExpression(self, Node):
      self.nodesStack.append(Node)
      pass

   def visitnullExpression(self, Node):
      self.nodesStack.append(Node)
      pass

   def visitidentifierExpression(self, Node):
      self.nodesStack.append(Node)
      pass

   def visitthisExpression(self, Node):
      self.nodesStack.append(Node)
      pass

   
   def visitcallExpression(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
      self.nodesStack.append(Node)
      pass

   
   def visitarrayExpression(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
      self.nodesStack.append(Node)
      pass

   
   def visitperiodExpression(self, Node):
      Node.childN1 = self.nodesStack.pop()
      self.nodesStack.append(Node)
      pass

   
   def visitnewExpression(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
      self.nodesStack.append(Node)
      pass

   
   def visitparenExpression(self, Node):
      Node.childN1 = self.nodesStack.pop()
      self.nodesStack.append(Node)
      pass

#end of expressions

   
   def visitArguments(self, node):
      if node.childN1 is None:
         self.nodesStack.append(node)
      else:
         node.childN1 = self.nodesStack.pop()
         self.nodesStack.append(node)

      pass
   
   def visitArgumentList(self, node):
      numChildren = len(node.children)
      node.children = []
      for child in range(numChildren):
         node.children.insert(0,self.nodesStack.pop())
      #node.children.sort(reverse=True)
      self.nodesStack.append(node)
      pass
   
   def visitIndex(self, node):
      node.childN1 = self.nodesStack.pop()
      self.nodesStack.append(node)
      pass

   def pre_visitASMnode(self,Node):
      pass
   def visitASMnode(self,Node):
      numChildren = len(Node.children)
      Node.children = []
      for child in range(numChildren):
         Node.children.insert(0,self.nodesStack.pop())
      #node.children.sort(reverse=True)
      self.nodesStack.append(Node)

   def pre_visitBlocknode(self, Node):
      pass
   def visitBlocknode(self, Node):
      numChildren = len(Node.children)
      Node.children = []
      for child in range(numChildren):
         Node.children.insert(0,self.nodesStack.pop())
      #node.children.sort(reverse=True)
      self.nodesStack.append(Node)

#ASMnode visits.... or just make an ASMnode pre and post visit that the rest of these nodes inherit from becuase they all hold relitiveally the same data
   def visitJMPnode(self, Node):
      pass
   def visitJMRnode(self, Node):
      pass
   def visitBNZnode(self, Node):
      pass
   def visitBGTnode(self, Node):
      pass
   def visitBLTnode(self, Node):
      pass
   def visitBRZnode(self, Node):
      pass
   def visitMOVnode(self, Node):
      pass
   def visitLDAnode(self, Node):
      pass
   def visitSTRLnode(self, Node):
      pass
   def visitLDRLnode(self, Node):
      pass
   def visitSTBLnode(self, Node):
      pass
   def visitLDBLnode(self, Node):
      pass
   def visitADInode(self, Node):
      pass
   def visitSUBnode(self, Node):
      pass
   def visitMULnode(self, Node):
      pass
   def visitDIVnode(self, Node):
      pass
   def visitCMPnode(self, Node):
      pass
   def visitANDnode(self, Node):
      pass
   def visitORnode(self, Node):
      pass
   def visitTRPZEROnode(self, Node):
      pass
   def visitTRPONEnode(self, Node):
      pass
   def visitTRPTWOnode(self, Node):
      pass
   def visitTRPTHREEnode(self, Node):
      pass
   def visitTRPFOURnode(self, Node):
      pass
   def visitSTRRnode(self, Node):
      pass
   def visitLDRRnode(self, Node):
      pass
   def visitSTBRnode(self, Node):
      pass
   def visitLDBRnode(self, Node):
      pass
   def visitALLCIMMEDIATEnode(self, Node):
      pass
   def visitALLCLABELnode(self, Node):
      pass
   def visitALLCREGISTERnode(self, Node):
      pass
   def visitDIRECTIVEnode(self, Node):
      pass



#if im not provided a constructor i have to create a default one... wouldnt that just be its normal activation record defaulted to zero?
#basically just add a constructor declaration with This as its argument and just return this or reference to object,, just make it have return statement that returns this. would need to do this before optimization of this
#because it puts a this in the arguments of the constructors and methods 
#do all the normal kxi nodes expansions and simplifications, returns, default constr, activation record so i can default initialize and correctly offset.

class DefaultConstrVisitor(ReConnectVisitor):#gonna need to keep a pointer and if its zero then i have to create a contructor function and append it. Have to do this before this optimization
   def __init__(self, globalst, classsts, functionsts):
      ReConnectVisitor.__init__(self, globalst, classsts, functionsts)
      self.constrCount = 0
   
   def pre_visitClassDef(self, node):
      self.stack.append(self.findClassST(node.id))
      self.current += 1
      self.constrCount = 0
      
   def visitClassDef(self, node):
      

      numChildren = len(node.methodChildren)
      node.methodChildren = []
      for child in range(numChildren):
         node.methodChildren.insert(0,self.nodesStack.pop())
      #node.methodChildren.sort(reverse=True)

      numChildren = len(node.dataChildren)
      node.dataChildren = []
      for child in range(numChildren):
         node.dataChildren.insert(0,self.nodesStack.pop())
      #node.dataChildren.sort(reverse=True)
      self.nodesStack.append(node)

      if self.constrCount == 0:
         #provide a default constructor
         defconstr = nodes.classMemDef(nodes.constructorDecl(self.stack[self.current].name, 0, nodes.methodSuf(None, nodes.methodBody([]))))
         node.methodChildren.append(defconstr)

      #have to do the above code before pop so we can get the class name
      #pop the scope off
      self.stack.pop()
      self.current -= 1

      

      
   
   def pre_visitConstructorDecl(self, node):
      self.stack.append(self.findFunctionST(node.id, self.stack[self.current].name))
      self.current += 1
      self.constrCount += 1
      
   def visitConstructorDecl(self, node):
      #pop the scope off
      self.stack.pop()
      self.current -= 1
      node.childN2 = self.nodesStack.pop()
      self.nodesStack.append(node)


#for each one that accesses a data member we need keep note of it for whichever symbol that is

class TransformThisVisitor(Visitor):
   def __init__(self, globalst, classsts, functionsts):
      self.globalST = globalst
      self.classSTS = classsts
      self.functionSTS = functionsts
      self.stack = []
      self.current = 0 #max depth for stack will be index 2, to keep track of that place should we just use current as a index tracker????
      
      self.stack.append(self.globalST)
      self.leftflag = False
      self.prevflags = []
      self.prevTypes = []
      self.nodesStack = []
   
   def findClassST(self,name):
      for st in self.classSTS:
         if st.name == name:
            return st
   
   def findFunctionST(self,name, parentN):
      for st in self.functionSTS:
         if st.name == name and st.parent == parentN:
            return st


   def pre_visitCompUnit(self, node):
      self.stack.append(self.findFunctionST(node.id, 'global'))
      self.current += 1
      
   def visitCompUnit(self, node):
      #pop the scope off
      self.stack.pop()
      self.current -= 1
      
   def pre_visitClassDef(self, node):
      self.stack.append(self.findClassST(node.id))
      self.current += 1
      
   def visitClassDef(self, node):
      #pop the scope off
      self.stack.pop()
      self.current -= 1

      
   def pre_visitMethodDecl(self, node):
      self.stack.append(self.findFunctionST(node.id, self.stack[self.current].name))
      self.current += 1
      
   def visitMethodDecl(self, node):
      #pop the scope off
      self.stack.pop()
      self.current -= 1
      
   def pre_visitConstructorDecl(self, node):
      self.stack.append(self.findFunctionST(node.id, self.stack[self.current].name))
      self.current += 1
      
   def visitConstructorDecl(self, node):
      #pop the scope off
      self.stack.pop()
      self.current -= 1

   def pre_visitParameterList(self, node):
      pass
   def visitParameterList(self, node):
      
      node.children.insert(0, nodes.thisExpression('this', 0))
      self.stack[self.current].insert('this', self.stack[self.current].parent ,0,False,'',False,True)
      pass

   def pre_visitMethodSuf(self, node):
      pass
   def visitMethodSuf(self, node):
      #make sure this is not main 
      if self.stack[self.current].parent != 'global':
         if node.childN1 is None:
            parL = nodes.parameterList(nodes.thisExpression('this', 0), [])
            #ussually you would assign a parameter with a type of the class of this but we can just put this and treat it as null
            node.childN1 = parL
            self.stack[self.current].insert('this', self.stack[self.current].parent ,0,False,'',False,True)
            #else just continue on since parameter list will be called and we will insert there
      pass


   def visitidentifierExpression(self, Node):

      pass
   def visitthisExpression(self, Node):
      pass

   def pre_visitcallExpression(self, Node):
      pass
   def visitcallExpression(self, Node):
      #what its an id that calls its sibling function
      if isinstance(Node.childN1, nodes.periodExpression):
         Id = Node.childN1.id
         #access arguments check for child
         if Node.childN2.childN1 is None:
            argL = nodes.argumentList(Node.childN1.childN1,[])
            Node.childN2.childN1 = argL
            Node.childN1 = nodes.identifierExpression(Id,0)
         else:
            #if we already have an argument list
            Node.childN2.childN1.children.insert(0, Node.childN1.childN1)
            Node.childN1 = nodes.identifierExpression(Id,0)
     
         
         
      elif isinstance(Node.childN1, nodes.identifierExpression):
         #case where it is an identifier and leads to another sibling function
         #make sure its not main
         if Node.childN1.value != 'main':
            if Node.childN2.childN1 is None:
               argL = nodes.argumentList(nodes.thisExpression('this', 0),[])
               Node.childN2.childN1 = argL
               
            else:
               #if we already have an argument list
               Node.childN2.childN1.children.insert(0, nodes.thisExpression('this', 0))
            
      
   def pre_visitperiodExpression(self, Node):
      pass
   def visitperiodExpression(self, Node):
      pass
   def pre_visitArguments(self, node):
      pass
   def visitArguments(self, node):
      pass
   def pre_visitArgumentList(self, node):
      pass
   def visitArgumentList(self, node):
      pass

#assume there are no data members   
#class ThisDataMemVisitor(ReConnectVisitor):
#   def __init__(self, globalst, classsts, functionsts):
#      ReConnectVisitor.__init__(self, globalst, classsts, functionsts)

#   def visitidentifierExpression(self, Node):
#      if self.stack[self.current].checkKey(Node.value):   
#         self.nodesStack.append(Node)
#      elif self.stack[self.current-1].checkKey(Node.value) and (self.current == 2): #this should be looking at the class scope
#         tempthis = nodes.thisExpression('this', 0)
#         tempdot = nodes.periodExpression(tempthis,Node.value,0)
#         self.nodesStack.append(tempdot)
#      else:
#         self.nodesStack.append(Node)


#need to add a return statement to each function
#still need to make the change of a to this.a for the visitor above

#so regardless, later on i still need to reatach or reassign my child to be the new node i created, issues: i dont know which child you are, i dont know if you belong to me
# child could belong to any kind of parent a lot to choose from. to fix this while it does redundant and a lot of code kinda not really, we can have base visitor
#that for each post visit for each node including ASM nodes i count the number of children i have and pop that off the stack and reassign those to my children
#then i push myself onto the stack for the next parent to take me. this works cause in post visit the current node will have the old children so it just counts
#how many it has and pops that many off the stack and reassigns, it doesnt care if what it popped off isnt its orignal or old child it will still reassign it as its child
#. this allows me to not have to worry about finding which parent belong to and which number child i am for that parent so it can reassign me correctly.
#instead i can inherit from this class and overide specific nodes to change to another node or set of nodes and instead of pushing the old on on the stack i push the new one so that the parent can take me instead.

#other classes/objects i will need possibly: activation record(offsets of parameters and local varaibles) 
# and a registerTracker(keeps track of what registers are being used and which ones are free, 
# ex: a plus could take 2 and 3 register so have a check box on those, but after it completes its job we can deselect those boxes to be free
#  for other isntructions)


#this issue i go into is the one in ms teams that one of them talks about and provides a solution, but when would that problem arise?
#check, do we every create a group of nodes or will we just create one node to be the parent of the additional nodes i created?? they said one solution to this
#is to have a block statement node that takes that group of nodes and pushes itself on the stack this way the parent can just pop the number of children it had with no issue

#should i store temporary varaibles in the activation record as i create them
#i should keep a counter for how many additional/temporay statements/variables i create going into statements, i should also have stack that keeps track of the last counters number and when i post visit pop
#that many children as the counter also store the counter maybe?? cant i do the same thing by calling len() on the list?

#simplify expressions
#should we simplify dot expressions?
class SimpleExpVisitor(ReConnectVisitor):
   def __init__(self, globalst, classsts, functionsts):
      ReConnectVisitor.__init__(self, globalst, classsts, functionsts)
      self.prevCounters = []
      #should i make counter global???
      self.prepcounter = 0
      self.prepStmts = []
      #this was added to see if could simplify period expressions
      self.periodtypes = []
      #just append temporary variables to our symbol table
      #self.activeRecords = []
      #self.currentRecords = [] #we dont have to keep a stack i think 
      

      #populate actvation records with current symbols
   #   for funST in self.functionSTS:
   #      actRec = ActivationRecord(funST.name, funST.parent)
   #      for id in funST.data:
   #         typeval, lineno, isarray, modifier, isfunction, isparameter = funST.lookup(id)         
   #         actRec.insert(id, typeval, isparameter)
   #      self.activeRecords.append(actRec)

         
   def findClassST(self,name):
      for st in self.classSTS:
         if st.name == name:
            return st
   
   def findFunctionST(self,name, parentN):
      for st in self.functionSTS:
         if st.name == name and st.parent == parentN:
            return st
   
   

   def pre_visitCompUnit(self, node):
      self.stack.append(self.findFunctionST(node.id, 'global'))
      self.current += 1
      #self.currentRecords.append(self.findFunctionActRec(node.id, '$global'))

      
   def visitCompUnit(self, node):
      #self.currentRecords.pop()
      #pop the scope off
      self.stack.pop()
      self.current -= 1
      #have to reverse sort afterwards
      numChildren = len(node.children)
      node.children = []
      for child in range(numChildren):
         node.children.insert(0,self.nodesStack.pop())
      #node.children.sort(reverse=True)

      
   def pre_visitClassDef(self, node):
      self.stack.append(self.findClassST(node.id))
      self.current += 1
      
   def visitClassDef(self, node):
      #pop the scope off
      self.stack.pop()
      self.current -= 1

      numChildren = len(node.methodChildren)
      node.methodChildren = []
      for child in range(numChildren):
         node.methodChildren.insert(0,self.nodesStack.pop())
      #node.methodChildren.sort(reverse=True)

      numChildren = len(node.dataChildren)
      node.dataChildren = []
      for child in range(numChildren):
         node.dataChildren.insert(0,self.nodesStack.pop())
      #node.dataChildren.sort(reverse=True)
      self.nodesStack.append(node)

   def pre_visitMethodDecl(self, node):
      self.stack.append(self.findFunctionST(node.id, self.stack[self.current].name))
      self.current += 1
      #self.activeRecords.append(self.findFunctionActRec(node.id, self.stack[self.current].name))
      
   def visitMethodDecl(self, node):
      #self.activeRecords.pop()
      #pop the scope off
      self.stack.pop()
      self.current -= 1

      node.childN3 = self.nodesStack.pop()
      node.childN2 = self.nodesStack.pop()
      node.childN1 = self.nodesStack.pop()
      self.nodesStack.append(node)
      
   def pre_visitConstructorDecl(self, node):
      self.stack.append(self.findFunctionST(node.id, self.stack[self.current].name))
      self.current += 1
      #self.activeRecords.append(self.findFunctionActRec(node.id, self.stack[self.current].name))
      
   def visitConstructorDecl(self, node):
      #self.activeRecords.pop()
      #pop the scope off
      self.stack.pop()
      self.current -= 1
      node.childN2 = self.nodesStack.pop()
      self.nodesStack.append(node)   

      #in previsits of statements i should save last counter and set counter to zero 
      #in plus expressions i have to make sure to push a child onto the normal stack for parent to take off

   def pre_visitcurlyBrackStatement(self, Node):
      self.prevCounters.append(self.prepcounter)
      self.prepcounter = 0

   def visitcurlyBrackStatement(self, Node):
      #have to reverse sort afterwards
      numChildren = len(Node.children)
      Node.children = []
      for child in range(numChildren):
         Node.children.insert(0,self.nodesStack.pop())

      numChildren = len(Node.prepChildren)
      Node.prepChildren = []
      for child in range(numChildren):
         Node.prepChildren.insert(0,self.nodesStack.pop())
      #Node.children.sort(reverse=True)
      


      #get the additional statments off the stack
      for i in range(self.prepcounter):
         Node.prepChildren.insert(0,self.prepStmts.pop())
      self.prepcounter = self.prevCounters.pop()

      self.nodesStack.append(Node)

      
   def pre_visitexpressionStatement(self, Node):
      self.prevCounters.append(self.prepcounter)
      self.prepcounter = 0

   def visitexpressionStatement(self, Node):
      Node.childN1 = self.nodesStack.pop()
      numChildren = len(Node.prepChildren)
      Node.prepChildren = []
      for child in range(numChildren):
         Node.prepChildren.insert(0,self.nodesStack.pop())
      

      #get the additional statments off the stack
      for i in range(self.prepcounter):
         Node.prepChildren.insert(0,self.prepStmts.pop())
      self.prepcounter = self.prevCounters.pop()

      self.nodesStack.append(Node)

   
   def pre_visitifStatement(self, Node):
      self.prevCounters.append(self.prepcounter)
      self.prepcounter = 0

   def visitifStatement(self, Node):
      if Node.childN3 is None:
         Node.childN2 = self.nodesStack.pop()
         Node.childN1 = self.nodesStack.pop()
         
      else:
         Node.childN3 = self.nodesStack.pop()
         Node.childN2 = self.nodesStack.pop()
         Node.childN1 = self.nodesStack.pop()

      numChildren = len(Node.prepChildren)
      Node.prepChildren = []
      for child in range(numChildren):
         Node.prepChildren.insert(0,self.nodesStack.pop())
      
      #get the additional statments off the stack
      for i in range(self.prepcounter):
         Node.prepChildren.insert(0,self.prepStmts.pop())
      self.prepcounter = self.prevCounters.pop()

      self.nodesStack.append(Node)
      

   def pre_visitwhileStatement(self, Node):
      self.prevCounters.append(self.prepcounter)
      self.prepcounter = 0
   
   def visitwhileStatement(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
      numChildren = len(Node.prepChildren)
      Node.prepChildren = []
      for child in range(numChildren):
         Node.prepChildren.insert(0,self.nodesStack.pop())
      self.nodesStack.append(Node)
      
      #get the additional statments off the stack
      for i in range(self.prepcounter):
         Node.prepChildren.insert(0,self.prepStmts.pop())
      self.prepcounter = self.prevCounters.pop()

   
   def pre_visitreturnStatement(self, Node):
      self.prevCounters.append(self.prepcounter)
      self.prepcounter = 0

   def visitreturnStatement(self, Node):
      if Node.childN1 is None:
         pass
         
      else:
         Node.childN1 = self.nodesStack.pop()
         

      numChildren = len(Node.prepChildren)
      Node.prepChildren = []
      for child in range(numChildren):
         Node.prepChildren.insert(0,self.nodesStack.pop())

      

      #get the additional statments off the stack
      for i in range(self.prepcounter):
         Node.prepChildren.insert(0,self.prepStmts.pop())
      self.prepcounter = self.prevCounters.pop()
      
      self.nodesStack.append(Node)
      

   def pre_visitcoutStatement(self, Node):
      self.prevCounters.append(self.prepcounter)
      self.prepcounter = 0
   
   def visitcoutStatement(self, Node):
      Node.childN1 = self.nodesStack.pop()
      numChildren = len(Node.prepChildren)
      Node.prepChildren = []
      for child in range(numChildren):
         Node.prepChildren.insert(0,self.nodesStack.pop())
      self.nodesStack.append(Node)
      
      #get the additional statments off the stack
      for i in range(self.prepcounter):
         Node.prepChildren.insert(0,self.prepStmts.pop())
      self.prepcounter = self.prevCounters.pop()

   
   def pre_visitcinStatement(self, Node):
      self.prevCounters.append(self.prepcounter)
      self.prepcounter = 0

   def visitcinStatement(self, Node):
      Node.childN1 = self.nodesStack.pop()
      numChildren = len(Node.prepChildren)
      Node.prepChildren = []
      for child in range(numChildren):
         Node.prepChildren.insert(0,self.nodesStack.pop())
      self.nodesStack.append(Node)

      #get the additional statments off the stack
      for i in range(self.prepcounter):
         Node.prepChildren.insert(0,self.prepStmts.pop())
      self.prepcounter = self.prevCounters.pop()

   def pre_visitswitchStatement(self, Node):
      self.prevCounters.append(self.prepcounter)
      self.prepcounter = 0

   def visitswitchStatement(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
      numChildren = len(Node.prepChildren)
      Node.prepChildren = []
      for child in range(numChildren):
         Node.prepChildren.insert(0,self.nodesStack.pop())
      self.nodesStack.append(Node)

      #get the additional statments off the stack
      for i in range(self.prepcounter):
         Node.prepChildren.insert(0,self.prepStmts.pop())
      self.prepcounter = self.prevCounters.pop()
      
   
   def pre_visitvarDeclStatement(self, Node):
      self.prevCounters.append(self.prepcounter)
      self.prepcounter = 0

   def visitvarDeclStatement(self, Node):
      Node.childN1 = self.nodesStack.pop()
      numChildren = len(Node.prepChildren)
      Node.prepChildren = []
      for child in range(numChildren):
         Node.prepChildren.insert(0,self.nodesStack.pop())
      self.nodesStack.append(Node)

      #get the additional statments off the stack
      for i in range(self.prepcounter):
         Node.prepChildren.insert(0,self.prepStmts.pop())
      self.prepcounter = self.prevCounters.pop()

   #this can hold a variable declaration which could have an expression which could be complex and need a place to prepend its prep statements
   def pre_visitDataMemDecl(self, node):
      self.prevCounters.append(self.prepcounter)
      self.prepcounter = 0

   def visitDataMemDecl(self, node):
      #need to go in reverse be cuase the first pop will be the child N2
      node.child2 = self.nodesStack.pop()
      node.child1 = self.nodesStack.pop()
      numChildren = len(node.prepChildren)
      node.prepChildren = []

      for child in range(numChildren):
         node.prepChildren.insert(0,self.nodesStack.pop())
   

      #get the additional statments off the stack
      for i in range(self.prepcounter):
         node.prepChildren.insert(0,self.prepStmts.pop())
      self.prepcounter = self.prevCounters.pop()
      self.nodesStack.append(node)
   









   #expressions
   #aldous said he recommoneds doing variable declarations instead of assignemnet nodes. this so when we simplify assignment nodes we arent looping over our
   #prepended statements of assignemnt nodes
   #we can have variable declarations in data member declarations of classes 

   
      
   #im gonna choose not to simplify assignment expression cause i never know if its assigning a char string int bool or whatever. and i cant predict what will be on either side of the assignment
   #one way is to have dot expressions and ids put their type on a stack, then when i visit assignment expression i just have to pop one of the types off the stack and depending on its type
   #insert the right symbol in the symbol table, also after im done, i put the type back on the stack so the parent if its another assignment expression, can evaluate what type its working with.
   #will also need literals to push their type on the stack as well

   def visitassignmentExpression(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
      if isinstance(Node.childN2, nodes.assignmentExpression):
         assigntype = self.periodtypes.pop()
         global tempCounter
         #global counter for temp variables
         id = 'temp_var'+str(tempCounter)
         #because we need to add the two children together first so we can assign the first child to the result
         asexp = nodes.assignmentExpression(Node.childN1, Node.childN2, 0)
         initial = nodes.initializer(asexp)
         typenode = nodes.typeN(assigntype,0)
         
         prep = nodes.varDecl(typenode,False,id,0,initial)

         self.prepStmts.append(prep)
         self.prepcounter += 1
         #insert into symbol table
         self.stack[self.current].insert(id,assigntype,0)
         
         tempCounter += 1
         self.nodesStack.append(nodes.identifierExpression(id,0))
      else:
         self.nodesStack.append(Node)

      
      

  
   def visitaddAssignmentExpression(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
      global tempCounter
      #global counter for temp variables
      id = 'temp_var'+str(tempCounter)
      #because we need to add the two children together first so we can assign the first child to the result
      plusexp = nodes.plusExpression(Node.childN1, Node.childN2, 0)
      initial = nodes.initializer(plusexp)
      typenode = nodes.typeN('int',0)
      
      prep = nodes.varDecl(typenode,False,id,0,initial)

      self.prepStmts.append(prep)
      self.prepcounter += 1
      #insert into symbol table
      self.stack[self.current].insert(id,'int',0)
      
      tempCounter += 1

      #replacement = nodes.assignmentExpression(Node.childN1, nodes.identifierExpression(id,0), 0)
      #self.nodesStack.append(nodes.identifierExpression(id,0))
      #id = 'temp_var'+str(tempCounter)
      replacement = nodes.assignmentExpression(Node.childN1, nodes.identifierExpression(id,0), 0)
      
      #self.stack[self.current].insert(id,'int',0)
      #tempCounter += 1
      self.prepcounter += 1
      #insert into symbol table
      
      self.prepStmts.append(replacement)
      

      self.nodesStack.append(nodes.identifierExpression(id,0))

   
   def visitsubAssignmentExpression(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
      global tempCounter
      #global counter for temp variables
      id = 'temp_var'+str(tempCounter)
      #because we need to add the two children together first so we can assign the first child to the result
      minusexp = nodes.minusExpression(Node.childN1, Node.childN2, 0)
      initial = nodes.initializer(minusexp)
      typenode = nodes.typeN('int',0)
      
      prep = nodes.varDecl(typenode,False,id,0,initial)

      self.prepStmts.append(prep)
      self.prepcounter += 1
      #insert into symbol table
      self.stack[self.current].insert(id,'int',0)
      
      tempCounter += 1

      #id = 'temp_var'+str(tempCounter)
      replacement = nodes.assignmentExpression(Node.childN1, nodes.identifierExpression(id,0), 0)
      
      #self.stack[self.current].insert(id,'int',0)
      #tempCounter += 1
      self.prepcounter += 1
      #insert into symbol table
      
      self.prepStmts.append(replacement)
      

      self.nodesStack.append(nodes.identifierExpression(id,0))
      

  
   def visitmultAssignmentExpression(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
      global tempCounter
      #global counter for temp variables
      id = 'temp_var'+str(tempCounter)
      #because we need to add the two children together first so we can assign the first child to the result
      multexp = nodes.multExpression(Node.childN1, Node.childN2, 0)
      initial = nodes.initializer(multexp)
      typenode = nodes.typeN('int',0)
      
      prep = nodes.varDecl(typenode,False,id,0,initial)

      self.prepStmts.append(prep)
      self.prepcounter += 1
      #insert into symbol table
      self.stack[self.current].insert(id,'int',0)
      
      tempCounter += 1

      
      #id = 'temp_var'+str(tempCounter)
      replacement = nodes.assignmentExpression(Node.childN1, nodes.identifierExpression(id,0), 0)
      
      #self.stack[self.current].insert(id,'int',0)
      #tempCounter += 1
      self.prepcounter += 1
      #insert into symbol table
      
      self.prepStmts.append(replacement)
      

      self.nodesStack.append(nodes.identifierExpression(id,0))
   

   
   def visitdivAssignmentExpression(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
      global tempCounter
      #global counter for temp variables
      id = 'temp_var'+str(tempCounter)
      #because we need to add the two children together first so we can assign the first child to the result
      divexp = nodes.divExpression(Node.childN1, Node.childN2, 0)
      initial = nodes.initializer(divexp)
      typenode = nodes.typeN('int',0)
      
      prep = nodes.varDecl(typenode,False,id,0,initial)

      self.prepStmts.append(prep)
      self.prepcounter += 1
      #insert into symbol table
      self.stack[self.current].insert(id,'int',0)
      
      tempCounter += 1

      #id = 'temp_var'+str(tempCounter)
      replacement = nodes.assignmentExpression(Node.childN1, nodes.identifierExpression(id,0), 0)
      
      #self.stack[self.current].insert(id,'int',0)
      #tempCounter += 1
      self.prepcounter += 1
      #insert into symbol table
      
      self.prepStmts.append(replacement)
      

      self.nodesStack.append(nodes.identifierExpression(id,0))

   
   #do the same thing for all the other binary expressions 
   def visitplusExpression(self, Node):
      
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
      global tempCounter
      #global counter for temp variables
      id = 'temp_var'+str(tempCounter)
      #identifier that will go with the prep statement
      #temp = nodes.identifierExpression(id,0)
      #prep = nodes.assignmentExpression(temp, Node,0)
      initial = nodes.initializer(Node)
      typenode = nodes.typeN('int',0)
      #i know we are in a plus so i know it must evaluate to an integer or int type
      prep = nodes.varDecl(typenode,False,id,0,initial)

      self.prepStmts.append(prep)
      self.prepcounter += 1
      #insert into symbol table
      self.stack[self.current].insert(id,'int',0)
      #im not really going higher than 0 index
      #self.currentRecords[0].insert(id, 'int', False)
      tempCounter += 1
      self.nodesStack.append(nodes.identifierExpression(id,0))

   
   def visitminusExpression(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
      global tempCounter
      #global counter for temp variables
      id = 'temp_var'+str(tempCounter)
      
      initial = nodes.initializer(Node)
      typenode = nodes.typeN('int',0)
      
      prep = nodes.varDecl(typenode,False,id,0,initial)

      self.prepStmts.append(prep)
      self.prepcounter += 1
      #insert into symbol table
      self.stack[self.current].insert(id,'int',0)
      
      tempCounter += 1
      self.nodesStack.append(nodes.identifierExpression(id,0))
      

   
   def visitmultExpression(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
      global tempCounter
      #global counter for temp variables
      id = 'temp_var'+str(tempCounter)
      
      initial = nodes.initializer(Node)
      typenode = nodes.typeN('int',0)
      
      prep = nodes.varDecl(typenode,False,id,0,initial)

      self.prepStmts.append(prep)
      self.prepcounter += 1
      #insert into symbol table
      self.stack[self.current].insert(id,'int',0)
      
      tempCounter += 1
      self.nodesStack.append(nodes.identifierExpression(id,0))

   
   def visitdivExpression(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
      global tempCounter
      #global counter for temp variables
      id = 'temp_var'+str(tempCounter)
      
      initial = nodes.initializer(Node)
      typenode = nodes.typeN('int',0)
      
      prep = nodes.varDecl(typenode,False,id,0,initial)

      self.prepStmts.append(prep)
      self.prepcounter += 1
      #insert into symbol table
      self.stack[self.current].insert(id,'int',0)
      
      tempCounter += 1
      self.nodesStack.append(nodes.identifierExpression(id,0))

   #results to a true or false, it could have different types on its children it will result to a bool
   def visitequalityExpression(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
      global tempCounter
      #global counter for temp variables
      id = 'temp_var'+str(tempCounter)
      
      initial = nodes.initializer(Node)
      typenode = nodes.typeN('bool',0)
      
      prep = nodes.varDecl(typenode,False,id,0,initial)

      self.prepStmts.append(prep)
      self.prepcounter += 1
      #insert into symbol table
      self.stack[self.current].insert(id,'bool',0)
      
      tempCounter += 1
      self.nodesStack.append(nodes.identifierExpression(id,0))

   
   def visitnotEqualExpression(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
      global tempCounter
      #global counter for temp variables
      id = 'temp_var'+str(tempCounter)
      
      initial = nodes.initializer(Node)
      typenode = nodes.typeN('bool',0)
      
      prep = nodes.varDecl(typenode,False,id,0,initial)

      self.prepStmts.append(prep)
      self.prepcounter += 1
      #insert into symbol table
      self.stack[self.current].insert(id,'bool',0)
      
      tempCounter += 1
      self.nodesStack.append(nodes.identifierExpression(id,0))

   
   def visitlessThanExpression(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
      global tempCounter
      #global counter for temp variables
      id = 'temp_var'+str(tempCounter)
      
      initial = nodes.initializer(Node)
      typenode = nodes.typeN('bool',0)
      
      prep = nodes.varDecl(typenode,False,id,0,initial)

      self.prepStmts.append(prep)
      self.prepcounter += 1
      #insert into symbol table
      self.stack[self.current].insert(id,'bool',0)
      
      tempCounter += 1
      self.nodesStack.append(nodes.identifierExpression(id,0))

   
   def visitgreaterThanExpression(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
      global tempCounter
      #global counter for temp variables
      id = 'temp_var'+str(tempCounter)
      
      initial = nodes.initializer(Node)
      typenode = nodes.typeN('bool',0)
      
      prep = nodes.varDecl(typenode,False,id,0,initial)

      self.prepStmts.append(prep)
      self.prepcounter += 1
      #insert into symbol table
      self.stack[self.current].insert(id,'bool',0)
      
      tempCounter += 1
      self.nodesStack.append(nodes.identifierExpression(id,0))

   
   def visitLTEqualsExpression(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
      global tempCounter
      #global counter for temp variables
      id = 'temp_var'+str(tempCounter)
      
      initial = nodes.initializer(Node)
      typenode = nodes.typeN('bool',0)
      
      prep = nodes.varDecl(typenode,False,id,0,initial)

      self.prepStmts.append(prep)
      self.prepcounter += 1
      #insert into symbol table
      self.stack[self.current].insert(id,'bool',0)
      
      tempCounter += 1
      self.nodesStack.append(nodes.identifierExpression(id,0))

   
   def visitGTEqualsExpression(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
      global tempCounter
      #global counter for temp variables
      id = 'temp_var'+str(tempCounter)
      
      initial = nodes.initializer(Node)
      typenode = nodes.typeN('bool',0)
      
      prep = nodes.varDecl(typenode,False,id,0,initial)

      self.prepStmts.append(prep)
      self.prepcounter += 1
      #insert into symbol table
      self.stack[self.current].insert(id,'bool',0)
      
      tempCounter += 1
      self.nodesStack.append(nodes.identifierExpression(id,0))

   
   def visitandExpression(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
      global tempCounter
      #global counter for temp variables
      id = 'temp_var'+str(tempCounter)
      
      initial = nodes.initializer(Node)
      typenode = nodes.typeN('bool',0)
      
      prep = nodes.varDecl(typenode,False,id,0,initial)

      self.prepStmts.append(prep)
      self.prepcounter += 1
      #insert into symbol table
      self.stack[self.current].insert(id,'bool',0)
      
      tempCounter += 1
      self.nodesStack.append(nodes.identifierExpression(id,0))

   
   def visitorExpression(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
      global tempCounter
      #global counter for temp variables
      id = 'temp_var'+str(tempCounter)
      
      initial = nodes.initializer(Node)
      typenode = nodes.typeN('bool',0)
      
      prep = nodes.varDecl(typenode,False,id,0,initial)

      self.prepStmts.append(prep)
      self.prepcounter += 1
      #insert into symbol table
      self.stack[self.current].insert(id,'bool',0)
      
      tempCounter += 1
      self.nodesStack.append(nodes.identifierExpression(id,0))
      
  
   def visitnotExpression(self, Node):
      Node.childN1 = self.nodesStack.pop()
      global tempCounter
      #global counter for temp variables
      id = 'temp_var'+str(tempCounter)
      
      initial = nodes.initializer(Node)
      typenode = nodes.typeN('bool',0)
      
      prep = nodes.varDecl(typenode,False,id,0,initial)

      self.prepStmts.append(prep)
      self.prepcounter += 1
      #insert into symbol table
      self.stack[self.current].insert(id,'bool',0)
      
      tempCounter += 1
      self.nodesStack.append(nodes.identifierExpression(id,0))

   
   def visitunaryPlusExpression(self, Node):
      Node.childN1 = self.nodesStack.pop()
      global tempCounter
      #global counter for temp variables
      id = 'temp_var'+str(tempCounter)
      
      initial = nodes.initializer(Node)
      typenode = nodes.typeN('int',0)
      
      prep = nodes.varDecl(typenode,False,id,0,initial)

      self.prepStmts.append(prep)
      self.prepcounter += 1
      #insert into symbol table
      self.stack[self.current].insert(id,'int',0)
      
      tempCounter += 1
      self.nodesStack.append(nodes.identifierExpression(id,0))

   
   def visitunaryMinusExpression(self, Node):
      Node.childN1 = self.nodesStack.pop()
      global tempCounter
      #global counter for temp variables
      id = 'temp_var'+str(tempCounter)
      
      initial = nodes.initializer(Node)
      typenode = nodes.typeN('int',0)
      
      prep = nodes.varDecl(typenode,False,id,0,initial)

      self.prepStmts.append(prep)
      self.prepcounter += 1
      #insert into symbol table
      self.stack[self.current].insert(id,'int',0)
      
      tempCounter += 1
      self.nodesStack.append(nodes.identifierExpression(id,0))



#should we simplify the dot expression and functions or would it overcomplicate things later on? for now lets hold off for a bit
#dont need to do functions i think because in an earlier visitor i already made changes of a.b.c.e() -> e(a.b.c)  or even c.b.d().e -> d(c.b).e
#should probably do it to dot expressions though, to do this i need to do it before i optimize this visitor
#another issue i found is for this, we could have a.b.c which if it references enclosing data member then it would become this.a.b.c meaning we cant check if left child isinstance() but if we simplify
#it could work cause then we this.a.b.c -> temp1 = this.a -> temp2 = temp1.b -> temp3 = temp2.c -> temp4 each time we are accessing class so we can evaluate what type the temp is gonna be or wait can we??? 

#callexpression.RT holds the return type of the call id a call or this.
#this is so we create the temporary variable with the correct type 
#we are simplifying these to temp variables so i can easily do evaluations in the later stages

   def visitliteralIntExpression(self, Node):
      self.nodesStack.append(Node)

   def visitliteralCharExpression(self, Node):
      self.nodesStack.append(Node)

   def visitliteralStringExpression(self, Node):
      self.nodesStack.append(Node)

   def visittrueExpression(self, Node):
      self.nodesStack.append(Node)

   def visitfalseExpression(self, Node):
      
      self.nodesStack.append(Node)
      pass
      
   def visitidentifierExpression(self, Node):
      self.nodesStack.append(Node)
      if self.stack[self.current].checkKey(Node.value):
         #if not then skip cause this means its attached to a function call so call expression will run and push the right value on 
         typeval, lineno, isarray, modifier, isfunction, isparameter = self.stack[self.current].lookup(Node.value)
         self.periodtypes.append(typeval)
      

   def visitthisExpression(self, Node):
      #this should/can only appear within functions
      self.nodesStack.append(Node)
      self.periodtypes.append(self.stack[self.current].parent)
      pass

   
   def visitcallExpression(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
      
      #check to see that we store the correct return type and display it 
      self.periodtypes.append(Node.RT)
      global tempCounter
      #global counter for temp variables
      id = 'temp_var'+str(tempCounter)
      
      initial = nodes.initializer(Node)
      typenode = nodes.typeN(Node.RT,0)
      
      prep = nodes.varDecl(typenode,False,id,0,initial)

      self.prepStmts.append(prep)
      self.prepcounter += 1
      #insert into symbol table
      self.stack[self.current].insert(id, Node.RT,0)
      
      tempCounter += 1
      self.nodesStack.append(nodes.identifierExpression(id,0))
      pass

   
   def visitperiodExpression(self, Node):
      Node.childN1 = self.nodesStack.pop()
      clST = self.findClassST(self.periodtypes.pop())
      typeval, lineno, isarray, modifier, isfunction, isparameter = clST.lookup(Node.id)
      #now i know what type i need to store in the temp variable
      self.periodtypes.append(typeval)#incase there are more period expressions stacked
      global tempCounter
      #global counter for temp variables
      id = 'temp_var'+str(tempCounter)
      
      initial = nodes.initializer(Node)
      typenode = nodes.typeN(typeval,0)
      
      prep = nodes.varDecl(typenode,False,id,0,initial)

      self.prepStmts.append(prep)
      self.prepcounter += 1
      #insert into symbol table
      self.stack[self.current].insert(id,typeval,0)
      
      tempCounter += 1
      self.nodesStack.append(nodes.identifierExpression(id,0))

#after we do all the prepend stuff for statements we will simplify while loop by first making the very first prep child hold a label that will be the jump for the loop,
#then we make an if statement node and conditional go to... should we make if statements hold afterchildren or how do we get if statement to run the conditional go to statemetn or whatever to jump back up an loop
#have to do block statements i think for while loop

#create specific tags for everything to ensure i have unique labels, so for example temp_, while_, if_, fun_ or something and add a counter to it that increases each time 
#i am going to have to have a pointer to an object in functions and also have activation record and record of class variables offsets to 
#accuratly and correctly convert to the right asm nodes

#register stack, have to store either the instruction node on it or just the registers that the instruction is using? i would need the register no?
#maybe when we call post visit on a destructive instruction we free up the register, for example ADD, STR for variable declarations and assignments
#we know that each variable declaration will be destructive so we dont need to hold onto that register we just free it because thats the end of a statement.
#whenever we post visit an expression statement we should pop one register off/free cause we could have things like tempvar8; which would load in the the temp into a register but not do anything.
#if we decide on the second way we have to do it for each expression that doesnt get simplified





class ReturnStmtVisitor(ReConnectVisitor): #place a return statement in each function/ do i need to return the type and value or just return; by itself, does the value we return that goes on the 
   def __init__(self, globalst, classsts, functionsts):
      ReConnectVisitor.__init__(self, globalst, classsts, functionsts)
      self.funRT = ''
   #place as the last statement in main constructor and methods 
   #can probably assume that there wont be a constructor 
   def pre_visitCompUnit(self, node):
      self.stack.append(self.findFunctionST(node.id, 'global'))
      self.current += 1
      
   def visitCompUnit(self, node):
      #pop the scope off
      self.stack.pop()
      self.current -= 1
      #have to reverse sort afterwards
      numChildren = len(node.children)
      node.children = []
      for child in range(numChildren):
         node.children.insert(0,self.nodesStack.pop())
      #node.children.sort(reverse=True)      

      #go to methodbody
      node.children[-1].children.append(nodes.returnStatement(None, 0))
      
   def visitMethodSuf(self, node):
      if node.childN1 is None:
         node.childN2 = self.nodesStack.pop()
      else:
         node.childN2 = self.nodesStack.pop()
         node.childN1 = self.nodesStack.pop()
      self.nodesStack.append(node)

      if self.funRT == 'void':
         node.childN2.children.append(nodes.returnStatement(None, 0))
      elif self.funRT == 'int':
         node.childN2.children.append(nodes.returnStatement(nodes.literalIntExpression('0', 0), 0))
      elif self.funRT == 'char':
         node.childN2.children.append(nodes.returnStatement(nodes.literalCharExpression('', 0), 0))
      elif self.funRT == 'bool':
         node.childN2.children.append(nodes.returnStatement(nodes.falseExpression('0', 0), 0))
      elif self.funRT == 'string':
         node.childN2.children.append(nodes.returnStatement(nodes.literalStringExpression('', 0), 0))

   def pre_visitMethodDecl(self, node):
      typeval, lineno, isarray, modifier, isfunction, isparameter = self.stack[self.current].lookup(node.id)
      self.funRT = typeval
      self.stack.append(self.findFunctionST(node.id, self.stack[self.current].name))
      self.current += 1
      
   def visitMethodDecl(self, node):
      #pop the scope off
      self.stack.pop()
      self.current -= 1

      node.childN3 = self.nodesStack.pop()
      node.childN2 = self.nodesStack.pop()
      node.childN1 = self.nodesStack.pop()
      self.nodesStack.append(node)
      
   def pre_visitConstructorDecl(self, node):
      #typeval, lineno, isarray, modifier, isfunction, isparameter = self.stack[self.current].lookup(node.id)
      #self.funRT = typeval
      #since constructor cant be called without new then we can assume there is no constructor

      self.stack.append(self.findFunctionST(node.id, self.stack[self.current].name))
      self.current += 1
      
   def visitConstructorDecl(self, node):
      #pop the scope off
      self.stack.pop()
      self.current -= 1
      node.childN2 = self.nodesStack.pop()
      self.nodesStack.append(node)
#stack assembler need to have the stack pointer point to it just have stack pointer point to where its supposed to be??
#outside of this if the return statement has none for its expression then just jump back to return address and dont allocate anything, becuase we already checked to make sure the any return statements user inputs has a return value if the function has a valid return type
   
   pass #i think we do need a return statement and return address for main


class SimpleBreaksVisitor(ReConnectVisitor):#maybe split up into two visitors
   def __init__(self, globalst, classsts, functionsts):
      ReConnectVisitor.__init__(self, globalst, classsts, functionsts)
      self.prevexitlabs = []
      self.currentexit = ''

   def pre_visitswitchStatement(self, Node):
      global switchCounter
      self.prevexitlabs.append(self.currentexit)
      self.currentexit = ''
      self.currentexit = 'switch_exit' + str(switchCounter)
      switchCounter += 1

   def visitswitchStatement(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
      numChildren = len(Node.prepChildren)
      Node.prepChildren = []
      for child in range(numChildren):
         Node.prepChildren.insert(0,self.nodesStack.pop())
      
      tempnode = nodes.BlockStatement([Node, nodes.ADInode('ADI R3, #0', self.currentexit)])
      self.nodesStack.append(tempnode)
      self.currentexit = self.prevexitlabs.pop()
      
   def pre_visitwhileStatement(self, Node):
      
      global whileCounter
      self.prevexitlabs.append(self.currentexit)
      self.currentexit = ''
      self.currentexit = 'while_exit' + str(whileCounter)
      whileCounter += 1

   def visitwhileStatement(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
      numChildren = len(Node.prepChildren)
      Node.prepChildren = []
      for child in range(numChildren):
         Node.prepChildren.insert(0,self.nodesStack.pop())
      
      tempnode = nodes.BlockStatement([Node, nodes.ADInode('ADI R3, #0', self.currentexit)])
      self.nodesStack.append(tempnode)
      self.currentexit = self.prevexitlabs.pop()

   def visitbreakStatement(self, Node):
      #change break to a jump to the exit label
      jmpnode = nodes.JMPnode('JMP ' + self.currentexit)
      self.nodesStack.append(jmpnode)
   

#have to create labels for static values like ints, chars, strings, to end a string we need to put a \0 at the end 
class WhileVisitor(ReConnectVisitor):
   def __init__(self, globalst, classsts, functionsts):
      ReConnectVisitor.__init__(self, globalst, classsts, functionsts)

      

   #i could do this after expressions are converted to asm nodes. that way i know for sure that the expression could contain a label 
   # that i just attach to if i have no perpChildren cause (expression) could just be (true)
   #previous frame pointer helps us know where to set our FP when we return, that way know that we are pointing to the right place on the stack 
   #we can just 
   # have to do switch before complex expressions
   def visitwhileStatement(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
      numChildren = len(Node.prepChildren)
      Node.prepChildren = []
      for child in range(numChildren):
         Node.prepChildren.insert(0,self.nodesStack.pop())

      global whileCounter
      looplabel = 'while_loop'+str(whileCounter)
      whileCounter += 1
      ifnode = nodes.ifStatement(Node.childN1, Node.childN2, None, 0)
      ifnode.prepChildren = Node.prepChildren
      ifnode.whloop = True
      ifnode.whlabel = looplabel
      tempnode = nodes.BlockStatement([nodes.ADInode('ADI R3, #0', looplabel), ifnode])
      self.nodesStack.append(tempnode)
      
      

   #ali said he turned his var decl eventually to just assignments like 
   #call this after simplification of expressions so we can just put the simplified expression in the conditionals of the if statements of cases
class SwCasesVisitor(ReConnectVisitor):#maybe split up into two visitors
   #switch has the expression which goes to to a couple of children so i need to see what i can do.
   #when i previsit the switch i can put the previous expression on a stack and push the vurrent one. then for each case i encounter i create an if statement and have its expression be the case value == self.switchcurrentexpression
   #have to hold an expression to compare for each of the conditionals for the new ifs for each case
   #need to keep track of switch
   #have to keep switch parent but just change cases to if statements

   def __init__(self, globalst, classsts, functionsts):
      ReConnectVisitor.__init__(self, globalst, classsts, functionsts)
      self.currentexpr = None
      self.prevexprs = []

   def pre_visitswitchStatement(self, Node):
      self.prevexprs.append(self.currentexpr)
      self.currentexpr = Node.childN1

   def visitswitchStatement(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
      numChildren = len(Node.prepChildren)
      Node.prepChildren = []
      for child in range(numChildren):
         Node.prepChildren.insert(0,self.nodesStack.pop())
      self.nodesStack.append(Node)

      self.currentexpr = self.prevexprs.pop()

   def visitCaseBlock(self, node):
      numChildren = len(node.defaultStmtChildren)
      node.defaultStmtChildren = []
      for child in range(numChildren):
         node.defaultStmtChildren.insert(0,self.nodesStack.pop())
      #node.defaultStmtChildren.sort(reverse=True)

      numChildren = len(node.caseChildren)
      node.caseChildren = []
      for child in range(numChildren):
         node.caseChildren.insert(0,self.nodesStack.pop())
      #node.caseChildren.sort(reverse=True)
      self.nodesStack.append(node)
      
   
   def visitCase(self, node):
      numChildren = len(node.statementChildren)
      node.statementChildren = []
      for child in range(numChildren):
         node.statementChildren.insert(0,self.nodesStack.pop())
      #node.statementChildren.sort(reverse=True)

      global tempCounter
      #global counter for temp variables
      id = 'temp_var'+str(tempCounter)
      #because we need to add the two children together first so we can assign the first child to the result
      
      if node.valType == 'char':
         tempcond = nodes.equalityExpression(nodes.literalCharExpression(node.value, 0), self.currentexpr, 0)
         typenode = nodes.typeN('char',0)
      else:
         #the only thing left is an int case 
         tempcond = nodes.equalityExpression(nodes.literalIntExpression(node.value, 0), self.currentexpr, 0)
         typenode = nodes.typeN('int',0)

      

      
      initial = nodes.initializer(tempcond)
      typenode = nodes.typeN('bool',0)
      prep = nodes.varDecl(typenode,False,id,0,initial)

      casestmts = nodes.BlockStatement(node.statementChildren)

      ifstmt = nodes.ifStatement(nodes.identifierExpression(id,0), casestmts, None,0)
      ifstmt.prepChildren.append(prep)
      
      
      #insert into symbol table
      #have to transfer children as a block statement
      self.stack[self.current].insert(id,'bool',0)
      
      tempCounter += 1

      self.nodesStack.append(ifstmt)


   


#he said he passed id on reg stack and my parents pop and set the right registers
class boolVisitor(ReConnectVisitor):#bool convert to just int of 4 bytes and change to be 1 or 0
   def __init__(self, globalst, classsts, functionsts):
      ReConnectVisitor.__init__(self, globalst, classsts, functionsts)

   def visitreturnStatement(self, Node):
      if Node.childN1 is None:
         pass
         
      else:
         Node.childN1 = self.nodesStack.pop()
         

      numChildren = len(Node.prepChildren)
      Node.prepChildren = []
      for child in range(numChildren):
         Node.prepChildren.insert(0,self.nodesStack.pop())

      self.nodesStack.append(Node)

   def visittrueExpression(self, Node):

      self.nodesStack.append(nodes.literalIntExpression('1',0))

   def visitfalseExpression(self, Node):
      self.nodesStack.append(nodes.literalIntExpression('0',0))

#get rid of var decl without an intializer and change ones with initializer to assingment nodes
   def visitVarDecl(self, node):

      if node.initializer is None:
         #have to get rid of it but my parent is expecting something. maybe just return something that does nothing when its accepted
         node.childN1 = self.nodesStack.pop()
         self.nodesStack.append(nodes.nullExpression('null',0))
      else:
         node.initializer = self.nodesStack.pop()
         node.childN1 = self.nodesStack.pop()
         self.nodesStack.append(nodes.assignmentExpression(nodes.identifierExpression(node.id, 0), node.initializer.childN1,0))
      

   #he said we can just get rid of all var declarations with no intializer and turn the the ones that do have one into just assignments nodes. since our activation record will default initailize everything

#have to create labels for static values like ints, chars, strings, to end a string we need to put a \0 at the end 
#i can create a global dictionary or table that contains all the label names and the values stored and if its a char or int or whatever. once we create this object we can just reference it whenever we dealing with literals
# we can give it function that when provided with a literal value it should look through its data and match the value return the label, need to make sure that each string has \0 at the end of it, could
#do it at the beginning but it might be better to do it at the end so i can easily match literals without needing to take off the \0
#true false labels can just be integer 1 and 0 
#we will need our own label for charnull which is .byt '\0' for string outputing

#before this i need to switch/ change true false to 0s and 1s
#mayb
class literalLabelsVisitor(Visitor): 
   def __init__(self):
      self.litlabels = LiteralLabels()

   #def visitCompUnit(self, node):
   #   self.litlabels.insert('char', '\0')
      global litLabelCounter

   def visitliteralIntExpression(self, Node):
      global litLabelCounter
      self.litlabels.insert('int',str(Node.value), litLabelCounter)
      litLabelCounter += 1
      pass

   def visitliteralCharExpression(self, Node):
      global litLabelCounter
      self.litlabels.insert('char', Node.value, litLabelCounter)
      litLabelCounter += 1

   def visitliteralStringExpression(self, Node):
      global litLabelCounter
      self.litlabels.insert('string',Node.value, litLabelCounter)
      litLabelCounter += 1



#get in parent and i need to create a block statement
#there after for each asm node i need to put the register that it will place its value in
#then after if i ever need those values i just make it so asm nodes either place their reg variable on the stack or place their whole asm node, then when i pop i just check if isinstance of asm node if so check the reg value
#int bool char string assign to assingment
#when i reach var decl or assignmnet just look up left id in the symbol table so we know what instruction to call on the right side if its not a int for register number
class CompExprsVisitor(ReConnectVisitor):#turn expressions to asm code
   def __init__(self, globalst, classsts, functionsts, litlabe):
      ReConnectVisitor.__init__(self, globalst, classsts, functionsts)
      #he said put it on stack then pop them off into registers??

      self.registers = []
      self.regstack = []
      #they said only ids but why? 
      self.funActiveRecords = []
      self.classActiveRecs = []
      self.currentfunRecord = None #we dont have to keep a stack i think 
      self.funcallrec = None
      self.parCounter = 0
      self.paramoffs = []
      self.littable = litlabe
      self.valueflag = False
      self.yourRegister = 0
      self.kidtypes = []
      #should we keep a counter to know where we are in the records?

      #populate actvation records with current symbols
      #when we find this in funactiverecord we need to address the class active record by just using the funactiverecord.parent to find the classactive record and using that to see what data member i accessed and where its located from the pointer

      for funST in self.functionSTS:
         actRec = ActivationRecord(funST.name, funST.parent)
         #default set this as the first parameter for functions that arent main
         if funST.name != 'main':
            actRec.insert('this', '', True)
         for id in funST.data:
            typeval, lineno, isarray, modifier, isfunction, isparameter = funST.lookup(id)       
            if isparameter:  
               actRec.insert(id, typeval, isparameter)
         #to have order set 
         for id in funST.data:
            typeval, lineno, isarray, modifier, isfunction, isparameter = funST.lookup(id)   
            if not isparameter:      
               actRec.insert(id, typeval, isparameter)
         self.funActiveRecords.append(actRec)

      #populate class active record
      for clST in self.classSTS:
         actRec = ActivationRecord(clST.name, clST.parent, 0)#because we allocate off heap
         for id in clST.data:
            typeval, lineno, isarray, modifier, isfunction, isparameter = clST.lookup(id)         
            actRec.insert(id, typeval, isparameter)
         self.classActiveRecs.append(actRec)

   def findFunctionActRec(self, name, parentN):
      for st in self.funActiveRecords:
         if st.name == name and st.parent == parentN:
            return st
   def findclassActRec(self, name):
      for st in self.classActiveRecs:
         if st.name == name:
            return st
#the only times we would need to check for specific register is assignment and var decl cause the right side could just be an id or an evaluation of bool int or whatever 
   def pre_visitCompUnit(self, node):
      self.stack.append(self.findFunctionST(node.id, 'global'))
      self.currentfunRecord = self.findFunctionActRec(node.id, 'global')
      self.current += 1
      
   def visitCompUnit(self, node):
      #pop the scope off
      self.stack.pop()
      self.current -= 1
      #have to reverse sort afterwards
      numChildren = len(node.children)
      node.children = []
      for child in range(numChildren):
         node.children.insert(0,self.nodesStack.pop())
      #node.children.sort(reverse=True)

      
   def pre_visitClassDef(self, node):
      self.stack.append(self.findClassST(node.id))
      self.current += 1
      self.currentfunRecord = self.findclassActRec(node.id)

   def visitClassDef(self, node):
      #pop the scope off
      self.stack.pop()
      self.current -= 1

      numChildren = len(node.methodChildren)
      node.methodChildren = []
      for child in range(numChildren):
         node.methodChildren.insert(0,self.nodesStack.pop())
      #node.methodChildren.sort(reverse=True)

      numChildren = len(node.dataChildren)
      node.dataChildren = []
      for child in range(numChildren):
         node.dataChildren.insert(0,self.nodesStack.pop())
      #node.dataChildren.sort(reverse=True)
      self.nodesStack.append(node)
      
   def visitMethodSuf(self, node):
      if node.childN1 is None:
         node.childN2 = self.nodesStack.pop()
      else:
         node.childN2 = self.nodesStack.pop()
         node.childN1 = self.nodesStack.pop()
      self.nodesStack.append(node)
      
   
   def visitMethodBody(self, node):
      #have to reverse sort afterwards
      numChildren = len(node.children)
      node.children = []
      for child in range(numChildren):
         node.children.insert(0,self.nodesStack.pop())
      #node.children.sort(reverse=True)
      self.nodesStack.append(node)


   def pre_visitDataMemDecl(self, node):
      pass
   def visitDataMemDecl(self, node):
      #need to go in reverse be cuase the first pop will be the child N2
      node.child2 = self.nodesStack.pop()
      node.child1 = self.nodesStack.pop()
      numChildren = len(node.prepChildren)
      node.prepChildren = []
      for child in range(numChildren):
         node.prepChildren.insert(0,self.nodesStack.pop())
      self.nodesStack.append(node)
      

      
   def pre_visitMethodDecl(self, node):
      self.stack.append(self.findFunctionST(node.id, self.stack[self.current].name))
      self.currentfunRecord = self.findFunctionActRec(node.id, self.stack[self.current].name)
      self.current += 1
      
   def visitMethodDecl(self, node):
      #pop the scope off
      self.stack.pop()
      self.current -= 1

      node.childN3 = self.nodesStack.pop()
      node.childN2 = self.nodesStack.pop()
      node.childN1 = self.nodesStack.pop()
      self.nodesStack.append(node)
   #def pre_visitParameterList(self, node):
      
   

   def pre_visitConstructorDecl(self, node):
      self.stack.append(self.findFunctionST(node.id, self.stack[self.current].name))
      self.currentfunRecord = self.findFunctionActRec(node.id, self.stack[self.current].name)
      self.current += 1
      
   def visitConstructorDecl(self, node):
      #pop the scope off
      self.stack.pop()
      self.current -= 1
      node.childN2 = self.nodesStack.pop()
      self.nodesStack.append(node)
   
      
      
   
   def visitVarDecl(self, node):
      if node.initializer is None:
         node.childN1 = self.nodesStack.pop()
      else:
         node.initializer = self.nodesStack.pop()
         node.childN1 = self.nodesStack.pop()
      self.nodesStack.append(node)
      
   
   def visitcurlyBrackStatement(self, Node):
      #have to reverse sort afterwards
      numChildren = len(Node.children)
      Node.children = []
      for child in range(numChildren):
         Node.children.insert(0,self.nodesStack.pop())

      numChildren = len(Node.prepChildren)
      Node.prepChildren = []
      for child in range(numChildren):
         Node.prepChildren.insert(0,self.nodesStack.pop())
      #Node.children.sort(reverse=True)
      self.nodesStack.append(Node)
      
   

   def visitexpressionStatement(self, Node):
      Node.childN1 = self.nodesStack.pop()
      numChildren = len(Node.prepChildren)
      Node.prepChildren = []
      for child in range(numChildren):
         Node.prepChildren.insert(0,self.nodesStack.pop())
      self.nodesStack.append(Node)
      

   
   def pre_visitifStatement(self, Node):
      self.valueflag = True
      self.yourRegister = 1
      Node.childN1.accept(self)
      Node.childN1 = self.nodesStack.pop()

      



   def visitifStatement(self, Node):
      if Node.childN3 is None:
         Node.childN2 = self.nodesStack.pop()
         Node.childN1 = self.nodesStack.pop()
         
      else:
         Node.childN3 = self.nodesStack.pop()
         Node.childN2 = self.nodesStack.pop()
         Node.childN1 = self.nodesStack.pop()

      numChildren = len(Node.prepChildren)
      Node.prepChildren = []
      for child in range(numChildren):
         Node.prepChildren.insert(0,self.nodesStack.pop())


      #Node.childN1.accept(self)
      #have to take it off the nodes stack
      #self.nodesStack.pop()
      
      #Regchild1 = self.regstack.pop()
      #typeval1, offset1, isparam1 = self.currentfunRecord.lookup(Regchild1)
      #has to be a bool for ifs conditional expression
      #just do Node.childN1 instead
      #blockstmt = nodes.BlockStatement([nodes.MOVnode('MOV R1, FP', '', 0), nodes.ADInode('ADI R1, #-'+str(offset1), '', 0), 
      #                                  nodes.LDRLnode('LDR R1, R1', '', 0)])
      #self.regstack.append(1)
      


      global ifCounter
      iflabel = 'if_label'+str(ifCounter)
      ifCounter += 1

      if Node.whloop:
         #have to manually go through the bgt or whatever asm node and reset its register but not its label, how??
         #could add another variable to asm nodes called jump labels in case it needs to jump to a label
         #true is one and false is 0
         #how do i check what the expression will be? well if its true its just a true expression which is 1 if zero branch
         #i dont have the register for brznode to check.... maybe have it so all the asm nodes that weve already made will continue to allocate and pop off the stack
         #this will help me so i can create other asm nodes since all i need to do is pop off the stack
         tempnode = nodes.BlockStatement([Node.prepChildren, Node.childN1, nodes.BRZnode('BRZ R1, ' + iflabel), Node.childN2, nodes.JMPnode('JMP '+ Node.whlabel), nodes.ADInode('ADI R3, #0', iflabel)])

      elif Node.childN3 is None:
         tempnode = nodes.BlockStatement([Node.prepChildren, Node.childN1, nodes.BRZnode('BRZ R1, ' + iflabel), Node.childN2, nodes.ADInode('ADI R3, #0', iflabel)])
      else:
       #it contains an else statement so it wasnt a while or switch statement.
       #  if expression fails go to the else statement if its true need to have another instruction that jumps once done so we dont run the else statement
         exitlabel = 'if_exitlabel'+str(ifCounter)
         ifCounter += 1
         tempnode = nodes.BlockStatement([Node.prepChildren, Node.childN1, nodes.BRZnode('BRZ R1, ' + iflabel), Node.childN2, nodes.JMPnode('JMP '+ exitlabel), nodes.ADInode('ADI R3, #0', iflabel),Node.childN3, nodes.ADInode('ADI R3, #0', exitlabel)])


      #have to find a way to make registers in a stack work and be updated constantly as go through visitors so in case i add a new asm node i 
      # can pop off the stack to see which register i need or which register is free

      self.nodesStack.append(tempnode)

   
   def visitwhileStatement(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
      numChildren = len(Node.prepChildren)
      Node.prepChildren = []
      for child in range(numChildren):
         Node.prepChildren.insert(0,self.nodesStack.pop())
      self.nodesStack.append(Node)
      





   def pre_visitreturnStatement(self, Node):
      self.valueflag = True
      self.yourRegister = 1

   def visitreturnStatement(self, Node):#value will be placed where fp was originally
      #make pfp equal to current fp then change fp to point to sp
      #other way around 

      if Node.childN1 is None:
         #convert to blockstatement with just returnign from function assume all registers are open to us
         #self.nodesStack.append(Node)
         pass
         
      else:
         #convert to blockstatement with just returnign from function assume all registers are open to us
         Node.childN1 = self.nodesStack.pop()
      


      #make sure that we place the prepchildren first in the block statement
      numChildren = len(Node.prepChildren)
      Node.prepChildren = []
      for child in range(numChildren):
         Node.prepChildren.insert(0,self.nodesStack.pop())



      if Node.childN1 is None:
         #convert to blockstatement with just returnign from function assume all registers are open to us
         #self.nodesStack.append(Node)
         #mov fp into a register adi immediate -4 pfp, then move fp into sp, ldr for pfp then mov into fp then 
         blockstmt = nodes.BlockStatement([Node.prepChildren,nodes.MOVnode('MOV R4, FP', '', 4), nodes.ADInode('ADI R4, #-4', '', 4), nodes.MOVnode('MOV SP, FP', '', 4),
                                             nodes.LDRLnode('LDR FP, R4', '', 4), 
                                             nodes.LDRLnode('LDR R5, SP'), nodes.JMRnode('JMR R5','',4)])
         
      else:
         #convert to blockstatement with just returnign from function assume all registers are open to us

         chtype = self.kidtypes.pop()

   
         if chtype == 'char':
#remember prep children then expression we return then jump back 
            blockstmt = nodes.BlockStatement([Node.prepChildren, Node.childN1 ,nodes.MOVnode('MOV R4, FP', '', 4), nodes.ADInode('ADI R4, #-4', '', 4), nodes.MOVnode('MOV SP, FP', '', 4),
                                                nodes.LDRLnode('LDR FP, R4', '', 4), #load return address first before placing return expression
                                                nodes.LDRLnode('LDR R5, SP'), nodes.STBRnode('STB R1, SP'), nodes.JMRnode('JMR R5','',4)])
         else: #should just be four bytes
         
            blockstmt = nodes.BlockStatement([Node.prepChildren,Node.childN1,nodes.MOVnode('MOV R4, FP', '', 4), nodes.ADInode('ADI R4, #-4', '', 4), nodes.MOVnode('MOV SP, FP', '', 4),
                                                   nodes.LDRLnode('LDR FP, R4', '', 4), #load return address first before placing return expression
                                                   nodes.LDRLnode('LDR R5, SP'), nodes.STRRnode('STR R1, SP'), nodes.JMRnode('JMR R5','',4)])
         
         
         #Node.childN1 = self.nodesStack.pop()
         #self.nodesStack.append(Node)


      
      self.regstack.append(1)
      self.nodesStack.append(blockstmt)
      self.yourRegister = 0
      self.valueflag = False
      #dont need to put back on kidtypes cause function call will load the correct value 
      

   def pre_visitcoutStatement(self, Node):
      self.yourRegister = 1
      self.valueflag = True

   def visitcoutStatement(self, Node):
      Node.childN1 = self.nodesStack.pop()
      numChildren = len(Node.prepChildren)
      Node.prepChildren = []
      for child in range(numChildren):
         Node.prepChildren.insert(0,self.nodesStack.pop())


      chtype = self.kidtypes.pop()


   #if string have to do some weird thing to print it out-- remember we will insert a \0 at then end of the string 
      if chtype == 'char':
#remember prep children then expression we return then jump back 
         blockstmt = nodes.BlockStatement([Node.prepChildren, Node.childN1, nodes.MOVnode('MOV R3, R1','',0), nodes.TRPTHREEnode('TRP #3','',3)])
      elif chtype == 'string':
         #need to set up a loop 
         global stringCounter
         strloop = 'output_string'+str(stringCounter)
         extloop = 'exit_string'+str(stringCounter)
         stringCounter += 1

         blockstmt = nodes.BlockStatement([Node.prepChildren, Node.childN1, nodes.LDBRnode('LDB R3, R1', strloop),nodes.LDBRnode('LDB R2, NULLTERM'), nodes.CMPnode('CMP R2, R3'),
                                          nodes.BRZnode('BRZ R2, '+extloop),  nodes.TRPTHREEnode('TRP #3','',3), nodes.ADInode('ADI R1, #1'), nodes.JMPnode('JMP '+strloop), nodes.ADInode('ADI R3, #0', extloop, 3)])

      else:
         blockstmt = nodes.BlockStatement([Node.prepChildren, Node.childN1, nodes.MOVnode('MOV R3, R1','',0), nodes.TRPTHREEnode('TRP #1','',3)])
         

      self.regstack.append(3)
      self.nodesStack.append(blockstmt)
      self.yourRegister = 0
      self.valueflag = False
      

   def pre_visitcinStatement(self, Node):
      self.yourRegister = 1
      self.valueflag = False

   def visitcinStatement(self, Node):
      Node.childN1 = self.nodesStack.pop()
      numChildren = len(Node.prepChildren)
      Node.prepChildren = []
      for child in range(numChildren):
         Node.prepChildren.insert(0,self.nodesStack.pop())

      #Regchild1 = self.regstack.pop()
      #typeval1, offset1, isparam1 = self.currentfunRecord.lookup(Regchild1)
      chtype = self.kidtypes.pop()
   #if string have to do some weird thing to print it out-- remember we will insert a \0 at then end of the string 
      if chtype == 'char':
#remember prep children then expression we return then jump back 
         blockstmt = nodes.BlockStatement([Node.prepChildren, nodes.TRPFOURnode('TRP #4','',3), Node.childN1, 
                                          nodes.STBRnode('STB R3, R1', '', 0), ])
      else:
         blockstmt = nodes.BlockStatement([Node.prepChildren, nodes.TRPTWOnode('TRP #2','',3), Node.childN1, 
                                          nodes.STRRnode('STR R3, R1', '', 0), ])
         

      self.regstack.append(3)
      self.nodesStack.append(blockstmt)
      self.yourRegister = 0 
      self.valueflag = False


  
   def visitswitchStatement(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
      numChildren = len(Node.prepChildren)
      Node.prepChildren = []
      for child in range(numChildren):
         Node.prepChildren.insert(0,self.nodesStack.pop())
      self.nodesStack.append(Node)
      

   def visitbreakStatement(self, Node):
      self.nodesStack.append(Node)
      

   
   def visitvarDeclStatement(self, Node):
      Node.childN1 = self.nodesStack.pop()
      numChildren = len(Node.prepChildren)
      Node.prepChildren = []
      for child in range(numChildren):
         Node.prepChildren.insert(0,self.nodesStack.pop())
      self.nodesStack.append(Node)
      

#end of statements
   
   def visitCaseBlock(self, node):
      numChildren = len(node.defaultStmtChildren)
      node.defaultStmtChildren = []
      for child in range(numChildren):
         node.defaultStmtChildren.insert(0,self.nodesStack.pop())
      #node.defaultStmtChildren.sort(reverse=True)

      numChildren = len(node.caseChildren)
      node.caseChildren = []
      for child in range(numChildren):
         node.caseChildren.insert(0,self.nodesStack.pop())
      #node.caseChildren.sort(reverse=True)
      self.nodesStack.append(node)
      
   
   def visitCase(self, node):
      numChildren = len(node.statementChildren)
      node.statementChildren = []
      for child in range(numChildren):
         node.statementChildren.insert(0,self.nodesStack.pop())
      #node.statementChildren.sort(reverse=True)
      self.nodesStack.append(node)
      


#    def visitExpression(node):
   def pre_visitassignmentExpression(self, Node):
      self.valueflag = False
      self.yourRegister = 0
      if isinstance(Node.childN2, nodes.identifierExpression):
         Node.rNeedLoad = True
  
   def visitassignmentExpression(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
      #Regchild2 = self.regstack.pop()
      #Regchild1 = self.regstack.pop()
      chtype = self.kidtypes.pop()
      #print(Regchild2, Regchild1)
      #print(Node.childN2, Node.childN1)
      if Node.rNeedLoad == True:#is load
         
         if chtype == 'char':
            blockstmt = nodes.BlockStatement([Node.childN2,nodes.LDBRnode('LDB R1, R1', '', 1), Node.childN1,
                                          nodes.STBRnode('STB R1, R0','',1)])
         else:
            blockstmt = nodes.BlockStatement([Node.childN2,nodes.LDBRnode('LDR R1, R1', '', 1), Node.childN1,
                                          nodes.STRRnode('STR R1, R0','',1)])
      else:
         
         if chtype == 'char':
            blockstmt = nodes.BlockStatement([Node.childN2, Node.childN1,
                                          nodes.STBRnode('STB R1, R0','',1)])
         else:
            blockstmt = nodes.BlockStatement([Node.childN2, Node.childN1,
                                          nodes.STRRnode('STR R1, R0','',1)])
            
         
#i have to make sure that i keep my children  incase the right side was a operation that turned into a block statement
      
      self.regstack.append(1)
      self.nodesStack.append(blockstmt)
      self.kidtypes.append(chtype)
      self.yourRegister = 0
      self.valueflag = False

  
   
   def pre_visitplusExpression(self, Node):
      self.yourRegister = 0
      self.valueflag = True
   
   def visitplusExpression(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
      
      #we know it has to be an int
      #did they also transform their literals to temps?
      #maybe just transform int literals to be temps then i know i just have to do
      #offsets
      #with assign i can just check the id of the left child and get its valtype from table to see how i should treat the right side
      #offset for regchild1 move fp to reg 0 then ADI r0 #-offset LDR r0 r0
      #assignment still needs right child because it could be a block statement of instructions
      #for assignment i think the register we should return is the register that had the value that way in case there is another assignment it just does the same thing with that value 
      blockstmt = nodes.BlockStatement([Node.childN1,Node.childN2, nodes.ADDnode('ADD R1, R0', '', 1) ])
      self.regstack.append(1)
      self.nodesStack.append(blockstmt)
      self.yourRegister = 0
      self.valueflag = False
      #IN THE NEXT VISITORS I HAVE TO ALSO MAKE ASM NODES APPEND THEIR REG VARIABLE ON THE REG STACK IN CASE I NEED IT LATER FOR OTHER SIMPLIFICATIONS

   def pre_visitminusExpression(self, Node):
      self.yourRegister = 0
      self.valueflag = True
   
   def visitminusExpression(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
   
      
      blockstmt = nodes.BlockStatement([Node.childN1,Node.childN2, nodes.SUBnode('SUB R0, R1', '', 1), nodes.MOVnode('MOV R1, R0', '', 1) ])

      self.regstack.append(1)
      self.nodesStack.append(blockstmt)
      self.yourRegister = 0
      self.valueflag = False
      pass

   def pre_visitmultExpression(self, Node):
      self.yourRegister = 0
      self.valueflag = True

   def visitmultExpression(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
      
      
      blockstmt = nodes.BlockStatement([Node.childN1,Node.childN2, nodes.MULnode('MUL R1, R0', '', 1) ])
      self.regstack.append(1)
      self.nodesStack.append(blockstmt)
      self.yourRegister = 0
      self.valueflag = False

   def pre_visitdivExpression(self, Node):
      self.yourRegister = 0
      self.valueflag = True

   def visitdivExpression(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()

      
      blockstmt = nodes.BlockStatement([Node.childN1,Node.childN2, nodes.DIVnode('DIV R0, R1', '', 1), nodes.MOVnode('MOV R1, R0', '', 1) ])
      self.regstack.append(1)
      self.nodesStack.append(blockstmt)
      self.yourRegister = 0
      self.valueflag = False


   def pre_visitequalityExpression(self, Node):
      self.yourRegister = 0
      self.valueflag = True

   def visitequalityExpression(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()

      chtype = self.kidtypes.pop()
      global compareCounter
      jmplabel = 'false_label'+str(compareCounter)
      compareCounter += 1
      extlabel = 'trueexit_label'+str(compareCounter)
      compareCounter += 1

      #print(Regchild2, Regchild1)
      #print(Node.childN2, Node.childN1)
      

      if chtype == 'char':
         blockstmt = nodes.BlockStatement([Node.childN1, Node.childN2, nodes.CMPnode('CMP R0, R1', '', 1), 
                                           nodes.BNZnode('BNZ R0, '+jmplabel, '', 1), nodes.LDRLnode('LDR R1, ONE'),
                                           nodes.JMPnode('JMP '+extlabel,'',1),nodes.LDRLnode('LDR R1, ZERO', jmplabel,1), nodes.ADInode('ADI R3, #0',extlabel,1)])

      #1 and 0 should already have a label
      #wait we need to start our labels with letters----> insert lab at the beginning of each one for example lablit1
      else:#int or string but string is just a pointer so we just compare pointers 

         blockstmt = nodes.BlockStatement([Node.childN1,Node.childN2, nodes.CMPnode('CMP R0, R1', '', 1), 
                                           nodes.BNZnode('BNZ R0, '+jmplabel, '', 1), nodes.LDRLnode('LDR R1, ONE'),
                                           nodes.JMPnode('JMP '+extlabel,'',1),nodes.LDRLnode('LDR R1, ZERO', jmplabel,1), nodes.ADInode('ADI R3, #0',extlabel,1)])
      self.regstack.append(1)
      self.nodesStack.append(blockstmt)
      self.yourRegister = 0
      self.valueflag = False
      self.kidtypes.append(chtype)

      

   def pre_visitnotEqualExpression(self, Node):
      self.yourRegister = 0
      self.valueflag = True

   def visitnotEqualExpression(self, Node):
      #when we enter we know we only operate on two variables nothing more because all other expressions go somewhere else
      #for assignment check if the right side goes to an assignment expression node if so reduce to temp
      #identifier just pushes itself 
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()

      chtype = self.kidtypes.pop()  
      global compareCounter
      jmplabel = 'false_label'+str(compareCounter)
      compareCounter += 1
      extlabel = 'trueexit_label'+str(compareCounter)
      compareCounter += 1
#for equality comparison we just have to check for char if so ldb but we also need to check for id as well but if its literal dont do anything 


      if chtype == 'char':
         blockstmt = nodes.BlockStatement([Node.childN1, Node.childN2, nodes.CMPnode('CMP R0, R1', '', 1), 
                                           nodes.BRZnode('BRZ R0, '+jmplabel, '', 1), nodes.LDRLnode('LDR R1, ONE'),
                                           nodes.JMPnode('JMP '+extlabel,'',1),nodes.LDRLnode('LDR R1, ZERO', jmplabel,1), nodes.ADInode('ADI R3, #0',extlabel,1)])

      #1 and 0 should already have a label
      #wait we need to start our labels with letters----> insert lab at the beginning of each one for example lablit1
      else:#int or string but string is just a pointer so we just compare pointers 

         blockstmt = nodes.BlockStatement([Node.childN1, Node.childN2, nodes.CMPnode('CMP R0, R1', '', 1), 
                                           nodes.BRZnode('BRZ R0, '+jmplabel, '', 1), nodes.LDRLnode('LDR R1, ONE'),
                                           nodes.JMPnode('JMP '+extlabel,'',1),nodes.LDRLnode('LDR R1, ZERO', jmplabel,1), nodes.ADInode('ADI R3, #0',extlabel,1)])
         
      self.regstack.append(1)
      self.nodesStack.append(blockstmt)
      self.yourRegister = 0
      self.valueflag = False
      self.kidtypes.append(chtype)


   def pre_visitlessThanExpression(self, Node):
      self.yourRegister = 0
      self.valueflag = True

   def visitlessThanExpression(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
      
      chtype = self.kidtypes.pop() 
      global compareCounter
      faljmplabel = 'false_label'+str(compareCounter)
      compareCounter += 1
      truextlabel = 'trueexit_label'+str(compareCounter)
      compareCounter += 1



      if chtype == 'char':
         blockstmt = nodes.BlockStatement([Node.childN1, Node.childN2, nodes.CMPnode('CMP R0, R1', '', 1), 
                                           nodes.BLTnode('BLT R0, '+truextlabel, '', 1), nodes.LDRLnode('LDR R1, ZERO'),
                                           nodes.JMPnode('JMP '+faljmplabel,'',1),nodes.LDRLnode('LDR R1, ONE', truextlabel,1), nodes.ADInode('ADI R3, #0',faljmplabel,1)])

      #1 and 0 should already have a label
      #wait we need to start our labels with letters----> insert lab at the beginning of each one for example lablit1
      else:#int or string but string is just a pointer so we just compare pointers 

         blockstmt = nodes.BlockStatement([Node.childN1, Node.childN2, nodes.CMPnode('CMP R0, R1', '', 1), 
                                           nodes.BLTnode('BLT R0, '+truextlabel, '', 1), nodes.LDRLnode('LDR R1, ZERO'),
                                           nodes.JMPnode('JMP '+faljmplabel,'',1),nodes.LDRLnode('LDR R1, ONE', truextlabel,1), nodes.ADInode('ADI R3, #0',faljmplabel,1)])
      self.regstack.append(1)
      self.nodesStack.append(blockstmt)
      self.yourRegister = 0
      self.valueflag = False
      self.kidtypes.append(chtype)


   def pre_visitgreaterThanExpression(self, Node):
      self.yourRegister = 0
      self.valueflag = True
      
   def visitgreaterThanExpression(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()

      chtype = self.kidtypes.pop() 

      
      global compareCounter
      faljmplabel = 'false_label'+str(compareCounter)
      compareCounter += 1
      truextlabel = 'trueexit_label'+str(compareCounter)
      compareCounter += 1



      if chtype == 'char':
         blockstmt = nodes.BlockStatement([Node.childN1, Node.childN2, nodes.CMPnode('CMP R0, R1', '', 1), 
                                           nodes.BGTnode('BGT R0, '+truextlabel, '', 1), nodes.LDRLnode('LDR R1, ZERO'),
                                           nodes.JMPnode('JMP '+faljmplabel,'',1),nodes.LDRLnode('LDR R1, ONE', truextlabel,1), nodes.ADInode('ADI R3, #0',faljmplabel,1)])

      #1 and 0 should already have a label
      #wait we need to start our labels with letters----> insert lab at the beginning of each one for example lablit1
      else:#int or string but string is just a pointer so we just compare pointers 

         blockstmt = nodes.BlockStatement([Node.childN1, Node.childN2, nodes.CMPnode('CMP R0, R1', '', 1), 
                                           nodes.BGTnode('BGT R0, '+truextlabel, '', 1), nodes.LDRLnode('LDR R1, ZERO'),
                                           nodes.JMPnode('JMP '+faljmplabel,'',1),nodes.LDRLnode('LDR R1, ONE', truextlabel,1), nodes.ADInode('ADI R3, #0',faljmplabel,1)])
      self.regstack.append(1)
      self.nodesStack.append(blockstmt)
      self.yourRegister = 0
      self.valueflag = False
      self.kidtypes.append(chtype)

   def pre_visitLTEqualsExpression(self, Node):
      self.yourRegister = 0
      self.valueflag = True

   def visitLTEqualsExpression(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()

      chtype = self.kidtypes.pop() 

      
      global compareCounter
      faljmplabel = 'false_label'+str(compareCounter)
      compareCounter += 1
      truextlabel = 'trueexit_label'+str(compareCounter)
      compareCounter += 1

      if chtype == 'char':
         blockstmt = nodes.BlockStatement([Node.childN1, Node.childN2, nodes.CMPnode('CMP R0, R1', '', 1), 
                                           nodes.BLTnode('BLT R0, '+truextlabel, '', 1), nodes.BRZnode('BRZ R0, '+truextlabel, '', 1), nodes.LDRLnode('LDR R1, ZERO'),
                                           nodes.JMPnode('JMP '+faljmplabel,'',1),nodes.LDRLnode('LDR R1, ONE', truextlabel,1), nodes.ADInode('ADI R3, #0',faljmplabel,1)])

      #1 and 0 should already have a label
      #wait we need to start our labels with letters----> insert lab at the beginning of each one for example lablit1
      else:#int or string but string is just a pointer so we just compare pointers 

         blockstmt = nodes.BlockStatement([Node.childN1, Node.childN2, nodes.CMPnode('CMP R0, R1', '', 1), 
                                           nodes.BLTnode('BLT R0, '+truextlabel, '', 1), nodes.BRZnode('BRZ R0, '+truextlabel, '', 1), nodes.LDRLnode('LDR R1, ZERO'),
                                           nodes.JMPnode('JMP '+faljmplabel,'',1),nodes.LDRLnode('LDR R1, ONE', truextlabel,1), nodes.ADInode('ADI R3, #0',faljmplabel,1)])
      self.regstack.append(1)
      self.nodesStack.append(blockstmt)
      self.yourRegister = 0
      self.valueflag = False
      self.kidtypes.append(chtype)

   def pre_visitGTEqualsExpression(self, Node):
      self.yourRegister = 0
      self.valueflag = True
   def visitGTEqualsExpression(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
      chtype = self.kidtypes.pop() 
      #have to do it again so that 

      
      global compareCounter
      faljmplabel = 'false_label'+str(compareCounter)
      compareCounter += 1
      truextlabel = 'trueexit_label'+str(compareCounter)
      compareCounter += 1

      if chtype == 'char':
         blockstmt = nodes.BlockStatement([Node.childN1, Node.childN2, nodes.CMPnode('CMP R0, R1', '', 1), 
                                           nodes.BGTnode('BGT R0, '+truextlabel, '', 1), nodes.BRZnode('BRZ R0, '+truextlabel, '', 1), nodes.LDRLnode('LDR R1, ZERO'),
                                           nodes.JMPnode('JMP '+faljmplabel,'',1),nodes.LDRLnode('LDR R1, ONE', truextlabel,1), nodes.ADInode('ADI R3, #0',faljmplabel,1)])

      #1 and 0 should already have a label
      #wait we need to start our labels with letters----> insert lab at the beginning of each one for example lablit1
      else:#int or string but string is just a pointer so we just compare pointers 

         blockstmt = nodes.BlockStatement([Node.childN1, Node.childN2, nodes.CMPnode('CMP R0, R1', '', 1), 
                                           nodes.BGTnode('BGT R0, '+truextlabel, '', 1), nodes.BRZnode('BRZ R0, '+truextlabel, '', 1), nodes.LDRLnode('LDR R1, ZERO'),
                                           nodes.JMPnode('JMP '+faljmplabel,'',1),nodes.LDRLnode('LDR R1, ONE', truextlabel,1), nodes.ADInode('ADI R3, #0',faljmplabel,1)])
      self.regstack.append(1)
      self.nodesStack.append(blockstmt)
      self.yourRegister = 0
      self.valueflag = False
      self.kidtypes.append(chtype)

   
   def pre_visitandExpression(self, Node):
      self.yourRegister = 0
      self.valueflag = True

   def visitandExpression(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
      
      global compareCounter
      faljmplabel = 'false_label'+str(compareCounter)
      compareCounter += 1
      truextlabel = 'trueexit_label'+str(compareCounter)
      compareCounter += 1

#this one expects bools

      blockstmt = nodes.BlockStatement([Node.childN1, Node.childN2, nodes.LDRLnode('LDR R2, ONE'), nodes.CMPnode('CMP R2, R1', '', 1), nodes.BGTnode('BGT R2, '+faljmplabel, '', 1),
                                          nodes.CMPnode('CMP R0, R1', '', 1), 
                                          nodes.BLTnode('BLT R0, '+faljmplabel, '', 1), nodes.LDRLnode('LDR R1, ONE'),
                                          nodes.JMPnode('JMP '+truextlabel,'',1),nodes.LDRLnode('LDR R1, ZERO', faljmplabel,1), nodes.ADInode('ADI R3, #0',truextlabel,1)])
      self.regstack.append(1)
      self.nodesStack.append(blockstmt)
      self.yourRegister = 0
      self.valueflag = False

   
   def pre_visitorExpression(self, Node):
      self.yourRegister = 0
      self.valueflag = True
   def visitorExpression(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
      
      
      global compareCounter
      faljmplabel = 'false_label'+str(compareCounter)
      compareCounter += 1
      truextlabel = 'trueexit_label'+str(compareCounter)
      compareCounter += 1


#this one expects bools

      blockstmt = nodes.BlockStatement([Node.childN1, Node.childN2, nodes.LDRLnode('LDR R2, ONE'), nodes.CMPnode('CMP R2, R1', '', 1), nodes.BRZnode('BRZ R2, '+truextlabel, '', 1),
                                          nodes.CMPnode('CMP R0, R1', '', 1), 
                                          nodes.BGTnode('BGT R0, '+truextlabel, '', 1), nodes.LDRLnode('LDR R1, ZERO'),
                                           nodes.JMPnode('JMP '+faljmplabel,'',1),nodes.LDRLnode('LDR R1, ONE', truextlabel,1), nodes.ADInode('ADI R3, #0',faljmplabel,1)])
      self.regstack.append(1)
      self.nodesStack.append(blockstmt)
      self.yourRegister = 0
      self.valueflag = False
  
   def pre_visitnotExpression(self, Node):
      self.yourRegister = 1
      self.valueflag = True
   def visitnotExpression(self, Node):
      Node.childN1 = self.nodesStack.pop()
      
      
      global compareCounter
      faljmplabel = 'false_label'+str(compareCounter)
      compareCounter += 1
      truextlabel = 'trueexit_label'+str(compareCounter)
      compareCounter += 1

#this one expects bools

      blockstmt = nodes.BlockStatement([Node.childN1, nodes.LDRLnode('LDR R2, ZERO'), nodes.CMPnode('CMP R2, R1', '', 1), nodes.BRZnode('BRZ R2, '+truextlabel, '', 1),
                                          nodes.LDRLnode('LDR R1, ZERO'),
                                           nodes.JMPnode('JMP '+faljmplabel,'',1),nodes.LDRLnode('LDR R1, ONE', truextlabel,1), nodes.ADInode('ADI R3, #0',faljmplabel,1)])
      self.regstack.append(1)
      self.nodesStack.append(blockstmt)
      self.yourRegister = 0
      self.valueflag = False

   def pre_visitunaryPlusExpression(self, Node):
      self.yourRegister = 1
      self.valueflag = True
   def visitunaryPlusExpression(self, Node):
      Node.childN1 = self.nodesStack.pop()
      
      
      global compareCounter
      exitlabel = 'exit_label'+str(compareCounter)
      compareCounter += 1
      

#this one expects bools

      blockstmt = nodes.BlockStatement([Node.childN1, nodes.LDRLnode('LDR R2, ZERO'), nodes.CMPnode('CMP R2, R1', '', 1), 
                                          nodes.BLTnode('BLT R2, '+exitlabel, '', 1),nodes.BRZnode('BRZ R2, '+exitlabel, '', 1),
                                          nodes.LDRLnode('LDR R2, ZERO'), nodes.ADInode('ADI R2, #-1'),
                                          nodes.MULnode('MUL R1, R2'), nodes.ADInode('ADI R3, #0',exitlabel,1)])
      self.regstack.append(1)
      self.nodesStack.append(blockstmt)
      self.yourRegister = 0
      self.valueflag = False

   def pre_visitunaryMinusExpression(self, Node):
      self.yourRegister = 1
      self.valueflag = True
   def visitunaryMinusExpression(self, Node):
      
      Node.childN1 = self.nodesStack.pop()
     
      global compareCounter
      exitlabel = 'exit_label'+str(compareCounter)
      compareCounter += 1

#we are just straight up applying a negative to it 

      blockstmt = nodes.BlockStatement([Node.childN1, nodes.LDRLnode('LDR R0, ZERO'), nodes.ADInode('ADI R0, #-1'), nodes.MULnode('MUL R1, R0', '', 1), nodes.ADInode('ADI R3, #0',exitlabel,1)])
      self.regstack.append(1)
      self.nodesStack.append(blockstmt)
      self.yourRegister = 0
      self.valueflag = False




   def visitliteralIntExpression(self, Node):
      #self.nodesStack.append(Node)
      #these can only appear on the right side of assignments
      #meaning we can just change this to be a block statement that loads the value into r1
      #self.regstack.append(Node.value)
      typev, bs, val, counter = self.littable.findLabel(str(Node.value))

      if self.yourRegister == 0:
         blockstmt = nodes.BlockStatement([nodes.LDRLnode('LDR R'+str(self.yourRegister)+', lablit'+str(counter), '', 1)])
      elif self.yourRegister == 1:
         blockstmt = nodes.BlockStatement([nodes.LDRLnode('LDR R'+str(self.yourRegister)+', lablit'+str(counter), '', 1)])
      else:
         print('hey literal or identfier obtained an incorrect register make sure we are clearing int pre and post visit of our parent')

      self.kidtypes.append('int')
      self.regstack.append(self.yourRegister)
      self.nodesStack.append(blockstmt)
      self.yourRegister += 1
      pass

   def visitliteralCharExpression(self, Node):
      #self.nodesStack.append(Node)
      #this can only show up on the right side of assigns and vardecl
      #self.regstack.append(Node.value)
      typev, bs, val, counter = self.littable.findLabel(Node.value)
      
      
      if self.yourRegister == 0:
         blockstmt = nodes.BlockStatement([nodes.LDBLnode('LDB R'+str(self.yourRegister)+', lablit'+str(counter), '', 1)])
      elif self.yourRegister == 1:
         blockstmt = nodes.BlockStatement([nodes.LDBLnode('LDB R'+str(self.yourRegister)+', lablit'+str(counter), '', 1)])
      else:
         print('hey literal or identfier obtained an incorrect register make sure we are clearing int pre and post visit of our parent')

      self.kidtypes.append('char')
      self.regstack.append(self.yourRegister)
      self.nodesStack.append(blockstmt)
      self.yourRegister += 1
      pass

   def visitliteralStringExpression(self, Node):
      #strings are just pointers to the memory
      #strings can only be in cout and static
      typev, bs, val, counter = self.littable.findLabel(Node.value)
      
      if self.yourRegister == 0:
         blockstmt = nodes.BlockStatement([nodes.LDAnode('LDA R'+str(self.yourRegister)+', lablit'+str(counter), '', 1)])
      elif self.yourRegister == 1:
         blockstmt = nodes.BlockStatement([nodes.LDAnode('LDA R'+str(self.yourRegister)+', lablit'+str(counter), '', 1)])
      else:
         print('hey literal or identfier obtained an incorrect register make sure we are clearing int pre and post visit of our parent')

      self.kidtypes.append('string')
      self.regstack.append(self.yourRegister)
      self.nodesStack.append(blockstmt)
      self.yourRegister += 1
      pass
   

   #ive already made changes to true and false
   def visittrueExpression(self, Node):
      self.nodesStack.append(Node)
      pass

   def visitfalseExpression(self, Node):
      self.nodesStack.append(Node)
      pass


   #can only be used on arrays and objects
   def visitnullExpression(self, Node):
      #can probably just LDR a null value or just 0
      blockstmt = nodes.BlockStatement([nodes.LDRLnode('LDR R1, ZERO', '', 1)])
      self.regstack.append(1)
      self.nodesStack.append(blockstmt)

      #self.nodesStack.append(Node)
      
#right side child is the only one that can have to possiblity of putting a register on the stack in use and this is for only assignment and vardecl
#pop children in reverse order
#when we compute we will either automatically store the right child as the R1 valueparam
   def visitidentifierExpression(self, Node):

      #we coult have an identifier for the beginning of a function call which we dont want to lookup the type of because we literally cant cause its defined somewhere else
      if self.currentfunRecord.checkKey(Node.value):
         typeval1, offset1, isparam1 = self.currentfunRecord.lookup(Node.value)
         
         #self.regstack.append(Node.value)
         if self.valueflag:
            if typeval1 == 'char':
               blockstmt = nodes.BlockStatement([nodes.MOVnode('MOV R'+str(self.yourRegister)+', FP', '', 1), nodes.ADInode('ADI R'+str(self.yourRegister)+', #-'+str(offset1), '', 1), 
                                                nodes.LDBLnode('LDB R'+str(self.yourRegister)+', R'+str(self.yourRegister), '', 1)])
            else:
               blockstmt = nodes.BlockStatement([nodes.MOVnode('MOV R'+str(self.yourRegister)+', FP', '', 1), nodes.ADInode('ADI R'+str(self.yourRegister)+', #-'+str(offset1), '', 1), 
                                                nodes.LDRLnode('LDR R'+str(self.yourRegister)+', R'+str(self.yourRegister), '', 1)])

         else:
            if typeval1 == 'char':
               blockstmt = nodes.BlockStatement([nodes.MOVnode('MOV R'+str(self.yourRegister)+', FP', '', 1), nodes.ADInode('ADI R'+str(self.yourRegister)+', #-'+str(offset1), '', 1)])
            else:
               blockstmt = nodes.BlockStatement([nodes.MOVnode('MOV R'+str(self.yourRegister)+', FP', '', 1), nodes.ADInode('ADI R'+str(self.yourRegister)+', #-'+str(offset1), '', 1)])



     
         self.kidtypes.append(typeval1)
         self.regstack.append(self.yourRegister)
         self.nodesStack.append(blockstmt)
         self.yourRegister += 1
      else:
         self.nodesStack.append(Node)

   def visitthisExpression(self, Node):
      self.nodesStack.append(Node)
      self.regstack.append('this')
      self.kidtypes.append('this')
      self.yourRegister += 1
      pass


   def visitperiodExpression(self, Node):
      Node.childN1 = self.nodesStack.pop()
      self.nodesStack.append(Node)
      pass

   
   

   
   def visitparenExpression(self, Node):
      Node.childN1 = self.nodesStack.pop()
      self.nodesStack.append(Node)
      pass

#end of expressions
#pre visit call set the functioncallrecord, use that for when we do storing those values in stack(note: all arguments will be tempvaraibles or just variable ids) as we go through arguments they will store themselves in order of their offset in actrecord
   def pre_visitcallExpression(self, Node):
      #we now that child1 has to be an id 
      self.funcallrec = self.findFunctionActRec(Node.childN1.value, Node.parentClass)
      
      self.parCounter = 0
      self.paramoffs = []
      self.paramoffs = self.funcallrec.getParOffs()
      Node.funName = Node.childN1.value
      self.yourRegister = 0
      self.valueflag = True


   

   def visitcallExpression(self, Node):
      Node.childN2 = self.nodesStack.pop()
      Node.childN1 = self.nodesStack.pop()
      #have to know use any registers i want to get ready to jump to funcion label
      #place param allocations first before my actual operations
      #needed to pop the id value off the stack
      #have to pop two off because we need the one from our id and the one from our parameterlis
      #we could have main with an argument or we could have a main wihtout arguments as such it should only pop off one 
      #if Node.childN2.childN1 is None:
      #   self.regstack.pop()
      #else:
       #  self.regstack.pop()
      #   self.regstack.pop()
      


      totaloffset = self.funcallrec.offset
#childn1 will be an id so just do Node.classparent+'_'+Node.childn1.value
      #print(Node.childN2)
      #print(Node.childN1, Node.childN1.value, Node.RT)

      if Node.RT == 'char':
      #remember prep children then expression we return then jump back 
         blockstmt = nodes.BlockStatement([Node.childN2,nodes.MOVnode('MOV R4, FP', '', 4),  nodes.MOVnode('MOV FP, SP', '', 4), nodes.ADInode('ADI SP, #-4', '', 0), 
                                                nodes.STRRnode('STR R4, SP', '', 4), nodes.ADInode('ADI SP, #-'+str(totaloffset), '', 0), 
                                                nodes.MOVnode('MOV R5, PC', '', 4), nodes.ADInode('ADI R5, #36', '', 0), nodes.STRRnode('STR R5, FP'), 
                                                nodes.JMPnode('JMP '+Node.parentClass+'_'+Node.funName,''), nodes.LDBRnode('LDB R1, SP','',1)])
      elif Node.RT == 'void': #should just be four bytes
      #need to do minus four to sp first then i can use the total offset number from the funrecord
         blockstmt = nodes.BlockStatement([Node.childN2,nodes.MOVnode('MOV R4, FP', '', 4),  nodes.MOVnode('MOV FP, SP', '', 4), nodes.ADInode('ADI SP, #-4', '', 0), 
                                                nodes.STRRnode('STR R4, SP', '', 4), nodes.ADInode('ADI SP, #-'+str(totaloffset), '', 0), 
                                                nodes.MOVnode('MOV R5, PC', '', 4), nodes.ADInode('ADI R5, #36', '', 0), nodes.STRRnode('STR R5, FP'), nodes.JMPnode('JMP '+Node.parentClass+'_'+Node.funName,'',1)])
      else:
         blockstmt = nodes.BlockStatement([Node.childN2,nodes.MOVnode('MOV R4, FP', '', 4),  nodes.MOVnode('MOV FP, SP', '', 4), nodes.ADInode('ADI SP, #-4', '', 0), 
                                                nodes.STRRnode('STR R4, SP', '', 4), nodes.ADInode('ADI SP, #-'+str(totaloffset), '', 0), 
                                                nodes.MOVnode('MOV R5, PC', '', 4), nodes.ADInode('ADI R5, #36', '', 0), nodes.STRRnode('STR R5, FP'), 
                                                nodes.JMPnode('JMP '+Node.parentClass+'_'+Node.funName,''), nodes.LDRRnode('LDR R1, SP','',1)])
#append 1 just incase this goes to an assignment 
      self.regstack.append(1)
      self.nodesStack.append(blockstmt)
      self.kidtypes.append(Node.RT)
      self.yourRegister = 0
      self.valueflag = False
      

#now i have to just take in id and alloc on stack pointer using offset in funcallrecord. how do i keep track of which number param im working with? maybe keep a counter 
#

   def visitArguments(self, node):
      
      if node.childN1 is None:
         self.nodesStack.append(node)
      else:
         node.childN1 = self.nodesStack.pop()
         self.nodesStack.append(node)

      

   
   #maybe put them back in reverse order since exprs are ids they will jsut be id values on regstack for the children i have, also check if it is this if so just put 0 in as replacement 
   def pre_visitArgumentList(self, node):
      self.yourRegister = 1
      self.valueflag = True
      numChildren = len(node.children)
      for child in range(numChildren):
         self.yourRegister = 1
         self.valueflag = True
         node.children[child].accept(self)

      node.children = []
      for child in range(numChildren):
         node.children.insert(0,self.nodesStack.pop())

   def visitArgumentList(self, node):
      #once we get here and know that we have arguments i think we can assume that we are no longer a main function
      numChildren = len(node.children)
      node.children = []
      for child in range(numChildren):
         node.children.insert(0,self.nodesStack.pop())
         #can pass offset and type 
      #pop the this off
      self.kidtypes.pop()
      #we need to do for range in len of children then pop id in reverse order and pop off params offs and when i create block statement
      #put it in a list then when im finally done assign that as my children for the node and pass the node back up, it doesnt matter what order i put them into the list as long as they store what they need to store
      paramblocks = []
      #node.children.sort(reverse=True)
      #self.nodesStack.append(node)
      for i in range(1, numChildren+1):
         poff = self.paramoffs.pop() #2nd offset 
         chtype = self.kidtypes.pop() 

         if chtype == 'this':
            blockstmt = nodes.BlockStatement([
                                           nodes.LDRLnode('LDR R0, ZERO', '', 0),nodes.MOVnode('MOV R1, SP', '', 1), nodes.ADInode('ADI R1, #-'+str(poff), '', 1), 
                                           nodes.STRRnode('STR R0, R1', '', 1)]) 
            
         else:
            

            if chtype == 'char':
               blockstmt = nodes.BlockStatement([node.children[-i],nodes.MOVnode('MOV R2, SP', '', 1), nodes.ADInode('ADI R2, #-'+str(poff), '', 1), 
                                           nodes.STBLnode('STB R1, R2', '', 1)]) 
            else:
               blockstmt = nodes.BlockStatement([node.children[-i],nodes.MOVnode('MOV R2, SP', '', 1), nodes.ADInode('ADI R2, #-'+str(poff), '', 1), 
                                           nodes.STRLnode('STR R1, R2', '', 1)]) 
         paramblocks.insert(0, blockstmt)



      self.kidtypes.append(chtype)   
      self.regstack.append(1)
      node.children = paramblocks
      self.nodesStack.append(node)


      
   
   

   

   def pre_visitBlocknode(self, Node):
      pass
   def visitBlocknode(self, Node):
      numChildren = len(Node.children)
      Node.children = []
      for child in range(numChildren):
         Node.children.insert(0,self.nodesStack.pop())
      #node.children.sort(reverse=True)
      self.nodesStack.append(Node)


   def pre_visitASMnode(self,Node):
      pass
   def visitASMnode(self,Node):
      numChildren = len(Node.children)
      Node.children = []
      for child in range(numChildren):
         Node.children.insert(0,self.nodesStack.pop())
      #node.children.sort(reverse=True)
      self.nodesStack.append(Node)


#maybe it would make sense to convert var decls to assignments
#he said store everything on the stack does he mean a new stack or the data segment stack? if we pop then a new stack right?
#need registers to perform this no?
#when i post visit an asm node i should push its register on the stack??

class ifVisitor(ReConnectVisitor):
   def __init__(self, globalst, classsts, functionsts, funrecords):
      ReConnectVisitor.__init__(self, globalst, classsts, functionsts)
      self.registers = []
      self.regstack = []
      #they said only ids but why? 
      self.funActiveRecords = funrecords
      
      self.currentfunRecord = None #we dont have to keep a stack i think 
      
      #we need records for functions and classes two separate lists so that when we go into a constructor we can use the class record and the 


   def findFunctionActRec(self, name, parentN):
      for st in self.funActiveRecords:
         if st.name == name and st.parent == parentN:
            return st
   def findclassActRec(self, name):
      for st in self.classActiveRecs:
         if st.name == name:
            return st

   def pre_visitCompUnit(self, node):
      self.stack.append(self.findFunctionST(node.id, 'global'))
      self.currentfunRecord = self.findFunctionActRec(node.id, 'global')
      self.current += 1
      
   def visitCompUnit(self, node):
      #pop the scope off
      self.stack.pop()
      self.current -= 1
      #have to reverse sort afterwards
      numChildren = len(node.children)
      node.children = []
      for child in range(numChildren):
         node.children.insert(0,self.nodesStack.pop())
      #node.children.sort(reverse=True)

   def pre_visitMethodDecl(self, node):
      self.stack.append(self.findFunctionST(node.id, self.stack[self.current].name))
      self.currentfunRecord = self.findFunctionActRec(node.id, self.stack[self.current].name)
      self.current += 1
      
   def visitMethodDecl(self, node):
      #pop the scope off
      self.stack.pop()
      self.current -= 1

      node.childN3 = self.nodesStack.pop()
      node.childN2 = self.nodesStack.pop()
      node.childN1 = self.nodesStack.pop()
      self.nodesStack.append(node)
      
   def pre_visitConstructorDecl(self, node):
      self.stack.append(self.findFunctionST(node.id, self.stack[self.current].name))
      self.currentfunRecord = self.findFunctionActRec(node.id, self.stack[self.current].name)
      self.current += 1
      
   def visitConstructorDecl(self, node):
      #pop the scope off
      self.stack.pop()
      self.current -= 1
      node.childN2 = self.nodesStack.pop()
      self.nodesStack.append(node)


   def visitifStatement(self, Node):
      if Node.childN3 is None:
         Node.childN2 = self.nodesStack.pop()
         Node.childN1 = self.nodesStack.pop()
         
      else:
         Node.childN3 = self.nodesStack.pop()
         Node.childN2 = self.nodesStack.pop()
         Node.childN1 = self.nodesStack.pop()

      numChildren = len(Node.prepChildren)
      Node.prepChildren = []
      for child in range(numChildren):
         Node.prepChildren.insert(0,self.nodesStack.pop())


      Node.childN1.accept(self)
      #have to take it off the nodes stack
      self.nodesStack.pop()
      
      Regchild1 = self.regstack.pop()
      typeval1, offset1, isparam1 = self.currentfunRecord.lookup(Regchild1)
      #has to be a bool for ifs conditional expression
      blockstmt = nodes.BlockStatement([nodes.MOVnode('MOV R1, FP', '', 0), nodes.ADInode('ADI R1, #-'+str(offset1), '', 0), 
                                        nodes.LDRLnode('LDR R1, R1', '', 0)])
      self.regstack.append(1)
      


      global ifCounter
      iflabel = 'if_label'+str(ifCounter)
      ifCounter += 1

      if Node.whloop:
         #have to manually go through the bgt or whatever asm node and reset its register but not its label, how??
         #could add another variable to asm nodes called jump labels in case it needs to jump to a label
         #true is one and false is 0
         #how do i check what the expression will be? well if its true its just a true expression which is 1 if zero branch
         #i dont have the register for brznode to check.... maybe have it so all the asm nodes that weve already made will continue to allocate and pop off the stack
         #this will help me so i can create other asm nodes since all i need to do is pop off the stack
         tempnode = nodes.BlockStatement([Node.prepChildren, blockstmt, nodes.BRZnode('BRZ R1, ' + iflabel), Node.childN2, nodes.JMPnode('JMP '+ Node.whlabel), nodes.ADInode('ADI R3, #0', iflabel)])

      elif Node.childN3 is None:
         tempnode = nodes.BlockStatement([Node.prepChildren, blockstmt, nodes.BRZnode('BRZ R1, ' + iflabel), Node.childN2, nodes.ADInode('ADI R3, #0', iflabel)])
      else:
       #it contains an else statement so it wasnt a while or switch statement.
       #  if expression fails go to the else statement if its true need to have another instruction that jumps once done so we dont run the else statement
         exitlabel = 'if_exitlabel'+str(ifCounter)
         ifCounter += 1
         tempnode = nodes.BlockStatement([Node.prepChildren, blockstmt, nodes.BRZnode('BRZ R1, ' + iflabel), Node.childN2, nodes.JMPnode('JMP '+ exitlabel), nodes.ADInode('ADI R3, #0', iflabel),Node.childN3, nodes.ADInode('ADI R3, #0', exitlabel)])


      #have to find a way to make registers in a stack work and be updated constantly as go through visitors so in case i add a new asm node i 
      # can pop off the stack to see which register i need or which register is free

      self.nodesStack.append(tempnode)

   def visitidentifierExpression(self, Node):
      self.nodesStack.append(Node)
      self.regstack.append(Node.value)
      
   def visitASMnode(self, Node):
      self.nodesStack.append(Node)
      self.regstack.append(Node.register)


    

      

class ReturningVisitor(ReConnectVisitor):#maybe split up into two visitorshave to return default value of return type
   #i know for a fact that we if we have an expression it will be an id temp, if not it will be empty and we can just return without bringing anything back
   def __init__(self,globalst,classsts,functionsts, funrecords):
      ReConnectVisitor.__init__(self, globalst, classsts, functionsts)
      self.registers = []
      self.regstack = []
      #they said only ids but why? 
      self.funActiveRecords = funrecords
      
      self.currentfunRecord = None #we dont have to keep a stack i think 
      
      #we need records for functions and classes two separate lists so that when we go into a constructor we can use the class record and the 


   def findFunctionActRec(self, name, parentN):
      for st in self.funActiveRecords:
         if st.name == name and st.parent == parentN:
            return st
   def findclassActRec(self, name):
      for st in self.classActiveRecs:
         if st.name == name:
            return st

   def pre_visitCompUnit(self, node):
      self.stack.append(self.findFunctionST(node.id, 'global'))
      self.currentfunRecord = self.findFunctionActRec(node.id, 'global')
      self.current += 1
      
   def visitCompUnit(self, node):
      #pop the scope off
      self.stack.pop()
      self.current -= 1
      #have to reverse sort afterwards
      numChildren = len(node.children)
      node.children = []
      for child in range(numChildren):
         node.children.insert(0,self.nodesStack.pop())
      #node.children.sort(reverse=True)

   def pre_visitMethodDecl(self, node):
      self.stack.append(self.findFunctionST(node.id, self.stack[self.current].name))
      self.currentfunRecord = self.findFunctionActRec(node.id, self.stack[self.current].name)
      self.current += 1
      
   def visitMethodDecl(self, node):
      #pop the scope off
      self.stack.pop()
      self.current -= 1

      node.childN3 = self.nodesStack.pop()
      node.childN2 = self.nodesStack.pop()
      node.childN1 = self.nodesStack.pop()
      self.nodesStack.append(node)
      
   def pre_visitConstructorDecl(self, node):
      self.stack.append(self.findFunctionST(node.id, self.stack[self.current].name))
      self.currentfunRecord = self.findFunctionActRec(node.id, self.stack[self.current].name)
      self.current += 1
      
   def visitConstructorDecl(self, node):
      #pop the scope off
      self.stack.pop()
      self.current -= 1
      node.childN2 = self.nodesStack.pop()
      self.nodesStack.append(node)


   

   def visitidentifierExpression(self, Node):
      self.nodesStack.append(Node)
      self.regstack.append(Node.value)
      
   def visitASMnode(self, Node):
      self.nodesStack.append(Node)
      self.regstack.append(Node.register)


   def visitMethodBody(self, node):
      #have to reverse sort afterwards
      numChildren = len(node.children)
      node.children = []
      for child in range(numChildren):
         node.children.insert(0,self.nodesStack.pop())
      #node.children.sort(reverse=True)
      self.nodesStack.append(node)

   def visitreturnStatement(self, Node):#value will be placed where fp was originally
      #make pfp equal to current fp then change fp to point to sp
      #other way around 

      if Node.childN1 is None:
         #convert to blockstatement with just returnign from function assume all registers are open to us
         #self.nodesStack.append(Node)
         pass
         
      else:
         #convert to blockstatement with just returnign from function assume all registers are open to us
         Node.childN1 = self.nodesStack.pop()
      


      #make sure that we place the prepchildren first in the block statement
      numChildren = len(Node.prepChildren)
      Node.prepChildren = []
      for child in range(numChildren):
         Node.prepChildren.insert(0,self.nodesStack.pop())



      if Node.childN1 is None:
         #convert to blockstatement with just returnign from function assume all registers are open to us
         #self.nodesStack.append(Node)
         #mov fp into a register adi immediate -4 pfp, then move fp into sp, ldr for pfp then mov into fp then 
         blockstmt = nodes.BlockStatement([Node.prepChildren,nodes.MOVnode('MOV R4, FP', '', 4), nodes.ADInode('ADI R4, #-4', '', 4), nodes.MOVnode('MOV SP, FP', '', 4),
                                             nodes.LDRLnode('LDR FP, R4', '', 4), 
                                             nodes.LDRLnode('LDR R5, SP'), nodes.JMRnode('JMR R5','',4)])
         
      else:
         #convert to blockstatement with just returnign from function assume all registers are open to us

         Regchild1 = self.regstack.pop()
         
         typeval1, offset1, isparam1 = self.currentfunRecord.lookup(Regchild1)

   
         if typeval1 == 'char':
#remember prep children then expression we return then jump back 
            blockstmt = nodes.BlockStatement([Node.prepChildren,nodes.MOVnode('MOV R0, FP', '', 0), nodes.ADInode('ADI R0, #-'+str(offset1), '', 0), 
                                           nodes.LDBLnode('LDB R0, R0', '', 0),nodes.MOVnode('MOV R4, FP', '', 4), nodes.ADInode('ADI R4, #-4', '', 4), nodes.MOVnode('MOV SP, FP', '', 4),
                                                nodes.LDRLnode('LDR FP, R4', '', 4), #load return address first before placing return expression
                                                nodes.LDRLnode('LDR R5, SP'), nodes.STBRnode('STB R0, SP'), nodes.JMRnode('JMR R5','',4)])
         else: #should just be four bytes
         
            blockstmt = nodes.BlockStatement([Node.prepChildren,nodes.MOVnode('MOV R0, FP', '', 0), nodes.ADInode('ADI R0, #-'+str(offset1), '', 0), 
                                             nodes.LDRLnode('LDR R0, R0', '', 0),nodes.MOVnode('MOV R4, FP', '', 4), nodes.ADInode('ADI R4, #-4', '', 4), nodes.MOVnode('MOV SP, FP', '', 4),
                                                   nodes.LDRLnode('LDR FP, R4', '', 4), #load return address first before placing return expression
                                                   nodes.LDRLnode('LDR R5, SP'), nodes.STRRnode('STR R0, SP'), nodes.JMRnode('JMR R5','',4)])
         
         
         #Node.childN1 = self.nodesStack.pop()
         #self.nodesStack.append(Node)


      
      self.regstack.append(1)
      self.nodesStack.append(blockstmt)
   


class CoutCinVisitor(ReConnectVisitor):#make sure i am either storing or loading with the correct instruction and if its a string have to use different instructions
   #since we know that we have an id for the expression we can just evaluate the type and do the right instructions 

   def __init__(self,globalst,classsts,functionsts, funrecords):
      ReConnectVisitor.__init__(self, globalst, classsts, functionsts)
      self.registers = []
      self.regstack = []
      #they said only ids but why? 
      self.funActiveRecords = funrecords
      
      self.currentfunRecord = None #we dont have to keep a stack i think 
      
      #we need records for functions and classes two separate lists so that when we go into a constructor we can use the class record and the 


   def findFunctionActRec(self, name, parentN):
      for st in self.funActiveRecords:
         if st.name == name and st.parent == parentN:
            return st
   def findclassActRec(self, name):
      for st in self.classActiveRecs:
         if st.name == name:
            return st
         
   def pre_visitCompUnit(self, node):
      self.stack.append(self.findFunctionST(node.id, 'global'))
      self.currentfunRecord = self.findFunctionActRec(node.id, 'global')
      self.current += 1
      
   def visitCompUnit(self, node):
      #pop the scope off
      self.stack.pop()
      self.current -= 1
      #have to reverse sort afterwards
      numChildren = len(node.children)
      node.children = []
      for child in range(numChildren):
         node.children.insert(0,self.nodesStack.pop())
      #node.children.sort(reverse=True)

   def pre_visitMethodDecl(self, node):
      self.stack.append(self.findFunctionST(node.id, self.stack[self.current].name))
      self.currentfunRecord = self.findFunctionActRec(node.id, self.stack[self.current].name)
      self.current += 1
      
   def visitMethodDecl(self, node):
      #pop the scope off
      self.stack.pop()
      self.current -= 1

      node.childN3 = self.nodesStack.pop()
      node.childN2 = self.nodesStack.pop()
      node.childN1 = self.nodesStack.pop()
      self.nodesStack.append(node)
      
   def pre_visitConstructorDecl(self, node):
      self.stack.append(self.findFunctionST(node.id, self.stack[self.current].name))
      self.currentfunRecord = self.findFunctionActRec(node.id, self.stack[self.current].name)
      self.current += 1
      
   def visitConstructorDecl(self, node):
      #pop the scope off
      self.stack.pop()
      self.current -= 1
      node.childN2 = self.nodesStack.pop()
      self.nodesStack.append(node)


   def visitcoutStatement(self, Node):
      Node.childN1 = self.nodesStack.pop()
      numChildren = len(Node.prepChildren)
      Node.prepChildren = []
      for child in range(numChildren):
         Node.prepChildren.insert(0,self.nodesStack.pop())


      Regchild1 = self.regstack.pop()
      typeval1, offset1, isparam1 = self.currentfunRecord.lookup(Regchild1)

   #if string have to do some weird thing to print it out-- remember we will insert a \0 at then end of the string 
      if typeval1 == 'char':
#remember prep children then expression we return then jump back 
         blockstmt = nodes.BlockStatement([Node.prepChildren,nodes.MOVnode('MOV R3, FP', '', 0), nodes.ADInode('ADI R3, #-'+str(offset1), '', 0), 
                                          nodes.LDBLnode('LDB R3, R3', '', 0), nodes.TRPTHREEnode('TRP #3','',3)])
      elif typeval1 == 'string':
         #need to set up a loop 
         global stringCounter
         strloop = 'output_string'+str(stringCounter)
         extloop = 'exit_string'+str(stringCounter)
         stringCounter += 1

         blockstmt = nodes.BlockStatement([Node.prepChildren,nodes.MOVnode('MOV R1, FP', '', 0), nodes.ADInode('ADI R1, #-'+str(offset1), '', 0), 
                                          nodes.LDRRnode('LDR R1, R1', '', 0), nodes.LDBRnode('LDB R3, R1', strloop),nodes.LDBRnode('LDB R2, NULLTERM'), nodes.CMPnode('CMP R2, R3'),
                                          nodes.BRZnode('BRZ R2, '+extloop),  nodes.TRPTHREEnode('TRP #3','',3), nodes.ADInode('ADI R1, #1'), nodes.JMPnode('JMP '+strloop), nodes.ADInode('ADI R3, #0', extloop, 3)])

      else:
         blockstmt = nodes.BlockStatement([Node.prepChildren,nodes.MOVnode('MOV R3, FP', '', 0), nodes.ADInode('ADI R3, #-'+str(offset1), '', 0), 
                                          nodes.LDRRnode('LDR R3, R3', '', 0), nodes.TRPTHREEnode('TRP #1','',3)])
         

      self.regstack.append(3)
      self.nodesStack.append(blockstmt)
      

   
   def visitcinStatement(self, Node):
      Node.childN1 = self.nodesStack.pop()
      numChildren = len(Node.prepChildren)
      Node.prepChildren = []
      for child in range(numChildren):
         Node.prepChildren.insert(0,self.nodesStack.pop())

      Regchild1 = self.regstack.pop()
      typeval1, offset1, isparam1 = self.currentfunRecord.lookup(Regchild1)

   #if string have to do some weird thing to print it out-- remember we will insert a \0 at then end of the string 
      if typeval1 == 'char':
#remember prep children then expression we return then jump back 
         blockstmt = nodes.BlockStatement([Node.prepChildren, nodes.TRPFOURnode('TRP #4','',3), nodes.MOVnode('MOV R1, FP', '', 0), nodes.ADInode('ADI R1, #-'+str(offset1), '', 0), 
                                          nodes.STBRnode('STB R3, R1', '', 0), ])
      else:
         blockstmt = nodes.BlockStatement([Node.prepChildren, nodes.TRPTWOnode('TRP #2','',3), nodes.MOVnode('MOV R1, FP', '', 0), nodes.ADInode('ADI R1, #-'+str(offset1), '', 0), 
                                          nodes.STRRnode('STR R3, R1', '', 0), ])
         

      self.regstack.append(3)
      self.nodesStack.append(blockstmt)



   def visitidentifierExpression(self, Node):
      self.nodesStack.append(Node)
      self.regstack.append(Node.value)
      
   def visitASMnode(self, Node):
      self.nodesStack.append(Node)
      self.regstack.append(Node.register)


#if its a class just set the pointer to null since we cant create them, also alduos will not be testing a.b data members or this.x in his test cases 


class DefaultInitVisitor(ReConnectVisitor): #default initialize for everything is what he said, how should we do it for paramaters and where. if we see that its a type of class just set pointer to null or 0 pretty much
   #for every previsit for a function or main go through act record and put zero in every local variable 
   #we just go to main we dont need to default params i think even if it has params so for the first jump just allocate stack size and place returns then jump 
   #could default initialize values after every use, so bassicaly when returning just clean up the paramater variables
#cant we just multiply by zero and move that into or store it as default???
#i can just do this all in the method body, easier to just do it in functions Visitor 
   def __init__(self,globalst,classsts,functionsts, funrecords):
      ReConnectVisitor.__init__(self, globalst, classsts, functionsts)
      self.registers = []
      self.regstack = []
      #they said only ids but why? 
      self.funActiveRecords = funrecords
   pass














#FUNCTIONSVISTOR() MUST BE THE LAST ONE BEFORE CALLING CODEGENERATIONVISITOR


#easy as just placing it as block statement and puting a noop in the first instruction that has label of the function
#i need to have my activation record and create all the instructions that default initialize my local variables and prepend it to the function or method. then i can move on to place a label and making it global
class functionsVisitor(ReConnectVisitor):#place functions in global scope with labels so that i know where to jump to,, make sure that we default initialize first for every variable except paramaters??? how do i initialize parameters to default?
#how do i turn functions into global scope with labels? and how do i keep track of that label if i want to call the function from somewhere else????   with arguments we just allocate on stack, callexpression has to 
#store the return address and call jump to the label, this is because call expression holds the parent class name. we know that all call expressions will have an id expression on the left side because of our 
#optimization#can just put a dummy instruction in a block statement before initializers and set a label on it for the function
   def __init__(self,globalst,classsts,functionsts, funrecords, labtable):
      ReConnectVisitor.__init__(self, globalst, classsts, functionsts)
      self.registers = []
      self.regstack = []
      #they said only ids but why? 
      self.litlabels = labtable #remember also do a sepcial label NULLTERM '\\0'
      self.funActiveRecords = funrecords

   def findFunctionActRec(self, name, parentN):
      for st in self.funActiveRecords:
         if st.name == name and st.parent == parentN:
            return st
   def findclassActRec(self, name):
      for st in self.classActiveRecs:
         if st.name == name:
            return st
         
   def pre_visitCompUnit(self, node):
      self.stack.append(self.findFunctionST(node.id, 'global'))
      self.currentfunRecord = self.findFunctionActRec(node.id, 'global')
      self.current += 1
      
   def visitCompUnit(self, node):
      #pop the scope off
      self.stack.pop()
      self.current -= 1
      #have to reverse sort afterwards
      numChildren = len(node.children)
      node.children = []
      for child in range(numChildren):
         node.children.insert(0,self.nodesStack.pop())

      self.currentfunRecord = self.findFunctionActRec(node.id, 'global')
      totaloffset = self.currentfunRecord.offset


      #we are adding an insertion point as the last child for compunit, when we run codegeneration make sure compunit accepts its children in the reverse order maybe do [-i]
      insertion = nodes.BlockStatement([nodes.JMPnode('JMP MAIN'),  nodes.MOVnode('MOV R4, FP', 'MAIN', 4),  nodes.MOVnode('MOV FP, SP', '', 4), nodes.ADInode('ADI SP, #-4', '', 0), 
                                                nodes.STRRnode('STR R4, SP', '', 4), nodes.ADInode('ADI SP, #-'+str(totaloffset), '', 0), 
                                                nodes.MOVnode('MOV R5, PC', '', 4), nodes.ADInode('ADI R5, #36', '', 0), nodes.STRRnode('STR R5, FP'),
                                                  nodes.JMPnode('JMP global_main','',1), nodes.TRPZEROnode('TRP #0')])
      node.children.append(insertion)

      #now place the labels in static memory
      statlabels = []
      #first the labels i absolutly need
      statlabels.append(nodes.DIRECTIVEnode('.INT #0','ZERO'))
      statlabels.append(nodes.DIRECTIVEnode('.INT #1','ONE'))
      statlabels.append(nodes.DIRECTIVEnode('.BYT \'\\0\'','NULLTERM'))
      for typeval, bytesize, value, counterN in self.litlabels.data.values():
         if typeval == 'string':
            value = value[1:-1]
            strlen = len(value)
            #we need to check that \n is together and not seperate, do we do the same for \\
            if strlen == 0:
               #we have to ouput a \0 as well so the string knows where to stop even if its blank cause other wise it will keep on going to run other code
               statlabels.append(nodes.DIRECTIVEnode('.BYT ','lablit'+str(counterN)))
               statlabels.append(nodes.DIRECTIVEnode('.BYT \'\\0\'',''))
            else:
               countstart = 1
               Lcounter= 0
               if value[0] == '\\':
                  countstart = 2
                  if value[Lcounter+1] == '"':
                        statlabels.append(nodes.DIRECTIVEnode('.BYT \''+value[1]+'\'','lablit'+str(counterN)))
                        Lcounter += 1
                  else:
                     statlabels.append(nodes.DIRECTIVEnode('.BYT \''+value[0]+value[1]+'\'','lablit'+str(counterN)))
                     Lcounter += 1
               else:
                  statlabels.append(nodes.DIRECTIVEnode('.BYT \''+value[0]+'\'','lablit'+str(counterN)))
               
               Lcounter = countstart
               while(Lcounter < strlen):
                  if value[Lcounter] == '\\':#escaped character

                     if value[Lcounter+1] == '"':
                        statlabels.append(nodes.DIRECTIVEnode('.BYT \''+value[Lcounter+1]+'\''))
                        Lcounter += 1
                     else:
                        statlabels.append(nodes.DIRECTIVEnode('.BYT \''+value[Lcounter]+value[Lcounter+1]+'\''))
                        Lcounter += 1
                  else:
                     statlabels.append(nodes.DIRECTIVEnode('.BYT \''+value[Lcounter]+'\''))
                  Lcounter += 1
               #for i in range(countstart,strlen):
               #   statlabels.append(nodes.DIRECTIVEnode('.BYT \''+value[i]+'\'',''))

               statlabels.append(nodes.DIRECTIVEnode('.BYT \'\\0\'',''))



         elif typeval == 'char':
            #if len(value) == 0:
            #   statlabels.append(nodes.DIRECTIVEnode('.BYT \'\'','lablit'+str(counterN)))
            #else:
            #dont need to place '' for empty cause without it it still allocates the space but just sets it to zero 
            #in order to not place two characters in one byt

            #need to allow it for \n\r\t and \\ so my assembler can read it in maybe not for \ just change it to \ maybe?
            if value == "'\\''":
               value = "'''"
            elif value == "'\\\"'":
               value = "'\"'"
            elif value == "\\\\":
               #this is becuase my assembler can handle it without the double \\
               value = "\\"

               

            statlabels.append(nodes.DIRECTIVEnode('.BYT '+value,'lablit'+str(counterN)))

            
         elif typeval == 'int':
            statlabels.append(nodes.DIRECTIVEnode('.INT #'+value,'lablit'+str(counterN)))


      node.children.append(nodes.BlockStatement(statlabels))



   def pre_visitMethodDecl(self, node):
      self.stack.append(self.findFunctionST(node.id, self.stack[self.current].name))
      self.currentfunRecord = self.findFunctionActRec(node.id, self.stack[self.current].name)
      self.current += 1
      
   def visitMethodDecl(self, node):
      #pop the scope off
      self.stack.pop()
      self.current -= 1

      node.childN3 = self.nodesStack.pop()
      node.childN2 = self.nodesStack.pop()
      node.childN1 = self.nodesStack.pop()
      self.nodesStack.append(node)
      
   def pre_visitConstructorDecl(self, node):
      self.stack.append(self.findFunctionST(node.id, self.stack[self.current].name))
      self.currentfunRecord = self.findFunctionActRec(node.id, self.stack[self.current].name)
      self.current += 1
      
   def visitConstructorDecl(self, node):
      #pop the scope off
      self.stack.pop()
      self.current -= 1
      node.childN2 = self.nodesStack.pop()
      self.nodesStack.append(node)

   def visitidentifierExpression(self, Node):
      self.nodesStack.append(Node)
      self.regstack.append(Node.value)
      
   def visitASMnode(self, Node):
      self.nodesStack.append(Node)
      self.regstack.append(Node.register)

   def visitMethodBody(self, node):
      #have to reverse sort afterwards
      numChildren = len(node.children)
      node.children = []
      for child in range(numChildren):
         node.children.insert(0,self.nodesStack.pop())
      #node.children.sort(reverse=True)
#ADI label, intial blocks, children

      initialBlocks = []
      for ty, off, isparam in self.currentfunRecord.data.values():
         if not isparam:
            if ty == 'char':
               blockstmt = nodes.BlockStatement([nodes.MOVnode('MOV R2, FP', '', 0), nodes.ADInode('ADI R2, #-'+str(off), '', 0), nodes.LDRRnode('LDR R1, ZERO'),
                                          nodes.STBRnode('STB R1, R2', '', 0)])

            else:
               blockstmt = nodes.BlockStatement([nodes.MOVnode('MOV R2, FP', '', 0), nodes.ADInode('ADI R2, #-'+str(off), '', 0), nodes.LDRRnode('LDR R1, ZERO'),
                                          nodes.STRRnode('STR R1, R2', '', 0)])
               
            initialBlocks.append(blockstmt)



#also make the label for the function
#probably have to support null ?
#if we can maybe make it so literals get their own specific tag along with their value char str int because we could have '0'
      finalblock = nodes.BlockStatement([nodes.ADInode('ADI R3, #0',self.currentfunRecord.parent+'_'+self.currentfunRecord.name), initialBlocks, node.children])
      self.nodesStack.append(finalblock)

   pass








#we have to first create all and store all the labels for literals. then we have to print in reverse order cause we need to have the first instruction be jmp main. maybe we can just have jmp main be the first thing to print
#and then we can just go in order and print functions since we are already jumping to main so we wont run the wrong code
class CodeGenerationVisitor(Visitor):
   #create a different accept for compunit that will accept in the reverse order
   def __init__(self):
      self.outputfile = open('output.asm', 'w')
      
      self.currentfunRecord = None #we dont have to keep a stack i think 
   #when we code generate we will pass it our literal labels record. and for the previsit of compunit printout all the labels either from the object or in constr
   def visitASMnode(self, Node):
      Node.__str__(self.outputfile)


