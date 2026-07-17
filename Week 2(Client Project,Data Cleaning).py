import pandas as pd 
import numpy as np
Data= { "Name":["Alice","bob","Charlie","rock"],
        "Age":[23,np.nan,21,24],
        "Roll no":[1,2,3,4]      
}
 
df= pd.DataFrame(Data)
df_clean =df.dropna(subset=["Age"])

print(df_clean)