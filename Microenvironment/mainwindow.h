#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <microenvironment.h>
#include <QTreeWidgetItem>

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();
    QVector<microenvironment> substrates; //List of substrates
    QTreeWidgetItem *environmentIndex; //Used to hold the pointer to the Microenvironment item in the Outline. Used to add more substrates
    int currentSub = 0; //Index of the substrate currently shown on screen

private slots:
    void save();

    void loadValues();

    void loadNew();

    void on_name_textEdited(const QString &arg1);

    void on_diffusionCoeff_textEdited(const QString &arg1);

    void on_decayRate_textEdited(const QString &arg1);

    void on_initialCond_textEdited(const QString &arg1);

    void on_Outline_itemClicked(QTreeWidgetItem *item, int column);

    void on_New_clicked();

    void on_Clone_clicked();

    void on_Remove_clicked();

private:
    Ui::MainWindow *ui;
};
#endif // MAINWINDOW_H
