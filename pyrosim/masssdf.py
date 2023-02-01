from pyrosim.commonFunctions import Save_Whitespace


class MASS_SDF: 

    def __init__(self, mass):

        self.mass = mass #could be wrong in mass patch in tips and tricks

        self.string =  '<mass>'+str(mass)+'</mass>'

        self.depth = 4

    def Save(self,f):

        Save_Whitespace(self.depth,f)

        f.write(self.string + '\n' )
