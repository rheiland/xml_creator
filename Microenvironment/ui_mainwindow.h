/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.9.7
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QScrollArea>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTreeWidget>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QAction *actionNew_Substrate;
    QAction *actionLoad;
    QAction *actionSave;
    QAction *actionExport_to_XML;
    QAction *actionLink;
    QAction *actionCell_Definitions;
    QAction *actionXML_Out;
    QAction *action2D;
    QAction *action3D;
    QWidget *centralwidget;
    QTreeWidget *Outline;
    QPushButton *New;
    QPushButton *Remove;
    QScrollArea *scrollArea;
    QWidget *scrollAreaWidgetContents;
    QLabel *label_5;
    QLabel *label_4;
    QLabel *label_3;
    QLabel *label_2;
    QLabel *label;
    QLineEdit *name;
    QCheckBox *checkBox;
    QLineEdit *diffusionCoeff;
    QLineEdit *decayRate;
    QLineEdit *initialCond;
    QLineEdit *dirchBoundary;
    QLabel *label_6;
    QLabel *label_7;
    QLabel *label_8;
    QLabel *label_9;
    QLabel *label_10;
    QLineEdit *lineEdit_6;
    QLineEdit *lineEdit_7;
    QLineEdit *lineEdit_8;
    QLineEdit *lineEdit_9;
    QCheckBox *checkBox_2;
    QCheckBox *checkBox_3;
    QCheckBox *checkBox_4;
    QCheckBox *checkBox_5;
    QLabel *label_11;
    QLabel *label_12;
    QPushButton *Clone;
    QMenuBar *menubar;
    QMenu *menuFile;
    QMenu *menuNew;
    QMenu *menuEdit;
    QMenu *menuView;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QStringLiteral("MainWindow"));
        MainWindow->resize(927, 610);
        actionNew_Substrate = new QAction(MainWindow);
        actionNew_Substrate->setObjectName(QStringLiteral("actionNew_Substrate"));
        actionLoad = new QAction(MainWindow);
        actionLoad->setObjectName(QStringLiteral("actionLoad"));
        actionSave = new QAction(MainWindow);
        actionSave->setObjectName(QStringLiteral("actionSave"));
        actionSave->setCheckable(false);
        actionExport_to_XML = new QAction(MainWindow);
        actionExport_to_XML->setObjectName(QStringLiteral("actionExport_to_XML"));
        actionLink = new QAction(MainWindow);
        actionLink->setObjectName(QStringLiteral("actionLink"));
        actionCell_Definitions = new QAction(MainWindow);
        actionCell_Definitions->setObjectName(QStringLiteral("actionCell_Definitions"));
        actionXML_Out = new QAction(MainWindow);
        actionXML_Out->setObjectName(QStringLiteral("actionXML_Out"));
        action2D = new QAction(MainWindow);
        action2D->setObjectName(QStringLiteral("action2D"));
        action3D = new QAction(MainWindow);
        action3D->setObjectName(QStringLiteral("action3D"));
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QStringLiteral("centralwidget"));
        Outline = new QTreeWidget(centralwidget);
        QTreeWidgetItem *__qtreewidgetitem = new QTreeWidgetItem();
        __qtreewidgetitem->setTextAlignment(0, Qt::AlignLeading|Qt::AlignVCenter);
        Outline->setHeaderItem(__qtreewidgetitem);
        new QTreeWidgetItem(Outline);
        new QTreeWidgetItem(Outline);
        Outline->setObjectName(QStringLiteral("Outline"));
        Outline->setGeometry(QRect(0, 0, 181, 561));
        Outline->setColumnCount(1);
        New = new QPushButton(centralwidget);
        New->setObjectName(QStringLiteral("New"));
        New->setGeometry(QRect(290, 40, 91, 23));
        Remove = new QPushButton(centralwidget);
        Remove->setObjectName(QStringLiteral("Remove"));
        Remove->setGeometry(QRect(650, 40, 111, 23));
        scrollArea = new QScrollArea(centralwidget);
        scrollArea->setObjectName(QStringLiteral("scrollArea"));
        scrollArea->setGeometry(QRect(290, 70, 451, 471));
        scrollArea->setWidgetResizable(true);
        scrollAreaWidgetContents = new QWidget();
        scrollAreaWidgetContents->setObjectName(QStringLiteral("scrollAreaWidgetContents"));
        scrollAreaWidgetContents->setGeometry(QRect(0, 0, 449, 469));
        label_5 = new QLabel(scrollAreaWidgetContents);
        label_5->setObjectName(QStringLiteral("label_5"));
        label_5->setGeometry(QRect(60, 230, 101, 21));
        label_4 = new QLabel(scrollAreaWidgetContents);
        label_4->setObjectName(QStringLiteral("label_4"));
        label_4->setGeometry(QRect(60, 180, 101, 21));
        label_3 = new QLabel(scrollAreaWidgetContents);
        label_3->setObjectName(QStringLiteral("label_3"));
        label_3->setGeometry(QRect(60, 130, 101, 21));
        label_2 = new QLabel(scrollAreaWidgetContents);
        label_2->setObjectName(QStringLiteral("label_2"));
        label_2->setGeometry(QRect(60, 80, 101, 21));
        label = new QLabel(scrollAreaWidgetContents);
        label->setObjectName(QStringLiteral("label"));
        label->setGeometry(QRect(60, 30, 101, 21));
        name = new QLineEdit(scrollAreaWidgetContents);
        name->setObjectName(QStringLiteral("name"));
        name->setGeometry(QRect(170, 30, 161, 20));
        checkBox = new QCheckBox(scrollAreaWidgetContents);
        checkBox->setObjectName(QStringLiteral("checkBox"));
        checkBox->setGeometry(QRect(30, 230, 16, 16));
        checkBox->setChecked(false);
        diffusionCoeff = new QLineEdit(scrollAreaWidgetContents);
        diffusionCoeff->setObjectName(QStringLiteral("diffusionCoeff"));
        diffusionCoeff->setGeometry(QRect(170, 80, 161, 20));
        diffusionCoeff->setInputMethodHints(Qt::ImhDigitsOnly);
        decayRate = new QLineEdit(scrollAreaWidgetContents);
        decayRate->setObjectName(QStringLiteral("decayRate"));
        decayRate->setGeometry(QRect(170, 130, 161, 20));
        initialCond = new QLineEdit(scrollAreaWidgetContents);
        initialCond->setObjectName(QStringLiteral("initialCond"));
        initialCond->setGeometry(QRect(170, 180, 161, 20));
        dirchBoundary = new QLineEdit(scrollAreaWidgetContents);
        dirchBoundary->setObjectName(QStringLiteral("dirchBoundary"));
        dirchBoundary->setEnabled(true);
        dirchBoundary->setGeometry(QRect(170, 230, 161, 20));
        label_6 = new QLabel(scrollAreaWidgetContents);
        label_6->setObjectName(QStringLiteral("label_6"));
        label_6->setGeometry(QRect(130, 270, 111, 16));
        label_7 = new QLabel(scrollAreaWidgetContents);
        label_7->setObjectName(QStringLiteral("label_7"));
        label_7->setGeometry(QRect(130, 310, 71, 21));
        label_8 = new QLabel(scrollAreaWidgetContents);
        label_8->setObjectName(QStringLiteral("label_8"));
        label_8->setGeometry(QRect(130, 350, 71, 21));
        label_9 = new QLabel(scrollAreaWidgetContents);
        label_9->setObjectName(QStringLiteral("label_9"));
        label_9->setGeometry(QRect(130, 390, 71, 21));
        label_10 = new QLabel(scrollAreaWidgetContents);
        label_10->setObjectName(QStringLiteral("label_10"));
        label_10->setGeometry(QRect(130, 430, 71, 21));
        lineEdit_6 = new QLineEdit(scrollAreaWidgetContents);
        lineEdit_6->setObjectName(QStringLiteral("lineEdit_6"));
        lineEdit_6->setGeometry(QRect(210, 310, 161, 20));
        lineEdit_7 = new QLineEdit(scrollAreaWidgetContents);
        lineEdit_7->setObjectName(QStringLiteral("lineEdit_7"));
        lineEdit_7->setGeometry(QRect(210, 350, 161, 20));
        lineEdit_8 = new QLineEdit(scrollAreaWidgetContents);
        lineEdit_8->setObjectName(QStringLiteral("lineEdit_8"));
        lineEdit_8->setGeometry(QRect(210, 390, 161, 20));
        lineEdit_9 = new QLineEdit(scrollAreaWidgetContents);
        lineEdit_9->setObjectName(QStringLiteral("lineEdit_9"));
        lineEdit_9->setGeometry(QRect(210, 430, 161, 20));
        checkBox_2 = new QCheckBox(scrollAreaWidgetContents);
        checkBox_2->setObjectName(QStringLiteral("checkBox_2"));
        checkBox_2->setGeometry(QRect(100, 310, 16, 16));
        checkBox_3 = new QCheckBox(scrollAreaWidgetContents);
        checkBox_3->setObjectName(QStringLiteral("checkBox_3"));
        checkBox_3->setGeometry(QRect(100, 350, 16, 16));
        checkBox_4 = new QCheckBox(scrollAreaWidgetContents);
        checkBox_4->setObjectName(QStringLiteral("checkBox_4"));
        checkBox_4->setGeometry(QRect(100, 390, 16, 16));
        checkBox_5 = new QCheckBox(scrollAreaWidgetContents);
        checkBox_5->setObjectName(QStringLiteral("checkBox_5"));
        checkBox_5->setGeometry(QRect(100, 430, 16, 16));
        label_11 = new QLabel(scrollAreaWidgetContents);
        label_11->setObjectName(QStringLiteral("label_11"));
        label_11->setGeometry(QRect(340, 80, 71, 16));
        label_12 = new QLabel(scrollAreaWidgetContents);
        label_12->setObjectName(QStringLiteral("label_12"));
        label_12->setGeometry(QRect(340, 130, 47, 13));
        scrollArea->setWidget(scrollAreaWidgetContents);
        Clone = new QPushButton(centralwidget);
        Clone->setObjectName(QStringLiteral("Clone"));
        Clone->setGeometry(QRect(390, 40, 91, 23));
        MainWindow->setCentralWidget(centralwidget);
        scrollArea->raise();
        Outline->raise();
        New->raise();
        Remove->raise();
        Clone->raise();
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName(QStringLiteral("menubar"));
        menubar->setGeometry(QRect(0, 0, 927, 21));
        menuFile = new QMenu(menubar);
        menuFile->setObjectName(QStringLiteral("menuFile"));
        menuNew = new QMenu(menuFile);
        menuNew->setObjectName(QStringLiteral("menuNew"));
        menuEdit = new QMenu(menubar);
        menuEdit->setObjectName(QStringLiteral("menuEdit"));
        menuView = new QMenu(menubar);
        menuView->setObjectName(QStringLiteral("menuView"));
        MainWindow->setMenuBar(menubar);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName(QStringLiteral("statusbar"));
        MainWindow->setStatusBar(statusbar);

        menubar->addAction(menuFile->menuAction());
        menubar->addAction(menuEdit->menuAction());
        menubar->addAction(menuView->menuAction());
        menuFile->addAction(menuNew->menuAction());
        menuFile->addAction(actionLoad);
        menuFile->addSeparator();
        menuFile->addAction(actionSave);
        menuNew->addAction(action2D);
        menuNew->addAction(action3D);
        menuView->addAction(actionXML_Out);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", Q_NULLPTR));
        actionNew_Substrate->setText(QApplication::translate("MainWindow", "New Substrate", Q_NULLPTR));
        actionLoad->setText(QApplication::translate("MainWindow", "Load", Q_NULLPTR));
        actionSave->setText(QApplication::translate("MainWindow", "Save", Q_NULLPTR));
        actionExport_to_XML->setText(QApplication::translate("MainWindow", "Export to XML", Q_NULLPTR));
        actionLink->setText(QApplication::translate("MainWindow", "Microenvironments", Q_NULLPTR));
        actionCell_Definitions->setText(QApplication::translate("MainWindow", "Cell Definitions", Q_NULLPTR));
        actionXML_Out->setText(QApplication::translate("MainWindow", "XML Out", Q_NULLPTR));
        action2D->setText(QApplication::translate("MainWindow", "2D", Q_NULLPTR));
        action3D->setText(QApplication::translate("MainWindow", "3D", Q_NULLPTR));
        QTreeWidgetItem *___qtreewidgetitem = Outline->headerItem();
        ___qtreewidgetitem->setText(0, QApplication::translate("MainWindow", "New 2D", Q_NULLPTR));

        const bool __sortingEnabled = Outline->isSortingEnabled();
        Outline->setSortingEnabled(false);
        QTreeWidgetItem *___qtreewidgetitem1 = Outline->topLevelItem(0);
        ___qtreewidgetitem1->setText(0, QApplication::translate("MainWindow", "Microenvironment", Q_NULLPTR));
        QTreeWidgetItem *___qtreewidgetitem2 = Outline->topLevelItem(1);
        ___qtreewidgetitem2->setText(0, QApplication::translate("MainWindow", "Cell Definitions", Q_NULLPTR));
        Outline->setSortingEnabled(__sortingEnabled);

        New->setText(QApplication::translate("MainWindow", "New Substrate", Q_NULLPTR));
        Remove->setText(QApplication::translate("MainWindow", "Remove Substrate", Q_NULLPTR));
        label_5->setText(QApplication::translate("MainWindow", "Dirichlet Boundary", Q_NULLPTR));
        label_4->setText(QApplication::translate("MainWindow", "Initial Condition", Q_NULLPTR));
        label_3->setText(QApplication::translate("MainWindow", "Decay Rate", Q_NULLPTR));
        label_2->setText(QApplication::translate("MainWindow", "Diffusion Coefficient", Q_NULLPTR));
        label->setText(QApplication::translate("MainWindow", "Name", Q_NULLPTR));
        name->setPlaceholderText(QApplication::translate("MainWindow", "Default", Q_NULLPTR));
        checkBox->setText(QString());
        diffusionCoeff->setPlaceholderText(QApplication::translate("MainWindow", "0", Q_NULLPTR));
        decayRate->setPlaceholderText(QApplication::translate("MainWindow", "0", Q_NULLPTR));
        initialCond->setPlaceholderText(QApplication::translate("MainWindow", "0", Q_NULLPTR));
        dirchBoundary->setPlaceholderText(QApplication::translate("MainWindow", "0", Q_NULLPTR));
        label_6->setText(QApplication::translate("MainWindow", "Advanced Boundary", Q_NULLPTR));
        label_7->setText(QApplication::translate("MainWindow", "X Maximum", Q_NULLPTR));
        label_8->setText(QApplication::translate("MainWindow", "X Minimum", Q_NULLPTR));
        label_9->setText(QApplication::translate("MainWindow", "Y Maximum", Q_NULLPTR));
        label_10->setText(QApplication::translate("MainWindow", "Y Minimum", Q_NULLPTR));
        lineEdit_6->setPlaceholderText(QApplication::translate("MainWindow", "0", Q_NULLPTR));
        lineEdit_7->setPlaceholderText(QApplication::translate("MainWindow", "0", Q_NULLPTR));
        lineEdit_8->setPlaceholderText(QApplication::translate("MainWindow", "0", Q_NULLPTR));
        lineEdit_9->setPlaceholderText(QApplication::translate("MainWindow", "0", Q_NULLPTR));
        checkBox_2->setText(QString());
        checkBox_3->setText(QString());
        checkBox_4->setText(QString());
        checkBox_5->setText(QString());
        label_11->setText(QApplication::translate("MainWindow", "micron^2/min", Q_NULLPTR));
        label_12->setText(QApplication::translate("MainWindow", "1/min", Q_NULLPTR));
        Clone->setText(QApplication::translate("MainWindow", "Clone Substrate", Q_NULLPTR));
        menuFile->setTitle(QApplication::translate("MainWindow", "File", Q_NULLPTR));
        menuNew->setTitle(QApplication::translate("MainWindow", "New", Q_NULLPTR));
        menuEdit->setTitle(QApplication::translate("MainWindow", "Edit", Q_NULLPTR));
        menuView->setTitle(QApplication::translate("MainWindow", "View", Q_NULLPTR));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
