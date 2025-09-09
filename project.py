from customtkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox, PhotoImage
from customtkinter import CTk, CTkButton, CTkLabel, CTkScrollableFrame, CTkImage
import webbrowser, ast

icon_path = "lizcoach.ico"
gender_data = 'Male'

def load_data():
    data = {}
    with open('data.txt', 'r') as f:
        lines = f.readlines()
    for line in lines:
        if ':' in line:
                key,value = line.strip().split(':', 1)
                data[key.strip()] = value.strip()
    return data

def save_user():
    if nameEntry.get() == " " or ageEntry.get() == " " or weightEntry.get() == " " or heightEntry.get() == " ":
        messagebox.showerror(title='LizCoach',
                             message='Fill each line!')
        return

    try:
        age = int(ageEntry.get())
    except ValueError:
        messagebox.showerror(title='LizCoach',
                             message='Age must be an integer.')
        return

    try:
        weight = int(weightEntry.get())

    except ValueError:
        messagebox.showerror(title='LizCoach',
                             message='Weight must be an integer.')
        return

    try:
        height = int(heightEntry.get())

    except ValueError:
        messagebox.showerror(title='LizCoach',
                             message='Height must be an integer.')
        return

    if age < 14 or age > 40:
        messagebox.showerror('LizCoach',
                             'Age must be between 14 and 40.')
        return

    gender_data = genderBox.get()

    user_data = (
        f"Name: {nameEntry.get()}\n"
        f"Age: {ageEntry.get()}\n"
        f"Weight: {weightEntry.get()}\n"
        f"Height: {heightEntry.get()}\n"
        f"Gender: {gender_data}\n"
    )

    with open('data.txt', 'w') as file:
        file.write(user_data)

    messagebox.showinfo("LizCoach", f"User data saved successfully\n"
                                    f"\n{user_data}")
    app.destroy()
    open_menu()

def close_and_open_menu(current_page):
    current_page.destroy()
    open_menu()

def open_menu():
    menu_window = CTk()
    menu_window.title("LizCoach Menu")
    menu_window.geometry("380x380")
    menu_window.iconbitmap(icon_path)
    menu_window.configure(fg_color="#101217")
    menu_window.resizable(False, False)

    buttonFrame = CTkFrame(menu_window,
                           fg_color="#23272D",
                           width=250,
                           height=293)
    buttonFrame.pack(pady=40, padx=20)
    buttonFrame.pack_propagate(False)


    main_menu = CTkLabel(buttonFrame,
                         text= f"Menu for {gender_data}",
                         font=("Cooper Black", 23),
                         text_color="#FF3399")
    main_menu.pack(pady=20)

    workout_click = CTkButton(buttonFrame,
                              text="Workout",
                              font=("Arial", 15, "bold"),
                              corner_radius=15, height=40, width=200,
                              fg_color="#C850C0", hover_color="#FF3399",
                              text_color="#FFFFFF",
                              command=lambda: workout_open(menu_window))  # Pass menu_window
    workout_click.pack(pady=(15, 12), padx=10)

    calculator_click = CTkButton(buttonFrame,
                                 text="Calories Calculator",
                                 font=("Arial", 15, "bold"),
                                 corner_radius=15, height=40, width=200,
                                 fg_color="#C850C0", hover_color="#FF3399",
                                 text_color="#FFFFFF",
                                 command=lambda: calculator_open(menu_window))
    calculator_click.pack(pady= (15, 12), padx=10)

    genderchanger_click = CTkButton(buttonFrame,
                                    text="Change Gender",
                                    font=("Arial", 15, "bold"),
                                    corner_radius=15, height=40, width=200,
                                    fg_color="#C850C0", hover_color="#FF3399",
                                    text_color="#FFFFFF",
                                    command= lambda: genderchanger_open(menu_window))
    genderchanger_click.pack(pady=(15, 12), padx=10)

    menu_window.mainloop()

def genderchanger_open(menu_window):
    menu_window.destroy()

    genderchanger_page = CTk()
    genderchanger_page.title("Gender Changer")
    genderchanger_page.geometry("370x370")
    genderchanger_page.iconbitmap(icon_path)
    genderchanger_page.configure(fg_color="#101217")
    genderchanger_page.resizable(False, False)

    genderchanger_frame = CTkFrame(genderchanger_page, fg_color='#23272D', width=265, height=300)
    genderchanger_frame.pack(pady=35, padx=20)
    genderchanger_frame.pack_propagate(False)

    title_label = CTkLabel(
        genderchanger_frame,
        text="Select your gender",
        font=("Cooper Black", 23),
        text_color="#FF3399"
    )
    title_label.pack(pady=(15, 10))

    CTkLabel(genderchanger_frame, text="Update",
             font=("Cooper Black", 19)).pack(pady=8, padx=10)

    def change_gender(new_gender):
        global gender_data
        gender_data = new_gender

        data = load_data()
        data['Gender'] = new_gender

        with open('data.txt', 'w') as file:
            for key, value in data.items():
                file.write(f"{key}: {value}\n")

        genderchanger_page.destroy()
        open_menu()

    CTkButton(
        genderchanger_frame,
        text="Male",
        text_color="#FFFFFF",
        font=("Arial", 15),
        fg_color="#C850C0",
        hover_color="#FF3399",
        command=lambda: change_gender("Male")
    ).pack(pady=10, padx=10)

    CTkButton(
        genderchanger_frame,
        text="Female",
        font=("Arial", 15),
        text_color="#FFFFFF",
        fg_color="#C850C0",
        hover_color="#FF3399",
        command=lambda: change_gender("Female")
    ).pack(pady=10, padx=10)

    back_button = CTkButton(
        genderchanger_frame,
        text="Back",
        font=("Arial", 13, "bold"),
        corner_radius=15,
        height=40,
        width=100,
        text_color="#FF3399",
        fg_color="#FFFFFF",
        hover_color="#C850C0",
        command=lambda: close_and_open_menu(genderchanger_page)
    )
    back_button.pack(pady=(30, 30))

    genderchanger_page.mainloop()

