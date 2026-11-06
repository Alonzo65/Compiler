from ply.yacc import yacc
from compilerLex import tokens
from semStarter import semanticVisitorRunner
from compilerLex import lexer
import sys

from nodes import *
from visitor import *




def p_comp_unit(p):
    'compunit : classdefrest VOID KXI2023 ID LPAREN RPAREN methodbody'
    if p[4] != 'main':
        #identifier or ID must be main if not throw an error
        print('error on line ' + str(p.lineno(4)) + ', ID must be main. ex: kxi2023 main')
        raise SyntaxError
    else:
        p[0] = compUnit(p[1], p[4], p.lineno(4), p[7])
       
def p_classdefrest(p):
    '''classdefrest : empty
                    | classdefinition classdefrest'''
    nData = []
    if len(p) == 3:
        nData.append(p[1])
        for node in p[2]:
            nData.append(node)


    p[0] = nData
   


def p_classdef(p):
    'classdefinition : CLASS ID LCBRACK cmdefs RCBRACK'
   
    p[0] = classDef(p[2], p.lineno(2), p[4])


#helper grammar rule for classdef for kleene star
def p_cmdefs(p):
    '''cmdefs : empty
              | classmemberdef cmdefs'''
    nData = []
    if len(p) == 3:
        nData.append(p[1])
        for node in p[2]:
            nData.append(node)
    p[0] = nData


def p_type(p):
    '''type : VOID
            | INTT
            | CHART
            | BOOL
            | STRINGT'''
   
    p[0] = typeN(p[1], p.lineno(1))


def p_modifier(p):
    '''modifier : PUBLIC
                | PRIVATE'''
    p[0] = modifierN(p[1], p.lineno(1))


def p_class_member_def(p):
    '''classmemberdef : methoddeclaration
                      | datamemberdeclaration
                      | constructordeclaration'''
    p[0] = classMemDef(p[1])
   
def p_data_member_decl(p):
    'datamemberdeclaration : modifier variabledeclaration'
    p[0] = dataMemDecl(p[1], p[2])


def p_method_decl(p):
    '''methoddeclaration : modifier type LRSBRACK ID methodsuffix
                         | modifier type ID methodsuffix
                         | modifier ID LRSBRACK ID methodsuffix
                         | modifier ID ID methodsuffix'''
    if len(p) == 6:
        if type(p[2]) is typeN:
            p[0] = methodDecl(p[1], p[2], True, p[4], p.lineno(4), p[5])
        else:
            p[0] = methodDecl(p[1], typeN(p[2], p.lineno(2)), True, p[4], p.lineno(4), p[5])
    else:
        if type(p[2]) is typeN:
            p[0] = methodDecl(p[1], p[2], False, p[3], p.lineno(3), p[4])
        else:
            p[0] = methodDecl(p[1], typeN(p[2], p.lineno(2)), False, p[3], p.lineno(3), p[4])


def p_constructor_decl(p):
    'constructordeclaration : ID methodsuffix'
    p[0] = constructorDecl(p[1], p.lineno(1), p[2])


def p_initializer(p):
    'initializer : ASSIGNMENT expression'
   
    p[0] = initializer(p[2])


def p_method_suffix(p):
    '''methodsuffix : LPAREN parameterlist RPAREN methodbody
                    | LPAREN RPAREN methodbody'''
   
    if len(p) == 5:
       
        p[0] = methodSuf(p[2], p[4])
    else:
        p[0] = methodSuf(None, p[3])
   


def p_method_body(p):
    '''methodbody : LCBRACK methodrest RCBRACK'''
    p[0] = methodBody(p[2])
   
#helper grammar rule for methodbody
def p_methodrest(p):
    '''methodrest : empty
                  | statement methodrest'''
    nData = []
    if len(p) == 3:
        nData.append(p[1])
        for node in p[2]:
            nData.append(node)
    p[0] = nData


def p_parameter_list(p):
    '''parameterlist : parameter parameterlrest'''
   
    p[0] = parameterList(p[1], p[2])
   
