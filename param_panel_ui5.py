# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'param_panel.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(670, 626)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbSubjects = QtWidgets.QLabel(Dialog)
        self.lbSubjects.setObjectName("lbSubjects")
        self.verticalLayout.addWidget(self.lbSubjects)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pbSelectAllSubjects = QtWidgets.QPushButton(Dialog)
        self.pbSelectAllSubjects.setObjectName("pbSelectAllSubjects")
        self.horizontalLayout_3.addWidget(self.pbSelectAllSubjects)
        self.pbUnselectAllSubjects = QtWidgets.QPushButton(Dialog)
        self.pbUnselectAllSubjects.setObjectName("pbUnselectAllSubjects")
        self.horizontalLayout_3.addWidget(self.pbUnselectAllSubjects)
        self.pbReverseSubjectsSelection = QtWidgets.QPushButton(Dialog)
        self.pbReverseSubjectsSelection.setObjectName("pbReverseSubjectsSelection")
        self.horizontalLayout_3.addWidget(self.pbReverseSubjectsSelection)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.lwSubjects = QtWidgets.QListWidget(Dialog)
        self.lwSubjects.setObjectName("lwSubjects")
        self.verticalLayout.addWidget(self.lwSubjects)
        self.lbBehaviors = QtWidgets.QLabel(Dialog)
        self.lbBehaviors.setObjectName("lbBehaviors")
        self.verticalLayout.addWidget(self.lbBehaviors)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pbSelectAllBehaviors = QtWidgets.QPushButton(Dialog)
        self.pbSelectAllBehaviors.setObjectName("pbSelectAllBehaviors")
        self.horizontalLayout_4.addWidget(self.pbSelectAllBehaviors)
        self.pbUnselectAllBehaviors = QtWidgets.QPushButton(Dialog)
        self.pbUnselectAllBehaviors.setObjectName("pbUnselectAllBehaviors")
        self.horizontalLayout_4.addWidget(self.pbUnselectAllBehaviors)
        self.pbReverseBehaviorsSelection = QtWidgets.QPushButton(Dialog)
        self.pbReverseBehaviorsSelection.setObjectName("pbReverseBehaviorsSelection")
        self.horizontalLayout_4.addWidget(self.pbReverseBehaviorsSelection)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.lwBehaviors = QtWidgets.QListWidget(Dialog)
        self.lwBehaviors.setObjectName("lwBehaviors")
        self.verticalLayout.addWidget(self.lwBehaviors)
        self.cbIncludeModifiers = QtWidgets.QCheckBox(Dialog)
        self.cbIncludeModifiers.setObjectName("cbIncludeModifiers")
        self.verticalLayout.addWidget(self.cbIncludeModifiers)
        self.cbExcludeBehaviors = QtWidgets.QCheckBox(Dialog)
        self.cbExcludeBehaviors.setObjectName("cbExcludeBehaviors")
        self.verticalLayout.addWidget(self.cbExcludeBehaviors)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbStartTime = QtWidgets.QLabel(Dialog)
        self.lbStartTime.setObjectName("lbStartTime")
        self.horizontalLayout.addWidget(self.lbStartTime)
        self.teStartTime = QtWidgets.QTimeEdit(Dialog)
        self.teStartTime.setObjectName("teStartTime")
        self.horizontalLayout.addWidget(self.teStartTime)
        self.dsbStartTime = QtWidgets.QDoubleSpinBox(Dialog)
        self.dsbStartTime.setDecimals(3)
        self.dsbStartTime.setMaximum(1000000.0)
        self.dsbStartTime.setObjectName("dsbStartTime")
        self.horizontalLayout.addWidget(self.dsbStartTime)
        self.lbEndTime = QtWidgets.QLabel(Dialog)
        self.lbEndTime.setObjectName("lbEndTime")
        self.horizontalLayout.addWidget(self.lbEndTime)
        self.teEndTime = QtWidgets.QTimeEdit(Dialog)
        self.teEndTime.setObjectName("teEndTime")
        self.horizontalLayout.addWidget(self.teEndTime)
        self.dsbEndTime = QtWidgets.QDoubleSpinBox(Dialog)
        self.dsbEndTime.setDecimals(3)
        self.dsbEndTime.setMaximum(1000000.0)
        self.dsbEndTime.setObjectName("dsbEndTime")
        self.horizontalLayout.addWidget(self.dsbEndTime)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pbCancel = QtWidgets.QPushButton(Dialog)
        self.pbCancel.setObjectName("pbCancel")
        self.horizontalLayout_2.addWidget(self.pbCancel)
        self.pbOK = QtWidgets.QPushButton(Dialog)
        self.pbOK.setObjectName("pbOK")
        self.horizontalLayout_2.addWidget(self.pbOK)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Parameters"))
        self.lbSubjects.setText(_translate("Dialog", "Subjects"))
        self.pbSelectAllSubjects.setText(_translate("Dialog", "Select all"))
        self.pbUnselectAllSubjects.setText(_translate("Dialog", "Unselect all"))
        self.pbReverseSubjectsSelection.setText(_translate("Dialog", "Reverse selection"))
        self.lbBehaviors.setText(_translate("Dialog", "Behaviors"))
        self.pbSelectAllBehaviors.setText(_translate("Dialog", "Select all"))
        self.pbUnselectAllBehaviors.setText(_translate("Dialog", "Unselect all"))
        self.pbReverseBehaviorsSelection.setText(_translate("Dialog", "Reverse selection"))
        self.cbIncludeModifiers.setText(_translate("Dialog", "Include modifiers"))
        self.cbExcludeBehaviors.setText(_translate("Dialog", "Exclude behaviors without events"))
        self.lbStartTime.setText(_translate("Dialog", "Start time"))
        self.teStartTime.setDisplayFormat(_translate("Dialog", "hh:mm:ss.zzz"))
        self.lbEndTime.setText(_translate("Dialog", "End time"))
        self.teEndTime.setDisplayFormat(_translate("Dialog", "hh:mm:ss.zzz"))
        self.pbCancel.setText(_translate("Dialog", "Cancel"))
        self.pbOK.setText(_translate("Dialog", "OK"))
