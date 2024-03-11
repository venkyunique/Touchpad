
from tkinter import *
import serial

ser = serial.Serial("COM9", baudrate=19200, timeout=5)

# file operations
file = open("swim.txt", "r")
cont = file.read()
cont = cont.split("\n")

lane1 = cont[0].split(",")
lane1_name = lane1[0]
lane1_state = lane1[1]

lane2 = cont[1].split(",")
lane2_name = lane2[0]
lane2_state = lane2[1]

lane3 = cont[2].split(",")
lane3_name = lane3[0]
lane3_state = lane3[1]

lane4 = cont[3].split(",")
lane4_name = lane4[0]
lane4_state = lane4[1]

lane5 = cont[4].split(",")
lane5_name = lane5[0]
lane5_state = lane5[1]

lane6 = cont[5].split(",")
lane6_name = lane6[0]
lane6_state = lane6[1]

lane7 = cont[6].split(",")
lane7_name = lane7[0]
lane7_state = lane7[1]

lane8 = cont[7].split(",")
lane8_name = lane8[0]
lane8_state = lane8[1]

file.close()

# info:
timervalue = "00:00:000"

player1_name = lane1_name
player1_lane = '1'
player1_time = "00:00:000"
player1_position = '1'
player1_state = lane1_state

player2_name = lane2_name
player2_lane = '2'
player2_time = "00:00:000"
player2_position = '2'
player2_state = lane2_state

player3_name = lane3_name
player3_lane = '3'
player3_time = "00:00:000"
player3_position = '3'
player3_state = lane3_state

player4_name = lane4_name
player4_lane = '4'
player4_time = "00:00:000"
player4_position = '4'
player4_state = lane4_state

player5_name = lane5_name
player5_lane = '5'
player5_time = "00:00:000"
player5_position = '5'
player5_state = lane5_state

player6_name = lane6_name
player6_lane = '6'
player6_time = "00:00:000"
player6_position = '6'
player6_state = lane6_state

player7_name = lane7_name
player7_lane = '7'
player7_time = "00:00:000"
player7_position = '7'
player7_state = lane7_state

player8_name = lane8_name
player8_lane = '8'
player8_time = "00:00:000"
player8_position = '8'
player8_state = lane8_state

window = Tk()
window.geometry("1920x1080")
window.configure(bg='#000')
window.title("KLH SWIM TIMER")

image_ = PhotoImage(file="swimbg.png")
imgLabel = Label(window, image=image_, bg='#148EE8').place(x=0, y=0, relwidth=1, relheight=1)

t = Label(window, text="______ KLH  SWIM  TIMER ______", font=('Century SchoolBook', 25, 'bold'), bg='#0C1472',
          fg="#fff",
          anchor="n", pady=20)
t.pack()

# icon = PhotoImage(file="klh.png")
# icon_label = Label(window, image=icon, bd=0).place(x=0, y=0)

# timer-------------------

stop_watch = Label(window, font=("arial", 30, "bold"), text=timervalue, fg='white', bg='#0C1472', height=2)
stop_watch.pack(anchor='e', padx=150)
# heading-----------------------
lane = Label(window, bg='#148EE8', height=3)
lane.pack(fill=X, pady=12)
lane_number = Label(lane, text="LANE", font=('Century Schoolbook', 20, 'bold'), bg='#148EE8', fg="white",
                    width=4).place(x=105, y=5)
lane_name = Label(lane, text="NAME", font=('Century Schoolbook', 20, 'bold'), bg='#148EE8', fg="white", width=20).place(
    x=200, y=5)
lane_state = Label(lane, text="STATE", font=('Century Schoolbook', 20, 'bold'), bg='#148EE8', fg="white",
                   width=20).place(x=550, y=5)
lane_time = Label(lane, text="TIME", font=('Century Schoolbook', 20, 'bold'), bg='#148EE8', fg="white", width=10).place(
    x=1000, y=5)
lane_position = Label(lane, text="POSITION", font=('Century Schoolbook', 20, 'bold'), bg='#148EE8', fg="white",
                      width=8).place(x=1250,
                                     y=5)
# table information-------------------------
label1 = Label(window, bg='#0C1472', height=3)
label1.pack(fill=X)
lane1_time = Label(window, text=player1_time, font=('Century Schoolbook', 20, 'bold'), bg='#0C1472', fg="white",
                   width=10)
lane1_time.place(x=1000, y=260)
lane1_number = Label(label1, text=player1_lane, font=('Century Schoolbook', 20, 'bold'), bg='#0C1472', fg="white",
                     width=4)
lane1_number.place(x=105, y=5)
lane1_name = Label(label1, text=player1_name, font=('Century Schoolbook', 20, 'bold'), bg="#0C1472", fg="white",
                   width=20)
lane1_name.place(x=200, y=5)
lane1_state = Label(label1, text=player1_state, font=('Century Schoolbook', 20, 'bold'), bg='#0C1472', fg="white",
                    width=20)
