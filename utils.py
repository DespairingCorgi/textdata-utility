import pandas as pd


def open_data(input, cols):
    if isinstance(input, str):
        extension = input.split('.')[-1]
        if extension == 'json':
            data= pd.read_json(input)
        elif extension == 'csv':
            data= pd.read_csv(input)
        else:
            raise Exception("open_data function error: path extension is invalid. the extension must be json or csv")
    elif isinstance(input, pd.DataFrame):
        data=input
    else:
        raise Exception("the input type must be path(str) or Dataframe")
    
    return data[cols]

def save_data(df, path):
    extension = path.split('.')
    if extension == 'json':
        df.to_json(path, index=False)
    elif extension == 'csv':
        df.to_csv(path, index=False)
    else:
        raise Exception("the extesion must be json or csv")