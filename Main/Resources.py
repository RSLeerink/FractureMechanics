from pandas import DataFrame
import pandas as pd
from numpy import sqrt,pi

#Table 18.2
def CreateMaterialDatabase():
    MaterialData = {    'Material':         ['2024-T351'],
                        'Tougness K_IC':    [34], 
                        'Yield':            [325],
                        'Ultimate':         [470]} 

    #Creates a DataFrame from the provided MaterialData
    MaterialData_df = DataFrame(MaterialData)

    #Sets index to the material property
    MaterialData_df = MaterialData_df.set_index('Material')
    
    #Prints the created DataFrame
    #print(MaterialData_df)

    #Outputs the created data in pickle format
    MaterialData_df.to_pickle("Test_df.pkl")
    

#Table 18.2
def selectMaterial(MaterialData_df,MaterialName):
    #MaterialData_df.loc['2024-T351']
    MaterialData_df = MaterialData_df.loc[MaterialName]
    
    #print(MaterialData_df)
    
    return MaterialData_df

#Table 18.2    
def FractureToughnessMaterials(MaterialName):
    MaterialData_df = pd.read_pickle('Test_df.pkl')
    MaterialProperties = selectMaterial(MaterialData_df,MaterialName)
    print(MaterialProperties)

    """
    [0] = Tougness K_IC []
    [1] = Yield [Mpa]
    [2] = Ultimate [Mpa]
    """
    return MaterialProperties




MaterialName = '2024-T351'
MaterialData_df = pd.read_pickle('Test_df.pkl')

FractureToughnessMaterials(MaterialName)

 #Table 18.3  

def StressIntensityFactors(Pos,sigma,a):
    if Pos == 12:
        K_I  = 1.122*sigma*sqrt(pi*a)
        K_II = 0
    else:
        K_I  = 0
        K_II = 0
    return K_I