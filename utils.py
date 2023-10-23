import pandas as pd
import numpy as np

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
        raise Exception("Invaid extension: the extesion must be json or csv")

def concat_df(dataframes, **kwargs):
    order = kwargs["order"] if "order" in kwargs.keys() else None
    df = pd.concat(dataframes, axis=1)
    if order == None:
        return df
    else:
        return df[order]

def to_index_label(df, label_col, index_label_col=None, reference_dictionary=None, rm_nan = True):
    
    index_col_name = f"{label_col}_idx" if index_label_col == None else index_label_col
    if rm_nan:
        df = df.dropna(subset=[label_col])
    index_dict = { k:i for i, k in enumerate(df[label_col].unique()) } if reference_dictionary == None else reference_dictionary

    print(index_dict)  
    
    def l2i(t):
        if pd.isna(t):
            return index_dict["nan"]
        else:
            return index_dict[t]
    
    df[index_col_name] = df[label_col].apply(lambda x: l2i(x))
    
    return df    
    