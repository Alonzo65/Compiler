#dict data    (id,type,lineno,isparameter,)
#id  (type,lineno,isparameter, )

#check if function redturn types as well if so change the tuple info 
#seperate the symboltables for functions/mehtods and classes because the constructors of classes have the same id as the class so when we 
#retrieve a symhbol table it could get the method scope instead of the class scope and vice versa

#before insert call symboltable checkkey to check for duplicates then increment visitor errorcounter else just call insert
#for classes we can just set type to class, for functions we can have a flag called isfunction
class SymbolTable:
    def __init__(self, idname, parentname=''):  #parentname=''
        #id  (type,lineno,isparameter, isfunction)
        self.data = dict()
        self.name = idname
        self.parent = parentname
        #at some point for typechecking or some error checking we need to make sure that the amount of parameters entered into a function match the 
        #functions number of allowed parameters and that the types match and are in the apporpriate order(probably just need to check types which does order as well )
        #need to check modifiers   
    def insert(self, id, typeval, lineno, isarray=False, modifier='', isfunction=False, isparameter=False):
        #print(id,typeval,lineno, isarray, modifier, isfunction, isparameter)
        self.data[id] = (typeval, lineno, isarray, modifier, isfunction, isparameter)

    def checkKey(self, key) -> bool:
        if key in self.data:
            return True
        else:
            return False
        
    def lookup(self, id):
        #if the id doesnt exist when looked up it will return None
        #if the id does exist it returns a tuple of data (type, lineno, isparameter, isfunction)
        return self.data[id]




#every function has a this allocated on except for main.
#need to make functions in the global scope with unique labels  classname_functionname
#scope as well so i can know if i need to access it using an object pointer
#the thing is is that data member accesses are now this.a or this.b so should i just search for these?
#we will need to also insert this expression/id as a symbol that is a parameter in the activation record for methods not main tho
#

#if we return a value our stackpointer will be automatcally pointing at it or itlll 4 bytes ahead, check this!!!!

class ActivationRecord:
    def __init__(self, idname, parentname='', startoff = 4):
        self.data = dict()
        self.paramoffs = []
        self.name = idname
        self.parent = parentname
        self.offset = startoff #first four bytes are for the return address which is computed and added on before/during a function call, the next four is for the PFP or previous frame pointer 
        #have to -minus the offset from fp its easier i think, fp will always point to return address

#so datamembers become dot expressiosn with this on the left side and its id is just id, so i guess just check if the left side of a dot expression is an instance of this expression if so then we know we are accessing data member
    def insert(self, id, typeval, isparam):#if param is false then we know its a local variable
        #what do i do for type of a class? it would be a pointer or reference but how do i store that?
        #what size is a bool
        bytesize = 0
        if not self.checkKey(id):
            if typeval == 'int':
                bytesize = 4
            elif typeval == 'char':
                bytesize = 1
            elif typeval == 'bool':
                #hesaid bool was logical not bitwise so im guessing 4 byes
                bytesize = 4
            else:
                #will be string or class or array so it just needs to store a pointer
                bytesize = 4
                
            self.offset += bytesize
            self.data[id] = (typeval, self.offset, isparam)

    def checkKey(self, key) -> bool:
        if key in self.data:
            return True
        else:
            return False
        
    def lookup(self, id):
        #if the id doesnt exist when looked up it will return None
        #if the id does exist it returns a tuple of data (type, offset, isparam)
        return self.data[id]
    
    def getParOffs(self):
        self.paramoffs = []
        for typeval, off, isparam in self.data.values():
            if isparam:
                self.paramoffs.append(off)
        #self.paramoffs.sort()
        return self.paramoffs
                

        

class LiteralLabels:
    def __init__(self):

        self.data = dict()
#label type bytesize(.BYT or .INT) value

    def insert(self, type, value, counter):
        
        #take out lablit and only use it for when we create asm nodes for the labels directives
        #this way i know what the value is that im storing 
        #maybe do specific tags for the different types like lablitstr or lablitint+value
        #manually input NULLTERM .byt '\0'
        if self.checklab(value):
            pass
        else:
            #global litLabelCounter
            #uniqlab = 'lit_label' + str(litLabelCounter)
            #litLabelCounter += 1
            if type == 'char' or type == 'string':

                self.data[value] = (type, 1, value, counter)
            else:
                self.data[value] = (type, 4, value, counter)

        pass
    def checklab(self, value):
        if value in self.data:
            return True
        else:
            return False
        
        #dont need this
    def findLabel(self, value):
        #have to put lablit for all literals
        for id in self.data:
            typev, bs, val, counter = self.data[id]
            if value == val:
                return self.data[id]
    
    def nullCharSTRAppend(self):
        #append a \0 character to each string
        pass




#we will enter and exit these records using a stack and whenever we enter record
#id, type, byte size, offset, local or param(so we can allocate space in the function or outside, cause outisde call have to allocate paramaters) maybe scope?? offset starts with four becuase the first four, either that or eight depending on how frame pointer starts out
#bytes are meant for returnaddress

#classes will always have its parent be the global scope
#gonna have to make it so post visit of datammemberdeclaration uses its child id to look up the data in the symbol table 
# thenput it back in with the modifier data. 
#message aaron and trina or ali
#the teams message says that you can handle it with a visitor but how?? if we can then we can combine the symboltables into one
#that way i will have just one insert function and wont need to check if im inserting in function ST or class ST 

#we also are gonna have to check in things like the variable declartion if the symobl table in 
# the stack that we are currently at is a class symbol table or function ST so that we make sure that we call
#  its repsective insert with the right parameters.




#st = SymbolTable()
#st.data['foo'] = ('char', 54, True)
#st.data['test'] = ('int', 54, True)
#print(st.data.get('def')) returns None if key doesnt exist
#
#def checkKey(dic, key):
#    if key in dic.keys():
#        print("Present, ", end =" ")
 #       print("value =", dic[key])
  #  else:
   #     print("Not present")
#print(st.data)
#x = ('int', 54, True, False)
#st.insert('y', 'int', 54, True, False)