#helper grammar rule for parameterlist
def p_parameterlrest(p):
    '''parameterlrest : empty
                      | COMMA parameter parameterlrest'''
    nData = []
    if len(p) == 4:
        nData.append(p[2])
        for node in p[3]:
            nData.append(node)
    p[0] = nData


def p_parameter(p):
    '''parameter : type LRSBRACK ID
                 | type ID
                 | ID LRSBRACK ID %prec PARA
                 | ID ID %prec PARA'''
   
    if len(p) == 4:
        if type(p[1]) is typeN:
            p[0] = parameter(p[1], True, p[3], p.lineno(3))
        else:
            p[0] = parameter(typeN(p[1], p.lineno(1)), True, p[3], p.lineno(3))
    else:
        if type(p[1]) is typeN:
            p[0] = parameter(p[1], False, p[2], p.lineno(2))
        else:
            p[0] = parameter(typeN(p[1], p.lineno(1)), False, p[2], p.lineno(2))
   
#does lsbrack matter does it mean an array?
def p_variable_decl(p):
    '''variabledeclaration : type LRSBRACK ID initializer SEMICOLON
                           | type LRSBRACK ID SEMICOLON
                           | type ID initializer SEMICOLON
                           | type ID SEMICOLON
                           | ID LRSBRACK ID initializer SEMICOLON %prec VARDEC
                           | ID LRSBRACK ID SEMICOLON
                           | ID ID initializer SEMICOLON
                           | ID ID SEMICOLON '''  
    if len(p) == 6:
        if type(p[1]) is typeN:
            p[0] = varDecl(p[1], True, p[3], p.lineno(3), p[4])
        else:
            p[0] = varDecl(typeN(p[1], p.lineno(1)), True, p[3], p.lineno(3), p[4])
    elif len(p) == 5 and p[2] == '[]':
        if type(p[1]) is typeN:
            p[0] = varDecl(p[1], True, p[3], p.lineno(3), None)
        else:
            p[0] = varDecl(typeN(p[1], p.lineno(1)), True, p[3], p.lineno(3), None)
    elif len(p) == 5:
        if type(p[1]) is typeN:
            p[0] = varDecl(p[1], False, p[2], p.lineno(2), p[3])
        else:
            p[0] = varDecl(typeN(p[1], p.lineno(1)), False, p[2], p.lineno(2), p[3])
    else:
        if type(p[1]) is typeN:
            p[0] = varDecl(p[1], False, p[2], p.lineno(2), None)
        else:
            p[0] = varDecl(typeN(p[1], p.lineno(1)), False, p[2], p.lineno(2), None)
       
def p_statement(p):
    '''statement : LCBRACK statementrest RCBRACK
                 | expression SEMICOLON
                 | IF LPAREN expression RPAREN statement elsestate
                 | WHILE LPAREN expression RPAREN statement
                 | RETURN posexp SEMICOLON
                 | COUT LSHIFT expression SEMICOLON
                 | CIN RSHIFT expression SEMICOLON
                 | SWITCH LPAREN expression RPAREN caseblock
                 | BREAK SEMICOLON
                 | variabledeclaration'''
 
    if p[1] == '{':
        p[0] = curlyBrackStatement(p[2])
    elif p[1] == 'if':
        p[0] = ifStatement(p[3], p[5], p[6], p.lineno(2))
    elif p[1] == 'while':
        p[0] = whileStatement(p[3], p[5], p.lineno(2))
    elif p[1] == 'return':
        p[0] = returnStatement(p[2], p.lineno(1))
    elif p[1] == 'cout':
        p[0] = coutStatement(p[3])
    elif p[1] == 'cin':
        p[0] = cinStatement(p[3], p.lineno(2))
    elif p[1] == 'switch':
        p[0] = switchStatement(p[3], p[5], p.lineno(2))
    elif p[1] == 'break':
        p[0] = breakStatement(p.lineno(1))
    elif len(p) == 3 and p[2] == ';':
        p[0] = expressionStatement(p[1])
    else:
        #variabledeclaration
        p[0] = varDeclStatement(p[1])


#def p_errstatement(p):
#    '''statement : error SEMICOLON'''
#    print('syntax error in expressionstatement')


