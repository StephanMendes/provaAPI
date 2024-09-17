import requests

def get_clima_api(api_key, city):
    urlBase = "https://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{urlBase}appid={api_key}&q={city}"

    reponse = requests.get(complete_url)
    
    return reponse.json()


def get_clima(nomeCidade):
    api_key = "30a52cc83bf321f85a056e3b6a785c48"
    clima_data = get_clima_api(api_key, nomeCidade)
    
    
    
    if clima_data["cod"] == 401:
        print('Problema durante a requisição!\n'
              f'Mensagem: {clima_data['message']}')
    elif clima_data["cod"] != 404:
        main_weather = clima_data["weather"][0]["main"]
        temperature = clima_data["main"]["temp"] 
        
        print(f"Clima em {nomeCidade}: {main_weather}")
        print(f"Temperatura: {temperature - 273.15:.2f}°C")
        
        
    else:
        print("Cidade não encontrada!")    