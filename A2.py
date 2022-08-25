#1.import necessary libraries
import pandas as pd


#2.merge those two csv files (after getting as dataframes, get them as a single dataframe)
import pandas as pd
d1=pd.read_csv("https://raw.githubusercontent.com/Manjupriya77/task_4/main/college_1.csv")
d2=pd.read_csv("https://raw.githubusercontent.com/Manjupriya77/task_4/main/college_2.csv")
df=pd.merge(d1,d2,how='right')
df

#3.consider if the codekata score exceeds 15000 points(present week) then make a csv on those observations as Exceeded expectations.csv
wr=d1[d1.CodeKata_Score>=15000]
wr

#4.if 10000<codekata score<15000 (Reached_expectations.csv)
d1[(d1.CodeKata_Score<=15000) & (d1.CodeKata_Score>=10000)]


#5.if 7000<codekata score<10000 (Needs_Improvement.csv)
d1[(d1.CodeKata_Score<=10000) & (d1.CodeKata_Score>=7000)]


#6.if codekate score < 7000 (Unsatisfactory.csv)
d1[d1.CodeKata_Score<=7000]


#7.Average of previous week geekions vs this week geekions (i.e Previous Geekions vs CodeKata Score)

#8.No of students participated
d1.Name.count()


#9.#Average completion of python course or my_sql or python english or computational thinking

#10.rising star of the week (top 3 candidate who performed well in that particular week)

#11.Shining stars of the week (top 3 candidates who has highest geekions)
d1.groupby(['Name','CodeKata_Score']).size().head(3)



#12.Department wise codekata performence (pie chart)
d3=d1.Department.value_counts()
d3.plot(kind="bar")



#13.Department wise toppers (horizantal bar graph or any visual representations of your choice)
