import pandas as pd
import ast

def get_out(list,key):
  new_list=[]
  for i in list:
    new_list.append(i[key])
  return new_list

def clean_it_even(list_char,element):
  for i in list_char:
    element=element.replace(i,"")
  element=element.split(",")
  del element[::2]
  for i in range(len(element)):
    element[i]=element[i].replace("name:","")
  return element

  
def clean_it_odd(list_char,element):
  for i in list_char:
    element=element.replace(i,"")
  element=element.split(",")
  del element[1::2]
  for i in range(len(element)):
    element[i]=element[i].replace("name:","")
  return element


def main():
    df_filmtv=pd.read_csv("filmtvMovies.csv")
    df_credits=pd.read_csv("tmdbCredits.csv")
    df_movies=pd.read_csv("tmdbMovies.csv")

    df_new=df_movies.set_index('id').join(df_credits.set_index('movie_id'),lsuffix='left', rsuffix='right')
    list_of_char=['[',']','{','}','"', " "]
    df_new['genres'] = df_new['genres'].apply(lambda x: clean_it_even(list_of_char,x))
    df_new['production_companies'] = df_new['production_companies'].apply(lambda x: clean_it_odd(list_of_char,x))
    df_new['production_countries'] = df_new['production_countries'].apply(lambda x: clean_it_even(list_of_char,x))
    df_new['cast'] = df_new['cast'].apply(ast.literal_eval)
    df_new['cast_names']=df_new['cast'].apply(lambda x: get_out(x,"name"))
    #these functions haven't been tested in google collab yet below
    df_new['mf_ratio']=df_new['cast'].apply(lambda x: sum(get_out(x,"gender"))/(2*len(x)))
    df_new['gender_lead']=df_new['cast'].apply(lambda x: "male" if x[1]['gender']==2 else "female")
    df_new=df_new.set_index('original_title').join(df_filmtv.set_index('title'),lsuffix='left', rsuffix='right')
    df_new['animation']=df_new['genres'].apply(lambda x: 1 if 'Animation' in x else 0)
    #looking for a way to seperate the words with white space again could be as simple as
    '''
    list_of_char=['[',']','{','}','"']
    def clean_it_even(list_char,element):
  for i in list_char:
    element=element.replace(i,"")
  element=element.split(",")
  del element[::2]
  for i in range(len(element)):
    element[i]=element[i].replace("name:","")
    element[i]=element[i].strip()
  return element


def clean_it_odd(list_char,element):
  for i in list_char:
    element=element.replace(i,"")
  element=element.split(",")
  del element[1::2]
  for i in range(len(element)):
    element[i]=element[i].replace("name:","")
    element[i]=element[i].strip()
  return element

    
    '''

