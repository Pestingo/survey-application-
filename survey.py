import tkinter as tk
from tkinter import ttk, messagebox

# Dictionary to store survey results
survey_results = {}


def show_survey_form():
    clear_frame(content_frame)
    create_survey_form(content_frame)


def show_survey_results():
    clear_frame(content_frame)
    if not survey_results:
        ttk.Label(content_frame, text="No survey results available.").grid(row=0, column=0, padx=10, pady=10)
    else:
        row_index = 0
        ttk.Label(content_frame, text="Survey Results:").grid(row=row_index, column=0, padx=10, pady=10, sticky=tk.W)
        row_index += 1

        for key, value in survey_results.items():
            if key == "Ratings":
                ttk.Label(content_frame, text="Ratings:").grid(row=row_index, column=0, padx=10, pady=2, sticky=tk.W)
                row_index += 1
                for question, rating in value.items():
                    ttk.Label(content_frame, text=f"{question}: {rating}").grid(row=row_index, column=0, padx=20,
                                                                                pady=2, sticky=tk.W)
                    row_index += 1
            elif key == "Favorite Food":
                food_str = ', '.join(value)
                ttk.Label(content_frame, text=f"{key}: {food_str}").grid(row=row_index, column=0, padx=10, pady=2,
                                                                         sticky=tk.W)
                row_index += 1
            else:
                ttk.Label(content_frame, text=f"{key}: {value}").grid(row=row_index, column=0, padx=10, pady=2,
                                                                      sticky=tk.W)
                row_index += 1


def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()


def submit_survey(full_name_var, email_var, dob_var, contact_var, food_vars, rating_vars):
    global survey_results
    survey_results = {
        "Full Name": full_name_var.get(),
        "Email": email_var.get(),
        "Date of Birth": dob_var.get(),
        "Contact Number": contact_var.get(),
        "Favorite Food": [food.get() for food in food_vars if food.get() != ""],
        "Ratings": {question: var.get() for question, var in rating_vars.items()}
    }
    messagebox.showinfo("Survey Submitted", "Your survey has been submitted successfully!")
    show_survey_results()


def create_survey_form(parent_frame):
    # Personal Details
    full_name_var = tk.StringVar()
    email_var = tk.StringVar()
    dob_var = tk.StringVar()
    contact_var = tk.StringVar()

    details_frame = ttk.Frame(parent_frame, padding="10")
    details_frame.grid(row=0, column=0, sticky=tk.W)

    ttk.Label(details_frame, text="Full Names:").grid(row=0, column=0, sticky=tk.W)
    ttk.Entry(details_frame, width=40, textvariable=full_name_var).grid(row=0, column=1, padx=5, pady=2)

    ttk.Label(details_frame, text="Email:").grid(row=1, column=0, sticky=tk.W)
    ttk.Entry(details_frame, width=40, textvariable=email_var).grid(row=1, column=1, padx=5, pady=2)

    ttk.Label(details_frame, text="Date of Birth:").grid(row=2, column=0, sticky=tk.W)
    ttk.Entry(details_frame, width=40, textvariable=dob_var).grid(row=2, column=1, padx=5, pady=2)

    ttk.Label(details_frame, text="Contact Number:").grid(row=3, column=0, sticky=tk.W)
    ttk.Entry(details_frame, width=40, textvariable=contact_var).grid(row=3, column=1, padx=5, pady=2)

    # Favorite Food
    food_vars = [tk.StringVar() for _ in range(4)]
    food_frame = ttk.Frame(parent_frame, padding="10")
    food_frame.grid(row=1, column=0, sticky=tk.W)

    ttk.Label(food_frame, text="What is your favorite food?").grid(row=0, column=0, sticky=tk.W)
    food_options = ["Pizza", "Pasta", "Pap and Wors", "Other"]
    for idx, option in enumerate(food_options):
        ttk.Checkbutton(food_frame, text=option, variable=food_vars[idx], onvalue=option, offvalue="").grid(row=0,
                                                                                                            column=idx + 1,
                                                                                                            padx=5)

    # Agree-Disagree Questions
    questions = [
        "I like to watch movies",
        "I like to listen to radio",
        "I like to eat out",
        "I like to watch TV"
    ]
    options = ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"]

    rating_vars = {question: tk.StringVar() for question in questions}
    survey_frame = ttk.Frame(parent_frame, padding="10")
    survey_frame.grid(row=2, column=0, sticky=tk.W)

    ttk.Label(survey_frame, text="").grid(row=0, column=0, pady=5)
    for idx, option in enumerate(options):
        ttk.Label(survey_frame, text=option).grid(row=0, column=idx + 1, padx=5)

    for row, question in enumerate(questions):
        ttk.Label(survey_frame, text=question).grid(row=row + 1, column=0, sticky=tk.W)
        for col, option in enumerate(options):
            ttk.Radiobutton(survey_frame, variable=rating_vars[question], value=option).grid(row=row + 1,
                                                                                             column=col + 1, padx=5)

    # Submit button
    submit_frame = ttk.Frame(parent_frame, padding="10")
    submit_frame.grid(row=3, column=0, sticky=tk.E)
    ttk.Button(submit_frame, text="Submit", command=lambda: submit_survey(
        full_name_var, email_var, dob_var, contact_var, food_vars, rating_vars)).grid(row=0, column=0)


def create_main_window():
    root = tk.Tk()
    root.title("Survey Application")
    root.geometry("800x600")

    # Menu bar
    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)

    survey_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Survey", menu=survey_menu)
    survey_menu.add_command(label="Fill Out Survey", command=show_survey_form)
    survey_menu.add_command(label="View Survey Results", command=show_survey_results)

    # Content frame
    global content_frame
    content_frame = ttk.Frame(root, padding="10")
    content_frame.pack(fill=tk.BOTH, expand=True)

    # Default view
    show_survey_form()

    root.mainloop()


create_main_window()
