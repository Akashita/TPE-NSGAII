from tkinter import *


def tk_interface():
    window = Tk()

    main_frame = Frame(window, width=768, height=576, borderwidth=1, bg="white")
    main_frame.pack(fill=BOTH)

    choice_algo_box = Frame(main_frame, width=768, height=576, borderwidth=1, bg="red")
    choice_algo_box.pack(fill=BOTH)

    choice_parameters_box = Frame(main_frame, width=768, height=576, borderwidth=1, bg="blue")
    choice_parameters_box.pack(fill=BOTH)

    problem_choice or= IntVar()

    field_multi= Label(choice_algo_box, text="Multi objective (NSGA2)")
    choice_sch = Radiobutton(choice_algo_box, text="SCH", variable=problem_choice, value=0)
    choice_fon = Radiobutton(choice_algo_box, text="FON", variable=problem_choice, value=1)
    choice_kursae = Radiobutton(choice_algo_box, text="Kursawe", variable=problem_choice, value=2)
    choice_z1 = Radiobutton(choice_algo_box, text="DTLZ1", variable=problem_choice, value=3)
    choice_z2 = Radiobutton(choice_algo_box, text="DTLZ2", variable=problem_choice, value=4)
    choice_z3 = Radiobutton(choice_algo_box, text="DTLZ3", variable=problem_choice, value=5)
    choice_z4 = Radiobutton(choice_algo_box, text="DTLZ4", variable=problem_choice, value=6)
    choice_z5 = Radiobutton(choice_algo_box, text="DTLZ5", variable=problem_choice, value=7)
    choice_z6 = Radiobutton(choice_algo_box, text="DTLZ6", variable=problem_choice, value=8)
    choice_z7 = Radiobutton(choice_algo_box, text="DTLZ7", variable=problem_choice, value=9)

    field_single = Label(choice_algo_box, text="Single objective")
    choice_ackley = Radiobutton(choice_algo_box, text="Ackley", variable=problem_choice, value=10)
    choice_griewank = Radiobutton(choice_algo_box, text="Griwank", variable=problem_choice, value=11)
    choice_rosenbrock = Radiobutton(choice_algo_box, text="Rosenbrock", variable=problem_choice, value=12)
    choice_schewfel = Radiobutton(choice_algo_box, text="Schewfel", variable=problem_choice, value=13)
    choice_sphere = Radiobutton(choice_algo_box, text="Sphere", variable=problem_choice, value=14)

    field_multi.pack()
    choice_sch.pack()
    choice_fon.pack()
    choice_kursae.pack()
    choice_z1.pack()
    choice_z2.pack()
    choice_z3.pack()
    choice_z4.pack()
    choice_z5.pack()
    choice_z6.pack()
    choice_z7.pack()

    field_single.pack()
    choice_ackley.pack()
    choice_griewank.pack()
    choice_rosenbrock.pack()
    choice_schewfel.pack()
    choice_sphere.pack()



    parameter_choice = StringVar()

    field_parameters= Label(choice_parameters_box, text="Parameter variation")
    choice_pop = Radiobutton(choice_parameters_box, text="Size of the population", variable=parameter_choice, value="pop_size")
    choice_gen = Radiobutton(choice_parameters_box, text="Number of generation", variable=parameter_choice, value="nmb_gen")
    choice_cross = Radiobutton(choice_parameters_box, text="Crossover probability", variable=parameter_choice, value="p_crossover")
    choice_mut = Radiobutton(choice_parameters_box, text="Mutation probability", variable=parameter_choice, value="p_mutation")

    field_parameters.pack()
    choice_pop.pack()
    choice_gen.pack()
    choice_cross.pack()
    choice_mut.pack()


    window.mainloop()
