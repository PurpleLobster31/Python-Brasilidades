from datetime import datetime, timedelta

class DatasBR():
    def __init__(self):
        self.momento_cadastro = datetime.today()
        
    def __str__(self):
        return self.formata_data()
    
    def mes_cadastro(self):
        meses = {1: 'Janeiro', 2: 'Fevereiro', 3: 'Março',
                 4: 'Abril', 5: 'Maio', 6: 'Junho', 7: 'Julho',
                 8: 'Agosto', 9: 'Setembro', 10: 'Outubro', 
                 11: 'Novembro', 12: 'Dezembro'}
        mes_cadastro = self.momento_cadastro.month
        return meses[mes_cadastro]
    
    def dia_semana_cadastro(self):
        dias = {1: 'Segunda', 2: 'Terça', 3: 'Quarta', 4: 'Quinta',
                5: 'Sexta', 6: 'Sábado', 7: 'Domingo'}
        dia_semana = self.momento_cadastro.isoweekday() #usando isoweekday pq o weekday começa a contar a segunda como 0
        return dias[dia_semana]
    
    def formata_data(self):
        data_cadastro = self.momento_cadastro.strftime("%d/%m/%Y - %H:%M") #converte tipo datetime em string
        return data_cadastro
    
    def tempo_cadastro(self):
        tempo_cadastro = datetime.today() - self.momento_cadastro
        return tempo_cadastro