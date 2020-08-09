def value_fix(datafile):
    """

    :param datafile:
    :return:

     change the unit of some specific columns
    """


    for i in range(len(datafile)):
        try:
            if datafile.iloc[i, 19] == '%':
                datafile.iloc[i, 18] = str(float(datafile.iloc[i, 18]) * 10000)
            elif datafile.iloc[i, 19] == 'ppb':
                datafile.iloc[i, 18] = str(float(datafile.iloc[i, 18]) * .001)
                # try:
            if "<" in datafile.iloc[i, 18]:
                tmp = list(datafile.iloc[i, 18])
                tmp[0] = '-'

                datafile.iloc[i, 18] = ''.join(tmp)

                # elif ">" in datafile.iloc[i,18]:
        # datafile.iloc[i,18][0] =  float(datafile.iloc[i,18]) * .001
        except ValueError:
            pass
    return datafile