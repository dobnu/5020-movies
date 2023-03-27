# Movie
### Data
The IMBD data is [here](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
  - I unzipped before importing
The filmtv data is [here](https://www.kaggle.com/datasets/stefanoleone992/filmtv-movies-dataset)
  - I checked a few titles and I think joining on title would be pretty successful
### Variables added
- Genres :contains list of multiple genres the film is apart of
- production_companies :which production companies are involved
- production_countries :location of companies
- cast_names :contians list of all actors and actresses names
- mf_ratio :female to male ratio of actors and actresses
- gender_lead :the leads gender
- animation :If the movie is animatied 
### What next
I think if we get a list of 
- [ ] top actors
- [ ] most funny actors
- [ ] most attractive actors
- [ ] actors with their award count
- [ ] movie award count
and combine it with cast or on index we'll have a very interesting set of variables
### Code explained
```
def get_out(list,key):
  new_list=[]
  for i in list:
    new_list.append(i[key])
  return new_list
```
Gets value out of a list of dictionaries
```
def clean_it_even(list_char,element):
  for i in list_char:
    element=element.replace(i,"")
  element=element.split(",")
  del element[::2]
  for i in range(len(element)):
    element[i]=element[i].replace("name:","")
  return element
 ```
 Designed for that weird dictionary format in imdb_movies
 takes in list of charecters you want to get rid of and a string
 iterates over the list of charecters and removes them
 splits element by comma
 deletes ever other element from list created from split
 gets rid of 'name:' in each element of list
 returns list
 and odd does the same but odd instead of even in a list
 
```
list_of_char=['[',']','{','}','"', " "]
```
The bad list of charecters

```
sum(get_out(x,"gender"))/(2*len(x)
```
sum a list of genders (genders in a 1 and 2 context) and then divided by length to get avg and then divided by 2 to get ratio

```
df_new['cast'] = df_new['cast'].apply(ast.literal_eval)
```
converts row to normal python form instead of string