#helper grammar rule for statement
def p_statementrest(p):
    '''statementrest : empty
                     | statement statementrest'''
    nData = []
    if len(p) == 3:
        nData.append(p[1])
        for node in p[2]:
            nData.append(node)
    p[0] = nData


#helper rule for statement in (else statement)?
def p_elsest(p):
    '''elsestate : empty
                 | ELSE statement'''
   
    if len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = p[1]


#helper rule for return statement
def p_posexp(p):
    '''posexp : empty
              | expression'''
    p[0] = p[1]


def p_case_block(p):
    'caseblock : LCBRACK caserest DEFAULT COLON casestrest RCBRACK'
    p[0] = caseBlock(p[2], p[5])


#caseblock helper grammar rules for Case* and statement*
def p_caserest(p):
    '''caserest : empty
                | case caserest'''
    nData = []
    if len(p) == 3:
        nData.append(p[1])
        for node in p[2]:
            nData.append(node)
    p[0] = nData


def p_casestrest(p):
    '''casestrest : empty
                  | statement casestrest'''
    nData = []
    if len(p) == 3:
        nData.append(p[1])
        for node in p[2]:
            nData.append(node)
    p[0] = nData


#casech is for when we have a char literal representing the case
def p_case(p):
    '''case : CASE INT COLON casest
            | casech'''
    if len(p) == 5:
        p[0] = case(p[2], 'int', p.lineno(2), p[4])
    else:
        p[0] = p[1]


def p_casech(p):
    '''casech : CASE CHAR COLON casest'''
    p[0] = case(p[2], 'char', p.lineno(2), p[4])


#helper grammar rule for case  statement*
def p_casestatementrest(p):
    '''casest : empty
              | statement casest'''
    nData = []
    if len(p) == 3:
        nData.append(p[1])
        for node in p[2]:
            nData.append(node)
    p[0] = nData