def workout_open(menu_window):
    global gender_data

    menu_window.destroy()

    workout_page = CTk()
    workout_page.title("LizCoach Workout")
    workout_page.geometry("400x415")
    workout_page.iconbitmap(icon_path)
    workout_page.configure(fg_color="#101217")
    workout_page.resizable(False, False)

    workout_frame = CTkFrame(workout_page, fg_color=None, width=260, height=300)
    workout_frame.pack(pady=30, padx=20)
    workout_frame.pack_propagate(False)

    title_label = CTkLabel(workout_frame,
                           text=f"Workouts for {gender_data}",
                           font=("Cooper Black", 20),
                           text_color="#FF3399")
    title_label.pack(pady=10)

    hand_button = CTkButton(workout_frame,
                            text="Hands",
                            font=("Arial", 15, "bold"),
                            corner_radius=15, height=40, width=200,
                            fg_color="#C850C0", hover_color="#FF3399",
                            text_color="#FFFFFF",
                            command=lambda: hand_open(workout_page, gender_data))
    hand_button.pack(pady=(10, 10))

    leg_button = CTkButton(workout_frame,
                           text="Legs",
                           font=("Arial", 15, "bold"),
                           corner_radius=15, height=40, width=200,
                           fg_color="#C850C0", hover_color="#FF3399",
                           text_color="#FFFFFF",
                           command=lambda: leg_open(workout_page, gender_data))
    leg_button.pack(pady=(10, 10))

    stomach_button = CTkButton(workout_frame,
                               text="Stomach",
                               font=("Arial", 15, "bold"),
                               corner_radius=15, height=40, width=200,
                               fg_color="#C850C0", hover_color="#FF3399",
                               text_color="#FFFFFF",
                               command=lambda: stomach_open(workout_page, gender_data))
    stomach_button.pack(pady=(10, 10))

    body_button = CTkButton(workout_frame,
                            text="Body",
                            font=("Arial", 15, "bold"),
                            corner_radius=15, height=40, width=200,
                            fg_color="#C850C0", hover_color="#FF3399",
                            text_color="#FFFFFF",
                            command=lambda: body_open(workout_page, gender_data))
    body_button.pack(pady=(10, 10))

    exit_button = CTkButton(workout_page,
                            text="Back",
                            font=("Arial", 14, "bold"),
                            corner_radius=15, height=40, width=100,
                            fg_color="#C850C0", hover_color="#FF3399",
                            text_color="#FFFFFF",
                            command=lambda: close_and_open_menu(workout_page))
    exit_button.pack(pady=(0, 10))

    workout_page.mainloop()

# Workout functions

def open_youtube_link(url):
    webbrowser.open(url)

def hand_open(workout_page, gender):
    workout_page.destroy()
    hand_page = CTk()
    hand_page.title("Hand workouts")
    hand_page.geometry("400x400")
    hand_page.iconbitmap(icon_path)
    hand_page.configure(fg_color="#101217")
    hand_page.resizable(False, False)

    title_label = CTkLabel(hand_page, text="Exercises", font=("Cooper Black", 30), text_color="#FF3399")
    title_label.pack(pady=10)

    h_frame = CTkFrame(hand_page, fg_color="#23272D")
    h_frame.pack(expand=True, fill="both", padx=10, pady=5)
    h_frame.pack_propagate(False)

    if gender == 'Female':
        exercises = [
            ("1.. Push-ups", "https://www.youtube.com/watch?v=tWjBnQX3if0"),
            ("2.. Tricep Dips", "https://www.youtube.com/watch?v=89_spgcdQlw"),
            ("3.. Dumbbell Bicep Curls", "https://www.youtube.com/shorts/YEyFdtni3uU"),
            ("4.. Arm Circles", "https://www.youtube.com/watch?v=kfP_9z-BtmA"),
            ("5.. Plank Shoulder Taps", "https://www.youtube.com/watch?v=8rgurWd-PB8")
        ]
    else:
        exercises = [
            ("1.. Push-ups", "https://www.youtube.com/watch?v=I9fsqKE5XHo"),
            ("2.. Tricep Dips", "https://www.youtube.com/watch?v=yN6Q1UI_xkE&t=105s"),
            ("3.. Dumbbell Bicep Curls", "https://www.youtube.com/watch?v=Zjv0tiMjkJU"),
            ("4.. Arm Circles", "https://www.youtube.com/watch?v=kfP_9z-BtmA"),
            ("5.. Plank Shoulder Taps", "https://www.youtube.com/watch?v=sUHHw35YTKU")
        ]

    for i, (exercise, url) in enumerate(exercises):
        parts = exercise.split('. ')
        number = parts[0]
        text = parts[1]

        CTkLabel(h_frame, text=number,
                 font=('Cooper Black', 20),
                 text_color="#FFFFFF").grid(row=i, column=0, padx=10, pady=10, sticky="e")
        exercise_label = CTkLabel(h_frame, text=text,
                                  font=('Cooper Black', 20, 'underline'),
                                  cursor="hand2",
                                  text_color="#00A8E8")
        exercise_label.grid(row=i, column=1, padx=10, pady=10, sticky="w")

        exercise_label.bind("<Button-1>", lambda e, url=url: open_youtube_link(url))

    button_frame = CTkFrame(hand_page, fg_color="#101217")
    button_frame.pack(side="bottom", pady=10)

    CTkButton(button_frame, text="Back", font=('Arial', 13, 'bold'),
              corner_radius=15,
              height=35, width=150,
              hover_color='#FF3399',
              fg_color='#C850C0',
              command=lambda: workout_open(hand_page)).grid(row=0, column=0, padx=20)

    CTkButton(button_frame, text="Close",
              font=('Arial', 13, 'bold'),
              corner_radius=15,
              height=35, width=150,
              hover_color='#FF3399',
              fg_color='#C850C0',
              command=lambda: close_and_open_menu(hand_page)).grid(row=0, column=1, padx=20)

    hand_page.mainloop()

def leg_open(workout_page, gender):
    workout_page.destroy()

    leg_page = CTk()
    leg_page.title("Leg workouts")
    leg_page.geometry("400x400")
    leg_page.iconbitmap(icon_path)
    leg_page.configure(fg_color="#101217")
    leg_page.resizable(False, False)

    title_label = CTkLabel(leg_page,
                           text="Exercises",
                           font=("Cooper Black", 30),
                           text_color="#FF3399")
    title_label.pack(pady=10)

    # Frame creating for implement
    l_frame = CTkFrame(leg_page, fg_color="#23272D")
    l_frame.pack(expand=True, fill="both", padx=10, pady=5)
    l_frame.pack_propagate(False)

    if gender == 'Female':
        exercises = [
            ("1.. Squats", "https://www.youtube.com/watch?v=xqvCmoLULNY"),
            ("2.. Lunges", "https://youtu.be/BbExjzx75Hs?si=f88uRbJMZU7TMLjU"),
            ("3.. Calf Raises", "https://youtu.be/Wp4BlxcFTkE?si=jAeJfkNAKtcx54AL"),
            ("4.. Steps Up", "https://www.youtube.com/watch?v=kkg0acmHXDI"),
            ("5.. Leg Raises (Side)", "https://www.youtube.com/watch?v=pNismoYr1Fg")
        ]
    else:
        exercises = [
            ("1. Squats", "https://www.youtube.com/watch?v=HFnSsLIB7a4&t=159s"),
            ("2. Lunges", "https://www.youtube.com/watch?v=Z6R8A5tcrTc"),
            ("3. Calf Raises", "https://www.youtube.com/watch?v=1qfb2pUzYRI"),
            ("4.. Steps Up", "https://www.youtube.com/watch?v=IeROFxPkXG8"),
            ("5.. Leg Raises (Side)", "https://www.youtube.com/watch?v=JRmu-BJw698")
        ]

    for i, (exercise, url) in enumerate(exercises):
        parts = exercise.split('. ')
        number = parts[0]
        text = parts[1]

        CTkLabel(l_frame, text=number,
                 font=('Cooper Black', 20),
                 text_color="#FFFFFF").grid(row=i, column=0, padx=10, pady=10, sticky="e")
        exercise_label = CTkLabel(l_frame, text=text,
                                  font=('Cooper Black', 20, 'underline'),
                                  cursor="hand2",
                                  text_color="#00A8E8")
        exercise_label.grid(row=i, column=1, padx=10, pady=10, sticky="w")

        exercise_label.bind("<Button-1>", lambda e, url=url: open_youtube_link(url))

    button_frame = CTkFrame(leg_page, fg_color="#101217")
    button_frame.pack(side="bottom", pady=10)

    CTkButton(button_frame, text="Back", font=('Arial', 13, 'bold'),
              corner_radius=15,
              height=35, width=150,
              hover_color='#FF3399',
              fg_color='#C850C0',
              command=lambda: workout_open(leg_page)).grid(row=0, column=0, padx=20)

    CTkButton(button_frame, text="Close",
              font=('Arial', 13, 'bold'),
              corner_radius=15,
              height=35, width=150,
              hover_color='#FF3399',
              fg_color='#C850C0',
              command=lambda: close_and_open_menu(leg_page)).grid(row=0, column=1, padx=20)
    leg_page.mainloop()

