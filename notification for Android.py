import kivy
kivy.require('0.11.1')  # replace with your kivy version

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from plyer import notification


class MyNotificationApp(App):
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
        title = "My Notification Title"
        message = "This is my notification message!"
        notification.notify(title=title, message=message, app_name='My App Name')

        self.status_label.text = "Notification shown!"


if __name__ == '__main__':
    MyNotificationApp().run()
