import pandas as pan
import numpy as np
import sys

df = pan.read_csv("AnimeListToClean.csv")
#df = pan.read_csv("AnimeListTest.csv")
#print(df['title_english'])
#print(df['premiered'])
NotTv = []

genres = []
producers = []
licensors = []
studios = []
seasonKey = {'Spring':0, 'Summer':1, 'Fall':2,'Winter':3}
sourceKey ={}
skIndx = 0;
rkIndx = 0;
ratingKey = {}
sources =[]
ratings = []
print("File has been imported. Beginning preprocessing...")


#print(df)

for index, row in df.iterrows():
    tempSeason = str(row['premiered']).split(" ")[0]
    df.at[index, 'premiered'] = seasonKey.get(tempSeason)
    dur = str(row['duration']).split(" ")[0]
    df.at[index, 'duration'] = dur
    #tempRating = str(row['rating'])
    #if tempRating not in ratingKey:
    #    ratingKey[tempRating] = rkIndx
    #    rkIndx = rkIndx+1
    #df.at[index, 'rating'] = ratingKey.get(tempRating)
    #tempSource = str(row['source'])
    #if tempSource not in sourceKey:
    #    sourceKey[tempSource] = skIndx
    #    skIndx = skIndx+1
    #df.at[index, 'source'] = sourceKey.get(tempSource);
    if row['episodes'] > 500:
        df.at[index, 'episodes'] = 0;
    if row['type'] != 'TV':
        NotTv.append(index)
    elif row['status'] == 'Not yet aired':
        NotTv.append(index)
    if pan.isnull(row['title_english']):
        df.at[index, 'title_english'] = row['title']
    if pan.isnull(row['licensor']):
        df.at[index, 'licensor'] = 'unknown'
    if pan.isnull(row['producer']):
        df.at[index, 'producer'] = 'unknown'
    if pan.isnull(row['studio']):
        df.at[index, 'studio'] = 'unknown'
    tempG = str(row['genre']).split(';')
    for item in tempG:
        tempItem = str(item).split(" ")
        if len(tempItem) == 1:
            item = " "+item
        if str(item)=='nan':
                item = 'unknown'
        if item not in genres:
            genres.append(item)
    tempL = str(row['licensor']).split(';')
    for item in tempL:
        tempItem = str(item).split(" ")
        if len(tempItem) == 1:
            item = " "+item
        if str(item)=='nan':
                item = 'unknown'
        if item not in licensors:
            licensors.append(item)
    tempP = str(row['producer']).split(';')
    for item in tempP:
        tempItem = str(item).split(" ")
        if len(tempItem) == 1:
            item = " "+item
        if str(item)=='nan':
                item = 'unknown'
        if item not in producers:
            producers.append(item)
    tempS = str(row['studio']).split(';')
    for item in tempS:
        tempItem = str(item).split(" ")
        if len(tempItem) == 1:
            item = " "+item
        if str(item)=='nan':
                item = 'unknown'
        if item not in studios:
            studios.append(item)
    tempSource = str(row['source']).split(';')
    for item in tempSource:
        tempItem = str(item).split(" ")
        if len(tempItem) == 1:
            item = " "+item
        if str(item)=='nan':
                item = 'unknown'
        if item not in sources:
            sources.append(item)
    tempRating = str(row['rating']).split(';')
    for item in tempRating:
        tempItem = str(item).split(" ")
        if len(tempItem) == 1:
            item = " "+item
        if str(item)=='nan':
                item = 'unknown'
        if item not in ratings:
            ratings.append(item)

print("Studios = " +str(len(studios)))
print("Licensors = " +str(len(licensors)))
print("Producers = " +str(len(producers)))
print("Genres = " +str(len(genres)))   
assert(0==1)   
#print(genres)    
#print(NotTv)
df = df.drop(df.index[NotTv])
toDrop = ['anime_id', 'title', 'title_japanese', 'title_synonyms', 'members', 'scored_by',
                         'image_url',  'airing', 'type', 'status', 'aired_string', 'aired',
                         'rank', 'popularity', 'favorites', 'background', 'broadcast',
                         'related', 'opening_theme', 'ending_theme']
