import pandas as pd 
dir = "/content/commonvoice/cv-corpus-7.0-2021-07-21/th/"
path = "validated.tsv"
train_file= os.path.join(dir,path)
train=pd.read_table(train_file,sep='\t')
#save to csv file
train.to_csv('validated_fullpath.csv',index=False)

train_data = train[['path', 'sentence']].copy()
train_data.to_csv('validated_fullpath_data.csv',index=False)

sum = ""
for index, row in train_data.iterrows():
  temp = '/content/commonvoice/cv-corpus-7.0-2021-07-21/th/clips/'+ row["path"] + '|' + row['sentence'] + '.' + '\n'
  sum += temp

with open('validated_fullpath.txt', 'w') as f:
    f.write(sum)
f.close()