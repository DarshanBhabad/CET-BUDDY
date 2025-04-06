import streamlit as st
import pandas as pd
import requests
import io
from PIL import Image
image = Image.open('branch_code_img_faded.jpg')

#Page Configurations
st.set_page_config(page_title="CETBUDDY",page_icon="",layout="wide",initial_sidebar_state="expanded")

#Hide the top-right hamburger navbar
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


col_names = ["CETCode",	"College" ,"Location",	"Branch",	"1G",	"1K",	"1R", 	"2AG",	"2AK",	"2AR",	"2BG",	"2BK",	"2BR",	"3AG",	"3AK",	"3AR",	"3BG",	"3BK",	"3BR",	"GM",	"GMK",	"GMR",	"SCG",	"SCK",	"SCR",	"STG",	"STK",	"STR"]
#df = pd.read_csv("https://github.com/VishnuSastryHK/KCETCollegePredictor/blob/master/CET_Database_Final2019.csv", sep='[:,|_()]\s+',names=col_names, header=None, 
#delimiter=',' , engine="python")#)#,sep=r'\s*,\s*', sep="\s+|;|:", error_bad_lines=False)# names=col_names)
#print(df)
url = "https://raw.githubusercontent.com/DarshanBhabad/CET-BUDDY/refs/heads/main/CET_Database_Final2020_DARSHAN.csv?token=GHSAT0AAAAAADBHWSHO3HA6ZERPEMX6OWXMZ7OKYGA" # Make sure the url is the raw version of the file on GitHub
download = requests.get(url).content

# Reading the downloaded content and turning it into a pandas dataframe
df = pd.read_csv(io.StringIO(download.decode('utf-8')))
st.write("Debugging: Available columns →", df.columns.tolist())

df.columns = df.columns.str.strip()  # Trim spaces from column names

#df = pd.read_csv(io.StringIO(download.decode('utf-8')))
#print(df.columns)  # Debugging step

outputdframe = pd.DataFrame(columns = ['Branch', 'College', 'Location', 'CET Code','Cutoff'])
pd.set_option('colheader_justify', 'left')

opdfCheckChance = pd.DataFrame(columns = ['Branch', 'Cutoff','Chances', 'Difference between your rank and Cutoff'])


st.write("""# CETBUDDY""")
st.write("""### Right Analysis and Prediction can lead to Right Choices !!\n Catch the right flight from MHTCET to your dreams """)

st.sidebar.subheader("""Enter the details here 👇""")
rank = st.sidebar.number_input('Enter your Rank*:', min_value=0, value=00, step=1)
rank=int(rank)

st.markdown('<style>' + open('style2.css').read() + '</style>', unsafe_allow_html=True)

Branch_List=st.sidebar.multiselect("Select preferred branch/branches*:",(
"AD",
"AE",                                                                        
"AI",
"AT",
"AU",
"BC",
"BD",
"BE",
"BI",
"BM",
"BT",
"CB",
"CC",
"CE",
"CH",
"CI",
"CO",
"CR",
"CS",
"CT",
"CY",
"DS",
"EC",
"EE",
"EI",
"EN",
"ER",
"ES",
"ET",
"IC",
"IE",
"II",
"IM",
"IO",
"IP",
"IT",
"LC",
"MC",
"MD",
"ME",
"MM",
"MR",
"MT",
"OP",
"PL",
"PT",
"RO",
"SE",
"SS",
"ST",
"TC",
"TX",
"UP",
"UR"))
st.sidebar.text("Scroll down for reference")
category=st.sidebar.selectbox("Select Category:*",("1G", "1K",	"1R",	"2AG",	"2AK",	"2AR",	"2BG",	"2BK",	"2BR",	"3AG",	"3AK",	"3AR",	"3BG",	"3BK",	"3BR",	"GM",	"GMK",	"GMR",	"SCG",	"SCK",	"SCR",	"STG",	"STK",	"STR"), index=15)
District_List=st.sidebar.multiselect("Select to filter by District:",("Pune",
"Nashik",
"Mumbai",
"Nagpur",
"Jalgaon",
"Baramati",
"Nanded",
"Mulund",
"Kurla",
"Kolhapur",
"Amravati",
"Navi Mumbai"



))

input_college=st.sidebar.multiselect("Select Preferred College/Colleges:",(
"COEP",
"VIT",
"VIIT",
"PICT",
"SPIT",
"VJTI",
"KK WAGH",
"RCOEM",
"D. Y. Patil ",
" K.B.S.S College",
"Walchand College of Engineering",
" Sanjivani College of Engineering",
" Amrutvahini College Of Engineering",
"PVGCOET ",
" G. H. Raisoni College of Engineering",
"IIIT",
"Rajarshi Shahu College of Engineering",
"SVKM's Dwarkadas J. Sanghvi College of Engineering",
" Thakur College of Engineering and Technology",
"Vivekanand Education Society's Institute Of Technology",
"Thadomal Shahani Engineering College",
"Vidyalankar Institute of Technology",
"Government College of Engineering,Amravati",
"Terna Engineering College"

))



