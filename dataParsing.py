import pandas as pd

def isNaN(num):
    return num!=num


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

def get_state_data(JHU_Data):
    Corona_Date_Columns=JHU_Data.columns[4:]
    Data_Dict={}
    def make_series(index):
        country_name=JHU_Data['Country/Region'][index]
        state_name=JHU_Data['Province/State'][index]
        if country_name[-2:]=='US' and len(state_name)>0:
            c_name=state_name
            data=[]
            for column in Corona_Date_Columns:
                val=JHU_Data[column][index]
                val= 0 if isNaN(val) else val
                data.append(int(val))
            Data_Dict[c_name]=data
    [make_series(index) for index in range(len(JHU_Data))]
    Data_Dict['Day']=[column for column in Corona_Date_Columns]
    return Data_Dict
   
#Creating class to hold all of our DataFrames
class DataParser:
    def __init__(self):
        JHU_DATA_URL='https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv'
        self.JHU_Data=pd.read_csv(JHU_DATA_URL)
        self.Country_Data=get_country_data(self.JHU_Data)
        self.State_Data=get_state_data(self.JHU_Data)
    

    
        
        
        