def stomach_open(workout_page, gender):
    workout_page.destroy()

    stomach_page = CTk()
    stomach_page.title("Belly workouts")
    stomach_page.geometry("400x400")
    stomach_page.iconbitmap(icon_path)
    stomach_page.configure(fg_color="#101217")
    stomach_page.resizable(False, False)

    title_label = CTkLabel(stomach_page,
                           text="Exercises",
                           font=("Cooper Black", 30),
                           text_color="#FF3399")
    title_label.pack(pady=10)

    # Frame creating for implement
    s_frame = CTkFrame(stomach_page, fg_color="#23272D")
    s_frame.pack(expand=True, fill="both", padx=10, pady=5)
    s_frame.pack_propagate(False)

    if gender == 'Female':
        exercises = [
            ("1.. Flutter Kicks", "https://www.youtube.com/watch?v=ZB1SwBRVLCc"),
            ("2.. Russian Twists", "https://www.youtube.com/watch?v=NeAtimSCxsY"),
            ("3.. Leg Raises", "https://youtu.be/6b1hu6iSqok?si=zVG66CxS0uH6niny"),
            ("4.. Mountain Climbers", "https://www.youtube.com/watch?v=cnyTQDSE884&t=5s"),
            ("5.. Bicycle Crunches", "https://www.youtube.com/watch?v=wnuLak2onoA")
        ]
    else:
        exercises = [
            ("1.. Flutter Kicks", "https://www.youtube.com/watch?v=ZB1SwBRVLCc"),
            ("2.. Russian Twists", "https://www.youtube.com/watch?v=FbXyZZLEKzg"),
            ("3.. Leg Raises", "https://youtu.be/6b1hu6iSqok?si=zVG66CxS0uH6niny"),
            ("4.. Mountain Climbers", "https://www.youtube.com/watch?v=ruQ4ZwncXBg"),
            ("5.. Bicycle Crunches", "https://www.youtube.com/watch?v=cbKIDZ_XyjY")
        ]

    for i, (exercise, url) in enumerate(exercises):
        parts = exercise.split('. ')
        number = parts[0]
        text = parts[1]

        CTkLabel(s_frame, text=number,
                 font=('Cooper Black', 20),
                 text_color="#FFFFFF").grid(row=i, column=0, padx=10, pady=10, sticky="e")
        exercise_label = CTkLabel(s_frame, text=text,
                                  font=('Cooper Black', 20, 'underline'),
                                  cursor="hand2",
                                  text_color="#00A8E8")
        exercise_label.grid(row=i, column=1, padx=10, pady=10, sticky="w")

        exercise_label.bind("<Button-1>",
                            lambda e, url=url: open_youtube_link(url))

    button_frame = CTkFrame(stomach_page, fg_color="#101217")
    button_frame.pack(side="bottom", pady=10)

    CTkButton(button_frame,
              text="Back",
              font=('Arial', 13, 'bold'),
              corner_radius=15,
              height=35, width=150,
              hover_color='#FF3399',
              fg_color='#C850C0',
              command=lambda: workout_open(stomach_page)).grid(row=0, column=0, padx=20)
    CTkButton(button_frame,
              text="Close",
              font=('Arial', 13, 'bold'),
              corner_radius=15,
              height=35, width=150,
              hover_color='#FF3399',
              fg_color='#C850C0',
              command=lambda: close_and_open_menu(stomach_page)).grid(row=0, column=1, padx=20)
    stomach_page.mainloop()

def body_open(workout_page, gender):
    workout_page.destroy()

    body_page = CTk()
    body_page.title("Body workouts")
    body_page.geometry("400x400")
    body_page.iconbitmap(icon_path)
    body_page.configure(fg_color="#101217")
    body_page.resizable(False, False)

    title_label = CTkLabel(body_page, text="Body Exercises", font=("Cooper Black", 30), text_color="#FF3399")
    title_label.pack(pady=10)

    b_frame = CTkFrame(body_page, fg_color="#23272D")
    b_frame.pack(expand=True, fill="both", padx=10, pady=20)
    b_frame.pack_propagate(False)

    if gender == 'Female':
        exercises = [
            ("1.. Heel touches", "https://www.youtube.com/watch?v=_xkkdocladU"),
            ("2.. Crunches", "https://www.youtube.com/watch?v=0t4t3IpiEao"),
            ("3.. Jumping Jacks", "https://www.youtube.com/watch?v=digpucxFbMo"),
            ("4.. Burpees", "https://www.youtube.com/watch?v=qLBImHhCXSw"),
            ("5.. High Knees", "https://www.youtube.com/watch?v=ZNDHivUg7vA")
        ]
    else:
        exercises = [
            ("1.. Heel touches", "https://www.youtube.com/watch?v=fLajmFLpJ_w"),
            ("2.. Crunches", "https://www.youtube.com/watch?v=5ER5Of4MOPI&t=42s"),
            ("3.. Jumping Jacks", "https://www.youtube.com/watch?v=-O7z3ilCu-s"),
            ("4.. Burpees", "https://www.youtube.com/watch?v=xQdyIrSSFnE"),
            ("5.. High Knees", "https://www.youtube.com/watch?v=VGb_fJ81yWc")
        ]

    for i, (exercise, url) in enumerate(exercises):
        parts = exercise.split('. ')
        number = parts[0]
        text = parts[1]

        CTkLabel(b_frame, text=number,
                 font=('Cooper Black', 20),
                 text_color="#FFFFFF").grid(row=i, column=0, padx=10, pady=10, sticky="e")
        exercise_label = CTkLabel(b_frame, text=text,
                                  font=('Cooper Black', 20, 'underline'),
                                  cursor="hand2",
                                  text_color="#00A8E8")
        exercise_label.grid(row=i, column=1, padx=10, pady=10, sticky="w")

        exercise_label.bind("<Button-1>", lambda e, url=url: open_youtube_link(url))

    button_frame = CTkFrame(body_page, fg_color="#101217")
    button_frame.pack(side="bottom", pady=10)

    CTkButton(button_frame, text="Back", font=('Arial', 13, 'bold'),
              corner_radius=15,
              height=35, width=150,
              hover_color='#FF3399',
              fg_color='#C850C0',
              command=lambda: workout_open(body_page)).grid(row=0, column=0, padx=20)

    CTkButton(button_frame, text="Close",
              font=('Arial', 13, 'bold'),
              corner_radius=15,
              height=35, width=150,
              hover_color='#FF3399',
              fg_color='#C850C0',
              command=lambda: close_and_open_menu(body_page)).grid(row=0, column=1, padx=20)
    body_page.mainloop()

