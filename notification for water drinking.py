import kivy
kivy.require('2.0.0')  # replace with your kivy version

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from plyer import notification
import time

class WaterReminderApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Add a button to trigger the notification
        button = Button(text="Show notification", size_hint=(0.4, 0.4))
        button.bind(on_press=self.show_notification)
        layout.add_widget(button)

        # Add a label to display the notification status
        self.status_label = Label(text="")
        layout.add_widget(self.status_label)

        return layout

    def show_notification(self, *args):
        title = "Water drinking reminder"
        message = "Drink water to stay hydrated!"
        notification.notify(title=title, message=message, app_name='Water Reminder')

        self.status_label.text = "Notification shown!"

    def schedule_notification(self, *args):
        while True:
            now = time.localtime()
            if now.tm_min % 2 == 1:
                self.show_notification()
            time.sleep(60)

if __name__ == '__main__':
    WaterReminderApp().schedule_notification()
