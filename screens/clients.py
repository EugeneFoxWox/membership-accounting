from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import SlideTransition
import gspread

class Clients(Screen):

    def logout(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'welcome'

     def id_client_list(self):
        id = '' # Тут ID таблицы
        gs = gspread.service_account(filename='fileapi.json')
        sh = gs.open_by_key(id)
        worksheet = sh.sheet1
        client_list = worksheet.get_all_records()
        return client_list
      
      
    def id_abonement_list(self):
        id = '' #Тут ID таблицы
        gs = grspread.service_account(filename='fileapi.json')
        sh = gs.open_by_key(id)
        worksheet = sh.get_worksheet(1)
        abonement_list = worksheet.get_all_records()
        return abonement_list

   