index_of_category=df.columns.get_loc(category)
Index_Labels_For_Branch=[]


##Code for - List of Colleges in which you can except a seat

for i in Branch_List:
    Index_Labels_For_Branch = df.query("Branch == @i").index.tolist()

    for j in Index_Labels_For_Branch:
        branch = df.iloc[j]['Branch']
        college = df.iloc[j]['College']
        location = df.iloc[j]['Location']
        cetcode = df.iloc[j]['CETCode']

        # Validate if cutoff exists and is numeric
        try:
            cutoff = int(float(df.iloc[j][category]))
        except (ValueError, TypeError, KeyError):  # Handles NaN or invalid values
            continue  # Skip this iteration if cutoff is invalid

        if cutoff != 0:
            rank = int(rank)

        if len(District_List) > 0:
            for k in District_List:
                if k in location and rank < cutoff:
                    new_row = pd.DataFrame([{
                        'Branch': branch,
                        'College': college,
                        'Location': location,
                        'CET Code': cetcode,
                        'Cutoff': cutoff
                    }])
                    outputdframe = pd.concat([outputdframe, new_row], ignore_index=True)
        else:
            if rank < cutoff:
                new_row = pd.DataFrame([{
                    'Branch': branch,
                    'College': college,
                    'Location': location,
                    'CET Code': cetcode,
                    'Cutoff': cutoff
                }])
                outputdframe = pd.concat([outputdframe, new_row], ignore_index=True)

            

outputdframe=outputdframe.sort_values(['Cutoff'], ascending = True,ignore_index=True) 

df2=outputdframe.style.set_properties(**{'text-align': 'left'}).set_table_styles([dict(selector='th', props=[('text-align', 'left')])])