#End of functions

def close_and_open_calculatorpage(current_page):
    current_page.destroy()

#Calculator functions

def calculator_open(menu_window):
    menu_window.destroy()

    calculator_page = CTk()
    calculator_page.title("Calculator Menu")
    calculator_page.geometry("400x415")
    calculator_page.iconbitmap(icon_path)
    calculator_page.configure(fg_color = "#101217")
    calculator_page.resizable(False, False)

    calculator_frame = CTkFrame(calculator_page, fg_color="#23272D", width=270, height=320)
    calculator_frame.pack(pady=(20, 20), padx = 30)
    calculator_frame.pack_propagate(False)

    title_label = CTkLabel(calculator_frame,
                           text = "Choose your focus:",
                           font = ("Cooper Black", 20),
                           text_color="#FF3399")
    title_label.pack(pady=10)

    productslist_button = CTkButton(calculator_frame,
                                    text="Product List",
                                    font=('Arial', 15, 'bold'),
                                    corner_radius=15, height=40, width=200,
                                    fg_color='#C850C0', hover_color='#FF3399',
                                    text_color = '#FFFFFF',
                                    command = lambda: products_open(calculator_page))
    productslist_button.pack(pady=(10, 10))

    addproduct_button = CTkButton(calculator_frame,
                                  text="Add Product",
                                  font=('Arial', 15, 'bold'),
                                  corner_radius=15, height=40, width=200,
                                  fg_color='#C850C0', hover_color='#FF3399',
                                  text_color = '#FFFFFF',
                                  command = lambda: addproduct_open(calculator_page))
    addproduct_button.pack(pady=(10, 10))

    ccalculator_button = CTkButton(calculator_frame,
                                  text="Calculate Calories",
                                  font=('Arial', 15, 'bold'),
                                  corner_radius=15, height=40, width=200,
                                  fg_color='#C850C0', hover_color='#FF3399',
                                  text_color = '#FFFFFF',
                                  command = lambda: ccalculator_open(calculator_page))
    ccalculator_button.pack(pady=(10, 10))

    total_button = CTkButton(calculator_frame,
                             text="Total Calories Calculated",
                             font=('Arial', 15, 'bold'),
                             corner_radius=15, height=40, width=200,
                             fg_color='#C850C0', hover_color='#FF3399',
                             text_color = '#FFFFFF',
                             command = lambda: total_open(calculator_page))
    total_button.pack(pady=(10, 10))

    back_button = CTkButton(calculator_page, text="Back",
                            font=('Arial', 14, 'bold'),
                            corner_radius=15, height=40, width=100,
                            fg_color='#FFFFFF', hover_color='#C850C0',
                            text_color = '#FF3399',
                            command = lambda: close_and_open_menu(calculator_page))
    back_button.pack(padx=5, pady=0)

    calculator_page.mainloop()

added_products = {}

