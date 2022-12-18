import pandas as pd
from itertools import repeat

'''def flatten(dataframe, col): 
    new_df = pd.DataFrame(columns = dataframe.columns)
    for row in dataframe.index:
        tmpa = dataframe.loc[row, col]
        for colu in dataframe.columns:
            if colu == col:
                continue
            tmpb = np.ones_like(tmpa, dtype = int)*dataframe.loc[row, colu]
            tmp = pd.DataFrame([tmpa, tmpb]).transpose()
            tmp.columns = [col, colu]
            new_df = pd.concat([new_df, tmp], ignore_index=True)
    return new_df


#new_df = pd.concat(map(pd.Series, dataframe[col]), ignore_index=True).to_frame()
print(a.dtypes)
'''
'''
def flatten(dataframe, col):
    new_df = pd.DataFrame() 
    for row in dataframe.index:
        a = dataframe.loc[row, col]
        if isinstance(a, (list, tuple)):
            la = len(a)
        else:
            la = 1
        for colu in dataframe.columns:
            if colu == col:
                continue
            tmp = pd.DataFrame([a, pd.to_numeric(pd.Series(repeat( dataframe.loc[row, colu], la)))]).transpose()
            print('__________')
            print(tmp)
            pd.concat([new_df, tmp])
            print('______')
            print(new_df)
    new_df.columns = dataframe.columns
    new_df.reset_index(inplace=True)
    for colu in new_df.columns:
        if colu == col:
            continue
        new_df[colu] = new_df[colu].astype(int)
    return new_df
'''
'''
def flatten(dataframe, col):
    data = []
    for row in dataframe.index:
        tmp = dataframe.loc[row, col]
        tmp0 = []
        for colu in dataframe.columns:
            if colu == col:
                tmp0.append(None)
                continue
            tmp0.append(dataframe.loc[row, colu])
        if isinstance(tmp, list):
            for i in tmp:
                tmp1 = list(map(lambda x: x.replace(None, i),tmp0.copy())) 
                data.append(tmp1)
        else:
            tmp1 = tmp0.copy()
            tmp1.insert(tmp0.index(None), i)
            data.append(tmp1)           
    return pd.DataFrame(data, columns=dataframe.columns)
'''
def flatten(dataframe, col):
    idx = dataframe.columns.get_loc(col)
    data = []
    for row in dataframe.index:
        row_tmp = list(dataframe.loc[row])
        if isinstance(row_tmp[idx], list):
            for i in row_tmp[idx]:
                tmp = row_tmp.copy()
                tmp[idx] = i
                data.append(tmp)
        else:
            data.append(row_tmp)
    df_new = pd.DataFrame(data, columns = dataframe.columns)
    for colu in df_new.columns:
        df_new[colu] = df_new[colu].astype(dataframe[colu].dtype)
    return df_new
    

def lilist(a, b):
    return [a, b]


#df
#a = pd.concat(map(pd.Series, df['A']), ignore_index=True).to_frame()
#df['A'] = a
df = pd.DataFrame(data=[[[1, 2],5], [[1, 2, 3], 6], [77, 3]], columns=list('AB'))
a = flatten(df, 'A')
print(a)
print(a.dtypes)
a = pd.concat(map(pd.Series, df['A']))
a
df
flatten(df, 'A')
