import twitter #biblioteca oficial tweeter
with open("Dados/tweets.csv", 'w', newline='', encoding="utf-8") as csvfile:

    def auth(): # esta função faz o loguin no api do twitter
        api = twitter.Api(
            consumer_key='NeVqQyK9QaXVNN0dn0lWqkqBI',
            consumer_secret='8o8nPOGfpgSHnoYyay8bmV1kh3A8sVH1VsZNVqTTWCFn23iUBx',
            access_token_key='95677431-LVrBp9FKSDvMHBP6pQCfn2IYqDKGnSQ3GdQmAhF0y',
            access_token_secret='048BtdyxDQ2XILFNubX5FG7bXjOXdUqHmOC6YrY5fRgRf')
        return api


    def get_msg(): # Esta Função é responsavel pela pesquisa
        api = auth() # função de loguin
        response = api.GetSearch(term='covid-19', count=100, lang='pt', result_type='recent')

        results = 0
        for tweet in response:
            results = results + 1 #contador de resultados
            csvfile.write(str(tweet.__getattribute__('text'))) #esta função é responsavel por armazenar os dados no arquivo CSV
            print(tweet.__getattribute__('text'))
        print(results)


    if __name__ == '__main__':
        get_msg()



