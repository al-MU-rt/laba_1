from kivy.config import Config
Config.set('graphics', 'resizable', False)
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import math

class FirstWindow(Screen):
    pass

class SecondWindow(Screen):

    def linear_alg(self):

        if self.ids.a.text != '' and self.ids.x.text != '' and self.ids.c.text != '':
            a = int(self.ids.a.text)
            x = int(self.ids.x.text)
            c = int(self.ids.c.text)

            Y1 = (((a+x)**2)/5) + (((a+c)**3)/2)

            self.ids.result.text = 'Результат: ' + str(Y1)

            self.ids.a.text = ''
            self.ids.x.text = ''
            self.ids.c.text = ''
        else:
            self.ids.result.text = 'Введінь дані!!!'
            self.ids.a.text = ''
            self.ids.x.text = ''
            self.ids.c.text = ''

class ThirdWindow(Screen):
    def branch_alg(self):
        if self.ids.k.text != '' and self.ids.cc.text != '' and self.ids.p.text != '' and self.ids.aa.text != '':
            k = int(self.ids.k.text)
            c = int(self.ids.cc.text)
            p = int(self.ids.p.text)
            a = int(self.ids.aa.text)
            y = 0
            if k*c>p:
                y = (math.sin(c*a))**2
            elif k*c<p:
                y = (math.cos(k*a))**2

            self.ids.result2.text = 'Результат: ' + str(y)

            self.ids.k.text = ''
            self.ids.cc.text = ''
            self.ids.p.text = ''
            self.ids.aa.text = ''
        else:
            self.ids.result2.text = 'Введінь дані!!!'
            self.ids.k.text = ''
            self.ids.cc.text = ''
            self.ids.p.text = ''
            self.ids.aa.text = ''

class FourthWindow(Screen):
    def cycle_alg(self):
        if self.ids.aaa.text != '' and self.ids.b.text != '' and self.ids.pp.text != '' and self.ids.n.text != '':
            a = int(self.ids.aaa.text)
            b = int(self.ids.b.text)
            n = int(self.ids.n.text)
            p = int(self.ids.pp.text)

            f = 0
            result = 1
            for i in range(1, n+1):
                for j in range(1, p+1):
                    prod = ((a**2) + (b**3))
                    result*=prod
                f+=result

            self.ids.result3.text = 'Результат: ' + str(f)

            self.ids.aaa.text = ''
            self.ids.b.text = ''
            self.ids.n.text = ''
            self.ids.pp.text = ''
        else:
            self.ids.result3.text = 'Введінь дані!!!'
            self.ids.aaa.text = ''
            self.ids.b.text = ''
            self.ids.n.text = ''
            self.ids.pp.text = ''

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('Laba__1.kv')

class Laba1App(App):
    def build(self):
        Window.clearcolor = (178/255, 102/255, 1, 1)
        Window.size = (450, 500)
        return kv

if __name__ == "__main__":
    Laba1App().run()