lane1_state.place(x=550, y=5)
lane1_position = Label(window, font=('Century Schoolbook', 20, 'bold'), bg='#0C1472', fg="white", width=8)
lane1_position.place(x=1250, y=260)

label2 = Label(window, bg='#148EE8', fg="white", height=3)
label2.pack(fill=X, pady=5)
lane2_number = Label(label2, text=player2_lane, font=('Century Schoolbook', 20, 'bold'), bg='#148EE8', fg="white",
                     width=4)
lane2_number.place(x=105, y=5)
lane2_name = Label(label2, text=player2_name, font=('Century Schoolbook', 20, 'bold'), bg='#148EE8', fg="white",
                   width=20)
lane2_name.place(x=200, y=5)
lane2_state = Label(label2, text=player2_state, font=('Century Schoolbook', 20, 'bold'), bg='#148EE8', fg="white",
                    width=20)
lane2_state.place(x=550, y=5)
lane2_time = Label(label2, text=player2_time, font=('Century Schoolbook', 20, 'bold'), bg='#148EE8', fg="white",
                   width=10)
lane2_time.place(x=1000, y=5)
lane2_position = Label(label2, font=('Century Schoolbook', 20, 'bold'), bg='#148EE8', fg="white", width=8)
lane2_position.place(x=1250, y=5)
label3 = Label(window, bg='#0C1472', fg="white", height=3)
label3.pack(fill=X, pady=0)
lane3_number = Label(label3, text=player3_lane, font=('Century Schoolbook', 20, 'bold'), bg='#0C1472', fg="white",
                     width=4)
lane3_number.place(x=105, y=5)
lane3_name = Label(label3, text=player3_name, font=('Century Schoolbook', 20, 'bold'), bg='#0C1472', fg="white",
                   width=20)
lane3_name.place(x=200, y=5)
lane3_state = Label(label3, text=player3_state, font=('Century Schoolbook', 20, 'bold'), bg='#0C1472', fg="white",
                    width=20)
lane3_state.place(x=550, y=5)
lane3_time = Label(label3, text=player3_time, font=('Century Schoolbook', 20, 'bold'), bg='#0C1472', fg="white",
                   width=10)
lane3_time.place(x=1000, y=5)
lane3_position = Label(label3, font=('Century Schoolbook', 20, 'bold'), bg='#0C1472', fg="white", width=8)
lane3_position.place(x=1250, y=5)


label4 = Label(window, bg='#148EE8', fg="white", height=3)
label4.pack(fill=X, pady=5)
lane4_number = Label(label4, text=player4_lane, font=('Century Schoolbook', 20, 'bold'), bg='#148EE8', fg="white",
                     width=4)
lane4_number.place(x=105, y=5)
lane4_name = Label(label4, text=player4_name, font=('Century Schoolbook', 20, 'bold'), bg='#148EE8', fg="white",
                   width=20)
lane4_name.place(x=200, y=5)
lane4_state = Label(label4, text=player4_state, font=('Century Schoolbook', 20, 'bold'), bg='#148EE8', fg="white",
                    width=20)
lane4_state.place(x=550, y=5)
lane4_time = Label(label4, text=player4_time, font=('Century Schoolbook', 20, 'bold'), bg='#148EE8', fg="white",
                   width=10)
lane4_time.place(x=1000, y=5)
lane4_position = Label(label4, font=('Century Schoolbook', 20, 'bold'), bg='#148EE8', fg="white", width=8)
lane4_position.place(x=1250, y=5)
label5 = Label(window, bg='#0C1472', fg="white", height=3)
label5.pack(fill=X)
lane5_number = Label(label5, text=player5_lane, font=('Century Schoolbook', 20, 'bold'), bg='#0C1472', fg="white",
                     width=4)
lane5_number.place(x=105, y=5)
lane5_name = Label(label5, text=player5_name, font=('Century Schoolbook', 20, 'bold'), bg='#0C1472', fg="white",
                   width=20)
lane5_name.place(x=200, y=5)
lane5_state = Label(label5, text=player5_state, font=('Century Schoolbook', 20, 'bold'), bg='#0C1472', fg="white",
                    width=20)
lane5_state.place(x=550, y=5)
lane5_time = Label(label5, text=player5_time, font=('Century Schoolbook', 20, 'bold'), bg='#0C1472', fg="white",
                   width=10)
lane5_time.place(x=1000, y=5)
lane5_position = Label(label5, font=('Century Schoolbook', 20, 'bold'), bg='#0C1472', fg="white", width=8)
lane5_position.place(x=1250, y=5)

label6 = Label(window, bg='#148EE8', fg="white", height=3)
label6.pack(fill=X, pady=5)
lane6_number = Label(label6, text=player6_lane, font=('Century Schoolbook', 20, 'bold'), bg='#148EE8', fg="white",
                     width=4)
lane6_number.place(x=105, y=5)
lane6_name = Label(label6, text=player6_name, font=('Century Schoolbook', 20, 'bold'), bg='#148EE8', fg="white",
                   width=20)
