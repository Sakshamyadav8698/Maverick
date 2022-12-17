from tkinter import*

import math,random,os

from tkinter import messagebox

class Bill_App:
    
    def __init__(self,root):
        
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("BILLING SOFTWARE PROJECT")
        bg_color="#ffe100"
        title=Label(self.root,text="MAVERICKS",bd=12,relief=GROOVE,bg=bg_color,fg="#000000",font=("algerian",30,"bold"),pady=2).pack(fill=X)
        
        #Supply variables
        
        self.tb=IntVar()
        self.tp=IntVar()
        self.sn=IntVar()
        self.tm=IntVar()
        self.sp=IntVar()
        self.fc=IntVar()
        
        #Snack variables
        
        self.c1=IntVar()
        self.c2=IntVar()
        self.c3=IntVar()
        self.c4=IntVar()
        self.c5=IntVar()
        self.c6=IntVar()
        
        #Ration variables
        
        self.r1=IntVar()
        self.r2=IntVar()
        self.r3=IntVar()
        self.r4=IntVar()
        self.r5=IntVar()
        self.r6=IntVar()
        
        #Total Price and Tax variables
        
        self.tspp=StringVar()
        self.tsnp=StringVar()
        self.trtp=StringVar()
        
        self.tspt=StringVar()
        self.tsnt=StringVar()
        self.trtt=StringVar()
        
        #Customer variables and random bill numbers
        
        self.cn=StringVar()
        self.cphn=StringVar()
        
        self.cbn=StringVar()
        x=random.randint(0000,9999)
        self.cbn.set(str(x))
        
        self.search=StringVar()
        
        #Customer frame
        
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="CUSTOMER DETAILS",font=("algerian",15,"bold"),fg="#000000",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)
        
        cname_lbl=Label(F1,text="Customer Name",bg=bg_color,fg="#000000",font=("algerian",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=15,textvariable=self.cn,font="algerian 14",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        
        cphn_lbl=Label(F1,text="Phone no.",bg=bg_color,fg="#000000",font=("algerian",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_txt=Entry(F1,width=15,textvariable=self.cphn,font="algerian 14",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)
        
        c_bill_lbl=Label(F1,text="Bill no.",bg=bg_color,fg="#000000",font=("algerian",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        c_bill_txt=Entry(F1,width=15,textvariable=self.search,font="algerian 14",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)
        
        bill_btn=Button(F1,text="Search",command=self.find_bill,width=10,bd=7,font="algerian 12 bold").grid(row=0,column=6,pady=10,padx=10)
        
        #Supplies Frame
        
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="SUPPLIES",font=("algerian",15,"bold"),fg="#000000",bg=bg_color)
        F2.place(x=5,y=180,width=325,height=380)
        
        tb_lbl=Label(F2,text="Toothbrush",font=("algerian",14),bg=bg_color,fg="#0011ff").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        tb_txt=Entry(F2,width=10,textvariable=self.tb,font=("arial",14),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
        
        tp_lbl=Label(F2,text="Toothpaste",font=("algerian",14),bg=bg_color,fg="#0011ff").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        tp_txt=Entry(F2,width=10,textvariable=self.tp,font=("arial",14),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
        
        sn_lbl=Label(F2,text="Sanitiser",font=("algerian",14),bg=bg_color,fg="#0011ff").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        sn_txt=Entry(F2,width=10,textvariable=self.sn,font=("arial",14),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
        
        tm_lbl=Label(F2,text="Trimmer",font=("algerian",14),bg=bg_color,fg="#0011ff").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        tm_txt=Entry(F2,width=10,textvariable=self.tm,font=("arial",14),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
        
        sp_lbl=Label(F2,text="Sanitary pad",font=("algerian",14),bg=bg_color,fg="#0011ff").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        sp_txt=Entry(F2,width=10,textvariable=self.sp,font=("arial",14),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
        
        fc_lbl=Label(F2,text="Face cream",font=("algerian",14),bg=bg_color,fg="#0011ff").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        fc_txt=Entry(F2,width=10,textvariable=self.fc,font=("arial",14),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
        
        #Snacks Frame
        
        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="SNACKS",font=("algerian",15,"bold"),fg="#000000",bg=bg_color)
        F3.place(x=340,y=180,width=325,height=380)
        
        ch_lbl=Label(F3,text="Chips",font=("algerian",14),bg=bg_color,fg="#0011ff").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        ch_txt=Entry(F3,width=10,textvariable=self.c1,font=("arial",14),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
        
        cl_lbl=Label(F3,text="Chocolate",font=("algerian",14),bg=bg_color,fg="#0011ff").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        cl_txt=Entry(F3,width=10,textvariable=self.c2,font=("arial",14),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
        
        sd_lbl=Label(F3,text="Soft drink",font=("algerian",14),bg=bg_color,fg="#0011ff").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        sd_txt=Entry(F3,width=10,textvariable=self.c3,font=("arial",14),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
        
        cn_lbl=Label(F3,text="Candy",font=("algerian",14),bg=bg_color,fg="#0011ff").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        cn_txt=Entry(F3,width=10,textvariable=self.c4,font=("arial",14),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
        
        ic_lbl=Label(F3,text="Ice cream",font=("algerian",14),bg=bg_color,fg="#0011ff").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        ic_txt=Entry(F3,width=10,textvariable=self.c5,font=("arial",14),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
        
        cc_lbl=Label(F3,text="Cup Cake",font=("algerian",14),bg=bg_color,fg="#0011ff").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        cc_txt=Entry(F3,width=10,textvariable=self.c6,font=("arial",14),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
        
        #Ration Frame
        
        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Stationery",font=("algerian",15,"bold"),fg="#000000",bg=bg_color)
        F4.place(x=670,y=180,width=325,height=380)
        
        r1_lbl=Label(F4,text="Register",font=("algerian",14),bg=bg_color,fg="#0011ff").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        r1_txt=Entry(F4,width=10,textvariable=self.r1,font=("arial",14),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)
        
        r2_lbl=Label(F4,text="Pen",font=("algerian",14),bg=bg_color,fg="#0011ff").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        r2_txt=Entry(F4,width=10,textvariable=self.r2,font=("arial",14),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)
        
        r3_lbl=Label(F4,text="Pencil",font=("algerian",14),bg=bg_color,fg="#0011ff").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        r3_txt=Entry(F4,width=10,textvariable=self.r3,font=("arial",14),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)
        
        r4_lbl=Label(F4,text="Geometry box",font=("algerian",14),bg=bg_color,fg="#0011ff").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        r4_txt=Entry(F4,width=10,textvariable=self.r4,font=("arial",14),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)
        
        r5_lbl=Label(F4,text="Notes",font=("algerian",14),bg=bg_color,fg="#0011ff").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        r5_txt=Entry(F4,width=10,textvariable=self.r5,font=("arial",14),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)
        
        r6_lbl=Label(F4,text="Sheets",font=("algerian",14),bg=bg_color,fg="#0011ff").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        r6_txt=Entry(F4,width=10,textvariable=self.r6,font=("arial",14),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
        
        #Bill Area

        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1000,y=180,width=350,height=380)
        bill_title=Label(F5,text="Bill",font="algerian 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        
        #Button Frame
        
        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="BILL MENU",font=("algerian",15,"bold"),fg="#000000",bg=bg_color)
        F6.place(x=0,y=560,relwidth=1,height=140)
        
        m1_lbl=Label(F6,text="Total Supplies Price",bg=bg_color,fg="#0011ff",font=("algerian",14)).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable=self.tspp,font="arial 10",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)
        
        m2_lbl=Label(F6,text="Total Snacks Price",bg=bg_color,fg="#0011ff",font=("algerian",14)).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(F6,width=18,textvariable=self.tsnp,font="arial 10",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)
        
        m3_lbl=Label(F6,text="Total ST     Price",bg=bg_color,fg="#0011ff",font=("algerian",14)).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(F6,width=18,textvariable=self.trtp,font="arial 10",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)
        
        c1_lbl=Label(F6,text="Supplies tax",bg=bg_color,fg="#0011ff",font=("algerian",14)).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        c1_txt=Entry(F6,width=18,textvariable=self.tspt,font="arial 10",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)
        
        c2_lbl=Label(F6,text="Snacks tax",bg=bg_color,fg="#0011ff",font=("algerian",14)).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        c2_txt=Entry(F6,width=18,textvariable=self.tsnt,font="arial 10",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)
        
        c3_lbl=Label(F6,text="ST     tax",bg=bg_color,fg="#0011ff",font=("algerian",14)).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        c3_txt=Entry(F6,width=18,textvariable=self.trtt,font="arial 10",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)
        
        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=750,width=580,height=105)
        
        total_btn=Button(btn_F,command=self.total,text="TOTAL",bg="#000000",fg="white",bd=5,pady=15,width=10,font="arial 14").grid(row=0,column=0,padx=5,pady=5)
        gb_btn=Button(btn_F,text="Generate bill",command=self.bill_area,bg="#000000",fg="white",bd=5,pady=15,width=10,font="arial 14").grid(row=0,column=1,padx=5,pady=5)
        clear_btn=Button(btn_F,text="CLEAR",command=self.clear_data,bg="#000000",fg="white",bd=5,pady=15,width=10,font="arial 14").grid(row=0,column=2,padx=5,pady=5)
        exit_btn=Button(btn_F,text="EXIT",command=self.Exit_app,bg="#000000",fg="white",bd=5,pady=15,width=10,font="arial 14").grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()
        
    def total(self):
        
        self.s_t_b=(self.tb.get()*50)
        self.s_t_p=(self.tp.get()*70)
        self.s_s_n=(self.sn.get()*40)
        self.s_t_m=(self.tm.get()*1500)
        self.s_s_p=(self.sp.get()*20)
        self.s_f_c=(self.fc.get()*90)
        
        self.s_c_p=(self.c1.get()*100)
        self.s_c_k=(self.c2.get()*70)
        self.s_s_d=(self.c3.get()*50)
        self.s_c_d=(self.c4.get()*10)
        self.s_i_c=(self.c5.get()*70)
        self.s_c_c=(self.c6.get()*30)
        
        self.r_f_r=(self.r1.get()*35)
        self.r_s_t=(self.r2.get()*20)
        self.r_s_g=(self.r3.get()*25)
        self.r_r_c=(self.r4.get()*100)
        self.r_g_m=(self.r5.get()*40)
        self.r_p_l=(self.r6.get()*100)
       
        self.total_supply_price=float(
            self.s_t_b+
            self.s_t_p+
            self.s_s_n+
            self.s_t_m+
            self.s_s_p+
            self.s_f_c)
        self.tspp.set("Rs. "+str(self.total_supply_price))
        self.sp_tax=round((self.total_supply_price*0.1),2)
        self.tspt.set("Rs. "+str(self.sp_tax))
        
        self.total_snack_price=float(
            self.s_c_p+
            self.s_c_k+
            self.s_s_d+
            self.s_c_d+
            self.s_i_c+
            self.s_c_c)
        self.tsnp.set("Rs. "+str(self.total_snack_price))
        self.sn_tax=round((self.total_snack_price*0.1),2)
        self.tsnt.set("Rs. "+str(self.sn_tax))
        
        self.total_ration_price=float(
            self.r_f_r+
            self.r_s_t+
            self.r_s_g+
            self.r_r_c+
            self.r_g_m+
            self.r_p_l)
        self.trtp.set("Rs. "+str(self.total_ration_price))
        self.r_tax=round((self.total_ration_price*0.1),2)
        self.trtt.set("Rs. "+str(self.r_tax))
        
        self.total_bill=float(self.total_supply_price+
                              self.total_snack_price+
                              self.total_ration_price+
                              self.sp_tax+
                              self.sn_tax+
                              self.r_tax)
    
    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\t     MAVERICKS\n")
        self.txtarea.insert(END,f"\n Bill Number : {self.cbn.get()}")
        self.txtarea.insert(END,f"\n Customer Name : {self.cn.get()} ")
        self.txtarea.insert(END,f"\n Phone Name : {self.cphn.get()}")
        self.txtarea.insert(END,f"\n======================================")
        self.txtarea.insert(END,f"\nProducts\t\tQTY\t\tPrice")
        self.txtarea.insert(END,f"\n======================================")
        
    
    def bill_area(self):
        
        if self.cn.get()=="" or self.cphn.get()=="":
            messagebox.showerror("Error","Customer details are required!")
        elif self.tspp.get()=="Rs. 0.0" and self.tsnp.get()=="Rs. 0.0" and self.trtp.get()=="Rs. 0.0":
            messagebox.showerror("Error","No Products Selected!")
        else:
            self.welcome_bill()
            
            #Supply loop
            
            if self.tb.get()!=0:
                self.txtarea.insert(END,f"\nToothbrush\t\t{self.tb.get()}\t\t{self.s_t_b}")
            if self.tp.get()!=0:
                self.txtarea.insert(END,f"\nToothpaste\t\t{self.tp.get()}\t\t{self.s_t_p}")
            if self.sn.get()!=0:
                self.txtarea.insert(END,f"\nSanitiser\t\t{self.sn.get()}\t\t{self.s_s_n}")
            if self.tm.get()!=0:
                self.txtarea.insert(END,f"\n Trimmer\t\t{self.tm.get()}\t\t{self.s_t_m}")
            if self.sp.get()!=0:
                self.txtarea.insert(END,f"\nSanitary pad\t\t{self.sp.get()}\t\t{self.s_s_p}")
            if self.fc.get()!=0:
                self.txtarea.insert(END,f"\nFace cream\t\t{self.fc.get()}\t\t{self.s_f_c}")
            
            #Snacks loop
            
            if self.c1.get()!=0:
                self.txtarea.insert(END,f"\n   Chips\t\t{self.c1.get()}\t\t{self.s_c_p}")
            if self.c2.get()!=0:
                self.txtarea.insert(END,f"\nChocolate\t\t{self.c2.get()}\t\t{self.s_c_k}")
            if self.c3.get()!=0:
                self.txtarea.insert(END,f"\nSoft drink\t\t{self.c3.get()}\t\t{self.s_s_d}")
            if self.c4.get()!=0:
                self.txtarea.insert(END,f"\n   Candy\t\t{self.c4.get()}\t\t{self.s_c_d}")
            if self.c5.get()!=0:
                self.txtarea.insert(END,f"\nIce cream\t\t{self.c5.get()}\t\t{self.s_i_c}")
            if self.c6.get()!=0:
                self.txtarea.insert(END,f"\nCup cake\t\t{self.c6.get()}\t\t{self.s_c_c}")
                
            #Ration loop
                    
            if self.r1.get()!=0:
                self.txtarea.insert(END,f"\n   Register\t\t{self.r1.get()}\t\t{self.r_f_r}")
            if self.r2.get()!=0:
                self.txtarea.insert(END,f"\n    Pen\t\t{self.r2.get()}\t\t{self.r_s_t}")
            if self.r3.get()!=0:
                self.txtarea.insert(END,f"\n   Pencil\t\t{self.r3.get()}\t\t{self.r_s_g}")
            if self.r4.get()!=0:
                self.txtarea.insert(END,f"\n    Geometry box\t\t{self.r4.get()}\t\t{self.r_r_c}")
            if self.r5.get()!=0:
                self.txtarea.insert(END,f"\n    Notes\t\t{self.r5.get()}\t\t{self.r_g_m}")
            if self.r6.get()!=0:
                self.txtarea.insert(END,f"\n   Sheets\t\t{self.r6.get()}\t\t{self.r_p_l}")
                
            self.txtarea.insert(END,f"\n--------------------------------------")
            if self.tspt.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\nSupply Tax\t\t\t{self.tspt.get()}")
            if self.tsnt.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\nSnacks Tax\t\t\t{self.tsnt.get()}")
            if self.trtt.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\nST     Tax\t\t\t{self.trtt.get()}")
            self.txtarea.insert(END,f"\n--------------------------------------")
            self.txtarea.insert(END,f"\nTotal Bill\t\t\tRs. {self.total_bill}")
            self.txtarea.insert(END,f"\n**************************************")
            self.save_bill()
            
    def save_bill(self):
        opt=messagebox.askyesno("Save Bill","Do you want the bill to be saved?",)
        
        if opt>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("Bills/"+str(self.cbn.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill {self.cbn.get()} was Saved Successfully!")
        else:
            return
    
    def find_bill(self):
        present="no"
        for i in os.listdir("Bills/"):
            if i.split('.')[0]==self.search.get():
                f1=open(f"Bills/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","The Bill no. Entered was Invalid!")
    
    def clear_data(self):
        
        opt=messagebox.askyesno("Clear","Are You Sure You Want to Clear?")
        if opt>0:
        
            #Variables to be cleared
            
            self.tb.set(0)
            self.tp.set(0)
            self.sn.set(0)
            self.tm.set(0)
            self.sp.set(0)
            self.fc.set(0)
            
            self.c1.set(0)
            self.c2.set(0)
            self.c3.set(0)
            self.c4.set(0)
            self.c5.set(0)
            self.c6.set(0)
            
            self.r1.set(0)
            self.r2.set(0)
            self.r3.set(0)
            self.r4.set(0)
            self.r5.set(0)
            self.r6.set(0)
            
            self.tspp.set("")
            self.tsnp.set("")
            self.trtp.set("")
            
            self.tspt.set("")
            self.tsnt.set("")
            self.trtt.set("")
            
            self.cn.set("")
            self.cphn.set("")
            
            self.cbn.set("")
            x=random.randint(0000,9999)
            self.cbn.set(str(x))
            
            self.search.set("")
        
    def Exit_app(self):
        opt=messagebox.askyesno("Exit","Are You Sure You Want to EXIT?")
        if opt>0:
            self.root.destroy()
    
root=Tk()
obj=Bill_App(root)
root.mainloop()