#include "mainwindow.h"
#include "ui_mainwindow.h"

#include <QFile>
#include "QXmlStreamWriter"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    //Setting up menu actions
    connect(ui->actionSave, SIGNAL(triggered()), this, SLOT(save()));

    //Setting up default substrate, eventually do the same with cell definitions
    microenvironment sub0 = microenvironment(currentSub);
    substrates.append(sub0);
    currentSub = 0;

    //Add object to represent the default substrate
    environmentIndex = ui->Outline->findItems("Microenvironment",Qt::MatchExactly,0)[0];
    environmentIndex->addChild(new QTreeWidgetItem(0));
    environmentIndex->child(0)->setText(0, substrates[currentSub].name);
}

MainWindow::~MainWindow()
{
    delete ui;
}

//Save the XML file to output.txt
//Uses QXmlStreamWriter to format in XML
void MainWindow::save()
{
    // QFile data("C:/School_Stuff/Spring_2021/Research/GUI/MicroenvironmentGUI/output.txt");
    // std::cout << "----- write to mygui.xml\n";
    QFile data("mygui.xml");
    if (!data.open(QIODevice::WriteOnly | QIODevice::Text)){
        // qDebug() << "Whelp"; //Sanity check
        return;
    }

    QXmlStreamWriter output;
    output.setDevice(&data);
    output.setAutoFormatting(true);
    output.writeStartDocument();

    //This section writes all the different substrates in XML format
    output.writeStartElement("microenvironment_setup");
    int i;
    for(i = 0;i < substrates.size(); i++){
        output.writeStartElement("variable");
        output.writeAttribute("name", substrates[i].name);
        output.writeAttribute("ID", QString::number(substrates[i].id));
        output.writeStartElement("physical_parameter_set");
        output.writeTextElement("diffusion_coefficient", QString::number(substrates[i].diffCoeff));
        output.writeTextElement("decay_rate", QString::number(substrates[i].decayR));
        output.writeEndElement();
        output.writeTextElement("initial_condition", QString::number(substrates[i].initialC));
        output.writeStartElement("Dirichlet_boundary_condition");
        output.writeAttribute("enabled", "false");
        output.writeCharacters(QString::number(substrates[i].dirch[0][0]));
        output.writeEndElement();
        output.writeEndElement();
    }
    //end of microenvironment section

    output.writeEndDocument();
    // output.writeEndDocument();

    // qDebug() << "Yay"; //Sanity check
}

//Loads the values of the current substrate into the text fields to then be edited by the user
void MainWindow::loadValues()
{
    ui->name->setText(substrates[currentSub].name);
    ui->diffusionCoeff->setText(QString::number(substrates[currentSub].diffCoeff));
    ui->decayRate->setText(QString::number(substrates[currentSub].decayR));
    ui->initialCond->setText(QString::number(substrates[currentSub].initialC));
}

//When a new substrate is made this fuction empties the text fields for more convenient typing
void MainWindow::loadNew()
{
    ui->name->setText("");
    ui->diffusionCoeff->setText("");
    ui->decayRate->setText("");
    ui->initialCond->setText("");
}


//The following fuctions are different actions in the GUI, the names are fairly intuitive

//Updates the name inside the microenvironment object for the current substrate, as well as in the Ouline on the left
void MainWindow::on_name_textEdited(const QString &arg1)
{
    if(arg1 == ""){
        substrates[currentSub].name = "Default";
        environmentIndex->child(currentSub)->setText(0, "Default");
    }
    else{
        substrates[currentSub].name = arg1;
        environmentIndex->child(currentSub)->setText(0, arg1);
    }
    // qDebug() << substrates[currentSub].name;
}

//Updates the diffusion coefficient inside the microenvironment object for the current substrate
void MainWindow::on_diffusionCoeff_textEdited(const QString &arg1)
{
    substrates[currentSub].diffCoeff = arg1.toDouble();
    // qDebug() << substrates[currentSub].diffCoeff;
}

//Updates the decay rate inside the microenvironment object for the current substrate
void MainWindow::on_decayRate_textEdited(const QString &arg1)
{
    substrates[currentSub].decayR = arg1.toDouble();
    // qDebug() << substrates[currentSub].decayR;
}

//Updates the initial condition inside the microenvironment object for the current substrate
void MainWindow::on_initialCond_textEdited(const QString &arg1)
{
    substrates[currentSub].initialC = arg1.toDouble();
    // qDebug() << substrates[currentSub].initialC;
}

//Determines the index of the substrate the user clicked in the Outline
void MainWindow::on_Outline_itemClicked(QTreeWidgetItem *item, int column)
{
    currentSub = environmentIndex->indexOfChild(item); //The index of the item in the outline is the same as the index in the substrate list as well as the id of the substrate
    loadValues();
}

//Creates a new object in the Outline and calls loadNew()
void MainWindow::on_New_clicked()
{
    currentSub = substrates.size();
    microenvironment newSub = microenvironment(currentSub);
    substrates.append(newSub);
    environmentIndex->addChild(new QTreeWidgetItem(0));
    environmentIndex->child(currentSub)->setText(0, substrates[currentSub].name);
    loadNew();
}

//Creates a clone of the current substrate but changes the id to the next avaliable value, then displays the cloned values with loadValues()
void MainWindow::on_Clone_clicked()
{
    // qDebug() << substrates.size();
    microenvironment newSub = microenvironment(substrates.size());
    newSub = substrates[currentSub];
    currentSub = substrates.size();
    newSub.id = currentSub;
    substrates.append(newSub);
    // qDebug() << substrates.size();
    environmentIndex->addChild(new QTreeWidgetItem(0));
    environmentIndex->child(currentSub)->setText(0, substrates[currentSub].name);
    loadValues();
}

//Removes the current substrate from the substrate list and the Outline, then reassigns the IDs of the remaining substrates. This function ensures there is at least 1 substrate
void MainWindow::on_Remove_clicked()
{
    if(substrates.size() == 1){
        // qDebug() << "Thats the last one!! You cannot remove it!";
        return;
    }
    substrates.remove(currentSub);
    environmentIndex->removeChild(environmentIndex->child(currentSub));
    int i;
    for(i=0;i<substrates.size();i++){
        substrates[i].id = i;
    }
    currentSub = 0;
    loadValues();
}
