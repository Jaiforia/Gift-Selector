from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QObject, QPointF, QPropertyAnimation, pyqtProperty, QParallelAnimationGroup, QSequentialAnimationGroup)
import sys, random

class CustomDialog(QDialog):

    def __init__(self, *args, **kwargs):
        #Pop Up Window for instructions
        super(CustomDialog, self).__init__(*args, **kwargs)
        
        self.setWindowTitle("Instructions")
        self.resize(650, 350)

        font = QtGui.QFont()
        font.setFamily("Goudy Old Style")
        font.setPointSize(12)
        self.gameInstructions = QtWidgets.QLabel()
        self.gameInstructions.setGeometry(QtCore.QRect(60, 70, 200, 200))
        self.gameInstructions.setFont(font)
        self.gameInstructions.setAlignment(QtCore.Qt.AlignCenter)
        self.gameInstructions.setWordWrap(True)
        self.gameInstructions.setObjectName("gameInstructions")
        self.gameInstructions.setText("Wishing You a very Happy Birthday!! :)\n"
                                      "Are you curious to know your birthday gift??\n"
                                      "Even if not I am very curious as to what will I have to give you.\n"
                                      "Confused? Worry Not. Let me help you."
                                      " The next window displays the gifts that I had in my mind."
                                      " Your task is to select any one of the box and choose your gift.\n"
                                      "But WAIT!!! If only it was that simple I would not have build this.\n"
                                      "The twist in the tale is after you click on start the gifts will be hidden and the boxes will be SHUFFLED!!!"
                                      "So basically its not you deciding your gift instead it is your luck doing it for you.\n"
                                      "What say?? Interesting right."
                                      "Without further delay let's begin. Click on begin to continue.\n"
                                      "NOTE: Please send me screenshot of your GIFT since I am not sending the data to myself."
                                      )
        
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.button(QDialogButtonBox.Ok).setText("Begin")
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.gameInstructions)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

