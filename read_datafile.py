def read_datafile(data):
    """
    
    :param data: 
    :return:
     
     in order to perform a geological analysis, data must be cleaned and orgonizaed with an specific format. this 
     function read a raw datafile and gathered data for each sample number from different row and write them in one
     row
     
    """
    import numpy as np
    import pandas as pd
    from value_fix import *

    # desired parameters split in two array to avoid missing any feature 
    Column1 = ['sample no', 'sample source', ' rock group',
             'litho name', 'start name', 'drill hole no',
             'drill hole name', 'dh depth from', 'dh depth to',
             'easting gda', 'northing gda', 'zone gda',
             'longitude gda 20', 'latitude gda 20',
             'longitude gda 94', 'latitude gda 94']

    Column2 = ['Ag', 'Al', 'Al2O3', 'As', 'Au', 'B', 'Ba', 'BaO', 'Be', 'Bi',
             'Br', 'C', 'Ca', 'CaCO3', 'CaO', 'CaSO4', 'Cd', 'Ce', 'Cl', 'Co',
             'CO2', 'CO3', 'Cr', 'Cr2O3', 'Cs', 'Cu', 'Dy', 'Er', 'Eu',
             'F', 'Fe', 'Fe2', 'Fe2O3', 'Fe3', 'FeO', 'FeS2', 'Ga', 'Gd',
             'Ge', 'GPSM', 'H2O_minus', 'H2O_plus', 'HCO3', 'Hf', 'Hg',
             'Ho', 'In', 'Insol', 'Ir', 'K', 'K2O', 'La', 'Li', 'LOI', 'Lu',
             'Mg', 'MgCO3', 'MgO', 'Mn', 'MnO', 'Mo', 'Na', 'Na2O', 'NaCl',
             'Nb', 'Nb2O5', 'Nd', 'Ni', 'NiO', 'NO3', 'O18', 'Os', 'P',
             'P2O5', 'Pb', 'Pd', 'Pr', 'Pt', 'Rb', 'Re', 'Rh', 'Ru', 'S',
             'Sb', 'Sc', 'Se', 'Si', 'SiO2', 'Sm', 'Sn', 'SO3', 'SO4', 'Sr',
             'Ta', 'Ta2O5', 'Tb', 'Te', 'Th', 'ThO2', 'Ti', 'TiO2', 'Tl',
             'Tm', 'U', 'U3O8', 'V', 'V2O3', 'V2O5', 'W', 'WO3', 'Y',
             'Yb', 'Zn', 'ZnO', 'Zr']

    ### copy required column from the raw datafile to separate array for a better control over different features
    Cl1 = data.iloc[:, 0]  # sample no
    Cl2 = data.iloc[:, 2]  # sample source
    Cl3 = data.iloc[:, 4]  # rock group
    Cl4 = data.iloc[:, 7]  # litho name
    Cl5 = data.iloc[:, 11]  # start name
    Cl6 = data.iloc[:, 15]  # drill hole no
    Cl7 = data.iloc[:, 16]  # drill hole name
    Cl8 = data.iloc[:, 17]  # dh depth from
    Cl9 = data.iloc[:, 18]  # dh depth to
    Cl10 = data.iloc[:, 20]  # easting gda
    Cl11 = data.iloc[:, 21]  # northing gda
    Cl12 = data.iloc[:, 22]  # zone gda
    Cl13 = data.iloc[:, 23]  # longitude gda 20
    Cl14 = data.iloc[:, 24]  # latitude gda 20
    Cl15 = data.iloc[:, 25]  # longitude gda 94
    Cl16 = data.iloc[:, 26]  # latitude gda 94
    Cl17 = data.iloc[:, 34]  # chem method code
    Cl18 = data.iloc[:, 31]  # .astype('int32').dtypes  # chem code
    Cl19 = data.iloc[:, 32]  # chem value 
    Cl20 = data.iloc[:, 33]  # unit

    ##concatenate these data to a dataframe 
    raw_dataframe = pd.concat(
        [Cl1, Cl2, Cl3, Cl4, Cl5, Cl6, Cl7, Cl8, Cl9, Cl10, Cl11, Cl12, Cl13, Cl14, Cl15, Cl16, Cl17, Cl18, Cl19, Cl20],
        axis=1)
    # since there are different datapoint for a specific sample, raw dataframe must be sorted
    sorted_dataframe = raw_dataframe.sort_values(by='SAMPLE_NO', ascending=True)

    # create the first row unique and save them in a variable sample_no
    sample_no = np.array([])  # ,dtype = 'str')#np.zeros([len(data),1])
    j = 0
    for i in range(1, len(data)):
        # try:
        if i == 1:
            sample_no = np.append(sample_no, sorted_dataframe.iloc[i, 0])
            j += 1
        elif sorted_dataframe.iloc[i, 0] != sorted_dataframe.iloc[i - 1, 0]:
            sample_no = np.append(sample_no, sorted_dataframe.iloc[i, 0])
            j += 1

    # fix the unit of different features
    sorted_dataframe = value_fix(sorted_dataframe)
    Cl_n = Column1 + Column2


    combined_dataframe = pd.DataFrame(np.zeros([len(sample_no), len(Cl_n)]), columns=Cl_n)
    # j=0
    # loop through the dataframe and combine different features into one row

    for j in range(len(sample_no)):
        for i in range(0, len(sorted_dataframe)):  # change to while 
            try:
                if sample_no[j] == sorted_dataframe.iloc[i, 0]:
                    cloc = combined_dataframe.columns.get_loc(sorted_dataframe.iloc[i, 17])
                    combined_dataframe.iloc[j, cloc] = sorted_dataframe.iloc[i, 18]
                    k = i
                    # print (k)

                    while sample_no[j] == sorted_dataframe.iloc[k, 0]:
                        for i1 in range(17):
                            if sorted_dataframe.iloc[i, i1] != 'nan' or sorted_dataframe.iloc[i, i1] != '0':
                                combined_dataframe.iloc[j, i1] = sorted_dataframe.iloc[i, i1]
                                # print ('yes')
                            continue
                        k += 1

            except:  # IndexError:
                pass

        #print(j)

    combined_dataframe['sample no'] = sample_no
    return combined_dataframe