def p_expression(p):
    '''expression : LPAREN expression RPAREN
                  | expression ASSIGNMENT expression
                  | expression PLUSASSIGN expression
                  | expression MINUSASSIGN expression
                  | expression MULTASSIGN expression
                  | expression DIVASSIGN expression
                  | expression PLUS expression
                  | expression MINUS expression
                  | expression MULTIPLY expression
                  | expression DIVIDE expression
                  | expression EQUALITY expression
                  | expression NOTEQUAL expression
                  | expression LESSTHAN expression
                  | expression GREATERTHAN expression
                  | expression LTEQUALS expression
                  | expression GTEQUALS expression
                  | expression AND expression
                  | expression OR expression
                  | NOT expression
                  | PLUS expression %prec UPLUS
                  | MINUS expression %prec UMINUS
                  | litint
                  | litchar
                  | litstring
                  | TRUE
                  | FALSE
                  | NULL
                  | chid
                  | NEW type argorindex
                  | NEW ID argorindex
                  | THIS
                  | expperio
                  | exparray
                  | exparg'''
   
    if len(p) == 4 and p[2] == '=':
        p[0] = assignmentExpression(p[1], p[3], p.lineno(2))
    elif len(p) == 4 and p[2] == '+=':
        p[0] = addAssignmentExpression(p[1], p[3], p.lineno(2))
    elif len(p) == 4 and p[2] == '-=':
        p[0] = subAssignmentExpression(p[1], p[3], p.lineno(2))
    elif len(p) == 4 and p[2] == '*=':
        p[0] = multAssignmentExpression(p[1], p[3], p.lineno(2))
    elif len(p) == 4 and p[2] == '/=':
        p[0] = divAssignmentExpression(p[1], p[3], p.lineno(2))
    elif len(p) == 4 and p[2] == '+':
        p[0] = plusExpression(p[1], p[3], p.lineno(2))
    elif len(p) == 4 and p[2] == '-':
        p[0] = minusExpression(p[1], p[3], p.lineno(2))
    elif len(p) == 4 and p[2] == '*':
        p[0] = multExpression(p[1], p[3], p.lineno(2))
    elif len(p) == 4 and p[2] == '/':
        p[0] = divExpression(p[1], p[3], p.lineno(2))
    elif len(p) == 4 and p[2] == '==':
        p[0] = equalityExpression(p[1], p[3], p.lineno(2))
    elif len(p) == 4 and p[2] == '!=':
        p[0] = notEqualExpression(p[1], p[3], p.lineno(2))
    elif len(p) == 4 and p[2] == '<':
        p[0] = lessThanExpression(p[1], p[3], p.lineno(2))
    elif len(p) == 4 and p[2] == '>':
        p[0] = greaterThanExpression(p[1], p[3], p.lineno(2))
    elif len(p) == 4 and p[2] == '<=':
        p[0] = LTEqualsExpression(p[1], p[3], p.lineno(2))
    elif len(p) == 4 and p[2] == '>=':
        p[0] = GTEqualsExpression(p[1], p[3], p.lineno(2))
    elif len(p) == 4 and p[2] == '&&':
        p[0] = andExpression(p[1], p[3], p.lineno(2))
    elif len(p) == 4 and p[2] == '||':
        p[0] = orExpression(p[1], p[3], p.lineno(2))
    elif p[1] == '(':
        p[0] = parenExpression(p[2])
    elif p[1] == '!':
        p[0] = notExpression(p[2], p.lineno(1))
    elif p[1] == '+':
        p[0] = unaryPlusExpression(p[2], p.lineno(1))
    elif p[1] == '-':
        p[0] = unaryMinusExpression(p[2], p.lineno(1))
    elif p[1] == 'true':
        p[0] = trueExpression(p[1], p.lineno(1))
    elif p[1] == 'false':
        p[0] = falseExpression(p[1], p.lineno(1))
    elif p[1] == 'null':
        p[0] = nullExpression(p[1], p.lineno(1))
    elif p[1] == 'this':
        p[0] = thisExpression(p[1], p.lineno(1))
    elif p[1] == 'new':
        if type(p[2]) is str:
            p[0] = newExpression(typeN(p[2], p.lineno(2)), p[3], p.lineno(1))
        else:
            p[0] = newExpression(p[2], p[3], p.lineno(1))
    elif len(p) == 4 and p[2] == '.':
        p[0] = periodExpression(p[1], p[3], p.lineno(3))
    elif len(p) == 3:
        #we have two rules with length of 3, can possible just remove this
        p[0] = p[1]
    else:
        #the rest should be lit int,char,string, and chid
        p[0] = p[1]


#have all three go to one and their left can go to procuction of itself 
def p_expper(p):
    '''expperio : chid PERIOD ID
                | exparray PERIOD ID
                | exparg PERIOD ID
                | THIS PERIOD ID
                | expperio PERIOD ID'''
    
    if type(p[1]) is str:
        p[0] = periodExpression(thisExpression(p[1], p.lineno(1)), p[3], p.lineno(3))
    else:
        p[0] = periodExpression(p[1], p[3], p.lineno(3))

#helper grammar rule for expression
#for now we have ID index which fixes it and then we have expression index to take care of the rest
def p_exparray(p):
    '''exparray : ID index
                | exparg index
                | expperio index'''
    if type(p[1]) is str:
        p[0] = arrayExpression(identifierExpression(p[1], p.lineno(1)), p[2])
    else:
        p[0] = arrayExpression(p[1], p[2])


#error checking for exparray
def p_errexparray(p):
    '''exparray : chid error'''
    print('syntax error in exparray ' + p[1].value)


#helper grammar rule for expression
def p_exparg(p):
    '''exparg : ID arguments
              | expperio arguments'''
    if type(p[1]) is str:
        p[0] = callExpression(identifierExpression(p[1], p.lineno(1)), p[2])
    else:
        p[0] = callExpression(p[1], p[2])
        
    


#expression literals and ID
def p_literalint(p):
    '''litint : INT'''
    p[0] = literalIntExpression(p[1], p.lineno(1))
   
def p_literalchar(p):
    '''litchar : CHAR'''  
    p[0] = literalCharExpression(p[1], p.lineno(1))
   
