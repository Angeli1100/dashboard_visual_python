from dash import *
from pandas.io.formats import style
import plotly.express as px
import pandas as pd
from dash.dependencies import Input,Output
import numpy as np

appName = dash.Dash(__name__)

dataset_1 = pd.read_csv("Assignment_2\Population_by_state_administrative_district_and_sex_2016-2018_Filter.csv")
dataset_2 = pd.read_csv("Assignment_2\Population_by_age_group_sex_and_ethnic_group_2010-2019e_Malaysia.csv")
dataset_3 = pd.read_csv("Assignment_2\Death_by_state_sex_and_age_group_Malaysia_2001-2018.csv")
dataset_4 = pd.read_csv("Assignment_2/Maternal Mortality.csv")
dataset_5 = pd.read_csv("Assignment_2/Number_and_rate_of_Infant_mortality_by_state_and_sex_2010-2018.csv")
dataset_6 = pd.read_csv("Assignment_2\GDP by State 2015 - 2021.csv")
dataset_7 = pd.read_csv("Assignment_2\Infant Mortality.csv")
dataset_8 = pd.read_csv("Assignment_2/Life Expectancy 2010-2021.csv")
dataset_9 = pd.read_csv("Assignment_2\Crude Death Rate in Malaysia 2015-2021.csv")


appName.layout = html.Div(
    [
        html.H1(
            "Simple Dashboard",
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Label("The Greatest Population"),
                        dcc.Dropdown(
                            id="population-dropdown",
                            options=[
                                {"label": "State in 2016", "value": "a1"},
                                {"label": "Gender in 2016", "value": "a2"},
                                {"label": "State in 2017", "value": "a3"},
                                {"label": "Gender in 2017", "value": "a4"},
                                {"label": "State in 2018", "value": "a5"},
                                {"label": "Gender in 2018", "value": "a6"},
                                {"label": "Ethnic Group (2010-2019)", "value": "a7"}
                            ],
                            className="dropdown",
                        ),
                    ]
                ),
                html.Div(
                    [
                        html.Label("The Highest Mortality Rate"),
                        dcc.Dropdown(
                            id="mortality-dropdown",
                            options=[
                                {"label": "State", "value": "b1"},
                                {"label": "Gender", "value": "b2"},
                                {"label": "Etnics Group 2015", "value": "b3"},
                                {"label": "Etnics Group 2016", "value": "b4"},
                                {"label": "Etnics Group 2017", "value": "b5"},
                                {"label": "Etnics Group 2018", "value": "b6"},
                                {"label": "Etnics Group 2019", "value": "b7"},
                                {"label": "Etnics Group 2020", "value": "b8"},
                                {"label": "Etnics Group 2021", "value": "b9"},
                            ],
                            className="dropdown",
                        ),
                    ]
                ),
                html.Div(
                    [
                        html.Label("Life Expectancy, Rate of maternal and infant mortality in Malaysia"),
                        dcc.Dropdown(
                            id="maternal-dropdown",
                            options=[
                                {"label": "Life Expectancy 2010-2021", "value": "f11"},

                                {"label": "Maternal", "value": "f1"},

                                {"label": "Infant", "value": "f2"},
                            ],
                            className="dropdown",
                        ),
                    ]
                  ),
                 html.Div(
                    [
                        html.Label("The State Finest and Worst to live by GDP of State"),
                        dcc.Dropdown(
                            id="states-dropdown",
                            options=[
                                {"label": "GDP in 2015", "value": "c1"},
                                {"label": "GDP in 2016", "value": "c2"},
                                {"label": "GDP in 2017", "value": "c3"},
                                {"label": "GDP in 2018", "value": "c4"},
                                {"label": "GDP in 2019", "value": "c5"},
                                {"label": "GDP in 2020", "value": "c6"},
                                {"label": "GDP in 2021", "value": "c7"},
                            ],
                            className="dropdown",
                        ),
                    ],
                ),
                 html.Div(
                    [
                        html.Label("The state with health and demographics prospects"),
                        dcc.Dropdown(
                            id="health-dropdown",
                            options=[
                                {"label": "Best and Worst", "value": "x1"},
                            ],
                            className="dropdown",
                        ),
                    ]
                  ),
            ],
            className="row",
        ),
        html.Div(dcc.Graph(id="assignment2_plot"), className="chart"), 
    ]
 #className="",
) 