def products_open(calculator_page):
    calculator_page.destroy()

    products_page = CTk()
    products_page.title("Products")
    products_page.geometry("400x415")
    products_page.iconbitmap(icon_path)
    products_page.configure(fg_color = "#101217")
    products_page.resizable(False, False)

    CTkLabel(products_page, text = "Main product types", text_color = "#FF3399",font = ("Cooper Black", 25)).pack(pady=(30, 10))
    products_frame = CTkScrollableFrame(products_page, width=260, height=300, label_text_color="#FFFFFF")
    products_frame.pack(pady=30, padx=20)

    def fruits_open():
        products_page.destroy()

        fruits_page = CTk()
        fruits_page.title("List of Products")
        fruits_page.geometry("400x415")
        fruits_page.iconbitmap(icon_path)
        fruits_page.configure(fg_color = "#101217")
        fruits_page.resizable(False, False)

        CTkLabel(fruits_page, text="Fruits List", text_color="#FF3399", font=("Cooper Black", 25)).pack(pady=(30, 10))
        CTkLabel(fruits_page, text = 'per 1 fruit', text_color="#FFFFFF", font=("Cooper Black", 20)).pack(pady=(10, 10))
        fruits_frame = CTkScrollableFrame(fruits_page, width=260, height=300, label_text_color="#FFFFFF")
        fruits_frame.pack(pady=30, padx=20)

        fruits_list = {
            'apple': 52,
            'grapes': 69,
            'orange': 47,
            'banana': 89,
            'kiwi': 61,
            'pineapple': 50,
            'peach': 57,
            'pomegranate': 83,
            'raspberries': 52,
            'mango': 60,
            'cherry': 50,
            'pear': 57,
            'watermelon': 30,
            'blackberry': 43,
            'apricot': 48
        }
        for key, value in fruits_list.items():
            title_label = CTkLabel(fruits_frame, text=f"{key} - {value} calories", text_color="#FFFFFF", font=("Arial", 14))
            title_label.pack(pady=(30, 10))

        back_button = CTkButton(fruits_frame, text="Back",
                                font=('Arial', 14, 'bold'),
                                corner_radius=15, height=50, width=100,
                                fg_color='#FFFFFF', hover_color='#C850C0',
                                text_color='#FF3399',
                                command=lambda: products_open(fruits_page))
        back_button.pack(pady=30)

        fruits_page.mainloop()

    def vegetables_open():
        products_page.destroy()

        vegetables_page = CTk()
        vegetables_page.title("Vegetables")
        vegetables_page.geometry("400x415")
        vegetables_page.iconbitmap("lizcoach.ico")
        vegetables_page.configure(fg_color="#101217")
        vegetables_page.resizable(False, False)

        CTkLabel(vegetables_page, text="List of vegetables", text_color="#FF3399", font=("Cooper Black", 25)).pack(pady=(30, 10))
        CTkLabel(vegetables_page, text='per 1 vegetable', text_color="#FFFFFF", font=("Cooper Black", 20)).pack(pady=(10, 10))
        vegetables_frame = CTkScrollableFrame(vegetables_page, width=260, height=300, label_text_color="#FFFFFF")
        vegetables_frame.pack(pady=30, padx=20)

        vegetables_list = {
            'potato': 77,
            'carrot': 41,
            'onion': 40,
            'lettuce': 15,
            'eggplant': 25,
            'mushrooms': 22,
            'broccoli': 32,
            'spinach': 23,
            'cucumber': 16,
            'tomato': 18,
            'celery': 16,
            'beetroot': 43,
            'cauli flower': 25,
            'bell pepper': 31,
            'zucchini': 17,
        }

        for key, value in vegetables_list.items():
            title_label = CTkLabel(vegetables_frame, text=f"{key} - {value} calories", text_color="#FFFFFF", font=("Arial", 14))
            title_label.pack(pady=(30, 10))

        back_button = CTkButton(vegetables_frame, text="Back",
                                font=('Arial', 14, 'bold'),
                                corner_radius=15, height=40, width=100,
                                fg_color='#FFFFFF', hover_color='#C850C0',
                                text_color='#FF3399',
                                command=lambda: products_open(vegetables_page))
        back_button.pack(pady=(10, 30))

        vegetables_page.mainloop()

    def oils_open():
        products_page.destroy()

        oils_page = CTk()
        oils_page.title("Oils")
        oils_page.geometry("400x415")
        oils_page.iconbitmap("icon_path")
        oils_page.configure(fg_color = "#101217")
        oils_page.resizable(False, False)

        CTkLabel(oils_page, text="List of oils", text_color="#FF3399", font=("Cooper Black", 25)).pack(pady=(30, 10))
        CTkLabel(oils_page, text='per 100 gramm', text_color="#FFFFFF", font=("Cooper Black", 20)).pack(pady=(10, 10))
        oils_frame = CTkScrollableFrame(oils_page, width=260, height=300, label_text_color="#FFFFFF")
        oils_frame.pack(pady=30, padx=20)

        oils_list = {
            'olive oil': 119,
            'cocnut oil': 117,
            'sunflower oil': 120,
            'ghee oil': 112,
            'avocado oil': 120,
            'peanut oil': 119,
            'butter': 102
        }
        for key, value in oils_list.items():
            title_label = CTkLabel(oils_frame, text=f"{key} - {value} calories", text_color="#FFFFFF", font=("Arial", 14))
            title_label.pack(pady=(30, 10))

        back_button = CTkButton(oils_frame, text="Back",
                                font=('Arial', 14, 'bold'),
                                corner_radius=15, height=40, width=100,
                                fg_color='#FFFFFF', hover_color='#C850C0',
                                text_color='#FF3399',
                                command=lambda: products_open(oils_page))
        back_button.pack(pady=(10, 30))

        oils_page.mainloop()

    def beverages_open():
        products_page.destroy()

        beverages_page = CTk()
        beverages_page.title("Beverages")
        beverages_page.geometry("400x415")
        beverages_page.configure(fg_color = "#101217")
        beverages_page.iconbitmap("icon_path")
        beverages_page.resizable(False, False)

        CTkLabel(beverages_page, text="List of beverages", text_color="#FF3399", font=("Cooper Black", 25)).pack(pady=(30, 10))
        CTkLabel(beverages_page, text='per 100 ml', text_color="#FFFFFF", font=("Cooper Black", 20)).pack(pady=(10, 10))
        beverages_frame = CTkScrollableFrame(beverages_page, width=260, height=300, label_text_color="#FFFFFF")
        beverages_frame.pack(pady=30, padx=20)

        beverages_list = {
            'coffee': 2,
            'latte': 150,
            'tea': 2,
            'soda': 140,
            'orange milk': 150,
            'lemonade': 120,
            'protein smoothie': 125
        }

        for key, value in beverages_list.items():
            title_label = CTkLabel(beverages_frame, text=f"{key} - {value} calories", text_color="#FFFFFF", font=("Arial", 14))
            title_label.pack(pady=(30, 10))

        back_button = CTkButton(beverages_frame, text="Back",
                                font=('Arial', 14, 'bold'),
                                corner_radius=15, height=40, width=100,
                                fg_color='#FFFFFF', hover_color='#C850C0',
                                text_color='#FF3399',
                                command=lambda: products_open(beverages_page))
        back_button.pack(pady=(10, 30))

        beverages_page.mainloop()


    def snacks_open():
        products_page.destroy()

        snacks_page = CTk()
        snacks_page.title("Snacks")
        snacks_page.geometry("400x415")
        snacks_page.configure(fg_color = "#101217")
        snacks_page.iconbitmap(icon_path)
        snacks_page.resizable(False, False)

        CTkLabel(snacks_page, text="List of snacks", text_color="#FF3399", font=("Cooper Black", 25)).pack(pady=(30, 10))
        CTkLabel(snacks_page, text='per 100 gramm', text_color="#FFFFFF", font=("Cooper Black", 20)).pack(pady=(10, 10))
        snacks_frame = CTkScrollableFrame(snacks_page, width=260, height=300, label_text_color="#FFFFFF")
        snacks_frame.pack(pady=30, padx=20)

        snacks_list = {
            'popcorn': 387,
            'dark chocolate': 598,
            'potato chips': 536,
            'vegie cheaps': 520,
            'rice cakes': 387,
            'hummus': 166,
            'frozen yogurt': 110,
        }

        for key, value in snacks_list.items():
            title_label = CTkLabel(snacks_frame, text=f"{key} - {value} calories", text_color="#FFFFFF", font=("Arial", 14))
            title_label.pack(pady=(30, 10))

        back_button = CTkButton(snacks_frame, text="Back",
                                font=('Arial', 14, 'bold'),
                                corner_radius=15, height=40, width=100,
                                fg_color='#FFFFFF', hover_color='#C850C0',
                                text_color='#FF3399',
                                command=lambda: products_open(snacks_page))
        back_button.pack(pady=(10, 30))

        snacks_page.mainloop()

    def proteins_open():
        products_page.destroy()

        proteins_page = CTk()
        proteins_page.title("Proteins")
        proteins_page.geometry("400x415")
        proteins_page.configure(fg_color = "#101217")
        proteins_page.iconbitmap(icon_path)
        proteins_page.resizable(False, False)

        CTkLabel(proteins_page, text="List of proteins", text_color="#FF3399", font=("Cooper Black", 25)).pack(pady=(30, 10))
        CTkLabel(proteins_page, text='per 100 gramm', text_color="#FFFFFF", font=("Cooper Black", 20)).pack(pady=(10, 10))
        proteins_frame = CTkScrollableFrame(proteins_page, width=260, height=300, label_text_color="#FFFFFF")
        proteins_frame.pack(pady=30, padx=20)

        proteins_list = {
            'tofu': 76,
            'chicken egg': 155,
            'peanuts': 567,
            'oats': 389,
            'walnuts': 654,
            'black bean pasta': 335,
            'green lentil pasta': 321,
        }

        for key, value in proteins_list.items():
            title_label = CTkLabel(proteins_frame, text=f"{key} - {value} calories", text_color="#FFFFFF", font=("Arial", 14))
            title_label.pack(pady=(30, 10))

        back_button = CTkButton(proteins_frame, text="Back",
                                font=('Arial', 14, 'bold'),
                                corner_radius=15, height=40, width=100,
                                fg_color='#FFFFFF', hover_color='#C850C0',
                                text_color='#FF3399',
                                command=lambda: products_open(proteins_page))
        back_button.pack(pady=(10, 30))

        proteins_page.mainloop()

    def milk_products_open():
        products_page.destroy()

        milk_products_page = CTk()
        milk_products_page.title("Milk Products")
        milk_products_page.geometry("400x415")
        milk_products_page.configure(fg_color = "#101217")
        milk_products_page.iconbitmap(icon_path)
        milk_products_page.resizable(False, False)

        CTkLabel(milk_products_page, text="Milk products list", text_color="#FF3399", font=("Cooper Black", 25)).pack(pady=(30, 10))
        CTkLabel(milk_products_page, text='per 100 ml', text_color="#FFFFFF", font=("Cooper Black", 20)).pack(pady=(10, 10))
        milk_products_frame = CTkScrollableFrame(milk_products_page, width=260, height=300, label_text_color="#FFFFFF")
        milk_products_frame.pack(pady=30, padx=20)

        milk_products_list = {
            'milk': 61,
            'butter': 717,
            'evaporated milk': 135,
            'kefir': 55,
            'sour cream': 198,
            'yogurt': 61,
            'greek yogurt': 59,
            'cottage cheese': 98,
            'cheddar cheese': 403,
            'mozzarella cheese': 280,
            'cream cheese': 342
        }

        for key, value in milk_products_list.items():
            title_label = CTkLabel(milk_products_frame, text=f"{key} - {value} calories", text_color="#FFFFFF", font=("Arial", 14))
            title_label.pack(pady=(30, 10))

        back_button = CTkButton(milk_products_frame, text="Back",
                                font=('Arial', 14, 'bold'),
                                corner_radius=15, height=40, width=100,
                                fg_color='#FFFFFF', hover_color='#C850C0',
                                text_color='#FF3399',
                                command=lambda: products_open(milk_products_page))
        back_button.pack(pady=(10, 30))

        milk_products_page.mainloop()


    def meat_products_open():
        products_page.destroy()

        meat_products_page = CTk()
        meat_products_page.title("Meat Products")
        meat_products_page.geometry("400x415")
        meat_products_page.configure(fg_color = "#101217")
        meat_products_page.iconbitmap(icon_path)
        meat_products_page.resizable(False, False)

        CTkLabel(meat_products_page, text="List of meat products", text_color="#FF3399", font=("Cooper Black", 25)).pack(pady=(30, 10))
        CTkLabel(meat_products_page, text='per 100 gramm', text_color="#FFFFFF", font=("Cooper Black", 20)).pack(pady=(10, 10))
        meat_products_frame = CTkScrollableFrame(meat_products_page, width=260, height=300, label_text_color="#FFFFFF")
        meat_products_frame.pack(pady=30, padx=20)

        meat_products_list = {
            'beef sirloin': 271,
            'beef jerky': 410,
            'sausage': 301,
            'ham': 145,
            'bacon': 541,
            'chicken breast': 165,
            'chicken thigh': 209,
            'lamb': 294,
            'salmon': 206,
            'crab': 83,
            'lobster': 89,
            'tuna': 132,
            'shrimp': 99,
            'duck': 337
        }

        for key, value in meat_products_list.items():
            title_label = CTkLabel(meat_products_frame, text=f"{key} - {value} calories", text_color="#FFFFFF", font=("Arial", 14))
            title_label.pack(pady=(30, 10))

        back_button = CTkButton(meat_products_frame, text="Back",
                                font=('Arial', 14, 'bold'),
                                corner_radius=15, height=40, width=100,
                                fg_color='#FFFFFF', hover_color='#C850C0',
                                text_color='#FF3399',
                                command=lambda: products_open(meat_products_page))
        back_button.pack(pady=(10, 30))

        meat_products_page.mainloop()

    def sweets_open():
        products_page.destroy()

        sweets_page = CTk()
        sweets_page.title("Sweets")
        sweets_page.geometry("400x415")
        sweets_page.configure(fg_color = "#101217")
        sweets_page.iconbitmap(icon_path)
        sweets_page.resizable(False, False)

        CTkLabel(sweets_page, text="List of sweets", text_color="#FF3399", font=("Cooper Black", 25)).pack(pady=(30, 10))
        CTkLabel(sweets_page, text='per 100 gramm', text_color="#FFFFFF", font=("Cooper Black", 20)).pack(pady=(10, 10))
        sweets_frame = CTkScrollableFrame(sweets_page, width=260, height=300, label_text_color="#FFFFFF")
        sweets_frame.pack(pady=30, padx=20)

        sweets_list = {
            'cupcake': 210,
            'muffin': 200,
            'macaroon': 90,
            'cookie': 150,
            'candy bar': 250,
            'ice cream': 137,
            'donut': 195,
            'brownie': 290,
            'cheesecake': 320,
        }

        for key, value in sweets_list.items():
            title_label = CTkLabel(sweets_frame, text=f"{key} - {value} calories", text_color="#FFFFFF", font=("Arial", 14))
            title_label.pack(pady=(30, 10))

        back_button = CTkButton(sweets_frame, text="Back",
                                font=('Arial', 14, 'bold'),
                                corner_radius=15, height=40, width=100,
                                fg_color='#FFFFFF', hover_color='#C850C0',
                                text_color='#FF3399',
                                command=lambda: products_open(sweets_page))
        back_button.pack(pady=(10, 30))

        sweets_page.mainloop()

    def grains_open():
        products_page.destroy()

        grains_page = CTk()
        grains_page.title("Grains")
        grains_page.geometry("400x415")
        grains_page.configure(fg_color = "#101217")
        grains_page.iconbitmap(icon_path)
        grains_page.resizable(False, False)

        CTkLabel(grains_page, text="List of grains", text_color="#FF3399", font=("Cooper Black", 25)).pack(pady=(30, 10))
        CTkLabel(grains_page, text='per 100 gramm', text_color="#FFFFFF", font=("Cooper Black", 20)).pack(pady=(10, 10))
        grains_frame = CTkScrollableFrame(grains_page, width=260, height=300, label_text_color="#FFFFFF")
        grains_frame.pack(pady=30, padx=20)

        grains_list = {
            'rice': 130,
            'quinoa': 120,
            'barley': 123,
            'millet': 119,
            'buckwheat': 92,
            'couscous': 112,
            'farro': 125,
            'bulgur': 83,
            'oats': 389,
            'mung beans': 105,
            'lentils': 116
        }

        for key, value in grains_list.items():
            title_label = CTkLabel(grains_frame, text=f"{key} - {value} calories", text_color="#FFFFFF", font=("Arial", 14))
            title_label.pack(pady=(30, 10))

        back_button = CTkButton(grains_frame, text="Back",
                                font=('Arial', 14, 'bold'),
                                corner_radius=15, height=40, width=100,
                                fg_color='#FFFFFF', hover_color='#C850C0',
                                text_color='#FF3399',
                                command=lambda: products_open(grains_page))
        back_button.pack(pady=(10, 30))

        grains_page.mainloop()

    def your_products_open():
        products_page.destroy()

        your_products_page = CTk()
        your_products_page.title("User products list")
        your_products_page.geometry("400x415")
        your_products_page.configure(fg_color = "#101217")
        your_products_page.iconbitmap(icon_path)
        your_products_page.resizable(False, False)

        CTkLabel(your_products_page, text="Your products are:", text_color="#FF3399", font=("Cooper Black", 25)).pack(
            pady=(30, 10))
        CTkLabel(your_products_page, text='per 100 gramm', text_color="#FFFFFF", font=("Cooper Black", 20)).pack(pady=(10, 10))
        your_products_frame = CTkScrollableFrame(your_products_page, width=260, height=300, label_text_color="#FFFFFF")
        your_products_frame.pack(pady=30, padx=20)

        for key, value in added_products.items():
            title_label = CTkLabel(your_products_frame, text=f"{key} - {value} calories", text_color="#FFFFFF",
                                   font=("Arial", 14))
            title_label.pack(pady=(30, 10))

        back_button = CTkButton(your_products_frame, text="Back",
                                font=('Arial', 14, 'bold'),
                                corner_radius=15, height=40, width=100,
                                fg_color='#FFFFFF', hover_color='#C850C0',
                                text_color='#FF3399',
                                command=lambda: products_open(your_products_page))
        back_button.pack(pady=(10, 30))

        your_products_page.mainloop()


    products_list = [
        ('Fruits', fruits_open),
        ('Vegetables', vegetables_open),
        ('Oils', oils_open),
        ('Beverages', beverages_open),
        ('Sweets', sweets_open),
        ('Grains', grains_open),
        ('Milk Products', milk_products_open),
        ('Meat Products', meat_products_open),
        ('Snacks', snacks_open),
        ('Proteins', proteins_open),
        ('Your Products', your_products_open),
    ]
    for name, func in products_list:
        button = CTkButton(products_frame,
                           text = name, text_color="#FFFFFF",
                           fg_color = "#C850C0", hover_color = "#FF3399",
                           font=('Arial', 15, 'bold') ,corner_radius=15,
                           command=func)
        button.pack(pady=10)

    back_button = CTkButton(products_frame, text="Back",
                            font=('Arial', 14, 'bold'),
                            corner_radius=15, height=40, width=100,
                            fg_color='#FFFFFF', hover_color='#C850C0',
                            text_color='#FF3399',
                            command=lambda: calculator_open(products_page))
    back_button.pack(pady=(0, 30))

    products_page.mainloop()

