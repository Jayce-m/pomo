import PySimpleGUI as sg
import os.path


# sg.Window(title="Hello World", layout=[[]], margins=(100,50)).read()

# layout = [
#     [sg.Text("Hello from the GUI! :)")],
#     [sg.Button("OK")],
#     [sg.Button("Another Button")]
# ]

# # Create the window

# window = sg.Window("Demo", layout)

# # Create an event loop

# while True:
#     event, values = window.read()
#     #Terminate if user closes window or presses the OK button
#     if event == "OK" or event == sg.WIN_CLOSED:
#         break

#     if event == "Another Button":
#         print("Button was pressed!")
#         break


# window.close()


file_list_column = [
    [
        sg.Text("Image Folder"),
        sg.In(size=(25,1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Text("TESTING"),
        sg.Listbox(
            values=[], enable_events=True, size=(40,20),
            key="-FILE LIST-"
        )
    ],

]

image_viewer_column = [
    [sg.Text("Choose an image from the list on the left:")],
    [sg.Text(size=(40,1), key="-TOUT-")],
    [sg.Image(key="-IMAGE-")],
]

#--- Layout ---

layout = [
    [
        sg.Column(file_list_column),
        sg.VSeperator(),
        sg.Column(image_viewer_column),
    ]

]

window = sg.Window("Image Viewer", layout)

#event loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            # get list of files in folder
            file_list = os.listdir(folder)
        except:
            file_list = []
        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".png", ".gif"))
        ]
        window["-FILE LIST-"].update(fnames)
    elif event == "-FILE LIST-": # a file was chosen from the list
        try:
            filename = os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"][0]
            )
            window["-TOUT-"].update(filename)
            window["-IMAGE-"].update(filename=filename)
        except:
            pass
window.close()