@appName.callback(
    Output("assignment2_plot", "figure"),
    Input("population-dropdown", "value"),
    Input("mortality-dropdown", "value"),
    Input("maternal-dropdown", "value"),
    Input("states-dropdown", "value"),
    Input("health-dropdown","value"),
)
def update_figure(value_1, value_2, value_3, value_4, value_5): #value bertambah ikut callback

#*************************************Graph choice*********************************************************************************************************************************************************************
    fig = px.bar()

    #Question_1
    #Malaysia Greatest Population 2016
    if value_1 =="a1": #ubah ikut question
        filtered_dataset = dataset_1[(dataset_1.State_2016 != value_1)] #ganti by question dan ubah dataset by question
        #By State
        fig = px.bar(
            
            filtered_dataset,
            #ganti pie dan bar untuk names, values, x, y
            x="State_2016",
            y="Population (2016)",
            color="State_2016",
        )

    #By Gender 2016
    if value_1 =="a2":
        filtered_dataset = dataset_1[(dataset_1.Sex_2016 != value_1)]

        fig = px.pie(
            
            filtered_dataset,
            names="Sex_2016",
            values="Population (2016)",
            color = "Sex_2016",
        )

    #Malaysia Greatest Population 2017
    if value_1 =="a3": #ubah ikut question
        filtered_dataset = dataset_1[(dataset_1.State_2017 != value_1)] #ganti by question dan ubah dataset by question
        #By State
        fig = px.bar(
            
            filtered_dataset,
            #ganti pie dan bar untuk names, values, x, y
            x="State_2017",
            y="Population (2017)",
            color="State_2017",
        )

    #By Gender 2017
    if value_1 =="a4":
        filtered_dataset = dataset_1[(dataset_1.Sex_2017 != value_1)]

        fig = px.pie(
            
            filtered_dataset,
            names="Sex_2017",
            values="Population (2017)",
            color = "Sex_2017",
        )

    #Malaysia Greatest Population 2018
    if value_1 =="a5": #ubah ikut question
        filtered_dataset = dataset_1[(dataset_1.State_2018 != value_1)] #ganti by question dan ubah dataset by question
        #By State
        fig = px.bar(
            
            filtered_dataset,
            #ganti pie dan bar untuk names, values, x, y
            x="State_2018",
            y="Population (2018)",
            color="State_2018",
        )

    #By Gender 2018
    if value_1 =="a6":
        filtered_dataset = dataset_1[(dataset_1.Sex_2018 != value_1)]

        fig = px.pie(
            
            filtered_dataset,
            names="Sex_2018",
            values="Population (2018)",
            color = "Sex_2018",
        )

    #Etnics Group
    if value_1 =="a7":
        filtered_dataset = dataset_2[(dataset_2.Ethnic != value_1)]
        
        fig = px.pie(
            filtered_dataset,
            names="Ethnic",
            values="Population (000)",
            color = "Ethnic",
        )

    #Question_2
    #Highest Mortality Group In Malaysia

    #By State
    if value_2 =="b1":
        filtered_dataset = dataset_3[(dataset_3.State != value_2)]
        
        fig = px.pie(
            filtered_dataset,
            names="State",
            values="Number of Death",
            color = "State",
        )
    
    #By Gender/Sex
    if value_2 =="b2":
        filtered_dataset = dataset_3[(dataset_3.Sex != value_2)]
        
        fig = px.pie(
            filtered_dataset,
            names="Sex",
            values="Number of Death",
            color = "Sex",
        )

    #By Etnics Group
    if value_2 =="b3":
        filtered_dataset = dataset_9[(dataset_9.Ethnics != value_2)]
        
        fig = px.bar(
            filtered_dataset,
            x ="Ethnics",
            y ="Year_2015",
            color = "Ethnics",
        )
    
    if value_2 =="b4":
        filtered_dataset = dataset_9[(dataset_9.Ethnics != value_2)]
        
        fig = px.bar(
            filtered_dataset,
            x ="Ethnics",
            y ="Year_2016",
            color = "Ethnics",
        )
    
    if value_2 =="b5":
        filtered_dataset = dataset_9[(dataset_9.Ethnics != value_2)]
        
        fig = px.bar(
            filtered_dataset,
            x ="Ethnics",
            y ="Year_2017",
            color = "Ethnics",
        )
    if value_2 =="b6":
        filtered_dataset = dataset_9[(dataset_9.Ethnics != value_2)]
        
        fig = px.bar(
            filtered_dataset,
            x ="Ethnics",
            y ="Year_2018",
            color = "Ethnics",
        )

    if value_2 =="b7":
        filtered_dataset = dataset_9[(dataset_9.Ethnics != value_2)]
        
        fig = px.bar(
            filtered_dataset,
            x ="Ethnics",
            y ="Year_2019",
            color = "Ethnics",
        )
        
    if value_2 =="b8":
        filtered_dataset = dataset_9[(dataset_9.Ethnics != value_2)]
        
        fig = px.bar(
            filtered_dataset,
            x ="Ethnics",
            y ="Year_2020",
            color = "Ethnics",
        )
    
    if value_2 =="b9":
        filtered_dataset = dataset_9[(dataset_9.Ethnics != value_2)]
        
        fig = px.bar(
            filtered_dataset,
            x ="Ethnics",
            y ="Year_2021",
            color = "Ethnics",
        )
    
