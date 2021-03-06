import pydicom
from tkinter import *
from tkinter import filedialog

# Main windows setup
mainWindow = Tk()  # Links main window to the interpreter
mainWindow.title("Cubes_Metadata by Kamil_Sokolowski")
mainWindow.geometry("396x310+300+200")  # Window size and initial position
mainWindow['bg'] = 'gray98'  # Background colour

# Main text area
textArea = Text(mainWindow, width=46, height=14, borderwidth=2, bg='old lace')
textArea.place(x=12, y=67)

def processDragDrop(importedFile):
    # Open Dicom with python dicom package
    dicomInfo = pydicom.dcmread(importedFile)

    # Create text file output naming structure
    dicomDateTime = dicomInfo.AcquisitionDateTime
    outputName = 'Dicom_Metadata_'
    dateTimeOutput = dicomDateTime[0:4] + '-' + dicomDateTime[4:6] + '-' + dicomDateTime[6:8] + '_' + dicomDateTime[
                                                                                                      8:12]

    # Initial Pydicom output not a string
    info = str(dicomInfo)

    # Writes text file
    with open("{0}{1}.txt".format(outputName, dateTimeOutput), 'w') as f:
        for i in info:
            f.write(i)

    textArea.insert(END, 'DICOM metadata output created for: \n' + str(dicomInfo.PatientName) + '\n')

def openAndProcessDicom():
    # Open Dicom with python dicom package

    textArea.delete("1.0", "end")

    importedFile = filedialog.askopenfilename(initialdir="C:/Users/MainFrame/Desktop/", title="Open Log file",
                                              filetypes=(("Dicom", "*.dcm"),))

    dicomInfo = pydicom.dcmread(importedFile)

    # Create text file output naming structure
    dicomDateTime = dicomInfo.AcquisitionDateTime
    outputName = 'Dicom_Metadata_'
    dateTimeOutput = dicomDateTime[0:4] + '-' + dicomDateTime[4:6] + '-' + dicomDateTime[6:8] + '_' + dicomDateTime[
                                                                                                      8:12]

    # Initial Pydicom output not a string
    info = str(dicomInfo)

    # Writes text file
    with open("{0}{1}.txt".format(outputName, dateTimeOutput), 'w') as f:
        for i in info:
            f.write(i)

    textArea.insert(END, '\n   DICOM metadata output created for: \n   ' + str(dicomInfo.PatientName) + '\n')

def aboutInformation():
    textArea.delete("1.0", "end")
    textArea.insert(END, "Cubes_Metadata\n\nVersion 1.0\n\n7th July 2021\n\nCubes_Metadata generates a text file with all the metadata "
                         "contained with a dicom file.\n\nCopyright (c) 2021 Kamil Sokolowski \n\n"
                         "Source code & license (MIT) available at:\nhttps://github.com/thatKamil/Cubes_Metadata")

def useInformation():
    textArea.delete("1.0", "end")
    textArea.insert(END, "-=Use Guide=-\n\nThe program can open dicom files generated by Molecubes PET & CT machines."
                         " It will likely\nwork for data generated by other machines, \nthough this hasn't been tested.\n\n"
                         "The Windows version of the program has two \noptions for use:\n\n1. Drag a dcm file onto the"
                         " program icon.\n\t\tor\n2. Open the program and click 'Open File'.")

Button(mainWindow, text="Open File", command=openAndProcessDicom, height=2, width=10,
       bg='snow', font='Courier').place(x=12, y=9)
Button(mainWindow, text="About", command=aboutInformation, height=1, width=6,
       bg='snow', font='Courier').place(x=315, y=1)
Button(mainWindow, text="Guide", command=useInformation, height=1, width=6,
       bg='snow', font='Courier').place(x=315, y=33)

if len(sys.argv) == 1:  #
    waitFlag = True
    textArea.insert(END,
                    '\t       +--------------+\n\t       |.------------.|\n\t       ||Open a Dicom||\n\t       ||file to     ||\n'
                    '\t       ||start:      ||\n\t       ||            ||\n\t       |+------------+|\n\t       +-..--------..-+\n'
                    '\t       .--------------.\n\t      / /============\ \\ \n\t     / /==============\ \\ \n\t'
                    '    /____________________\\ \n\t    \____________________/')
else:
    # Drag drop functionality in Windows
    importedFile = sys.argv[1]
    processDragDrop(importedFile)

mainWindow.mainloop()