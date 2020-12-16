import requests
import json
import mysql.connector as my
from mysql.connector import Error

def remplir_table_mysql_from_api(numb):
    #etape1: 
    #dict des données 
    id_beer=data_json[numb].get('id',None)
    name=data_json[numb].get('name',None)
    tagline=data_json[numb].get('tagline',None)
    first_brewed=data_json[numb].get('first_brewed',None)
    description=data_json[numb].get('description',None)
    image_url=data_json[numb].get('image_url',None)
    abv=data_json[numb].get('abv',None)
    ibu=data_json[numb].get('ibu',None) 
    target_fg=data_json[numb].get('target_fg',None) 
    target_og=data_json[numb].get('target_og',None)  
    ebc=data_json[numb].get('ebc',None)
    srm=data_json[numb].get('srm',None)
    ph=data_json[numb].get('ph',None)
    attenuation_level=data_json[numb].get('attenuation_level',None)
    volume_unit=data_json[numb].get('volume',None).get('unit',None)
    volume_value=data_json[numb].get('volume',None).get('value',None)
    boil_volume_unit=data_json[numb].get('boil_volume',None).get('unit',None)
    boil_volume_value=data_json[numb].get('boil_volume',None).get('value',None)
    method_fermentation_temp_unit=data_json[numb].get('method',None).get('fermentation',None).get('temp',None).get('unit',None)
    method_fermentation_temp_value=data_json[numb].get('method',None).get('fermentation',None).get('temp',None).get('value',None)
    mash_temp_duration=data_json[numb].get('method',None).get('mash_temp',None)[0].get('duration',None)
    mash_temp_unit=data_json[numb].get('method',None).get('mash_temp',None)[0].get('temp',None).get('unit',None)
    mash_temp_value=data_json[numb].get('method',None).get('mash_temp',None)[0].get('temp',None).get('value',None)
    food_pairing=data_json[numb].get('food_pairing',None)
    contributed_by=data_json[numb].get('contributed_by',None)
    try:
        #connection à la base de données 
        con=my.connect(host='localhost',user='root',passwd='PutYourPassword',db='db')
        cursor=con.cursor()
        #requette sql d'insertion
        sql_query=("insert into beer values({},'{}','{}','{}','{}','{}',{},{},{},{},{},{},{},{},'{}',{},'{}','{}');".format(id_beer,name,tagline,first_brewed,description,image_url,abv,ibu,target_fg,target_og,ebc,srm,ph,attenuation_level,volume_unit,volume_value,description,contributed_by))
        cursor.execute(sql_query)
        #on commit le changement 
        con.commit()
        #au cas ou on recontre une erreur
    except Error as e:
        print(e)
    cursor.close()
    con.close()




if __name__ == "__main__":
    #obtenir les données de l'API avec la méthode get 
    r = requests.get('https://api.punkapi.com/v2/beers')
    #on transforme les données en format json 
    data_json=r.json()
    #print(data_json)
    for numb in range(0,24):
        remplir_table_mysql_from_api(numb)
