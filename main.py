from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout

class Test(BoxLayout) :
	pass
	
class MyApp(MDApp) :
    def build(self) :
        return Test()
        
MyApp().run()