def p_literalstring(p):
    '''litstring : STRING'''
    p[0] = literalStringExpression(p[1], p.lineno(1))


def p_chid(p):
    '''chid : ID'''
    p[0] = identifierExpression(p[1], p.lineno(1))


#precedence levels
precedence = (
    ('right', 'ASSIGNMENT', 'PLUSASSIGN', 'MINUSASSIGN', 'MULTASSIGN', 'DIVASSIGN'),
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'EQUALITY', 'NOTEQUAL'),
    ('left', 'LESSTHAN', 'GREATERTHAN', 'LTEQUALS', 'GTEQUALS'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE'),
    ('right', 'UPLUS', 'UMINUS', 'NOT'),
    ('nonassoc', 'PARA'),
    ('nonassoc', 'VARDEC'),  
)    


#helper grammar rule for expression new
def p_argorindex(p):
    '''argorindex : arguments
                  | index'''
    p[0] = p[1]


def p_arguments(p):
    '''arguments : LPAREN posarglist RPAREN'''
    p[0] = arguments(p[2], p.lineno(1))
   
#helper grammar rule for arguments
def p_possible_arglist(p):
    '''posarglist : empty
                  | argumentlist'''
    p[0] = p[1]




#kleene (, expression)*

def p_argument_list(p):
    'argumentlist : expression arglistrest'
    p[0] = argumentList(p[1], p[2])
   
#tester helper grammar rule for argumentlist
def p_arglistrest(p):
    '''arglistrest : empty
                   | COMMA expression arglistrest'''
    nData = []
    if len(p) == 4:
        nData.append(p[2])
        for node in p[3]:
            nData.append(node)
    p[0] = nData


def p_index(p):
    '''index : LSBRACK expression RSBRACK'''
    p[0] = index(p[2], p.lineno(1))
   


def p_empty(p):
    'empty :'
    pass


#def p_errindex(p):
#    '''index : error RSBRACK
#             | error LSBRACK expression RSBRACK'''
#    print('syntax error in index')


#rule for emitting tokens that it cannot parse
#def p_unknown(p):
#    'unknown : UNKNOWN'
#    print('Could not parse token ' + str(p[1]) + ' found on line ' + str(p.lineno(1)) + 'and lexing position of ' + str(p.lexpos(1)))




#rule for syntax errors
def p_error(p):
    if p is not None:
        print("Syntax error in input!")
        print('Could not parse token ' + str(p.type) + ' value of ' + str(p.value) +' found on line ' + str(p.lineno) + ' and lexing position of ' + str(p.lexpos))
        #print(parser.token())
        #print(parser.token())
       
        if str(p.type) == 'UNKNOWN':
            print('unkown token with'+ ' value of ' + str(p.value) +' found on line ' + str(p.lineno) + ' and lexing position of ' + str(p.lexpos))


#build parser
parser = yacc(debug=True)



#are we provided a file in the arguments?
#data = open('sequentialtestcase.txt')
#result = parser.parse(data.read())
#lexer.input(data.read())
#result = parser.parse(data.read())
#lexer.input(data.read())

args = len(sys.argv)

if args < 3:
    print('i need a file and a flag')
