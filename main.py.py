from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.graphics import Ellipse,Color,Line
from kivy.uix.button import Button
import random
#RGBA
Window.clearcolor=(0,0,0,1)

class PaintWindow(Widget):
    def on_touch_down(self, touch):
        colorR = random.randint(0,255)
        colorG = random.randint(0,255)
        colorB = random.randint(0,255)
        self.canvas.add(Color(rgb=(colorR/255,colorG/225,colorB/255)))
        d=30
        self.canvas.add(Ellipse(pos=(touch.x-d/2,touch.y-d/2), size=(d,d)))
        touch.ud['line']=Line(points=(touch.x,touch.y))
        self.canvas.add(touch.ud['line'])

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x,touch.y]
#Root window = Paint Window +Button
class PaintApp(App):
    def build(self):
        rootWindow = Widget()
        self.painter = PaintWindow()
        clearBtn = Button(text='clear')
        clearBtn.bind(on_release=self.clear_canvas)
        rootWindow.add_widget(self.painter)
        rootWindow.add_widget(clearBtn)
        return rootWindow

    def clear_canvas(self,obj):
        self.painter.canvas.clear()


PaintApp().run()

# 1) Changing background colour
# 2) on_touch_down
# 3) Color
# 4) Drawing a circle/elipse