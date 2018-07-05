# Summation Toolkit
# Author: JJac     Date: 8/14/2017
# Collaboration and references: isbn(9781590282571), isbn(9780716783060)


class Summation():
    def __init__(self, index, limit, expression):
        """Initializes Summation with values index, limit, and expression."""
        self.__index = index
        self.__limit = limit
        self.__expression = expression


    def summation(index, limit):
        """Returns a summation from INDEX(i) to LIMIT(n)"""
        theSum = 0
        for k in range(index, limit + 1):
            theSum = theSum + k
        return theSum


    def summationExpression(index, limit):
        """Returns a summation from INDEX(i) to LIMIT(n) where expression is k"""
        theSum = 0
        for k in range(index, limit +1):
            expression = (3*k) #Manually Enter Expression Here for Now, Next Version expression is external to function
            k = expression
            theSum = theSum + k
        return theSum

    # def getExpression(self):
    #     """Returns the expression of an expression summation"""
    #     return self.__expression
    #
    # def setExpression(self, value):
    #     """Sets the expression to the provided value"""
    #     self.__expression = value
    #
    # def summationExpression2(index, limit, expression):
    #     """Returns a summation from INDEX(i) to LIMIT(n) where expression is k (expression is external to function)"""
    #     theSum = 0
    #     for k in range(index, limit + 1):
    #         expression = expression
    #         k = expression
    #         theSum = theSum + k
    #     return theSum

print(Summation.summationExpression(1,5))
print(Summation.summation(7,405))
#print(Summation.summationExpression2(1,200,((2*k)+5)))