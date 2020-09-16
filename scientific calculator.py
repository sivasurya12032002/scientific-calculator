from tkinter import *
from tkinter import ttk

w2=Tk()
w2.title("Scientific calculator")

string = StringVar()
string = ''

def f4():
    if v1.get()=='Normal operations':
        w2.destroy()

        w1 = Tk()
        w1.title("Simple Calculator")
        def f1(n):
            global string
            string += str(n)
            txt.set(string)

        def f2():
            global string
            txt.set(float(eval(string)))

        def f3():
            global string
            string = ''
            txt.set("Start Calculating....")



        txt = StringVar(value="Start Calculating....")

        # ===========================Row1=======================================
        eb = Entry(bd=50, font=('arial', 30, 'bold'), bg='green', fg='white', justify='right', textvariable=txt)
        eb.grid(columnspan=4)

        # ===========================Row2=======================================
        b7 = Button(text='7', bd=8, padx=30, pady=15, font=('arial', 30, 'bold')
                    , command=lambda: f1(7))
        b7.grid(row=1, column=0)
        b8 = Button(text='8', bd=8, padx=30, pady=15, font=('arial', 30, 'bold'), command=lambda: f1(8))
        b8.grid(row=1, column=1)
        b9 = Button(text='9', bd=8, padx=30, pady=15, font=('arial', 30, 'bold'), command=lambda: f1(9))
        b9.grid(row=1, column=2)
        bc = Button(text='C', bd=8, padx=30, pady=15, bg='green', font=('arial', 30, 'bold'), command=f3)
        bc.grid(row=1, column=3)

        # ===========================Row3=======================================
        b4 = Button(text='4', bd=8, padx=30, pady=15, font=('arial', 30, 'bold'), command=lambda: f1(4))
        b4.grid(row=2, column=0)
        b5 = Button(text='5', bd=8, padx=30, pady=15, font=('arial', 30, 'bold'), command=lambda: f1(5))
        b5.grid(row=2, column=1)
        b6 = Button(text='6', bd=8, padx=30, pady=15, font=('arial', 30, 'bold'), command=lambda: f1(6))
        b6.grid(row=2, column=2)
        bplus = Button(text='+', bd=8, padx=33, pady=15, bg='orange', font=('arial', 30, 'bold')
                       , command=lambda: f1('+'))
        bplus.grid(row=2, column=3)

        # ===========================Row4=======================================
        b1 = Button(text='1', bd=8, padx=30, pady=15, font=('arial', 30, 'bold'), command=lambda: f1(1))
        b1.grid(row=3, column=0)
        b2 = Button(text='2', bd=8, padx=30, pady=15, font=('arial', 30, 'bold'), command=lambda: f1(2))
        b2.grid(row=3, column=1)
        b3 = Button(text='3', bd=8, padx=30, pady=15, font=('arial', 30, 'bold'), command=lambda: f1(3))
        b3.grid(row=3, column=2)
        bminus = Button(text='-', bd=8, padx=37, pady=15, bg='orange', font=('arial', 30, 'bold'),
                        command=lambda: f1('-'))
        bminus.grid(row=3, column=3)

        # ===========================Row5=======================================
        b0 = Button(text='0', bd=8, padx=30, pady=15, font=('arial', 30, 'bold'), command=lambda: f1(0))
        b0.grid(row=4, column=0)
        bpoint = Button(text='.', bd=8, padx=35, pady=15, font=('arial', 30, 'bold'), bg='orange'
                        , command=lambda: f1('.'))
        bpoint.grid(row=4, column=1)
        bmul = Button(text='x', bd=8, padx=30, pady=15, bg='orange', font=('arial', 30, 'bold')
                      , command=lambda: f1('*'))
        bmul.grid(row=4, column=2)
        bdiv = Button(text='/', bd=8, padx=37, pady=15, bg='orange', font=('arial', 30, 'bold')
                      , command=lambda: f1('/'))
        bdiv.grid(row=4, column=3)

        # ===========================Row6=======================================
        bequal = Button(text='=', bd=8, padx=95, pady=10, font=('arial', 30, 'bold'), bg='green'
                        , command=f2)
        bequal.grid(row=5, column=0, columnspan=2)
        bbrac1 = Button(text='(', bd=8, padx=35, pady=10, font=('arial', 30, 'bold'), bg='orange'
                        , command=lambda: f1('('))
        bbrac1.grid(row=5, column=2)
        bbrac2 = Button(text=')', bd=8, padx=38, pady=10, font=('arial', 30, 'bold'), bg='orange'
                        , command=lambda: f1(')'))
        bbrac2.grid(row=5, column=3)


        w1.mainloop()
    if v1.get()=="Complex operations":
        w2.destroy()

        w3 = Tk()
        w3.title("Complex calculator")

        string = ''
        txt = StringVar(value="Start Calculating....")

        def f1(n):
            global string
            string += str(n)
            txt.set(string)

        def f2():
            global string
            z = eval(string)
            txt.set(z)

        def f3():
            global string
            string = ''
            txt.set("Start Calculating...")

        # ===========================Row1=======================================
        eb = Entry(w3, bd=50, font=('arial', 30, 'bold'), bg='green', fg='white', justify='right', textvariable=txt)
        eb.grid(columnspan=4)

        # ===========================Row2=======================================
        b7 = Button(w3, text='7', bd=8, padx=30, pady=15, font=('arial', 30, 'bold')
                    , command=lambda: f1(7))
        b7.grid(row=1, column=0)
        b8 = Button(w3, text='8', bd=8, padx=30, pady=15, font=('arial', 30, 'bold'), command=lambda: f1(8))
        b8.grid(row=1, column=1)
        b9 = Button(w3, text='9', bd=8, padx=30, pady=15, font=('arial', 30, 'bold'), command=lambda: f1(9))
        b9.grid(row=1, column=2)
        bc = Button(w3, text='C', bd=8, padx=30, pady=15, bg='green', font=('arial', 30, 'bold')
                    , command=f3)
        bc.grid(row=1, column=3)

        # ===========================Row3=======================================
        b4 = Button(w3, text='4', bd=8, padx=30, pady=15, font=('arial', 30, 'bold'), command=lambda: f1(4))
        b4.grid(row=2, column=0)
        b5 = Button(w3, text='5', bd=8, padx=30, pady=15, font=('arial', 30, 'bold'), command=lambda: f1(5))
        b5.grid(row=2, column=1)
        b6 = Button(w3, text='6', bd=8, padx=30, pady=15, font=('arial', 30, 'bold'), command=lambda: f1(6))
        b6.grid(row=2, column=2)
        bplus = Button(w3, text='+', bd=8, padx=33, pady=15, bg='orange', font=('arial', 30, 'bold')
                       , command=lambda: f1('+'))
        bplus.grid(row=2, column=3)

        # ===========================Row4=======================================
        b1 = Button(w3, text='1', bd=8, padx=30, pady=15, font=('arial', 30, 'bold'), command=lambda: f1(1))
        b1.grid(row=3, column=0)
        b2 = Button(w3, text='2', bd=8, padx=30, pady=15, font=('arial', 30, 'bold'), command=lambda: f1(2))
        b2.grid(row=3, column=1)
        b3 = Button(w3, text='3', bd=8, padx=30, pady=15, font=('arial', 30, 'bold'), command=lambda: f1(3))
        b3.grid(row=3, column=2)
        bminus = Button(w3, text='-', bd=8, padx=37, pady=15, bg='orange', font=('arial', 30, 'bold'),
                        command=lambda: f1('-'))
        bminus.grid(row=3, column=3)

        # ===========================Row5=======================================
        b0 = Button(w3, text='0', bd=8, padx=30, pady=15, font=('arial', 30, 'bold'), command=lambda: f1(0))
        b0.grid(row=4, column=0)
        bpoint = Button(w3, text='.', bd=8, padx=35, pady=15, font=('arial', 30, 'bold'), bg='orange'
                        , command=lambda: f1('.'))
        bpoint.grid(row=4, column=1)
        bmul = Button(w3, text='x', bd=8, padx=30, pady=15, bg='orange', font=('arial', 30, 'bold')
                      , command=lambda: f1('*'))
        bmul.grid(row=4, column=2)
        bdiv = Button(w3, text='/', bd=8, padx=37, pady=15, bg='orange', font=('arial', 30, 'bold')
                      , command=lambda: f1('/'))
        bdiv.grid(row=4, column=3)

        # ===========================Row6=======================================
        bequal = Button(w3, text='=', bd=8, padx=30, pady=10, font=('arial', 30, 'bold'), bg='green'
                        , command=f2)
        bequal.grid(row=5, column=0)
        bcmplx = Button(w3, text='j', bd=8, padx=30, pady=10, font=('arial', 30, 'bold'), bg='green'
                        , command=lambda: f1('j'))
        bcmplx.grid(row=5, column=1)
        bbrac1 = Button(w3, text='(', bd=8, padx=30, pady=10, font=('arial', 30, 'bold'), bg='orange'
                        , command=lambda: f1('('))
        bbrac1.grid(row=5, column=2)
        bbrac2 = Button(w3, text=')', bd=8, padx=30, pady=10, font=('arial', 30, 'bold'), bg='orange'
                        , command=lambda: f1(')'))
        bbrac2.grid(row=5, column=3)

        w3.mainloop()
    if v1.get() == 'Complex conversions':

        import cmath
        import math
        w4 = Tk()
        w4.title("Complex conversions")

        def f1():
            w4.destroy()
            w5 = Tk()
            w5.title("Rectangular to polar converter")

            def do():
                r = complex(e1.get())
                p = cmath.polar(r)
                e2.insert(0, str(p))

            def clear():
                e2.delete(0, END)
                e1.delete(0, END)

            l1 = Label(w5, text="Rectangular form:", font=('arial', 15, 'bold'), ).grid(row=0)
            e1 = Entry(w5, font=('arial', 15), width=50)
            e1.grid(row=0, column=1)
            l2 = Label(w5, text="Polar form:", font=('arial', 15, 'bold'), ).grid(row=1)
            e2 = Entry(w5, font=('arial', 15), width=50)
            e2.grid(row=1, column=1)
            b1 = Button(w5, text="Calculate", font=('arial', 15, 'bold'),
                        command=do).grid(row=3, column=1, sticky=NW)
            b2 = Button(w5, text="Clear", font=('arial', 15, 'bold'),
                        command=clear).grid(row=3, column=1)

            w5.mainloop()

        def f2():
            w4.destroy()
            w5 = Tk()
            w5.title("Polar to Rectangular converter")

            def do():
                rad = float(e1.get())
                ang = float(e2.get())
                r = cmath.rect(rad, ang)
                e3.insert(0, str(r))

            def clear():
                e2.delete(0, END)
                e1.delete(0, END)

            l1 = Label(w5, text="Radius:", font=('arial', 15, 'bold'), ).grid(row=0)
            e1 = Entry(w5, font=('arial', 15), width=50)
            e1.grid(row=0, column=1)
            l2 = Label(w5, text="Angle(in radians):", font=('arial', 15, 'bold'), ).grid(row=1)
            e2 = Entry(w5, font=('arial', 15), width=50)
            e2.grid(row=1, column=1)
            l3 = Label(w5, text="Rectangular form:", font=('arial', 15, 'bold'),
                       ).grid(row=2)
            e3 = Entry(w5, font=('arial', 15), width=50)
            e3.grid(row=2, column=1)
            b1 = Button(w5, text="Calculate", font=('arial', 15, 'bold'),
                        command=do).grid(row=3, column=1, sticky=NW)
            b2 = Button(w5, text="Clear", font=('arial', 15, 'bold'),
                        command=clear).grid(row=3, column=1)

            w5.mainloop()

        def f3():
            w4.destroy()
            w5 = Tk()
            w5.title("Degrees to Radians converter")

            def do():
                d = float(e1.get())
                rd = math.radians(d)
                e2.insert(0, str(rd))

            def clear():
                e2.delete(0, END)
                e1.delete(0, END)

            l1 = Label(w5, text="Degrees:", font=('arial', 15, 'bold'), ).grid(row=0)
            e1 = Entry(w5, font=('arial', 15), width=50)
            e1.grid(row=0, column=1)
            l2 = Label(w5, text="Radians:", font=('arial', 15, 'bold'), ).grid(row=1)
            e2 = Entry(w5, font=('arial', 15), width=50)
            e2.grid(row=1, column=1)
            b1 = Button(w5, text="Calculate", font=('arial', 15, 'bold'),
                        command=do).grid(row=3, column=1, sticky=NW)
            b2 = Button(w5, text="Clear", font=('arial', 15, 'bold'),
                        command=clear).grid(row=3, column=1)

            w5.mainloop()

        def f4():
            w4.destroy()
            w5 = Tk()
            w5.title("Radians to Degrees converter")

            def do():
                rd = float(e1.get())
                d = math.degrees(rd)
                e2.insert(0, str(d))

            def clear():
                e2.delete(0, END)
                e1.delete(0, END)

            l1 = Label(w5, text="Radians:", font=('arial', 15, 'bold'), ).grid(row=0)
            e1 = Entry(w5, font=('arial', 15), width=50)
            e1.grid(row=0, column=1)
            l2 = Label(w5, text="Degrees:", font=('arial', 15, 'bold'), ).grid(row=1)
            e2 = Entry(w5, font=('arial', 15), width=50)
            e2.grid(row=1, column=1)
            b1 = Button(w5, text="Calculate", font=('arial', 15, 'bold'),
                        command=do).grid(row=3, column=1, sticky=NW)
            b2 = Button(w5, text="Clear", font=('arial', 15, 'bold'),
                        command=clear).grid(row=3, column=1)

            w5.mainloop()

        b1 = Button(w4, text="RECTANGULAR TO POLAR", font=('arial', 30, 'bold'), bd=15, bg='orange',
                    padx=30, pady=15
                    , fg='white', command=f1).grid(row=0)
        b2 = Button(w4, text="POLAR TO RECTANGULAR", font=('arial', 30, 'bold'), bd=15, bg='blue',
                    padx=30, pady=15
                    , fg='white', command=f2).grid(row=1)
        b3 = Button(w4, text="DEGREES TO RADIANS", font=('arial', 30, 'bold'), bd=15, bg='green',
                    padx=63, pady=15, command=f3
                    , fg='white').grid(row=2)
        b4 = Button(w4, text="RADIANS TO DEGREES", font=('arial', 30, 'bold'), bd=15, bg='yellow',
                    padx=63, pady=15, command=f4
                    , fg='white').grid(row=3)

        w4.mainloop()

    if v1.get()=='Trigonometric operations':

        w2.destroy()
        import math
        w6 = Tk()
        w6.title("Trigonometric and Inverse Trigonometric")

        def f1():
            w6.destroy()
            w5 = Tk()
            w5.title("Trigonometric calculator")

            def do1():
                val = float(e1.get())
                if v2.get() == 'Sine':
                    e2.insert(0, math.sin(val))
                if v2.get() == 'Cosine':
                    e2.insert(0, math.cos(val))
                if v2.get() == 'Tangent':
                    e2.insert(0, math.tan(val))
                if v2.get() == 'Secant':
                    e2.insert(0, (1 / (math.cos(val))))
                if v2.get() == 'Cosecant':
                    e2.insert(0, (1 / (math.sin(val))))
                if v2.get() == 'Cotangent':
                    e2.insert(0, (1 / (math.cos(val))))

            def clear():
                e2.delete(0, END)
                e1.delete(0, END)

            v2 = StringVar(value='Enter from below')

            l1 = Label(w5, text="Enter Radians", font=('arial', 15, 'bold')).grid(row=0)
            e1 = Entry(w5, font=('arial', 15), width=50)
            e1.grid(row=0, column=1)
            l3 = Label(w5, text="Enter mode", font=('arial', 15, 'bold')).grid(row=1)
            cb1 = ttk.Combobox(w5, textvariable=v2,
                               font=('arial', 15, 'bold'), width=48)
            cb1['values'] = ('Sine', 'Cosine', 'Tangent', 'Secant', 'Cosecant', 'Cotangent')
            cb1.grid(row=1, column=1)
            l2 = Label(w5, text="Answer is", font=('arial', 15, 'bold')).grid(row=2)
            e2 = Entry(w5, font=('arial', 15), width=50)
            e2.grid(row=2, column=1)

            b1 = Button(w5, text="Calculate", font=('arial', 15, 'bold')
                        , command=do1).grid(row=3, column=1, sticky=NW)
            b2 = Button(w5, text="Clear", font=('arial', 15, 'bold')
                        , command=clear).grid(row=3, column=1)

            w5.mainloop()

        def f2():
            w6.destroy()
            w5 = Tk()
            w5.title("Trigonometric calculator")

            def do2():
                val = float(e1.get())
                if v2.get() == 'Inverse Sine':
                    e2.insert(0, math.asin(val))
                if v2.get() == 'Inverse Cosine':
                    e2.insert(0, math.acos(val))
                if v2.get() == 'Inverse Tangent':
                    e2.insert(0, math.atan(val))
                if v2.get() == 'Inverse Secant':
                    e2.insert(0, (1 / (math.acos(val))))
                if v2.get() == 'Inverse Cosecant':
                    e2.insert(0, (1 / (math.asin(val))))
                if v2.get() == 'Inverse Cotangent':
                    e2.insert(0, (1 / (math.acos(val))))

            def clear():
                e2.delete(0, END)
                e1.delete(0, END)

            v2 = StringVar(value='Enter from below')

            l1 = Label(w5, text="Enter values", font=('arial', 15, 'bold')).grid(row=0)
            e1 = Entry(w5, font=('arial', 15), width=50)
            e1.grid(row=0, column=1)
            l3 = Label(w5, text="Enter mode", font=('arial', 15, 'bold')).grid(row=1)
            cb1 = ttk.Combobox(w5, textvariable=v2,
                               font=('arial', 15, 'bold'), width=48)
            cb1['values'] = ('Inverse Sine', 'Inverse Cosine', 'Inverse Tangent',
                             'Inverse Secant', 'Inverse Cosecant', 'Inverse Cotangent')
            cb1.grid(row=1, column=1)
            l2 = Label(w5, text="Answer is", font=('arial', 15, 'bold')).grid(row=2)
            e2 = Entry(w5, font=('arial', 15), width=50)
            e2.grid(row=2, column=1)
            l3 = Label(w5, text="Note:Answer is in Radians",
                       font=('arial', 15, 'bold')).grid(row=4)

            b1 = Button(w5, text="Calculate", font=('arial', 15, 'bold')
                        , command=do2).grid(row=3, column=1, sticky=NW)
            b2 = Button(w5, text="Clear", font=('arial', 15, 'bold')
                        , command=clear).grid(row=3, column=1)

            w5.mainloop()

        def f3():
            w6.destroy()
            w5 = Tk()
            w5.title("Degrees to Radians converter")

            def do():
                d = float(e1.get())
                rd = math.radians(d)
                e2.insert(0, str(rd))

            def clear():
                e2.delete(0, END)
                e1.delete(0, END)

            l1 = Label(w5, text="Degrees:", font=('arial', 15, 'bold'), ).grid(row=0)
            e1 = Entry(w5, font=('arial', 15), width=50)
            e1.grid(row=0, column=1)
            l2 = Label(w5, text="Radians:", font=('arial', 15, 'bold'), ).grid(row=1)
            e2 = Entry(w5, font=('arial', 15), width=50)
            e2.grid(row=1, column=1)
            b1 = Button(w5, text="Calculate", font=('arial', 15, 'bold'),
                        command=do).grid(row=3, column=1, sticky=NW)
            b2 = Button(w5, text="Clear", font=('arial', 15, 'bold'),
                        command=clear).grid(row=3, column=1)

            w5.mainloop()

        def f4():
            w6.destroy()
            w5 = Tk()
            w5.title("Radians to Degrees converter")

            def do():
                rd = float(e1.get())
                d = math.degrees(rd)
                e2.insert(0, str(d))

            def clear():
                e2.delete(0, END)
                e1.delete(0, END)

            l1 = Label(w5, text="Radians:", font=('arial', 15, 'bold'), ).grid(row=0)
            e1 = Entry(w5, font=('arial', 15), width=50)
            e1.grid(row=0, column=1)
            l2 = Label(w5, text="Degrees:", font=('arial', 15, 'bold'), ).grid(row=1)
            e2 = Entry(w5, font=('arial', 15), width=50)
            e2.grid(row=1, column=1)
            b1 = Button(w5, text="Calculate", font=('arial', 15, 'bold'),
                        command=do).grid(row=3, column=1, sticky=NW)
            b2 = Button(w5, text="Clear", font=('arial', 15, 'bold'),
                        command=clear).grid(row=3, column=1)

            w5.mainloop()

        b1 = Button(w6, text="TRIGONOMETRY", font=('arial', 30, 'bold'), bd=15, bg='orange',
                    padx=124, pady=15
                    , fg='white', command=f1).grid(row=0)
        b2 = Button(w6, text="INVERSE TRIGONOMETRY", font=('arial', 30, 'bold'), bd=15, bg='blue',
                    padx=30, pady=15
                    , fg='white', command=f2).grid(row=1)
        b3 = Button(w6, text="DEGREES TO RADIANS", font=('arial', 30, 'bold'), bd=15, bg='green',
                    padx=63, pady=15, command=f3
                    , fg='white').grid(row=2)
        b4 = Button(w6, text="RADIANS TO DEGREES", font=('arial', 30, 'bold'), bd=15, bg='yellow',
                    padx=63, pady=15, command=f4
                    , fg='white').grid(row=3)

        w6.mainloop()

    if v1.get()=='Logarithmic and exponential':
        w2.destroy()
        import math

        w7 = Tk()
        w7.title("Logarithmic and exponential")

        def f1():
            w7.destroy()
            w8 = Tk()
            w8.title("Logarithmic")

            def do():
                val = float(e1.get())
                b = float(e2.get())
                d = math.log(val, b)
                e3.insert(0, str(d))

            def clear():
                e2.delete(0, END)
                e1.delete(0, END)
                e3.delete(0, END)


            l1 = Label(w8, text="Enter Value:", font=('arial', 15, 'bold'), ).grid(row=0)
            e1 = Entry(w8, font=('arial', 15), width=50)
            e1.grid(row=0, column=1)
            l3 = Label(w8, text="Logarithm value :", font=('arial', 15, 'bold'), ).grid(row=2)
            e3 = Entry(w8, font=('arial', 15), width=50)
            e3.grid(row=2, column=1)
            l2 = Label(w8, text="Enter base :", font=('arial', 15, 'bold'), ).grid(row=1)
            e2 = Entry(w8, font=('arial', 15), width=50)
            e2.grid(row=1, column=1)
            l4 = Label(w8, text="Note: if base is 'e' then type 2.718281828459045 ",
                       font=('arial', 15, 'bold'), ).grid(row=4)

            b1 = Button(w8, text="Calculate", font=('arial', 15, 'bold'),
                        command=do).grid(row=3, column=1, sticky=NW)
            b2 = Button(w8, text="Clear", font=('arial', 15, 'bold'),
                        command=clear).grid(row=3, column=1)

            w8.mainloop()

        def f2():
            w7.destroy()
            w8 = Tk()
            w8.title("Exponential")

            def do():
                val = float(e1.get())
                d = math.exp(val)
                e3.insert(0, str(d))

            def clear():
                e1.delete(0, END)
                e3.delete(0, END)


            l1 = Label(w8, text="Enter Value:", font=('arial', 15, 'bold'), ).grid(row=0)
            e1 = Entry(w8, font=('arial', 15), width=50)
            e1.grid(row=0, column=1)
            l3 = Label(w8, text="Exponential value :", font=('arial', 15, 'bold'), ).grid(row=1)
            e3 = Entry(w8, font=('arial', 15), width=50)
            e3.grid(row=1, column=1)

            b1 = Button(w8, text="Calculate", font=('arial', 15, 'bold'),
                        command=do).grid(row=3, column=1, sticky=NW)
            b2 = Button(w8, text="Clear", font=('arial', 15, 'bold'),
                        command=clear).grid(row=3, column=1)

            w8.mainloop()

        b2 = Button(w7, text="LOGARITHMIC", font=('arial', 30, 'bold'), bd=15, bg='blue',
                    padx=30, pady=15
                    , fg='white', command=f1).grid(row=1)
        b3 = Button(w7, text="EXPONENTIAL", font=('arial', 30, 'bold'), bd=15, bg='green',
                    padx=30, pady=15
                    , fg='white', command=f2).grid(row=2)

        w7.mainloop()

    if v1.get()=='Higher and lower powers':
        w2.destroy()
        w8 = Tk()
        w8.title("HP and LP")

        def do():
            val = float(e1.get())
            b = float(e2.get())
            d = val ** b
            e3.insert(0, str(d))

        def clear():
            e2.delete(0, END)
            e1.delete(0, END)
            e3.delete(0, END)

        l1 = Label(w8, text="Enter Value:", font=('arial', 15, 'bold'), ).grid(row=0)
        e1 = Entry(w8, font=('arial', 15), width=50)
        e1.grid(row=0, column=1)
        l3 = Label(w8, text="Answer :", font=('arial', 15, 'bold'), ).grid(row=2)
        e3 = Entry(w8, font=('arial', 15), width=50)
        e3.grid(row=2, column=1)
        l2 = Label(w8, text="Enter power value :", font=('arial', 15, 'bold'), ).grid(row=1)
        e2 = Entry(w8, font=('arial', 15), width=50)
        e2.grid(row=1, column=1)
        l4 = Label(w8, text="Note:Enter lower powers in float values", font=('arial', 15, 'bold'), ).grid(row=4)

        b1 = Button(w8, text="Calculate", font=('arial', 15, 'bold'),
                    command=do).grid(row=3, column=1, sticky=NW)
        b2 = Button(w8, text="Clear", font=('arial', 15, 'bold'),
                    command=clear).grid(row=3, column=1)
        w8.mainloop()

    if v1.get()=='Other operations':
        w2.destroy()

        import math
        w6 = Tk()
        w6.title("OTHERS")

        def f1():
            w8 = Tk()
            w8.title("GCD")

            def do():
                val = int(e1.get())
                b = int(e2.get())
                d = math.gcd(val, b)
                e3.insert(0, str(d))

            def clear():
                e2.delete(0, END)
                e1.delete(0, END)
                e3.delete(0, END)

            w6.destroy()
            l1 = Label(w8, text="Enter Number 1:", font=('arial', 15, 'bold'), ).grid(row=0)
            e1 = Entry(w8, font=('arial', 15), width=50)
            e1.grid(row=0, column=1)
            l3 = Label(w8, text="GCD:", font=('arial', 15, 'bold'), ).grid(row=2)
            e3 = Entry(w8, font=('arial', 15), width=50)
            e3.grid(row=2, column=1)
            l2 = Label(w8, text="Enter Number 2 :", font=('arial', 15, 'bold'), ).grid(row=1)
            e2 = Entry(w8, font=('arial', 15), width=50)
            e2.grid(row=1, column=1)
            l4 = Label(w8, text="Note: Enter integers to calculate GCD",
                       font=('arial', 15, 'bold'), ).grid(row=4)

            b1 = Button(w8, text="Calculate", font=('arial', 15, 'bold'),
                        command=do).grid(row=3, column=1, sticky=NW)
            b2 = Button(w8, text="Clear", font=('arial', 15, 'bold'),
                        command=clear).grid(row=3, column=1)

            w8.mainloop()

        def f2():
            w8 = Tk()
            w8.title("GCD")

            def do():
                val = int(e1.get())
                b = int(e2.get())
                d = math.gcd(val, b)
                lcm = (val * b) / d
                e3.insert(0, str(int(lcm)))

            def clear():
                e2.delete(0, END)
                e1.delete(0, END)
                e3.delete(0, END)

            w6.destroy()
            l1 = Label(w8, text="Enter Number 1:", font=('arial', 15, 'bold'), ).grid(row=0)
            e1 = Entry(w8, font=('arial', 15), width=50)
            e1.grid(row=0, column=1)
            l3 = Label(w8, text="LCM:", font=('arial', 15, 'bold'), ).grid(row=2)
            e3 = Entry(w8, font=('arial', 15), width=50)
            e3.grid(row=2, column=1)
            l2 = Label(w8, text="Enter Number 2 :", font=('arial', 15, 'bold'), ).grid(row=1)
            e2 = Entry(w8, font=('arial', 15), width=50)
            e2.grid(row=1, column=1)
            l4 = Label(w8, text="Note: Enter integers to calculate LCM",
                       font=('arial', 15, 'bold'), ).grid(row=4)

            b1 = Button(w8, text="Calculate", font=('arial', 15, 'bold'),
                        command=do).grid(row=3, column=1, sticky=NW)
            b2 = Button(w8, text="Clear", font=('arial', 15, 'bold'),
                        command=clear).grid(row=3, column=1)

            w8.mainloop()

        def f3():
            w8 = Tk()
            w8.title("GCD")

            def do():
                val = int(e1.get())
                d = math.factorial(val)
                e3.insert(0, str(int(d)))

            def clear():
                e1.delete(0, END)
                e3.delete(0, END)

            w6.destroy()
            l1 = Label(w8, text="Enter Number :", font=('arial', 15, 'bold'), ).grid(row=0)
            e1 = Entry(w8, font=('arial', 15), width=50)
            e1.grid(row=0, column=1)
            l3 = Label(w8, text="Factorial:", font=('arial', 15, 'bold'), ).grid(row=2)
            e3 = Entry(w8, font=('arial', 15), width=50)
            e3.grid(row=2, column=1)

            l4 = Label(w8, text="Note: Enter positive integers to calculate Factorial",
                       font=('arial', 15, 'bold'), ).grid(row=4)

            b1 = Button(w8, text="Calculate", font=('arial', 15, 'bold'),
                        command=do).grid(row=3, column=1, sticky=NW)
            b2 = Button(w8, text="Clear", font=('arial', 15, 'bold'),
                        command=clear).grid(row=3, column=1)

            w8.mainloop()

        b1 = Button(w6, text="GCD", font=('arial', 30, 'bold'), bd=15, bg='orange',
                    padx=130, pady=15
                    , fg='white', command=f1).grid(row=0)
        b2 = Button(w6, text="LCM", font=('arial', 30, 'bold'), bd=15, bg='blue',
                    padx=130, pady=15, command=f2
                    , fg='white').grid(row=1)
        b3 = Button(w6, text="FACTORIAL", font=('arial', 30, 'bold'), bd=15, bg='green',
                    padx=63, pady=15, command=f3
                    , fg='white').grid(row=2)

        w6.mainloop()






v1=StringVar(value="Select your mode..")
Label(text="SCIENTIFIC CALCULATOR :) :)",font=('arial',30,'bold'),
borderwidth=15,relief='raised',bg='orange',fg='white').grid(row=0)
c1=ttk.Combobox(font=('arial',30,'bold'),textvariable=v1)
c1['values']=('Normal operations','Complex operations','Higher and lower powers','Complex conversions',
              'Trigonometric operations','Logarithmic and exponential'
              ,'Other operations')

c1.grid(row=2)
bm1=Button(text="GO",font=('arial',30,'bold'),bd=15,bg='green',
          fg='white',command=f4).grid(row=3)

w2.mainloop()