def addproduct_open(calculator_page):
    global productName_entry, calories_entry
    global product, calories

    calculator_page.destroy()

    addedproducts_page = CTk()
    addedproducts_page.title("Your Products")
    addedproducts_page.geometry("400x415")
    addedproducts_page.iconbitmap(icon_path)
    addedproducts_page.configure(fg_color="#101217")
    addedproducts_page.resizable(False, False)

    addedproducts_frame = CTkFrame(addedproducts_page, fg_color="#23272D", width=260, height=300)
    addedproducts_frame.pack(pady=30, padx=20)
    addedproducts_frame.pack_propagate(False)


    subtitle1 = CTkLabel(addedproducts_frame, text="Add your own products", font=("Cooper Black", 25),
                        text_color='#FF3399')
    subtitle1.grid(row=0, column=0, columnspan=100, pady=20, padx=15)

    subtitle2 = CTkLabel(addedproducts_frame, text="Enter info for product", font=("Cooper Black", 20),
                         text_color='#FFFFFF')
    subtitle2.grid(row=2, column=0, columnspan=200, pady=15, padx=30)

    productName_label = CTkLabel(master = addedproducts_frame, text="Name of product:", font=("Arial", 15, "bold"))
    productName_label.grid(row=3, column=0, padx=5, pady=5)
    productName_entry = CTkEntry(master = addedproducts_frame, placeholder_text="Product...", font=('Arial', 13, 'bold'))
    productName_entry.grid(row=3, column=1, padx=10, pady=5)

    calories_label = CTkLabel(master = addedproducts_frame, text="Calories for portion:", font=("Arial", 15, "bold"))
    calories_label.grid(row=4, column=0, padx=10, pady=5)
    calories_entry = CTkEntry(master = addedproducts_frame, placeholder_text="Calories...", font=('Arial', 13, 'bold'))
    calories_entry.grid(row=4, column=1, padx=10, pady=5)

    buttonFrame1 = CTkFrame(addedproducts_frame, fg_color='#23272D')
    buttonFrame1.grid(row=7, column=0, columnspan=100, padx = 10, pady = 10)

    saveButton1 = CTkButton(buttonFrame1, text='Save data',
                           font=('Arial', 15, 'bold'),
                           command=save_product,
                           corner_radius=15, height=38,
                           width=100, hover_color='#FF3399',
                           fg_color='#C850C0')
    saveButton1.grid(row=0, column=0, columnspan = 100, pady=5, padx = 5)

    buttonFrame2 = CTkFrame(addedproducts_frame, fg_color='#23272D')
    buttonFrame2.grid(row=9, column=0, columnspan=100, pady = 10, padx = 10)

    back_button = CTkButton(buttonFrame2, text="Back",
                            font=('Arial', 15, 'bold'),
                            corner_radius=15, height=40, width=100,
                            fg_color='#FFFFFF', hover_color='#C850C0',
                            text_color='#FF3399',
                            command=lambda: calculator_open(addedproducts_page))
    back_button.grid(row=0, column=0, columnspan = 100, pady=5, padx = 5)

    addedproducts_page.mainloop()

