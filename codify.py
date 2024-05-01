from textx import metamodel_from_file
codify_meta = metamodel_from_file(r'c:\Users\Xavie\OneDrive\ClassesOne\3rdyear2ndsem\CS420\Final\codify.tx')
codify_model = codify_meta.model_from_file(r'c:\Users\Xavie\OneDrive\ClassesOne\3rdyear2ndsem\CS420\Final\exampletwo.codify')

class codify:
    def __init__(self):
        self.state = dict()
    
    def varmap(self, targetVar):
        if targetVar.isidentifier():
            if targetVar in self.state:
                return self.state[targetVar]
            else:
                raise ValueError("Error: Var not found")
        else:
            return int(targetVar)

    def assignVarInt(self, var, expression):
        self.state[var] = expression

    def assignVarString(self, var, expression):
        self.state[var] = expression

    def assignVarCalc(self, var, expression):
        self.state[var] = self.computeExpression(expression)

    def computeExpression(self, valExpression):
        if '+' in valExpression:
            leftSide, rightSide = valExpression.split('+')
            return self.computeExpression(leftSide) + self.computeExpression(rightSide)
        elif '-' in valExpression:
            leftSide, rightSide = valExpression.split('-')
            return self.computeExpression(leftSide) - self.computeExpression(rightSide)
        elif '*' in valExpression:
            leftSide, rightSide = valExpression.split('*')
            return self.computeExpression(leftSide) * self.computeExpression(rightSide)
        elif '/' in valExpression:
            leftSide, rightSide = valExpression.split('/')
            return self.computeExpression(leftSide) / self.computeExpression(rightSide)
        elif '%' in valExpression:
            leftSide, rightSide = valExpression.split('%')
            return self.computeExpression(leftSide) % self.computeExpression(rightSide)
        else:
            return self.varmap(valExpression)
    
    def printvar(self, var):
        try:
            val = self.varmap(var)
            print(val)
        except:
            print("Error: Var not found")

    def printstring(self, string):
        print(string)
    
    def loop(self, booltobe, statements):
        boolexpression = eval(booltobe, self.state)
        while not (boolexpression):
            self.interpreter(statements)
            boolexpression = eval(booltobe, self.state)
    
    def ifstatement(self, booltobe, statements):
        boolexpression = eval(booltobe, self.state)
        if boolexpression:
            self.interpreter(statements)

    def ifelsestatement(self, booltobe, statements):
        boolexpression = eval(booltobe, self.state)
        if boolexpression:
            self.interpreter(statements.Ifbody)
        else:
            self.interpreter(statements.Elsebody)

    

    def interpreter(self, model):
        for line in model.statements:
            if line.__class__.__name__ == "intAssignment":
                self.assignVarInt(line.variable, line.val)
            if line.__class__.__name__ == "stringAssignment":
                self.assignVarString(line.variable, line.val)
            if line.__class__.__name__ == "calcAssignment":
                self.assignVarCalc(line.variable, line.expression)
            if line.__class__.__name__ == 'printvar':
                self.printvar(line.variable)
            if line.__class__.__name__ == 'printstring':
                self.printstring(line.string)
            if line.__class__.__name__ == 'loop':
                self.loop(line.bool, line)
            if line.__class__.__name__ == 'if':
                self.ifstatement(line.bool, line)    
            if line.__class__.__name__ == 'ifelse':
                self.ifelsestatement(line.bool, line)        

codify1 = codify()
codify1.interpreter(codify_model)


