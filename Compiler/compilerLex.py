#My lex file to generate tokens


from ply.lex import lex






#KEYWORDS


reserved = {
   'bool' : 'BOOL',
   'break' : 'BREAK',
   'case' : 'CASE',
   'class' : 'CLASS',
   'char' : 'CHART',
   'cin' : 'CIN',
   'cout' : 'COUT',
   'default' : 'DEFAULT',
   'else' : 'ELSE',
   'false' : 'FALSE',
   'if' : 'IF',
   'int' : 'INTT',
   'kxi2023' : 'KXI2023',
   'new' : 'NEW',
   'null' : 'NULL',
   'public' : 'PUBLIC',
   'private' : 'PRIVATE',
   'return' : 'RETURN',
   'string' : 'STRINGT',
   'switch' : 'SWITCH',
   'true' : 'TRUE',
   'void' : 'VOID',
   'while' : 'WHILE',
   'this' : 'THIS',
}


tokens = [
   'INT',
   'CHAR',
   'STRING',
   'UNKNOWN',
   'COLON',
   'SEMICOLON',
   'LCBRACK',
   'RCBRACK',
   'LPAREN',
   'RPAREN',
   'LSBRACK',
   'RSBRACK',
   'ASSIGNMENT',
   'EQUALITY',
   'NOTEQUAL',
   'GTEQUALS',
   'LTEQUALS',
   'GREATERTHAN',
   'LESSTHAN',
   'AND',
   'OR',
   'NOT',
   'PLUS',
   'MINUS',
   'MULTIPLY',
   'DIVIDE',
   'PLUSASSIGN',
   'MINUSASSIGN',
   'MULTASSIGN',
   'DIVASSIGN',
   'LSHIFT',
   'RSHIFT',
   'PERIOD',
   'COMMA',
   'ID',  
   'LRSBRACK',
] + list(reserved.values())


#PUNCTUATION
t_COLON = r'\:'
t_SEMICOLON = r'\;'
t_LCBRACK = r'\{'
t_RCBRACK = r'\}'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LSBRACK = r'\['
t_RSBRACK = r'\]'
t_ASSIGNMENT = r'\='
t_EQUALITY = r'\=\='
t_NOTEQUAL = r'\!\='
t_GTEQUALS = r'\>\='
t_LTEQUALS = r'\<\='
t_GREATERTHAN = r'\>'
t_LESSTHAN = r'\<'
t_AND = r'\&\&'
t_OR = r'\|\|'
t_NOT = r'\!'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_PLUSASSIGN = r'\+\='
t_MINUSASSIGN = r'\-\='
t_MULTASSIGN = r'\*\='
t_DIVASSIGN = r'\/\='
t_LSHIFT = r'\<\<'
t_RSHIFT = r'\>\>'
t_PERIOD = r'\.'
t_COMMA = r'\,'


t_CHAR = r'\'[a-zA-Z\" 0-9\:\;\,\<\=\>\?\@\[\]\^\_\{\|\~\`\}\~\*\$\-\+\.\/\!\#\&\%\(\)]\'|\'\\[rnt\\\']\''
t_STRING = r'\"([a-zA-Z \'0-9\:\,\;\<\=\>\?\@\[\]\^\_\{\|\~\`\~\}\*\$\-\+\.\/\!\#\&\%\(\)\]\']|\\[rnt\"\\])*\"'
#t_STRING = r'\"(a-zA-Z| |\r|\n|\t|\"|\')*\"'
t_UNKNOWN = r'.+'


#make sure that it can pick up unprintable characters
#pytest flags for running
#in t_ID will be checking if the string matched is a keyword
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t
   
def t_INT(t):
    r'\d+'
    t.value = int(t.value)  
    return t


#define a [] token also be able to ignore comments within it
def t_LRSBRACK(t):
    r'\[((//[^\r\n]*)*[\r\n]*)*[\s\t]*\]'
    t.value = '[]'
    #print(t.value)
    #print(t)
    return t


def t_comment(t):
    r'//[^\r\n]*'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters
t_ignore  = ' \t'


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex()


#get file name from user
#file = input("Provide a text document with kxi source code: ")
#data = open(file)
#lexer.input(data.read())


#while True:
#    tok = lexer.token()
#    if not tok:
#        break      
#    print(tok.type, tok.lineno, tok.value)


#for tok in lexer:
#    print(tok)