def save_product():
    global productName_entry, calories_entry, added_products, products
    product = productName_entry.get().strip()
    calories = calories_entry.get().strip()

    if product == "" or calories == "":
        messagebox.showerror('LizCoach', 'Fill out each line')
        return
    with open('productslist.txt', 'r') as file:
        data = file.read()
    products = ast.literal_eval(data)
    if product in products:
        messagebox.showerror(title="Error", message="Product already exists")
    else:
        products[product] = calories
        with open('productslist.txt', 'w') as file:
            file.write(str(products))
        newproducts = f"{product} - {calories} calories for one portion\n"
        with open('newproduct.txt', 'w') as file:
            file.write(newproducts)
        messagebox.showinfo('LizCoach', 'Saved your products successfully!')
        added_products[product] = calories

total = 0
consumed = {}
mtotal = 0

def search():
    global mtotal, total, consumed
    product = product_entry.get().strip()
    portion = int(portion_entry.get().strip())

    with open('productslist.txt', 'r') as file:
        data = file.read().strip()
        products = ast.literal_eval(data) if data else {}

    if product in products:
        calories = int(products[product])
        mtotal = calories * portion
        total += mtotal
        consumed[product] = mtotal
        messagebox.showinfo(title ="LizCoach",
                             message=f"portion x calories of {product} is {mtotal}")
    else:
       messagebox.showwarning(message=f"{product} is not found")