df = df[df.columns.difference(toDrop)]              
df = df[['title_english', 'score', 
         'premiered', 'episodes',
         'duration', 'rating', 'source',
         'producer', 'licensor', 'studio', 'genre']]

for item in sources:
    name = "Source Material: "+str(item)
    df[name]= pan.Series(0, index=df.index)
for item in ratings:
    name = "Rating: "+str(item)
    df[name]= pan.Series(0, index=df.index)
for item in producers:
    name = "Producer: "+str(item)
    df[name]= pan.Series(0, index=df.index)
for item in licensors:
    name = "Licensor: "+str(item)
    df[name]= pan.Series(0, index=df.index)
for item in studios:
    name = "Studio: "+str(item)
    df[name]= pan.Series(0, index=df.index)
for item in genres:
    name = "Genre: "+str(item)
    df[name]= pan.Series(0, index=df.index)


for index, row in df.iterrows():
    tempG = str(row['genre']).split(';')
    for item in tempG:
        tempItem = str(item).split(" ")
        if len(tempItem) == 1:
            item = " "+item
        if str(item)=='nan':
                item = 'unknown'
        name = "Genre: "+str(item)
        df.at[index, name] = 1
    tempL = str(row['licensor']).split(';')
    for item in tempL:
        tempItem = str(item).split(" ")
        if len(tempItem) == 1:
            item = " "+item
        if str(item)=='nan':
                item = 'unknown'
        name = "Licensor: "+str(item)
        df.at[index, name] = 1
    tempP = str(row['producer']).split(';')
    for item in tempP:
        tempItem = str(item).split(" ")
        if len(tempItem) == 1:
            item = " "+item
        if str(item)=='nan':
                item = 'unknown'
        name = "Producer: "+str(item)
        df.at[index, name] = 1
    tempS = str(row['studio']).split(';')
    for item in tempS:
        tempItem = str(item).split(" ")
        if len(tempItem) == 1:
            item = " "+item
        if str(item)=='nan':
                item = 'unknown'
        name = "Studio: "+str(item)
        df.at[index, name] = 1
    tempSource = str(row['source']).split(';')
    for item in tempSource:
        tempItem = str(item).split(" ")
        if len(tempItem) == 1:
            item = " "+item
        if str(item)=='nan':
                item = 'unknown'
        name = "Source Material: "+str(item)
        df.at[index, name] = 1
    tempRating = str(row['rating']).split(';')
    for item in tempRating:
        tempItem = str(item).split(" ")
        if len(tempItem) == 1:
            item = " "+item
        if str(item)=='nan':
                item = 'unknown'
        name = "Rating: "+str(item)
        df.at[index, name] = 1
    

print("Preprocessing completed. Seperating test data...")
df=df.reset_index(drop=True)
#print(df)
testData = df.sample(n=500)
#print(testData)
sToDrop = []
for index,row in testData.iterrows():
    sToDrop.append(index)
df = df.drop(df.index[sToDrop])
testData=testData.reset_index(drop=True)
df=df.reset_index(drop=True)
testData.to_csv("AnimeListTestingDataWithExtras.csv")

print("Test data saved. Saving training data...")

#print(df['title_english'])
#print(df['premiered'])

#df.to_csv("TestOut.csv")
df.to_csv("AnimeListCleanedWithExtras.csv")
print("Training data saved.")

sys.stdout.close()
#sys.stdout = open("EncodedDataKey.txt","w")
#print("premiered key: ")
#for key, value in seasonKey.items():
#    print(str(key)+" "+str(value))
#print(" ")
#print("rating key: ")
#for key, value in ratingKey.items():
#    print(str(key)+" "+str(value))
#print(" ")
#print("source key: ")
#for key, value in sourceKey.items():
#    print(str(key)+" : "+str(value))
#sys.stdout.close()
exit()






