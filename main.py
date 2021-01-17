from tkinter import *
from tkinter import filedialog, ttk
import pygame
import time
from mutagen.mp3 import MP3
root = Tk()

root.title("MP3 Player")
root.geometry("500x400")

# Pygame initialization
pygame.mixer.init()


# Create a function for time


def play_time():
    # Check to see if song is stopped
    if stopped:
        return
    # grab current song time and convert it to time format,
    # add current time to status bar
    # then create loop to check the time every second
    current_time = pygame.mixer.music.get_pos() / 1000
    converted_current_time = time.strftime("%M:%S", time.gmtime(current_time))
    # reconstruct song with dir
    song = playlist_box.get(ACTIVE)
    song = f'C:/Users/LENOVO/PycharmProjects/mp3/audio/{song}.mp3'

    # Find Current Song Length
    song_mut = MP3(song)
    global song_length
    song_length = song_mut.info.length

    # convert to time format
    converted_song_length = time.strftime("%M:%S", time.gmtime(song_length))
    # check if song is over
    if int(song_slider.get() == int(song_length)):
        stop()
    elif paused:
        # check if paused and if, pass
        pass
    else:
        # move slider along one second at a time
        next_time = int(song_slider.get()) + 1
        # output new time value to slider and to length of song
        song_slider.config(to=song_length, value=next_time)
        # convert slider position to time format
        converted_current_time = time.strftime("%M:%S", time.gmtime(int(song_slider.get())))
        #     out put slider
        status_bar.config(text=f'Time Played:{converted_current_time} of {converted_song_length}  ')

    # add time to status bar
    if current_time > 0:
        status_bar.config(text=f'Time Played:{converted_current_time} of {converted_song_length}  ')

    # loop to play every second
    status_bar.after(1000, play_time)


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
    # Delete Highlighted Song From Playlist
    playlist_box.delete(ANCHOR)


def delete_all_songs():
    playlist_box.delete(0, END)


#  create play, stop, pause, next,back functions

def play():
    # set stopped to false since a song is now playing
    global stopped
    stopped = False
    # reconstruct song with dir
    song = playlist_box.get(ACTIVE)
    song = f'C:/Users/LENOVO/PycharmProjects/mp3/audio/{song}.mp3'
    # my_label.config(text=song)
    # load and play song with pygame mixer
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    play_time()


# create stop variable
stopped = False


def stop():
    pygame.mixer.music.stop()
    #     clear playlist box
    playlist_box.selection_clear(ACTIVE)
    status_bar.config(text='')

#     set our slider to zero
    song_slider.config(value=0)

#     set stop variable to True
    global stopped
    stopped = True


def next_song():
    # reset slider position and status bar
    status_bar.config(text='')
    song_slider.config(value=0)
    #  correct song and num
    next_one = playlist_box.curselection()

    # adding 1 to the current selection
    next_one = next_one[0] + 1

    # get song from the playlist
    song = playlist_box.get(next_one)

    # add directory structure to the song title
    song = f'C:/Users/LENOVO/PycharmProjects/mp3/audio/{song}.mp3'

    # load and play song with pygame mixer
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    # clear active bar in playlist
    playlist_box.selection_clear(0, END)

    # Move active bar to the next song
    playlist_box.activate(next_one)

    # Set active bar to the next Song
    playlist_box.selection_set(next_one, last=None)


def previous_song():
    # reset slider position and status bar
    status_bar.config(text='')
    song_slider.config(value=0)
    #  correct song and num
    next_one = playlist_box.curselection()

    # adding 1 to the current selection
    next_one = next_one[0] - 1

    # get song from the playlist
    song = playlist_box.get(next_one)

    # add directory structure to the song title
    song = f'C:/Users/LENOVO/PycharmProjects/mp3/audio/{song}.mp3'

    # load and play song with pygame mixer
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    # clear active bar in playlist
    playlist_box.selection_clear(0, END)

    # Move active bar to the next song
    playlist_box.activate(next_one)

    # Set active bar to the next Song
    playlist_box.selection_set(next_one, last=None)


paused = False


def pause(is_paused):
    global paused
    paused = is_paused
    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True


# Create volume function and song slider function


def volume(x):
    pygame.mixer.music.set_volume(volume_slider.get())


def song_slide(x):
    # reconstruct song with dir
    song = playlist_box.get(ACTIVE)
    song = f'C:/Users/LENOVO/PycharmProjects/mp3/audio/{song}.mp3'
    # my_label.config(text=song)
    # load and play song with pygame mixer
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0, start=song_slider.get())


# Create main frame
main_frame = Frame(root)
main_frame.pack(pady=20)

# create volume slider frame
volume_frame = LabelFrame(main_frame, text="Volume")
volume_frame.grid(row=0, column=1, padx=15)

#  Create Playlist Box
playlist_box = Listbox(main_frame, bg="black", fg="green", width=60, selectbackground="red", selectforeground="yellow")
playlist_box.grid(row=0, column=0)

# create volume slider
volume_slider = ttk.Scale(volume_frame, from_=0, to=1, orient=VERTICAL, length=125, value=1, command=volume)
volume_slider.pack(pady=10)

# Create song slider
song_slider = ttk.Scale(main_frame, from_=0, to=100, orient=HORIZONTAL, length=360, value=0, command=song_slide)
song_slider.grid(row=2, column=0, pady=20)

# Define Button Images For Controls
back_btn_img = PhotoImage(file='images/back50.png')
forward_btn_img = PhotoImage(file='images/forward50.png')
play_btn_img = PhotoImage(file='images/play50.png')
pause_btn_img = PhotoImage(file='images/pause50.png')
stop_btn_img = PhotoImage(file='images/stop50.png')

# Create Button Frame
control_frame = Frame(main_frame)
control_frame.grid(row=1, column=0, pady=20)

# Create play and pause button
back_button = Button(control_frame, image=back_btn_img, borderwidth=0, command=previous_song)
forward_button = Button(control_frame, image=forward_btn_img, borderwidth=0, command=next_song)
play_button = Button(control_frame, image=play_btn_img, borderwidth=0, command=play)
pause_button = Button(control_frame, image=pause_btn_img, borderwidth=0, command=lambda: pause(paused))
stop_button = Button(control_frame, image=stop_btn_img, borderwidth=0, command=stop)

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

# create status bar
status_bar = Label(root, text='', bd=1, relief=GROOVE, anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=2)

# Temporary Label
my_label = Label(root, text='')
my_label.pack(pady=20)

root.mainloop()
