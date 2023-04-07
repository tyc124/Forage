import pandas as pd

reaction_db = pd.read_csv('C:/Users/fanca/Desktop/CS/Forage/Accenture/Reactions.csv')
types_db = pd.read_csv('C:/Users/fanca/Desktop/CS/Forage/Accenture/ReactionTypes.csv')
content_db = pd.read_csv('C:/Users/fanca/Desktop/CS/Forage/Accenture/Content.csv')

#clean the rows with missing values
content_db = content_db.dropna(how='any', axis=0)
reaction_db = reaction_db.dropna(how='any', axis=0)
types_db = types_db.dropna(how='any', axis=0)

for s in content_db['Category']:
    s.replace('"', '') #some data is written with "" -> make it consistent


#select the columns per needs only
content_db.rename(columns = {'Type': 'Content Type'}, inplace=True)
content_db = content_db[['Unnamed: 0', 'Content ID', 'Content Type', 'Category']]
reaction_db.rename(columns = {'Type': 'Reaction Type'}, inplace=True)
reaction_db = reaction_db[['Unnamed: 0', 'Content ID', 'Reaction Type', 'Datetime']] #keep datetime for traceability


#merge the datasets
cleaned = pd.merge(reaction_db, content_db, how='outer')
cleaned = pd.merge(cleaned, types_db, how='outer')
#print(cleaned)

#show the top 5 categories
print(cleaned['Category'].value_counts())
#travel, science, culture, fitness, animals

#save the result
cleaned.to_csv(r'C:/Users/fanca/Desktop/CS/Forage/Accenture/result.csv', index=None, header=True)
