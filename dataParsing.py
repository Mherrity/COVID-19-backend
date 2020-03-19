import pandas as pd
def get_country_data(JHU_Data):
    Data_I_Like=JHU_Data.groupby('Country/Region').sum().reset_index()
    Corona_Date_Columns=Data_I_Like.columns[3:]
    Data_Dict={}
    def make_series(index):
        c_name=Data_I_Like['Country/Region'][index] 
        data=[]
        for column in Corona_Date_Columns:
            data.append(int(Data_I_Like[column][index]))
        Data_Dict[c_name]=data
    [make_series(index) for index in range(len(Data_I_Like))]
    Data_Dict['Day']=[column for column in Corona_Date_Columns]
    # Country_Data=pd.to_DataFrame(Data_Dict)
    # Country_Data['Day']=pd.to_datetime(Country_Data['Day'])
    return Data_Dict
   
#Creating class to hold all of our DataFrames

class DataParser:
    def __init__(self):
        JHU_DATA_URL='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv'
        self.JHU_Data=pd.read_csv(JHU_DATA_URL)
        self.Country_Data=get_country_data(self.JHU_Data)
    

    
        
        
        