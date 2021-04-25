##Psutil,kivy moduls
import os
#os.environ["KIVY_NO_CONSOLELOG"] = "1"
import psutil
import win32process, win32gui, win32con
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from functools import partial
'''
def callback(hwnd, pid):
  if win32process.GetWindowThreadProcessId(hwnd)[1] == pid:
    win32gui.ShowWindow(hwnd, 0)
win32gui.EnumWindows(callback, os.getppid())
'''
class PsVyApp(App):
    def build(self):
        title = ("PsVy")
        layout = BoxLayout(orientation='vertical')
        #partition = Button(text='Partitions')
        #spinner = Spinner(text = 'Disk Management', values = ('Partitions', 'Partitions_Sizes'))
        spinner_disk = Spinner(text = 'Disk Management', values = ('Partitions','Partitions_Sizes'))
        #network_ifs = Button(text='Networks')
        spinner_networks = Spinner(text = 'Networks', values = ('Network_Cards', 'Network_Addresses'))
        win_services = Button(text='Services')
        users = Button(text='Users')
        #layout.add_widget(partition)
        layout.add_widget(spinner_networks)
        layout.add_widget(spinner_disk)
        #layout.add_widget(network_ifs)
        layout.add_widget(win_services)
        layout.add_widget(users)
        spinner_networks.bind(text=self.spinner_networks_def)
        spinner_disk.bind(text=self.spinner_partitions_def)
        #partition.bind(on_press=lambda x:self.popupevent_partition(None))
        #network_ifs.bind(on_press=lambda x:self.popupevent_network_ifs(None))
        win_services.bind(on_press=lambda x:self.popupevent_win_services(None))
        users.bind(on_press=lambda x:self.popupevent_users(None))
        return layout

    def spinner_networks_def(self,spinner,text):
        if (text == 'Network_Cards'):
            self.popupevent_network_ifs(self)
        if (text == 'Network_Addresses'):
            self.popupevent_network_addr(self)
    def spinner_partitions_def(self,spinner,text):
      if (text == 'Partitions'):
          self.popupevent_partitions(self)
      if (text == 'Partitions_Sizes'):
          self.popupevent_partitions_sizes(self)

    def popupevent_network_addr(self,obj):
        network_addrs = psutil.net_if_addrs()
        layout = BoxLayout(orientation='vertical')
        network_addr_tomb = ''
        for i in network_addrs:
            network_addr_tomb += str(network_addrs.get(i))+'\n'
        szoveg = TextInput(text=network_addr_tomb)
        kilepes = Button(text='Exit')
        layout.add_widget(szoveg)
        layout.add_widget(kilepes)
        popup = Popup(title='Network adresses', content=layout, auto_dismiss=False, size=(400,400))
        kilepes.bind(on_press=popup.dismiss)
        popup.open()
        
    def popupevent_partitions(self,obj):
        disk_information = psutil.disk_partitions()
        layout = BoxLayout(orientation='vertical')
        particiok_tomb = ''
        for i in disk_information:
            particiok_tomb += ' '.join(map(str, i))+'\n'
        szoveg = TextInput(text=particiok_tomb)
        kilepes = Button(text='Exit')
        layout.add_widget(szoveg)
        layout.add_widget(kilepes)
        popup = Popup(title='Partition datas', content=layout, auto_dismiss=False, size=(400, 400))
        kilepes.bind(on_press=popup.dismiss)
        popup.open()

    def popupevent_partitions_sizes(self,obj):
        disk_partitions = psutil.disk_partitions()
        number_of_sizes_disk_partitions = len(list(disk_partitions))-1
        layout = BoxLayout(orientation='vertical')
        partitions_sizes_tomb = ''
        szamlalo = 0
        while szamlalo != number_of_sizes_disk_partitions:
            if disk_partitions[szamlalo][3] == 'cdrom':
                szamlalo+=1
            else:
                partitions_sizes_tomb += str(disk_partitions[szamlalo][1])+ ' ' + str(psutil.disk_usage(disk_partitions[szamlalo][1]))+'\n'
                szamlalo+=1
        kilepes = Button(text='Exit')
        szoveg = TextInput(text=partitions_sizes_tomb)
        layout.add_widget(szoveg)
        layout.add_widget(kilepes)
        popup = Popup(title='Partitions Sizes', content=layout, auto_dismiss=False, size=(400,400))
        kilepes.bind(on_press=popup.dismiss)
        popup.open()
        
    def popupevent_network_ifs(self,obj):
        network_ifs_information = psutil.net_if_stats()
        layout = BoxLayout(orientation='vertical')
        network_ifs_tomb = ''
        for i in network_ifs_information:
            network_ifs_tomb += ' '.join(map(str, i))+'\n'
        szoveg = TextInput(text=network_ifs_tomb)
        kilepes = Button(text='Exit')
        layout.add_widget(szoveg)
        layout.add_widget(kilepes)
        popup = Popup(title='Network Cards', content=layout, auto_dismiss=False, size=(400, 400))
        kilepes.bind(on_press=popup.dismiss)
        popup.open()

    def popupevent_win_services(self,obj):
        win_services_information = list(psutil.win_service_iter())
        layout = BoxLayout(orientation='vertical')
        win_services_tomb = ''
        for i in win_services_information:
            win_services_tomb += ' '.join(str(i))+'\n\n'
        szoveg = TextInput(text=win_services_tomb)
        kilepes = Button(text='Exit')
        layout.add_widget(szoveg)
        layout.add_widget(kilepes)
        popup = Popup(title='Services', content=layout, auto_dismiss=False, size=(400, 400))
        kilepes.bind(on_press=popup.dismiss)
        popup.open()

    def popupevent_users(self,obj):
        users_information = list(psutil.users())
        layout = BoxLayout(orientation='vertical')
        users_tomb = ''
        for i in users_information:
            users_tomb += ' '.join(str(i))+'\n\n'
        szoveg = TextInput(text=users_tomb)
        kilepes = Button(text='Exit')
        layout.add_widget(szoveg)
        layout.add_widget(kilepes)
        popup = Popup(title='Users', content=layout, auto_dismiss=False, size=(400,400))
        kilepes.bind(on_press=popup.dismiss)
        popup.open()
PsVyApp().run()