#Question 3

    if value_3 =="f11":
        filtered_dataset = dataset_8[(dataset_8.Year != value_3)]
        
        fig = px.pie(
            filtered_dataset,
            names ="Year",
            values ="Life expectancy",
            color = "Year",
        )

    if value_3 =="f1":
        filtered_dataset = dataset_4[(dataset_4.Malaysia != value_3)]
        
        fig = px.pie(
            filtered_dataset,
            names="Malaysia",
            values="Maternal Ratio",
            color = "Malaysia",
        )

    if value_3 =="f2":
        filtered_dataset = dataset_7[(dataset_7.Malaysia != value_3)]
        
        fig = px.bar(
            filtered_dataset,
            x="Malaysia",
            y="Rate on Infant Mortality",
            color = "Malaysia",
        )

    #Question 4
    #Finest and Worst State
    if value_4 =="c1":
        filtered_dataset = dataset_6[(dataset_6.State != value_4)]
        
        fig = px.bar(
            filtered_dataset,
            x="State",
            y="2015",
            color = "State",
        )

    if value_4 =="c2":
        filtered_dataset = dataset_6[(dataset_6.State != value_4)]
        
        fig = px.bar(
            filtered_dataset,
            x="State",
            y="2016",
            color = "State",
        )
    
    if value_4 =="c3":
        filtered_dataset = dataset_6[(dataset_6.State != value_4)]
        
        fig = px.bar(
            filtered_dataset,
            x="State",
            y="2017",
            color = "State",
        )

    if value_4 =="c4":
        filtered_dataset = dataset_6[(dataset_6.State != value_4)]
        
        fig = px.bar(
            filtered_dataset,
            x="State",
            y="2018",
            color = "State",
        )
    
    if value_4 =="c5":
        filtered_dataset = dataset_6[(dataset_6.State != value_4)]
        
        fig = px.bar(
            filtered_dataset,
            x="State",
            y="2019",
            color = "State",
        )
    
    if value_4 =="c6":
        filtered_dataset = dataset_6[(dataset_6.State != value_4)]
        
        fig = px.bar(
            filtered_dataset,
            x="State",
            y="2020",
            color = "State",
        )
    
    if value_4 =="c7":
        filtered_dataset = dataset_6[(dataset_6.State != value_4)]
        
        fig = px.bar(
            filtered_dataset,
            x="State",
            y="2021",
            color = "State",
        )

    #Question 5
    #The best and Worst prospect for Health and Demography
    #Best
    if value_5 =="x1":
        filtered_dataset = dataset_3[(dataset_3.State != value_5)]
        
        fig = px.pie(
            filtered_dataset,
            names ="State",
            values ="Number of Death",
            color = "State",
        ) 


    return fig

if __name__ == "__main__":
    appName.run_server(debug=True)