else:
    filename = sys.argv[1]
    flag = sys.argv[2]
    data = open(filename)

    if flag == '-l':
        lexer.input(data.read())
   
        while True:
            tok = lexer.token()
            if not tok: 
                break      
            print(tok.type, tok.lineno, tok.value)
        for tok in lexer:
            print(tok)
    elif flag == '-p':
        result = parser.parse(data.read())   
        visvar = visitorDot()
        result.accept(visvar)
    elif flag == '-s':
        result = parser.parse(data.read())   
        #visvar = visitorDot()
        #result.accept(visvar)
        STvis = STVisitor()
        result.STaccept(STvis)
        if STvis.errorCounter > 0:
            print('Total errors detected:', STvis.errorCounter)
        else:
            semanticVisitorRunner(result, STvis)
    elif flag == '-c':
        result = parser.parse(data.read())   
        #visvar = visitorDot()
        #result.accept(visvar)
        STvis = STVisitor()
        result.STaccept(STvis)
        semanticVisitorRunner(result, STvis)
        thisvis = TransformThisVisitor(STvis.globalST, STvis.classSTS, STvis.functionSTS)
        result.STaccept(thisvis)

        returnplacevis = ReturnStmtVisitor(thisvis.globalST, thisvis.classSTS, thisvis.functionSTS)
        result.STaccept(returnplacevis)

        breakvis = SimpleBreaksVisitor(thisvis.globalST, thisvis.classSTS, thisvis.functionSTS)
        result.STaccept(breakvis)
        whilevis = WhileVisitor(breakvis.globalST, breakvis.classSTS, breakvis.functionSTS)
        result.STaccept(whilevis)
        swcasesvis = SwCasesVisitor(whilevis.globalST, whilevis.classSTS, whilevis.functionSTS)
        result.STaccept(swcasesvis)
        #visvar = visitorDot()
        #result.accept(visvar)
        expvis = SimpleExpVisitor(swcasesvis.globalST, swcasesvis.classSTS, swcasesvis.functionSTS)
        result.STaccept(expvis)

        boolvis = boolVisitor(expvis.globalST, expvis.classSTS, expvis.functionSTS)
        result.STaccept(boolvis)

        #this one contains a symbol table for literal labels
        litlabvis = literalLabelsVisitor()
        result.STaccept(litlabvis)

        compexpvis = CompExprsVisitor(expvis.globalST, expvis.classSTS, expvis.functionSTS, litlabvis.litlabels)
        result.STaccept(compexpvis)  
        
#dont run the couple ones below ive implmented them all into the one above for better design and implmentation
        #ifsimpvis = ifVisitor(compexpvis.globalST, compexpvis.classSTS, compexpvis.functionSTS, compexpvis.funActiveRecords)
        #result.STaccept(ifsimpvis)

        #funreturnvis = ReturningVisitor(ifsimpvis.globalST, ifsimpvis.classSTS, ifsimpvis.functionSTS, ifsimpvis.funActiveRecords)
        #result.STaccept(funreturnvis)

        #coutcinvis = CoutCinVisitor(funreturnvis.globalST, funreturnvis.classSTS, funreturnvis.functionSTS, funreturnvis.funActiveRecords)
        #result.STaccept(coutcinvis)

        funlabvis = functionsVisitor(compexpvis.globalST, compexpvis.classSTS, compexpvis.functionSTS, compexpvis.funActiveRecords, litlabvis.litlabels)
        result.STaccept(funlabvis)
        #functionsVisitor
        #make sure that functionsvisitor is the last visitor we run before codegenerationvisitor, it changes the structure
        codegenvis = CodeGenerationVisitor()
        result.FINALaccept(codegenvis)
        




if False:#personal error checking
    #symboltable creation visitor
    data = open('basictest.txt')
    result = parser.parse(data.read())
    STvis = STVisitor()
    result.STaccept(STvis)
    print(result)
    