def ccalculator_open(calculator_page):
    calculator_page.destroy()
    global product_entry, portion_entry, mtotal, total, consumed

    ccalculator_page = CTk()
    ccalculator_page.title("Calories Calculator")
    ccalculator_page.geometry("600x400")
    ccalculator_page.iconbitmap(icon_path)
    ccalculator_page.configure(fg_color="#101217")
    ccalculator_page.resizable(False, False)


    ccalculator_frame = CTkFrame(ccalculator_page, fg_color="#23272D", width=400, height=200)
    ccalculator_frame.pack(side = 'left', fill = 'y')
    ccalculator_frame.pack_propagate(False)

    photo2_frame = CTkFrame(ccalculator_page, fg_color='#23272D', width=200, height=200)
    photo2_frame.pack(side = 'right', fill = 'y')
    photo2_frame.pack_propagate(False)

    CTkLabel(ccalculator_frame, text="Calculate eaten calories", font=("Cooper Black", 25), text_color='#FF3399').pack(padx=20, pady=20)

    image2 = Image.open('ProductsLizard.png')
    image2 = image2.resize((500, 500))
    photo2 = ImageTk.PhotoImage(image2)
    image2_label = CTkLabel(photo2_frame, image=photo2, text = "")
    image2_label.image2 = photo2
    image2_label.pack(side="right", padx=10, pady=10, expand=True)

    product_label = CTkLabel(ccalculator_frame, text="Name of product:", font=("Arial", 15, "bold"))
    product_label.pack(padx=10, pady=10)
    product_entry = CTkEntry(ccalculator_frame, placeholder_text="Product...", font=('Arial', 11, 'bold'))
    product_entry.pack(padx=10, pady=10)

    portion_label = CTkLabel(ccalculator_frame, text="Portion:", font=("Arial", 15, "bold"))
    portion_label.pack(padx=10, pady=10)
    portion_entry = CTkEntry(ccalculator_frame, placeholder_text="Portion", font=('Arial', 11, 'bold'))
    portion_entry.pack(padx=10, pady=10)

    calculateButton = CTkButton(ccalculator_frame, text='Calculate',
                            font=('Arial', 14, 'bold'),
                            command=search,
                            corner_radius=15, height=35,
                            width=100, hover_color='#FF3399',
                            fg_color='#C850C0')
    calculateButton.pack(pady=20, padx = 15)

    back_button = CTkButton(ccalculator_frame, text="Back",
                             font=('Arial', 14, 'bold'),
                             corner_radius=15, height=40, width=100,
                             fg_color='#FFFFFF', hover_color='#C850C0',
                             text_color='#FF3399',
                             command=lambda: calculator_open(ccalculator_page))
    back_button.pack(pady=(10, 20))

    ccalculator_page.mainloop()

def total_open(calculator_page):
    global total, consumed
    calculator_page.destroy()

    total_page = CTk()
    total_page.title("Calculated Calories")
    total_page.geometry("400x415")
    total_page.iconbitmap(icon_path)
    total_page.configure(fg_color="#101217")
    total_page.resizable(False, False)

    CTkLabel(total_page, text="Total calculations", font=("Cooper Black", 25), text_color='#FF3399').pack(padx=20, pady=20)

    CTkLabel(total_page, text=f"Total: {total} calories", font=("Cooper Black", 20), text_color='#FFFFFF').pack(padx=10, pady=10)

    total_frame = CTkScrollableFrame(total_page, width=260, height=320, label_text_color="#FFFFFF")
    total_frame.pack(pady=30, padx=20)

    for key, value in consumed.items():
        title_label = CTkLabel(total_frame, text=f"{key} - {value} calories", text_color="#FFFFFF",
                               font=("Arial", 14))
        title_label.pack(pady=(30, 10))

    back_button = CTkButton(total_frame, text="Back",
                            font=('Arial', 14, 'bold'),
                            corner_radius=15, height=40, width=100,
                            fg_color='#FFFFFF', hover_color='#C850C0',
                            text_color='#FF3399',
                            command=lambda: calculator_open(total_page))
    back_button.pack(pady=(10, 30))

    total_page.mainloop()

#End of calculator parts

app = CTk()
app.title("LizCoach")
app.iconbitmap(icon_path)
app.geometry("600x400")
app.configure(fg_color="#101217")
app.resizable(False, False)


image = Image.open("LizCoach.jpg")
resized_image = image.resize((325, 400))
ctk_image = CTkImage(light_image=resized_image,
                     dark_image=resized_image,
                     size=(325, 400))

left_frame = CTkFrame(master=app, fg_color="#23272D")
left_frame.grid(row=0, column=0, rowspan=2, padx=10)

image_label = CTkLabel(master=left_frame, image=ctk_image, text="")
image_label.pack(pady=0)

right_frame = CTkFrame(master=app, fg_color="#23272D")
right_frame.grid(row=0, column=1, padx=5, pady=6)

subtitle = CTkLabel(master=right_frame, text="Welcome to LizCoach!", font=("Cooper Black", 18), text_color='#FF3399')
subtitle.grid(row=0, column=0, columnspan=100, pady=10, padx=15)

nameLabel = CTkLabel(master=right_frame, text="Name", font=("Arial", 13, "bold"))
nameLabel.grid(row=2, column=0, padx=5, pady=5)

nameEntry = CTkEntry(master=right_frame, placeholder_text="Type name...", font=('Arial', 11, 'bold'))
nameEntry.grid(row=2, column=1, padx=10, pady=5)

ageLabel = CTkLabel(master=right_frame, text="Age", font=("Arial", 13, "bold"))
ageLabel.grid(row=3, column=0, padx=5, pady=5)

ageEntry = CTkEntry(master=right_frame, placeholder_text="Type age...", font=('Arial', 11, 'bold'))
ageEntry.grid(row=3, column=1, padx=10, pady=5)

weightLabel = CTkLabel(master=right_frame, text="Weight", font=("Arial", 13, "bold"))
weightLabel.grid(row=4, column=0, padx=10, pady=5)

weightEntry = CTkEntry(master=right_frame, placeholder_text="Type weight...", font=('Arial', 11, 'bold'))
weightEntry.grid(row=4, column=1, padx=5, pady=5)

heightLabel = CTkLabel(master=right_frame, text="Height", font=("Arial", 13, "bold"))
heightLabel.grid(row=5, column=0, padx=10, pady=5)

heightEntry = CTkEntry(master=right_frame, placeholder_text="Type height...", font=('Arial', 11, 'bold'))
heightEntry.grid(row=5, column=1, padx=5, pady=5)

genderLabel = CTkLabel(master=right_frame, text="Gender", font=("Arial", 13, "bold"))
genderLabel.grid(row=6, column=0, padx=15, pady=5, sticky='w')

gender_options = ['Male', 'Female']
genderBox = CTkComboBox(master=right_frame, values=gender_options, font=('Arial', 11, 'bold'))
genderBox.grid(row=6, column=1, padx=5, pady=5)

buttonFrame = CTkFrame(master=right_frame, fg_color='#23272D')
buttonFrame.grid(row=7, column=0, columnspan=100)

data = load_data()

if data:
    nameEntry.insert(0, data.get('Name', ''))
    ageEntry.insert(0, data.get('Age', ''))
    weightEntry.insert(0, data.get('Weight', ''))
    heightEntry.insert(0, data.get('Height', ''))
    gender = data.get('Gender', 'Male')
    genderBox.set(gender)
    gender_data = gender

else:
    gender_data = 'Male'

saveButton = CTkButton(buttonFrame, text='Save data',
                       font=('Arial', 13, 'bold'),
                       command=save_user,
                       corner_radius=15, height=35,
                       width=100, hover_color='#FF3399',
                       fg_color='#C850C0')
saveButton.grid(row=1, column=0, pady=15)

load_data()
app.mainloop()