if(len(Branch_List)>0):
    st.text("\n\n")
    st.write("##### List of Colleges in which you can except a seat:")
    st.markdown('<style>' + open('style.css').read() + '</style>', unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    st.text("      ")
    st.markdown('<style>' + open('style2.css').read() + '</style>', unsafe_allow_html=True)
    st.markdown('<style>div[title="OK"] { color: green; } div[title="KO"] { color: red; } .data:hover{ background:rgb(243 246 255)}</style>', unsafe_allow_html=True)
    st.dataframe(df2)


##Code for - Check your chances of getting into the preferred collges:


if(len(input_college)>0):
    st.text("\n")
    st.text("\n")
    st.text("                        ")
    st.text("                        ")
    st.text("                        ")
    st.write("##### Check your chances of getting into the preferred colleges:")
    st.markdown('<style>' + open('style.css').read() + '</style>', unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    listOfUnavailableBranches=[]
    listOfUnavailableBranchesForCategory=[]

    for i in input_college:
       
        lst=df.loc[(df['College']==i),'Branch'].tolist()
        #st.write(lst)

        for j in Branch_List:

            if(j in lst):
                cutoff1=df.loc[(df['College']==i) & (df['Branch'] == j),category]
                cutoff1=int(cutoff1)
                #st.write(cutoff1)
                
                if(cutoff1!= 0):
                    
                    if(rank<cutoff1):
                        string=int(cutoff1-rank);#+ "   ;   Rank < Cutoff"
                        opdfCheckChance = opdfCheckChance.append({'Branch' : j,  'Cutoff' : cutoff1,'Chances' : 'High', 'Difference between your rank and Cutoff' : string }, ignore_index = True) 
                    else:
                        string=int(-rank+cutoff1);#+"   ;   Rank > Cutoff"
                        opdfCheckChance = opdfCheckChance.append({'Branch' : j,  'Cutoff' : cutoff1,'Chances' : 'Low', 'Difference between your rank and Cutoff' : string}, ignore_index = True) 
                else:
                    listOfUnavailableBranchesForCategory.append(j)
                    #st.write(listOfUnavailableBranchesForCategory)
            else:
                listOfUnavailableBranches.append(j)
 
    
        st.write("####", i,":")
        st.text("\n")
        lenOfListOfUnavailableBranches=len(listOfUnavailableBranches)

        lenOfListOfUnavailableBranchesForCategory=len(listOfUnavailableBranchesForCategory)

        joined_list1 = ", ".join(listOfUnavailableBranches)
        joined_list2 = ", ".join(listOfUnavailableBranchesForCategory)
    
        if((lenOfListOfUnavailableBranches)>0):
            if(lenOfListOfUnavailableBranches==1):
               st.write("This college doesn't offer ",joined_list1,"branch")
                
            else:
                st.write("This college doesn't offer ",joined_list1," branches")
        
            listOfUnavailableBranches=[]

        if((lenOfListOfUnavailableBranchesForCategory)>0):
            if(lenOfListOfUnavailableBranchesForCategory==1):
               st.write(joined_list2,"branch is not available for this cateory")
                
            else:
                st.write(joined_list2," branches are not available for this category")
        
            listOfUnavailableBranchesForCategory=[]    
        
        df2=opdfCheckChance.style.set_properties(**{'text-align': 'left'}).set_table_styles([dict(selector='th', props=[('text-align', 'left')])])
            
        if(opdfCheckChance.shape[0]>0):
            st.dataframe(df2)
            #Code for the Line Chart
            for i in range(1):
                opdfCheckChance_copy=opdfCheckChance.copy(deep=True)
                opdfCheckChance_copy['Rank']=opdfCheckChance_copy['Cutoff']-opdfCheckChance_copy['Difference between your rank and Cutoff']
                chart_data=pd.DataFrame(opdfCheckChance_copy[['Cutoff','Rank']])
                if(chart_data.shape[0]>1):
                    st.line_chart(chart_data)
            st.text("\n\n\n")
            opdfCheckChance=opdfCheckChance[0:0]

        


##Code for - Option Entry / Preference List


import pandas as pd

def generateOptionEntry():
    outputdframe = pd.DataFrame(columns=['Branch', 'College', 'Location', 'CET Code', 'Cutoff'])
    count_rows = 0

    for i in Branch_List:
        Index_Labels_For_Branch = df.query("Branch == @i").index.tolist()

        for j in Index_Labels_For_Branch: 
            branch = df.iloc[j]['Branch']
            college = df.iloc[j]['College']
            location = df.iloc[j]['Location']
            cetcode = df.iloc[j]['CETCode']

            # Validate if cutoff exists and is numeric
            try:
                cutoff = int(df.iloc[j][category])
            except (ValueError, TypeError):  # Handles NaN or invalid values
                continue  # Skip this iteration if cutoff is invalid

            if cutoff != 0:
                rank = int(rank)  # Ensure rank is converted to int

            if len(District_List) > 0:
                for k in District_List:
                    if k in location:
                        if rank < cutoff:
                            new_row = pd.DataFrame([{
                                'Branch': branch,
                                'College': college,
                                'Location': location,
                                'CET Code': cetcode,
                                'Cutoff': cutoff
                            }])
                            outputdframe = pd.concat([outputdframe, new_row], ignore_index=True)
                            count_rows += 1
            else:
                if rank < cutoff:
                    new_row = pd.DataFrame([{
                        'Branch': branch,
                        'College': college,
                        'Location': location,
                        'CET Code': cetcode,
                        'Cutoff': cutoff
                    }])
                    outputdframe = pd.concat([outputdframe, new_row], ignore_index=True)
                    


    outputdframe=outputdframe.sort_values(['Cutoff'], ascending = True,ignore_index=True) 

    
    df2=outputdframe.style.set_properties(**{'text-align': 'left'}).set_table_styles([dict(selector='th', props=[('text-align', 'left')])])
    df2.set_properties(subset=["Branch", "Location"],**{'text-align': 'left'}).hide_index()
   

    
    if(len(Branch_List)>0):
        st.text("\n")
        st.text("\n")
        st.text("                        ")
        st.text("                        ")
        st.write("##### Here is your Option Entry / Preference List:")
        st.markdown('<style>' + open('style.css').read() + '</style>', unsafe_allow_html=True)
        st.markdown("<hr>", unsafe_allow_html=True)
        st.text("\n")
        st.dataframe(df2)



st.markdown('<style>' + open('style.css').read() + '</style>', unsafe_allow_html=True)

button=st.sidebar.button("Generate Option Entry / Preference List")
if(button==True):
    generateOptionEntry()

st.text("\n")
st.text("\n")
st.text("Note: The predictions made in this app are purely based on MHT CET CUTOFFS - Second Extended\nRound Cutoff Data.")
st.text("\n")
st.text("Copyrights Reserved ©")
st.text("For any queries, drop in an email to us at dbhabad69@gmail.com")
st.text("\n")
st.text("\n")
st.write("[Click Here](https://drive.google.com/file/d/1Dz4ujeNT7z4cWF90UJznM84OFK-CgXxN/view?usp=sharing)for more information about colleges")
st.sidebar.text("\n")
st.sidebar.text("Branch Codes for Reference:")
#streamlit run KCETCollegePredictor.py
#https://raw.githubusercontent.com/DarshanBhabad/CET-BUDDY/refs/heads/main/CET_Database_Final2020_DARSHAN.csv?token=GHSAT0AAAAAADBHWSHOEKGUARPV5FLPWR2GZ7OIVYQ
#https://github.com/VishnuSastryHK/KCETCollegePredictor/raw/master/CET_Database_Final2020.csv