#lexer.input(data.read())
    #result = parser.parse(data.read())
    #check if the vistor errorcounter is more than zero

    #when i create errorchecking visitor pass the symbol tables and in the constructor of visitor immediatly put the global ST onto the stack
    #type checking also means making sure that if staemtns and while statement conditionals have a type bool
    #the only time we have to check for private and public modifiers is when the dot expression is used, since that is the only way to access members of a class which have'
    #a modifier on them, this works for instances of other classes within a class and within main function


    #undeclared variables
    unvis = UndeclaredVisitor(STvis.globalST, STvis.classSTS, STvis.functionSTS)
    result.STaccept(unvis)
    #check if type nodes are a valid type, 
    vtV = ValidTypeVisitor(STvis.globalST, STvis.classSTS, STvis.functionSTS)
    result.STaccept(vtV)
    writeVis = ValidWriteVisitor(STvis.globalST, STvis.classSTS, STvis.functionSTS)
    result.STaccept(writeVis)
    typecheckvis = TypeCheckingVisitor(STvis.globalST, STvis.classSTS, STvis.functionSTS)
    result.STaccept(typecheckvis)
    indexevalvis = IndexEvalVisitor(STvis.globalST, STvis.classSTS, STvis.functionSTS)
    result.STaccept(indexevalvis)

    functionevalvis = FunctionCallVisitor(STvis.globalST, STvis.classSTS, STvis.functionSTS)
    result.STaccept(functionevalvis)
    ifwhilevis = IfWhileCondVisitor(STvis.globalST, STvis.classSTS, STvis.functionSTS)
    result.STaccept(ifwhilevis)
    paramvis = ParameterCheckingVisitor(STvis.globalST, STvis.classSTS, STvis.functionSTS)
    result.STaccept(paramvis)
    switchvis = SwitchCaseVisitor(STvis.globalST, STvis.classSTS, STvis.functionSTS)
    result.STaccept(switchvis)
    returnvis = FunctionReturnVisitor(STvis.globalST, STvis.classSTS, STvis.functionSTS)
    result.STaccept(returnvis)
    visbreak = BreakVisitor(STvis.globalST, STvis.classSTS, STvis.functionSTS)
    result.STaccept(visbreak)
    thisvis = TransformThisVisitor(STvis.globalST, STvis.classSTS, STvis.functionSTS)
    result.STaccept(thisvis)

    returnplacevis = ReturnStmtVisitor(thisvis.globalST, thisvis.classSTS, thisvis.functionSTS)
    result.STaccept(returnplacevis)

    breakvis = SimpleBreaksVisitor(thisvis.globalST, thisvis.classSTS, thisvis.functionSTS)
    result.STaccept(breakvis)
    whilevis = WhileVisitor(breakvis.globalST, breakvis.classSTS, breakvis.functionSTS)
    result.STaccept(whilevis)
    swcasesvis = SwCasesVisitor(whilevis.globalST, whilevis.classSTS, whilevis.functionSTS)
    result.STaccept(swcasesvis)

    expvis = SimpleExpVisitor(swcasesvis.globalST, swcasesvis.classSTS, swcasesvis.functionSTS)
    result.STaccept(expvis)

    boolvis = boolVisitor(expvis.globalST, expvis.classSTS, expvis.functionSTS)
    result.STaccept(boolvis)

    #this one contains a symbol table for literal labels
    litlabvis = literalLabelsVisitor()
    result.STaccept(litlabvis)

    compexpvis = CompExprsVisitor(expvis.globalST, expvis.classSTS, expvis.functionSTS, litlabvis.litlabels)
    result.STaccept(compexpvis)  
    
#dont run the couple ones below ive implmented them all into the one above for better design and implmentation
    #ifsimpvis = ifVisitor(compexpvis.globalST, compexpvis.classSTS, compexpvis.functionSTS, compexpvis.funActiveRecords)
    #result.STaccept(ifsimpvis)

    #funreturnvis = ReturningVisitor(ifsimpvis.globalST, ifsimpvis.classSTS, ifsimpvis.functionSTS, ifsimpvis.funActiveRecords)
    #result.STaccept(funreturnvis)

    #coutcinvis = CoutCinVisitor(funreturnvis.globalST, funreturnvis.classSTS, funreturnvis.functionSTS, funreturnvis.funActiveRecords)
    #result.STaccept(coutcinvis)

    funlabvis = functionsVisitor(compexpvis.globalST, compexpvis.classSTS, compexpvis.functionSTS, compexpvis.funActiveRecords, litlabvis.litlabels)
    result.STaccept(funlabvis)
    visvar = visitorDot()
    result.accept(visvar)
    #functionsVisitor
    #make sure that functionsvisitor is the last visitor we run before codegenerationvisitor, it changes the structure
    codegenvis = CodeGenerationVisitor()
    result.FINALaccept(codegenvis)
        
#call a visitor that partially or fully creates an intermediatary represenatino and print out as output.png
#ensure its simplfied such that it makes sense and would be easy to move onto asm node creations

def testing(fname):
    data = open(fname)
    print(fname)
    result = parser.parse(data.read())
    data.close()
    visvar = visitorDot()
    result.accept(visvar)

    return result
   



