from tkinter import *
from tkinter import filedialog

root = Tk()

root.title("MP3 Player")
root.geometry("500x400")

# function to add one song to playlist


def add_song():
    song = filedialog.askopenfilename(initialdir='audio/', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"),))
    # dir structure stripping
    song = song.replace("C:/Users/LENOVO/PycharmProjects/mp3/audio/", "")
    song = song.replace(".mp3", "")
    playlist_box.insert(END, song)

# function to add many songs to playlist


def add_many_songs():
    songs = filedialog.askopenfilenames(initialdir='audio/', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"),))
    # Loop through song list then replace dir structure and mp3 to song name
    for song in songs:
        # dir structure stripping
        song = song.replace("C:/Users/LENOVO/PycharmProjects/mp3/audio/", "")
        song = song.replace(".mp3", "")
        # Add to end of playlist
        playlist_box.insert(END, song)

# Function to delete song from playlist


def delete_song():
    playlist_box.delete()


def delete_all_songs():
    pass


# Create Playlist Box
playlist_box = Listbox(root, bg="black", fg="green", width=60, selectbackground="red", selectforeground="yellow")
playlist_box.pack(pady=20)

# Define Button Images For Controls
back_btn_img = PhotoImage(file='images/back50.png')
forward_btn_img = PhotoImage(file='images/forward50.png')
play_btn_img = PhotoImage(file='images/play50.png')
pause_btn_img = PhotoImage(file='images/pause50.png')
stop_btn_img = PhotoImage(file='images/stop50.png')

# Create Button Frame
control_frame = Frame(root)
control_frame.pack(pady=20)

# Create play and pause button
back_button = Button(control_frame, image=back_btn_img, borderwidth=0)
forward_button = Button(control_frame, image=forward_btn_img, borderwidth=0)
play_button = Button(control_frame, image=play_btn_img, borderwidth=0)
pause_button = Button(control_frame, image=pause_btn_img, borderwidth=0)
stop_button = Button(control_frame, image=stop_btn_img, borderwidth=0)

back_button.grid(row=0, column=0, padx=10)
forward_button.grid(row=0, column=1, padx=10)
play_button.grid(row=0, column=2, padx=10)
pause_button.grid(row=0, column=3, padx=10)
stop_button.grid(row=0, column=4, padx=10)

# Create menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Create Add Song Menu Dropdown
add_song_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Add Songs", menu=add_song_menu)
# add one song to playlist
add_song_menu.add_command(label="Add One Song to playlist", command=add_song)
# add many songs to playlist
add_song_menu.add_command(label="Add Many Songs to playlist", command=add_many_songs)

# Create Delete Song Menu Dropdowns
remove_song_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Remove Songs", menu=remove_song_menu)
remove_song_menu.add_command(label="Delete A Song From Playlist", command=delete_song)
remove_song_menu.add_command(label="Delete All Songs From Playlist", command=delete_all_songs)

# Temporary Label
my_label = Label(root, text='')
my_label.pack(pady=20)

root.mainloop()