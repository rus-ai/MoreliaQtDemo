from os import path
from random import randrange
from PyQt5 import QtWidgets, uic
from faker import Faker


fake = Faker(['ru-RU', 'en_US'])


class ContactItem(QtWidgets.QWidget):
    def __init__(self, contactName, lastMessageText):
        super(ContactItem, self).__init__()
        uic.loadUi(path.join("ui", "ContactItem.ui"), self)
        namesWord = contactName.split(" ")
        self.nameLabel.setText(contactName)
        self.lastmessageLabel.setText(lastMessageText)
        self.ContactAvatar.setText(namesWord[0][0]+namesWord[1][0])
        self.ContactAvatar.setStyleSheet(f"background-color: rgb({randrange(200)},{randrange(200)},{randrange(200)}); ")


class MessageItem(QtWidgets.QWidget):
    def __init__(self, contactName, MessageText, MessageTime):
        super(MessageItem, self).__init__()
        uic.loadUi(path.join("ui", "MessageItem.ui"), self)
        userColor = f"rgb({randrange(200)},{randrange(200)},{randrange(200)}); "
        namesWord = contactName.split(" ")
        self.usernameLabel.setText(contactName)
        self.usernameLabel.setStyleSheet("color: "+userColor)
        self.messageLabel.setText(MessageText)
        self.timeLabel.setText(MessageTime)
        self.ContactAvatar.setText(namesWord[0][0]+namesWord[1][0])
        self.ContactAvatar.setStyleSheet("background-color: "+userColor)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        stileFile = open(path.join("ui", "ChatMain.dark.qss"), 'r')
        self.styleData = stileFile.read()
        stileFile.close()
        self.ui = uic.loadUi(path.join("ui", "ChatMain.ui"), self)
        self.ui.setStyleSheet(self.styleData)
        for count in range(29):
            self.ContactsLayout.addWidget(ContactItem(fake.name(), "..."))
        for count in range(5):
            self.MessageLayout.addWidget(MessageItem(fake.name(), fake.text(), f"00:0{count}"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