lane6_name.place(x=200, y=5)
lane6_state = Label(label6, text=player6_state, font=('Century Schoolbook', 20, 'bold'), bg='#148EE8', fg="white",
                    width=20)
lane6_state.place(x=550, y=5)
lane6_time = Label(label6, text=player6_time, font=('Century Schoolbook', 20, 'bold'), bg='#148EE8', fg="white",
                   width=10)
lane6_time.place(x=1000, y=5)
lane6_position = Label(label6, font=('Century Schoolbook', 20, 'bold'), bg='#148EE8', fg="white", width=8)
lane6_position.place(x=1250, y=5)
label7 = Label(window, bg='#0C1472', fg="white", height=3)
label7.pack(fill=X)
lane7_number = Label(label7, text=player7_lane, font=('Century Schoolbook', 20, 'bold'), bg='#0C1472', fg="white",
                     width=4)
lane7_number.place(x=105, y=5)
lane7_name = Label(label7, text=player7_name, font=('Century Schoolbook', 20, 'bold'), bg='#0C1472', fg="white",
                   width=20)
lane7_name.place(x=200, y=5)
lane7_state = Label(label7, text=player7_state, font=('Century Schoolbook', 20, 'bold'), bg='#0C1472', fg="white",
                    width=20)
lane7_state.place(x=550, y=5)
lane7_time = Label(label7, text=player7_time, font=('Century Schoolbook', 20, 'bold'), bg='#0C1472', fg="white",
                   width=10)
lane7_time.place(x=1000, y=5)
lane7_position = Label(label7, font=('Century Schoolbook', 20, 'bold'), bg='#0C1472', fg="white", width=8)
lane7_position.place(x=1250, y=5)

label8 = Label(window, bg='#148EE8', fg="white", height=3)
label8.pack(fill=X, pady=5)
lane8_number = Label(label8, text=player8_lane, font=('Century Schoolbook', 20, 'bold'), bg='#148EE8', fg="white",
                     width=4)
lane8_number.place(x=105, y=5)
lane8_name = Label(label8, text=player8_name, font=('Century Schoolbook', 20, 'bold'), bg='#148EE8', fg="white",
                   width=20)
lane8_name.place(x=200, y=5)
lane8_state = Label(label8, text=player8_state, font=('Century Schoolbook', 20, 'bold'), bg='#148EE8', fg="white",
                    width=20)
lane8_state.place(x=550, y=5)
lane8_time = Label(label8, text=player8_time, font=('Century Schoolbook', 20, 'bold'), bg='#148EE8', fg="white",
                   width=10)
lane8_time.place(x=1000, y=5)
lane8_position = Label(label8, font=('Century Schoolbook', 20, 'bold'), bg='#148EE8', fg="white", width=8)
lane8_position.place(x=1250, y=5)

file1 = open("result.txt", "w")


def updategui():
    x = ser.readline().decode()
    # y = x
    if len(x) != 0:
        data = x.split()
        print(data)
        if data[0] == '#':
            stop_watch['text'] = data[1]
        elif data[0] == '$':
            file1.close()
        else:
            if data[1] == '1':
                # print(data[3])
                lane1_time['text'] = data[2]
                lane1_position['text'] = data[3]
                file1.write("1," + lane1[0] + "," + lane1[1] + "," + data[2] + "," + data[3] + "\n")
            elif data[1] == '2':
                # print(data[3])
                lane2_time['text'] = data[2]
                lane2_position['text'] = data[3]
                file1.write("2," + lane2[0] + "," + lane2[1] + "," + data[2] + "," + data[3] + "\n")
            elif data[1] == '3':
                lane3_time.configure(text=data[2])
                lane3_position.configure(text=data[3])
                file1.write("3," + lane3[0] + "," + lane3[1] + "," + data[2] + "," + data[3] + "\n")
            elif data[1] == '4':
                lane4_time.configure(text=data[2])
                lane4_position.configure(text=data[3])
                file1.write("4," + lane4[0] + "," + lane4[1] + "," + data[2] + "," + data[3] + "\n")
            elif data[1] == '5':
                lane5_time.configure(text=data[2])
                lane5_position.configure(text=data[3])
                file1.write("5," + lane5[0] + "," + lane5[1] + "," + data[2] + "," + data[3] + "\n")
            elif data[1] == '6':
                lane6_time.configure(text=data[2])
                lane6_position.configure(text=data[3])
                file1.write("6," + lane6[0] + "," + lane6[1] + "," + data[2] + "," + data[3] + "\n")
            elif data[1] == '7':
                lane7_time.configure(text=data[2])
                lane7_position.configure(text=data[3])
                file1.write("7," + lane7[0] + "," + lane7[1] + "," + data[2] + "," + data[3] + "\n")
            elif data[1] == '8':
                lane8_time.configure(text=data[2])
                lane8_position.configure(text=data[3])
                file1.write("8," + lane8[0] + "," + lane8[1] + "," + data[2] + "," + data[3] + "\n")

    window.after(1, updategui)


updategui()
window.mainloop()
