from pandas import DataFrame

#Table 18.2
def FractureToughnessMaterials(MatterialName):
#ToDo


    MaterialData = {    'Material':         ['2024-T351'],
                        'Tougness K_IC':    [34], 
                        'Yield':            [325],
                        'Ultimate':         [470]} 

    MaterialData_df = DataFrame(MaterialData)

    print(MaterialData_df)

    return MaterialData_df 


#Table 18.3
#def 

MatterialName = '2024-T351'

FractureToughnessMaterials(MatterialName)