class Ui_GiftSelector(object):
    def onStartInstructions(self, GiftSelector):
        #print(self," ",GiftSelector)
        window = CustomDialog(GiftSelector)
        if window.exec_():
            self.setupUi(GiftSelector)
        else:
            sys.exit(app.exec_())
    def setupUi(self, GiftSelector):
        GiftSelector.setObjectName("GiftSelector")
        GiftSelector.resize(970, 640)
        num = ['One', 'Two', 'Three']

        #Gift Box Container Settings
        self.centralwidget = QtWidgets.QWidget(GiftSelector)
        self.centralwidget.setObjectName("centralwidget")
        self.giftContainer = QtWidgets.QGroupBox(self.centralwidget)
        self.giftContainer.setEnabled(True)
        self.giftContainer.setGeometry(QtCore.QRect(60, 40, 880, 530))
        self.giftContainer.setTitle("")
        self.giftContainer.setObjectName("giftContainer")
        
        #Gift Box Top Image
        self.giftContainer.giftBoxTopIm = QPixmap('GiftBoxTop.png')
        x=100        
        for gift in num:
            giftBoxTop = QtWidgets.QLabel(self.giftContainer)
            giftBoxTop.setPixmap(self.giftContainer.giftBoxTopIm)
            giftBoxTop.setGeometry(QtCore.QRect(x, 00, 160, 100))
            giftBoxTop.setObjectName("giftBox" + gift + "Top")
            setattr(self, 'giftBox' + gift + 'Top', giftBoxTop)
            x+=260

        #Gift Box Bottom Image
        self.giftContainer.giftBoxBaseIm = QPixmap('GiftBoxBase.png')
        x=100        
        for gift in num:
            giftBoxBase = QtWidgets.QLabel(self.giftContainer)
            giftBoxBase.setPixmap(self.giftContainer.giftBoxBaseIm)
            giftBoxBase.setGeometry(QtCore.QRect(x, 180, 155, 100))
            giftBoxBase.setObjectName("giftBox" + gift + "Base")
            setattr(self, 'giftBox' + gift + 'Base', giftBoxBase)
            x += 260

        #Font and Label Setting
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(13)
        x=120        
        for gift in num:
            giftNum = QtWidgets.QLabel(self.giftContainer)
            giftNum.setGeometry(QtCore.QRect(x, 100, 120, 80))
            giftNum.setFont(font)
            giftNum.setAlignment(QtCore.Qt.AlignCenter)
            giftNum.setWordWrap(True)
            giftNum.setObjectName("gift" + gift)
            giftNum.setStyleSheet("color:rgb(255,0,0)")
            setattr(self, 'gift' + gift, giftNum)
            x += 260

        #Gift Opening Button
        x=100        
        for gift in num:
            giftOpenBt = QtWidgets.QPushButton(self.giftContainer)
            giftOpenBt.setGeometry(QtCore.QRect(x, 320, 160, 40))
            giftOpenBt.setObjectName("openGift" + gift)
            giftOpenBt.setFont(font)
            giftOpenBt.setEnabled(False)
            setattr(self, 'openGift' + gift, giftOpenBt)
            x += 260

        #Start Button Setting
        self.hideAndShuffle = QtWidgets.QPushButton(self.giftContainer)
        self.hideAndShuffle.setGeometry(QtCore.QRect(360, 400, 160, 40))
        self.hideAndShuffle.setObjectName("hideAndShuffle")
        self.hideAndShuffle.setFont(font)
        
        GiftSelector.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(GiftSelector)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 653, 25))
        self.menubar.setObjectName("menubar")
        GiftSelector.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(GiftSelector)
        self.statusbar.setObjectName("statusbar")
        GiftSelector.setStatusBar(self.statusbar)

        self.retranslateUi(GiftSelector)
        self.hideAndShuffle.clicked.connect(lambda: self.closingAndShuffling())
        self.openGiftOne.clicked.connect(lambda: self.open('One'))
        self.openGiftTwo.clicked.connect(lambda: self.open('Two'))
        self.openGiftThree.clicked.connect(lambda: self.open('Three'))
        QtCore.QMetaObject.connectSlotsByName(GiftSelector)

    def retranslateUi(self, GiftSelector):
        _translate = QtCore.QCoreApplication.translate
        GiftSelector.setWindowTitle(_translate("GiftSelector", "GiftSelector"))
        self.giftOne.setText(_translate("GiftSelector", "A"))#"Any Book under ₹500"
        self.giftTwo.setText(_translate("GiftSelector", "B"))#"Your Family/GF gift 50% sponsered by me upto ₹500 "
        self.giftThree.setText(_translate("GiftSelector", "C"))#"Chole Bhature Meal upto ₹500"
        self.openGiftOne.setText(_translate("GiftSelector", "Open this Gift"))
        self.openGiftTwo.setText(_translate("GiftSelector", "Open this Gift"))
        self.openGiftThree.setText(_translate("GiftSelector", "Open this Gift"))
        self.hideAndShuffle.setText(_translate("GiftSelector", "Start"))

    def closingAndShuffling(self):
        num = ['One', 'Two', 'Three']
        
        #Closing the Lids and Fading the Gifts     
        x = 100
        seqGroup = QSequentialAnimationGroup(self.giftContainer)
        parallelGroupOne = QParallelAnimationGroup(self.giftContainer)
        for number in num:
            opacity = QGraphicsOpacityEffect(self.giftContainer)
            setattr(self, 'opacityEffect' + number, opacity)
            giftNum = getattr(self, 'gift' + number)
            giftNum.setGraphicsEffect(opacity)  
            closing = QPropertyAnimation(getattr(self, 'giftBox' + number + 'Top'), b"pos")
            setattr(self, 'close' + number, closing)
            fadeOut = QPropertyAnimation(getattr(self, 'opacityEffect' + number), b"opacity")
            setattr(self, 'fadeText' + number, fadeOut)
            closing.setDuration(800)
            fadeOut.setDuration(800)
            giftBoxTop = getattr(self, 'giftBox' + number + 'Top')
            closing.setStartValue(giftBoxTop.pos())
            closing.setEndValue(QtCore.QPoint(x,85))
            x += 260
            fadeOut.setStartValue(1.0)
            fadeOut.setEndValue(0.0)
            parallelGroupOne.addAnimation(closing)
            parallelGroupOne.addAnimation(fadeOut)
           
        seqGroup.addAnimation(parallelGroupOne)
        seqGroup.addPause(300)

        #Shuffling the gift Boxes
        x = 100
        parallelGroupTwo = QParallelAnimationGroup(self.giftContainer)
        parallelGroupThree = QParallelAnimationGroup(self.giftContainer)
        for number in num:
            if number != 'Two':
                mergeTop = QPropertyAnimation(getattr(self, 'giftBox' + number + 'Top'), b"pos")
                mergeBase = QPropertyAnimation(getattr(self, 'giftBox' + number+ 'Base'), b"pos")
                setattr(self, 'merge' + number + 'Top', mergeTop)
                setattr(self, 'merge' + number + 'Base', mergeBase)
                mergeTop.setDuration(500)
                mergeBase.setDuration(500)
                #top = getattr(self, 'giftBox' + number + 'Top')
                base = getattr(self, 'giftBox' + number + 'Base')
                mergeTop.setStartValue(QtCore.QPoint(x,85))
                mergeBase.setStartValue(base.pos())
                mergeTop.setEndValue(QtCore.QPoint(360,85))
                mergeBase.setEndValue(QtCore.QPoint(360,180))
                parallelGroupTwo.addAnimation(mergeTop)
                parallelGroupTwo.addAnimation(mergeBase)

                sepTop = QPropertyAnimation(getattr(self, 'giftBox' + number + 'Top'), b"pos")
                sepBase = QPropertyAnimation(getattr(self, 'giftBox' + number+ 'Base'), b"pos")
                setattr(self, 'sep' + number + 'Top', sepTop)
                setattr(self, 'sep' + number + 'Base', sepBase)
                sepTop.setDuration(500)
                sepBase.setDuration(500)
                sepTop.setStartValue(QtCore.QPoint(360,85))
                sepBase.setStartValue(QtCore.QPoint(360,180))
                sepTop.setEndValue(QtCore.QPoint(x,85))
                sepBase.setEndValue(base.pos())
                parallelGroupThree.addAnimation(sepTop)
                parallelGroupThree.addAnimation(sepBase)                
            x += 260
            
        seqGroup.addAnimation(parallelGroupTwo)
        seqGroup.addPause(300)
        seqGroup.addAnimation(parallelGroupThree)
        seqGroup.start()
        
        self.hideAndShuffle.setEnabled(False)
        self.openGiftOne.setEnabled(True)
        self.openGiftTwo.setEnabled(True)
        self.openGiftThree.setEnabled(True)

    def open(self, giftBoxNum):
        num = ['One', 'Two', 'Three']
        shuffledGifts = random.sample(num, len(num))
        index = num.index(giftBoxNum)
        #Disabling other 2 Buttons and Opening the gift
        lidPos = 360 if giftBoxNum == 'Two' else 620 if giftBoxNum == 'Three' else 100
        textPos = 380 if giftBoxNum == 'Two' else 640 if giftBoxNum == 'Three' else 120
        for number in num:
                giftOpen = getattr(self, 'openGift' + number)
                giftOpen.setEnabled(False)
                opacity = QGraphicsOpacityEffect(self.giftContainer)
                setattr(self, 'opacity' + shuffledGifts[index], opacity)
                giftNum = getattr(self, 'gift' + shuffledGifts[index])
                giftNum.setGraphicsEffect(opacity)
                giftNum.setGeometry(QtCore.QRect(textPos, 100, 120, 80))
                fadeIn = QPropertyAnimation(getattr(self, 'opacity' + shuffledGifts[index]), b"opacity")
                setattr(self, 'fadeText' + shuffledGifts[index], fadeIn)   
                giftBoxNumber = getattr(self, 'giftBox' + giftBoxNum + 'Top')
                openLid = QPropertyAnimation(giftBoxNumber, b"pos")
                setattr(self, 'openLid' + number, openLid)
                fadeIn.setDuration(200)
                openLid.setDuration(200)
                fadeIn.setStartValue(0.0)
                openLid.setStartValue(giftBoxNumber.pos())
                fadeIn.setEndValue(1.0)
                openLid.setEndValue(QtCore.QPoint(lidPos,00))
                fadeIn.start()
                openLid.start()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GiftSelector = QtWidgets.QMainWindow()
    ui = Ui_GiftSelector()
    ui.onStartInstructions(GiftSelector)
    GiftSelector.show()
    sys.exit(app.exec_())
