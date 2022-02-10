import copy
import sys
import os
from os import path
import numpy as np
from matplotlib.image import imread
from PIL import Image, ImageOps
import shutil
import ntpath
from tkinter import *
from tkinter import font
from tkinter import messagebox
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

from convert_sra import convert_sra
import helptext as ht

import IC_modelMethods as model


#Toggle Functions
def simpleToggle(toggle, input):
    if toggle.get() == "False":
        input.config(state='disabled')
    elif toggle.get()== "True":
        input.config(state='enabled')

def tidaltoggle():
    if variables["tidal_var"].get() == 'True':
        stellon_n.config(state='enabled')
        desync_n.config(state='enabled')
        tempcon_n.config(state='enabled')
    else:
        stellon_n.config(state='disabled')
        desync_n.config(state='disabled')
        tempcon_n.config(state='disabled')

def aquatoggle():
    if variables["aquap_var"].get() == "True":
        desertp_n.config(state='disabled')
        imgsratogtog_n.config(state='disabled')
        hghtmpimg_n.config(state='disabled')
        hghtmpimg_b.config(state='disabled')
        waterhres_n.config(state='disabled')
        highelev_n.config(state='disabled')
        lowelev_n.config(state='disabled')
        imgdebugtog_n.config(state='disabled')
        sranme_n.config(state='disabled')
        lndsra_n.config(state='disabled')
        lndsra_b.config(state='disabled')
        tposra_n.config(state='disabled')
        tposra_b.config(state='disabled')
    elif variables["aquap_var"].get() == "False":
        desertp_n.config(state='enabled')
        imgsratogtog_n.config(state='enabled')
        if variables["imgsratogtog_var"].get() == "False":
            hghtmpimg_n.config(state='enabled')
            hghtmpimg_b.config(state='enabled')
            waterhres_n.config(state='enabled')
            highelev_n.config(state='enabled')
            imgdebugtog_n.config(state='enabled')
            sranme_n.config(state='enabled')
            lndsra_n.config(state='disabled')
            lndsra_b.config(state='disabled')
            tposra_n.config(state='disabled')
            tposra_b.config(state='disabled')
        elif variables["imgsratogtog_var"].get() == "True":
            hghtmpimg_n.config(state='disabled')
            hghtmpimg_b.config(state='disabled')
            waterhres_n.config(state='disabled')
            highelev_n.config(state='disabled')
            imgdebugtog_n.config(state='disabled')
            sranme_n.config(state='disabled')
            lndsra_n.config(state='enabled')
            lndsra_b.config(state='enabled')
            tposra_n.config(state='enabled')
            tposra_b.config(state='enabled')

def dsrtoggle():
    if variables["desertp_var"].get() == "True":
        aquap_n.config(state='disabled')
        #variables["aquaptog_var"] = "False" #looks like toggling the aquatog triggers the event just like if it had been done by user
        
        print(variables["imgsratogtog_var"].get())
        if variables["imgsratogtog_var"].get() == "image":
            lowelev_n.config(state='enabled')
    elif variables["desertp_var"].get() == "False":
        aquap_n.config(state='enabled')
        #variables["aquaptog_var"] = "True"
        lowelev_n.config(state='disabled')
        
def soilalbtoggle():
    simpleToggle(variables["soilalbtog_var"], soilalb_n)

def soildepthtoggle():
    simpleToggle(variables["soildepthtog_var"], soildepth_n)

def capsoiltoggle():
    simpleToggle(variables["capsoiltog_var"], capsoil_n)

def soilwcptoggle():
    simpleToggle(variables["soilwcptog_var"], soilwcp_n)
    
def soilsattoggle():
    simpleToggle(variables["soilsattog_var"], soilsat_n)

def vegtoggle(self):
    if variables["vegetat_var"].get() == "None":
        vegacce_n.config(state='disabled')
        initgrw_n.config(state='disabled')
        nfrtgrw_n.config(state='disabled')
        initstcd_n.config(state='disabled')
        initrgh_n.config(state='disabled')
        initslc_n.config(state='disabled')
        initplc_n.config(state='disabled')
    else:
        vegacce_n.config(state='enabled')
        initgrw_n.config(state='enabled')
        nfrtgrw_n.config(state='enabled')
        initstcd_n.config(state='enabled')
        initrgh_n.config(state='enabled')
        initslc_n.config(state='enabled')
        initplc_n.config(state='enabled')

def snowalbtoggle():
    simpleToggle(variables["snowalb_var"], snowalb_n)

def mxsnowtoggle():
    simpleToggle(variables["mxsnowtog_var"], mxsnow_n)

def mldepthtoggle():
    simpleToggle(variables["mldepthtog_var"], mldepth_n)

def oceanalbtoggle():
    simpleToggle(variables["oceanalbtog_var"], oceanalb_n)

def imgsratoggle():
    global desertog
    if variables["imgsratogtog_var"].get() == "sra": #SRA mode
        aquap_n.config(state='disabled')
        desertp_n.config(state='disabled')
        hghtmpimg_n.config(state='disabled')
        hghtmpimg_b.config(state='disabled')
        waterhres_n.config(state='disabled')
        highelev_n.config(state='disabled')
        lowelev_n.config(state='disabled')
        imgdebugtog_n.config(state='disabled')
        sranme_n.config(state='disabled')
        lndsra_n.config(state='enabled')
        lndsra_b.config(state='enabled')
        tposra_n.config(state='enabled')
        tposra_b.config(state='enabled')
    elif variables["imgsratogtog_var"].get() == "image": #image mode
        aquap_n.config(state='enabled')
        desertp_n.config(state='enabled')
        hghtmpimg_n.config(state='enabled')
        hghtmpimg_b.config(state='enabled')
        waterhres_n.config(state='enabled')
        highelev_n.config(state='enabled')
        if variables["desertp_var"].get() == "True":
            lowelev_n.config(state='enabled')
        imgdebugtog_n.config(state='enabled')
        sranme_n.config(state='enabled')
        lndsra_n.config(state='disabled')
        lndsra_b.config(state='disabled')
        tposra_n.config(state='disabled')
        tposra_b.config(state='disabled')

def hghtimgget():
    filename = askopenfilename(filetypes=(("png files","*.png"),("All files","*.*")))
    variables["hghtmpimg_var"].set(filename) # add this

def landsraget():
    filename = askopenfilename(filetypes=(("sra files","*.sra"),("All files","*.*")))
    variables["hghtmpimg_var"].set(filename) # add this

def toposraget():
    filename = askopenfilename(filetypes=(("sra files","*.sra"),("All files","*.*")))
    variables["hghtmpimg_var"].set(filename) # add this

def pressuretoggle():
    simpleToggle(variables["pressuretog_var"], pressure_n)

def gascontoggle():
    simpleToggle(variables["gascontog_var"], gascon_n)

def ptoggle():
    global ptog
    #if ptog == 0:
    if variables["partialptog_var"].get() == "True":
        pH2_n.config(state='enabled')
        pHe_n.config(state='enabled')
        pN2_n.config(state='enabled')
        pO2_n.config(state='enabled')
        pAr_n.config(state='enabled')
        pNe_n.config(state='enabled')
        pKr_n.config(state='enabled')
        pH2O_n.config(state='enabled')
        pCO2_n.config(state='enabled')
    elif variables["partialptog_var"].get() == "False":
        pH2_n.config(state='disabled')
        pHe_n.config(state='disabled')
        pN2_n.config(state='disabled')
        pO2_n.config(state='disabled')
        pAr_n.config(state='disabled')
        pNe_n.config(state='disabled')
        pKr_n.config(state='disabled')
        pH2O_n.config(state='disabled')
        pCO2_n.config(state='disabled')

def gtoggle():
    global gtog
    #if gtog == 0:
    if variables["glacialtog_var"].get() == "True":
        gtog = 1
        inith_n.config(state='enabled')
        mndph_n.config(state='enabled')
    elif variables["glacialtog_var"].get() == "False":
        inith_n.config(state='disabled')
        mndph_n.config(state='disabled')

def stmtoggle():
    simpleToggle(variables["stmtog_var"], highcadtog_n)
    
def baltoggle ():
    global baltog
    if variables["rntbaltog_var"].get() == "True":
        runtme_n.config(state='disabled')
        trshld_n.config(state='enabled')
        bselne_n.config(state='enabled')
        maxyr_n.config(state='enabled')
        minyr_n.config(state='enabled')
    elif variables["rntbaltog_var"].get() == "False":
        runtme_n.config(state='enabled')
        trshld_n.config(state='disabled')
        bselne_n.config(state='disabled')
        maxyr_n.config(state='disabled')
        minyr_n.config(state='disabled')

#Functions
txtcol = '#0f0f9f'

def strip_vardict(variables):
    vars_to_pass = variables.copy()
    #iterate over every value in vars_to_pass
    for key, value in vars_to_pass.items():
        vars_to_pass[key] = value.get()

    return vars_to_pass

def system_check(variables):
    return model.system_check(strip_vardict(variables))

def save_file(variables):

    """Save the current file."""
    filepath = asksaveasfilename(
        defaultextension=".py",
        filetypes=[("Python Files", "*.py"), ("All Files", "*.*")],
    )
    if not filepath:
        return


    return model.save_file(strip_vardict(variables), filepath)
    


window = Tk()# Start the application
window.title("ExoPlaSim: Input Configurator (EPS:IC)")
window.rowconfigure([2], minsize=10, weight=0)
window.columnconfigure([2,4,6,8], minsize=10, weight=1)

default_font = font.nametofont("TkDefaultFont")
default_font.configure(size=7)
text_font = font.nametofont("TkTextFont")
text_font.configure(size=7)
help_font = font.nametofont("TkFixedFont")
help_font.configure(size=7)

#Frame creation method
def createColFrame(rowIn, colIn, gridIndex):
    frame = Frame()
    frame.grid(row=rowIn,column=colIn,sticky="n")
    frame.rowconfigure(gridIndex, minsize=10, weight=1)
    return frame

def createParameterFrame(masterIn, rowIn, colIn, gridIndex):
    frame = Frame(master=masterIn,relief=GROOVE,borderwidth=3)
    frame.grid(row=rowIn,column=colIn,sticky="new")
    frame.rowconfigure(gridIndex, minsize=20)
    return frame

def createOptionLabel(masterIn, textIn, helpText, rowIn, colIn):
    label = Label(master=masterIn,text=textIn,foreground=txtcol)
    label.bind("<Motion>", lambda event: ht.helpTextTk(helpText, statusBox , event))
    label.grid(row=rowIn, column=colIn, sticky="w")
    return label

#Could have gone strongly object oriented with enums and whatnot, but KISS, right?
variables = {
"name_var" : StringVar(),
"year_var" : IntVar(),
"output_var" : StringVar(),
"cpu_var" : IntVar(),
"res_var" : StringVar(),
"res_var" : StringVar(),
"crash_var" : StringVar(),
"layers_var" : IntVar(),
"recom_var" : StringVar(),
"startemp_var" : DoubleVar(),
"flux_var" : DoubleVar(),
"orbp_var" : DoubleVar(),
"rot_var" : DoubleVar(),
"ecc_var" : DoubleVar(),
"obli_var" : DoubleVar(),
"lon_var" : DoubleVar(),
"fixed_var" : StringVar(),
"tidal_var" : StringVar(),
"lon_var" : IntVar(),
"desync_var" : DoubleVar(),
"tempcon_var" : DoubleVar(),
"gravity_var" : DoubleVar(),
"radius_var" : DoubleVar(),
"orogph_var" : DoubleVar(),
"aquap_var" : StringVar(),
"desertp_var" : StringVar(),
"vegetat_var" : StringVar(),
"vegacce_var" : IntVar(),
"nfrtgrw_var" : DoubleVar(),
"initgrw_var" : DoubleVar(),
"initstcd_var" : DoubleVar(),
"initrgh_var" : DoubleVar(),
"initslc_var" : DoubleVar(),
"initplc_var" : DoubleVar(),
"wetso_var" : StringVar(),
"soilalb_var" : DoubleVar(),
"soilalbtog_var" : StringVar(),
"soildepth_var" : DoubleVar(),
"soildepthtog_var" : StringVar(),
"capsoil_var" : DoubleVar(),
"capsoiltog_var" : StringVar(),
"soilwcp_var" : DoubleVar(),
"soilwcptog_var" : StringVar(),
"soilsat_var" : DoubleVar(),
"soilsattog_var" : StringVar(),
"snowalb_var" : DoubleVar(),
"snowalbtog_var" : StringVar(),
"mxsnow_var" : DoubleVar(),
"mxsnowtog_var" : StringVar(),
"seaice_var" : StringVar(),
"oceanalb_var" : DoubleVar(),
"oceanalbtog_var" : StringVar(),
"mldepth_var" : DoubleVar(),
"mldepthtog_var" : StringVar(),
"oceanzen_var" : StringVar(),
"imgsratogtog_var" : StringVar(),
"hghtmpimg_var" : StringVar(),
"res_var" : IntVar(),
"highelev_var" : DoubleVar(),
"lowelev_var" : DoubleVar(),
"imgdebugtog_var" : StringVar(),
"sranme_var" : StringVar(),
"lndsra_var" : StringVar(),
"tposra_var" : StringVar(),
"pressure_var" : DoubleVar(),
"pressuretog_var" : StringVar(),
"gascon_var" : DoubleVar(),
"gascontog_var" : StringVar(),
"drycoretog_var" : StringVar(),
"ozone_var" : StringVar(),
"partialptog_var" : StringVar(),
"pH2_var" : DoubleVar(),
"pHe_var" : DoubleVar(),
"pN2_var" : DoubleVar(),
"pO2_var" : DoubleVar(),
"pAr_var" : DoubleVar(),
"pNe_var" : DoubleVar(),
"pKr_var" : DoubleVar(),
"pH2O_var" : DoubleVar(),
"pCO2_var" : DoubleVar(),
"glacialtog_var" : StringVar(),
"inith_var" : DoubleVar(),
"mndph_var" : DoubleVar(),
"tmestp_var" : DoubleVar(),
"runstp_var" : IntVar(),
"snpsht_var" : IntVar(),
"nsptw_var" : IntVar(),
"phyfilt1_var" : StringVar(),
"phyfilt2_var" : StringVar(),
"stormcltog_var" : StringVar(),
"highcadtog_var" : StringVar(),
"rntbaltog_var" : StringVar(),
"runtme_var" : IntVar(),
"trshld_var" : DoubleVar(),
"bselne_var" : IntVar(),
"maxyr_var" : IntVar(),
"minyr_var" : IntVar(),
"cshibrktog_var" : StringVar(),
"cleantog_var" : StringVar(),
"allyrstog_var" : StringVar(),
"kprststog_var" : StringVar()
}

#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------

col_one_frame = createColFrame(1, 1, [2,4,6])

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------

#Model Parameter Frame
modpar_frame = createParameterFrame(col_one_frame, 1, 1, [1,2,3,4,5,6,7,8,9])

modelparam = Label(master=modpar_frame,text="Model Parameters")
modelparam.grid(row=0, column=1,columnspan=2,sticky="n")

#Project Name
project = createOptionLabel(masterIn=modpar_frame, textIn="Project Name: ", helpText="helpjctnme", rowIn=1, colIn=1)
variables["name_var"].set('Earth')
name = Entry(master=modpar_frame,width=7, textvariable=variables["name_var"])
name.grid(row=1, column=2, sticky="w")

#Start Year
year = createOptionLabel(masterIn=modpar_frame, textIn="Start Year: ", helpText="helpstrtyr", rowIn=2, colIn=1)
variables["year_var"].set(1)
year_n = Entry(master=modpar_frame,textvariable=variables["year_var"], width=7)
year_n.grid(row=2, column=2, sticky="w")

#Output Type
outputtype = createOptionLabel(masterIn=modpar_frame, textIn="Output Type: ", helpText="helpotptype", rowIn=3, colIn=1)
output_options = [".nc", ".nc", ".npy", ".npz", ".hdf5", ".he5", ".h5", ".csv", ".gz", ".txt", ".tar", ".tar.gz", ".tar.xz", ".tar.bz2"]
variables["output_var"].set(output_options[0])
outputtxt = OptionMenu(modpar_frame, variables["output_var"], *output_options)
outputtxt.config(width=6)
outputtxt.grid(row=3,column=2, sticky="w")

#CPU Count
cpu = createOptionLabel(masterIn=modpar_frame, textIn="CPU Count: ", helpText="helpcpucnt", rowIn=4, colIn=1)
variables["cpu_var"].set(4)
cpu_n = Entry(master=modpar_frame,textvariable=variables["cpu_var"], width=7)
cpu_n.grid(row=4, column=2, sticky="w")

#Precision
pres = createOptionLabel(masterIn=modpar_frame, textIn="Precision: ", helpText="helpresision", rowIn=5, colIn=1)
pres_options = ["8", "4", "8"]

variables["res_var"].set(pres_options[0])
pres_n = OptionMenu(modpar_frame, variables["res_var"], *pres_options)
pres_n.config(width=6)
pres_n.grid(row=5, column=2, sticky="w")

#Resolution
resolution = createOptionLabel(masterIn=modpar_frame, textIn="Resolution: ", helpText="helpresolution", rowIn=6, colIn=1)
res_options = ["T21", "T21", "T42", "T63", "T85", "T106", "T127", "T170"]

variables["res_var"].set(res_options[0])
res = OptionMenu(modpar_frame, variables["res_var"], *res_options)
res.config(width=6)
res.grid(row=6,column=2, sticky="w")

#Crash Tolerant
crash = resolution = createOptionLabel(masterIn=modpar_frame, textIn="Crash Tolerant: ", helpText="helpcrshtlrnt", rowIn=7, colIn=1)
variables["crash_var"].set("False")
crashtol = Checkbutton(master=modpar_frame,variable=variables["crash_var"], onvalue='True', offvalue='False')
crashtol.grid(row=7, column=2, sticky="w")

#Layers
layers = createOptionLabel(masterIn=modpar_frame, textIn="Layers: ", helpText="helplayers", rowIn=8, colIn=1)
variables["layers_var"].set(10)
layers_n = Entry(master=modpar_frame,textvariable=variables["layers_var"], width=7)
layers_n.grid(row=8, column=2, sticky="w")

#Recompile
recom = resolution = createOptionLabel(masterIn=modpar_frame, textIn="Recompile: ", helpText="helprecompile", rowIn=9, colIn=1)
variables["recom_var"].set("False")
recom_n = Checkbutton(master=modpar_frame,variable=variables["recom_var"], onvalue='True', offvalue='False')
recom_n.grid(row=9, column=2, sticky="w")

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------

#Stellar Parameter Frame
stelpar_frame = createParameterFrame(masterIn=col_one_frame, rowIn=3, colIn=1, gridIndex=[1,2])

modelparam = Label(master=stelpar_frame,text="Stellar Parameters")
modelparam.grid(row=0,column=1,columnspan=2,sticky="n")

#Star Temperature
startemp = createOptionLabel(masterIn=stelpar_frame, textIn="Star Temp. (K): ", helpText="helpstrtmp", rowIn=1, colIn=1)
variables["startemp_var"].set(5772.0)
startemp_n = Entry(master=stelpar_frame,textvariable=variables["startemp_var"], width=7)
startemp_n.grid(row=1, column=2, sticky="w")

#Stellar Flux
flux = createOptionLabel(masterIn=stelpar_frame, textIn="Stellar Flux (W/m²): ", helpText="helpstlrflx", rowIn=2, colIn=1)
variables["flux_var"].set(1367.0)
flux_n = Entry(master=stelpar_frame,textvariable=variables["flux_var"], width=7)
flux_n.grid(row=2, column=2, sticky="w")

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------

#Orbital Parameter Frame
orbitpar_frame = createParameterFrame(masterIn=col_one_frame, rowIn=5, colIn=1, gridIndex=[1,2,3,4,5,6])

orbitparam = Label(master=orbitpar_frame,text="Orbital Parameters")
orbitparam.grid(row=0,column=1,columnspan=2,sticky="n")

#Orbital Period
orbp = createOptionLabel(masterIn=orbitpar_frame, textIn="Year Length (E. Days): ", helpText="helpyrlngth", rowIn=1, colIn=1)
variables["orbp_var"].set(365.25)
orbp_n = Entry(master=orbitpar_frame,textvariable=variables["orbp_var"], width=7)
orbp_n.grid(row=1, column=2, sticky="w")

#Rotation Period
rot = createOptionLabel(masterIn=orbitpar_frame, textIn="Day Length (E. Days): ", helpText="helpdaylngth", rowIn=2, colIn=1)
variables["rot_var"].set(1.0)
rot_n = Entry(master=orbitpar_frame,textvariable=variables["rot_var"], width=7)
rot_n.grid(row=2, column=2, sticky="w")

#Eccentricity
ecc = createOptionLabel(masterIn=orbitpar_frame, textIn="Eccentricity: ", helpText="helpeccentr", rowIn=3, colIn=1)
variables["ecc_var"].set(0.016715)
ecc_n = Entry(master=orbitpar_frame,textvariable=variables["ecc_var"], width=7)
ecc_n.grid(row=3, column=2, sticky="w")

#Obliquity
obli = createOptionLabel(masterIn=orbitpar_frame, textIn="Obliquity (°): ", helpText="helpoblqty", rowIn=4, colIn=1)
variables["obli_var"].set(23.441)
obli_n = Entry(master=orbitpar_frame,textvariable=variables["obli_var"], width=7)
obli_n.grid(row=4, column=2, sticky="w")

#Longitude of Periapsis
lon = createOptionLabel(masterIn=orbitpar_frame, textIn="Long. of Periapsis (°): ", helpText="helplngpri", rowIn=5, colIn=1)
variables["lon_var"].set(102.7)
lon_n = Entry(master=orbitpar_frame,textvariable=variables["lon_var"], width=7)
lon_n.grid(row=5, column=2, sticky="w")

#Fixed Orbit
fixed = createOptionLabel(masterIn=orbitpar_frame, textIn="Fixed Orbit: ", helpText="helpfxdobt", rowIn=6, colIn=1)
variables["fixed_var"].set('True')
fixedorb = Checkbutton(master=orbitpar_frame,variable=variables["fixed_var"], onvalue='True', offvalue='False')
fixedorb.grid(row=6, column=2, sticky="w")

#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------

col_two_frame = createColFrame(1, 3, [2,4])

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------

#Rotational Parameter Frame

rotatpar_frame = createParameterFrame(col_two_frame, 1, 1, [1,2,3,4])
rotatpar_frame.columnconfigure([2], minsize=60)

rotatparam = Label(master=rotatpar_frame,text="Rotational Parameters")
rotatparam.grid(row=0,column=1,columnspan=2,sticky="n")

#Tidally Locked
tidal = createOptionLabel(masterIn=rotatpar_frame, textIn="Tidally Locked: ", helpText="helptdlkd", rowIn=1, colIn=1)
variables["tidal_var"].set('False')
tidalock = Checkbutton(master=rotatpar_frame,variable=variables["tidal_var"],command=tidaltoggle, onvalue='True', offvalue='False')
tidalock.grid(row=1, column=2, sticky="w")

#Substellar Longitude
stellon = createOptionLabel(masterIn=rotatpar_frame, textIn="Substellar Longitude (°): ", helpText="helpsbstlrlng", rowIn=2, colIn=1)
variables["lon_var"].set(180)
stellon_n = Entry(master=rotatpar_frame,textvariable=variables["lon_var"], width=7)
stellon_n.config(state='disabled')
stellon_n.grid(row=2, column=2, sticky="w")

#Desync
desync = createOptionLabel(masterIn=rotatpar_frame, textIn="Substellar Desync (°/min): ", helpText="helpsbstlrdsync", rowIn=3, colIn=1)
variables["desync_var"].set(0.0)
desync_n = Entry(master=rotatpar_frame,textvariable=variables["desync_var"], width=7)
desync_n.config(state='disabled')
desync_n.grid(row=3, column=2, sticky="w")

#Temp. Contrast
tempcon = createOptionLabel(masterIn=rotatpar_frame, textIn="Temp. Contrast (K): ", helpText="helptmpcntrst", rowIn=4, colIn=1)
variables["tempcon_var"].set(0.0)
tempcon_n = Entry(master=rotatpar_frame,textvariable=variables["tempcon_var"], width=7)
tempcon_n.config(state='disabled')
tempcon_n.grid(row=4, column=2, sticky="w")

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------

#Planetary Parameters Frame
planetpar_frame = Frame(master=col_two_frame,relief=GROOVE,borderwidth=3)
planetpar_frame.grid(row=3,column=1,sticky="new")
planetpar_frame.rowconfigure([1,2,3,4,5], minsize=20)
planetpar_frame.columnconfigure([2], minsize=100)

planetparam = Label(master=planetpar_frame,text="Planetary Parameters")
planetparam.grid(row=0,column=1,columnspan=2,sticky="n")

#Surface Gravity
gravity = createOptionLabel(masterIn=planetpar_frame, textIn="Gravity (m/s²): ", helpText="helpgrvty", rowIn=1, colIn=1)
variables["gravity_var"].set(9.80665)
gravity_n = Entry(master=planetpar_frame,textvariable=variables["gravity_var"], width=7)
gravity_n.grid(row=1, column=2, sticky="w")

#Radius
radius = createOptionLabel(masterIn=planetpar_frame, textIn="Radius (E. Radii): ", helpText="helprdus", rowIn=2, colIn=1)
variables["radius_var"].set(1.0)
radius_n = Entry(master=planetpar_frame,textvariable=variables["radius_var"], width=7)
radius_n.grid(row=2, column=2, sticky="w")

#Orography
orogph = createOptionLabel(masterIn=planetpar_frame, textIn="Orography: ", helpText="helporgrphy", rowIn=3, colIn=1)
variables["orogph_var"].set(1.0)
orogph_n = Entry(master=planetpar_frame,textvariable=variables["orogph_var"], width=7)
orogph_n.grid(row=3, column=2, sticky="w")

#Aqua Planet
aquap = createOptionLabel(masterIn=planetpar_frame, textIn="Aqua Planet: ", helpText="helpaquaplnt", rowIn=4, colIn=1)
variables["aquap_var"].set('False')
aquap_n = Checkbutton(master=planetpar_frame,variable=variables["aquap_var"],command=aquatoggle, onvalue='True', offvalue='False')
aquap_n.config(state='enabled')
aquap_n.grid(row=4, column=2, sticky="w")

#Desert Planet
desertp = createOptionLabel(masterIn=planetpar_frame, textIn="Desert Planet: ", helpText="helpdsrtplnt", rowIn=5, colIn=1)
variables["desertp_var"].set('False')
desertp_n = Checkbutton(master=planetpar_frame,variable=variables["desertp_var"],command=dsrtoggle, onvalue='True', offvalue='False')
desertp_n.config(state='enabled')
desertp_n.grid(row=5, column=2, sticky="w")

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------

#Vegetation Parameter Frame

vegpar_frame = createParameterFrame(masterIn=col_two_frame, rowIn=5, colIn=1, gridIndex=[1,2,3,4,5,6,7,8])

vegparam = Label(master=vegpar_frame,text="Vegetation Parameters")
vegparam.grid(row=0,column=1,columnspan=2,sticky="n")

#Vegetation
vegetat = createOptionLabel(masterIn=vegpar_frame, textIn="Vegetation: ", helpText="helpvgtn", rowIn=1, colIn=1)
vegetat_options = ["None", "None", "Proscribed", "Dynamic"]

variables["vegetat_var"].set(vegetat_options[0])
vegetat_n = OptionMenu(vegpar_frame, variables["vegetat_var"], *vegetat_options, command=vegtoggle)
vegetat_n.config(width=7)
vegetat_n.grid(row=1, column=2, sticky="w")

#Veg. Acceleration
vegacce = createOptionLabel(masterIn=vegpar_frame, textIn="Veg. Acceleration: ", helpText="helpvgaclrtn", rowIn=2, colIn=1)
variables["vegacce_var"].set(1)
vegacce_n = Entry(master=vegpar_frame,textvariable=variables["vegacce_var"], width=7)
vegacce_n.config(state='disabled')
vegacce_n.grid(row=2, column=2, sticky="w")

#Biomass Growth
nfrtgrw = createOptionLabel(masterIn=vegpar_frame, textIn="Biomass Growth: ", helpText="helpbiomsgrwth", rowIn=3, colIn=1)
variables["nfrtgrw_var"].set(1.0)
nfrtgrw_n = Entry(master=vegpar_frame,textvariable=variables["nfrtgrw_var"], width=7)
nfrtgrw_n.config(state='disabled')
nfrtgrw_n.grid(row=3, column=2, sticky="w")

#Initial Growth
initgrw = createOptionLabel(masterIn=vegpar_frame, textIn="Initial Growth: ", helpText="helpintlgrth", rowIn=4, colIn=1)
variables["initgrw_var"].set(0.5)
initgrw_n = Entry(master=vegpar_frame,textvariable=variables["initgrw_var"], width=7)
initgrw_n.config(state='disabled')
initgrw_n.grid(row=4, column=2, sticky="w")

#Initial Stomatal Conductance
initstcd = createOptionLabel(masterIn=vegpar_frame, textIn="Stomatal Conductance: ", helpText="helpstmtlcndtnce", rowIn=5, colIn=1)
variables["initstcd_var"].set(1.0)
initstcd_n = Entry(master=vegpar_frame,textvariable=variables["initstcd_var"], width=7)
initstcd_n.config(state='disabled')
initstcd_n.grid(row=5, column=2, sticky="w")

#Initial Vegetative Surface Roughness
initrgh = createOptionLabel(masterIn=vegpar_frame, textIn="Vegetation Roughness: ", helpText="helpvgtnrghns", rowIn=6, colIn=1)
variables["initrgh_var"].set(2.0)
initrgh_n = Entry(master=vegpar_frame,textvariable=variables["initrgh_var"], width=7)
initrgh_n.config(state='disabled')
initrgh_n.grid(row=6, column=2, sticky="w")

#Initial Soil Carbon Content
initslc = createOptionLabel(masterIn=vegpar_frame, textIn="Soil Carbon Content: ", helpText="helpslcbncntnt", rowIn=7, colIn=1)
variables["initslc_var"].set(0.0)
initslc_n = Entry(master=vegpar_frame,textvariable=variables["initslc_var"], width=7)
initslc_n.config(state='disabled')
initslc_n.grid(row=7, column=2, sticky="w")

#Initial Vegetative Carbon Content
initplc = createOptionLabel(masterIn=vegpar_frame, textIn="Plant Carbon Content: ", helpText="helplntcbncntnt", rowIn=8, colIn=1)
variables["initplc_var"].set(0.0)
initplc_n = Entry(master=vegpar_frame,textvariable=variables["initplc_var"], width=7)
initplc_n.config(state='disabled')
initplc_n.grid(row=8, column=2, sticky="w")

#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------

col_three_frame = createColFrame(1, 5, [2])

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------

#Surface Parameter Frame
surfpar_frame = createParameterFrame(masterIn=col_three_frame, rowIn=1, colIn=1, gridIndex=[1,2,3,4,5,6,7,8,9,10,11,12])
surfparam = Label(master=surfpar_frame,text="Surface Parameters")
surfparam.grid(row=0,column=1,columnspan=3,sticky="n")

#Wet Soil
wetso = createOptionLabel(masterIn=surfpar_frame, textIn="Wet Soil: ", helpText="helpwtsl", rowIn=1, colIn=1)
variables["wetso_var"].set("False")
wetsoil = Checkbutton(master=surfpar_frame,variable=variables["wetso_var"], onvalue='True', offvalue='False')
wetsoil.grid(row=1, column=2, sticky="w")

#Soil Albedo
soilalb = createOptionLabel(masterIn=surfpar_frame, textIn="Soil Albedo: ", helpText="helpslalbdo", rowIn=2, colIn=1)
variables["soilalb_var"].set(0.0)
soilalb_n = Entry(master=surfpar_frame,textvariable=variables["soilalb_var"], width=7)
soilalb_n.config(state='disabled')
soilalb_n.grid(row=2, column=2, sticky="w")
##Soil Albedo Toggle
variables["soilalbtog_var"].set('False')
soilalbtog_n = Checkbutton(master=surfpar_frame,variable=variables["soilalbtog_var"],command=soilalbtoggle, onvalue='True', offvalue='False')
soilalbtog_n.grid(row=2, column=3, sticky="w")

#Soil Depth
soildepth = createOptionLabel(masterIn=surfpar_frame, textIn="Soil Depth (m): ", helpText="helpsldpth", rowIn=3, colIn=1)
variables["soildepth_var"].set(12.4)
soildepth_n = Entry(master=surfpar_frame,textvariable=variables["soildepth_var"], width=7)
soildepth_n.config(state='disabled')
soildepth_n.grid(row=3, column=2, sticky="w")
##Soil Depth Toggle
variables["soildepthtog_var"].set('False')
soildepthtog_n = Checkbutton(master=surfpar_frame,variable=variables["soildepthtog_var"],command=soildepthtoggle, onvalue='True', offvalue='False')
soildepthtog_n.grid(row=3, column=3, sticky="w")

#Soil Heat Capacity
capsoil = createOptionLabel(masterIn=surfpar_frame, textIn="Soil Heat Capacity: ", helpText="helpslhtcpsty", rowIn=4, colIn=1)
variables["capsoil_var"].set(2.4)
capsoil_n = Entry(master=surfpar_frame,textvariable=variables["capsoil_var"], width=7)
capsoil_n.config(state='disabled')
capsoil_n.grid(row=4, column=2, sticky="w")
##Soil Heact Capacity Toggle
variables["capsoiltog_var"].set('False')
capsoiltog_n = Checkbutton(master=surfpar_frame,variable=variables["capsoiltog_var"],command=capsoiltoggle, onvalue='True', offvalue='False')
capsoiltog_n.grid(row=4, column=3, sticky="w")

#Soil Water Capacity
soilwcp = createOptionLabel(masterIn=surfpar_frame, textIn="Soil Water Capacity: ", helpText="helpslwtrcpsty", rowIn=5, colIn=1)
variables["soilwcp_var"].set(0.5)
soilwcp_n = Entry(master=surfpar_frame,textvariable=variables["soilwcp_var"], width=7)
soilwcp_n.config(state='disabled')
soilwcp_n.grid(row=5, column=2, sticky="w")
##Soil Water Capacity Toggle
variables["soilwcptog_var"].set('False')
soilwcptog_n = Checkbutton(master=surfpar_frame,variable=variables["soilwcptog_var"],command=soilwcptoggle, onvalue='True', offvalue='False')
soilwcptog_n.grid(row=5, column=3, sticky="w")

#Soil Saturation
soilsat = createOptionLabel(masterIn=surfpar_frame, textIn="Soil Saturation: ", helpText="helpslstrtn", rowIn=6, colIn=1)
variables["soilsat_var"].set(0.0)
soilsat_n = Entry(master=surfpar_frame,textvariable=variables["soilsat_var"], width=7)
soilsat_n.config(state='disabled')
soilsat_n.grid(row=6, column=2, sticky="w")
##Soil Water Capacity Toggle
variables["soilsattog_var"].set('False')
soilsattog_n = Checkbutton(master=surfpar_frame,variable=variables["soilsattog_var"],command=soilsattoggle, onvalue='True', offvalue='False')
soilsattog_n.grid(row=6, column=3, sticky="w")

#Snow Albedo
snowalb = createOptionLabel(masterIn=surfpar_frame, textIn="Snow Albedo: ", helpText="helpsnwalb", rowIn=7, colIn=1)
variables["snowalb_var"].set(0.0)
snowalb_n = Entry(master=surfpar_frame,textvariable=variables["snowalb_var"], width=7)
snowalb_n.config(state='disabled')
snowalb_n.grid(row=7, column=2, sticky="w")
##Snow Albedo Toggle
variables["snowalbtog_var"].set('False')
snowalbtog_n = Checkbutton(master=surfpar_frame,variable=variables["snowalbtog_var"],command=snowalbtoggle, onvalue='True', offvalue='False')
snowalbtog_n.grid(row=7, column=3, sticky="w")

#Max Snow
mxsnow = createOptionLabel(masterIn=surfpar_frame, textIn="Max Snow (m): ", helpText="helpmxsnw", rowIn=8, colIn=1)
variables["mxsnow_var"].set(5.0)
mxsnow_n = Entry(master=surfpar_frame,textvariable=variables["mxsnow_var"], width=7)
mxsnow_n.config(state='disabled')
mxsnow_n.grid(row=8, column=2, sticky="w")
##Snow Albedo Toggle
variables["mxsnowtog_var"].set('False')
mxsnowtog_n = Checkbutton(master=surfpar_frame,variable=variables["mxsnowtog_var"],command=mxsnowtoggle, onvalue='True', offvalue='False')
mxsnowtog_n.grid(row=8, column=3, sticky="w")

#Sea Ice
seaice = createOptionLabel(masterIn=surfpar_frame, textIn="Sea Ice: ", helpText="helpseaice", rowIn=9, colIn=1)
variables["seaice_var"].set('True')
seaice_n = Checkbutton(master=surfpar_frame,variable=variables["seaice_var"], onvalue='True', offvalue='False')
seaice_n.grid(row=9, column=2, sticky="w")

#Ocean Albedo
oceanalb = createOptionLabel(masterIn=surfpar_frame, textIn="Ocean Albedo: ", helpText="helpocnalb", rowIn=10, colIn=1)
variables["oceanalb_var"].set(0.0)
oceanalb_n = Entry(master=surfpar_frame,textvariable=variables["snowalb_var"], width=7)
oceanalb_n.config(state='disabled')
oceanalb_n.grid(row=10, column=2, sticky="w")
##Snow Albedo Toggle
variables["oceanalbtog_var"].set('False')
oceanalbtog_n = Checkbutton(master=surfpar_frame,variable=variables["oceanalbtog_var"],command=oceanalbtoggle, onvalue='True', offvalue='False')
oceanalbtog_n.grid(row=10, column=3, sticky="w")

#Mixed Ocean Depth
mldepth = createOptionLabel(masterIn=surfpar_frame, textIn="Mixed Layer Depth (m): ", helpText="helpmxdlyrdpth", rowIn=11, colIn=1)
variables["mldepth_var"].set(50.0)
mldepth_n = Entry(master=surfpar_frame,textvariable=variables["mldepth_var"], width=7)
mldepth_n.config(state='disabled')
mldepth_n.grid(row=11, column=2, sticky="w")
##Mixed Ocean Depth Toggle
variables["mldepthtog_var"].set('False')
mldepthtog_n = Checkbutton(master=surfpar_frame,variable=variables["mldepthtog_var"],command=mldepthtoggle, onvalue='True', offvalue='False')
mldepthtog_n.grid(row=11, column=3, sticky="w")

#Ocean Zenith
oceanzen = createOptionLabel(masterIn=surfpar_frame, textIn="Ocean Zenith: ", helpText="helpocnznth", rowIn=12, colIn=1)
oceanzen_options = ["ECHAM-3", "Lambertian", "uniform", "ECHAM-3", "plasim", "default", "ECHAM-6"]

variables["oceanzen_var"].set(oceanzen_options[0])
oceanzen_n = OptionMenu(surfpar_frame, variables["oceanzen_var"], *oceanzen_options)
oceanzen_n.config(width=7)
oceanzen_n.grid(row=12,column=2, sticky="w")

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------

#Geographic Parameter Frame
geopar_frame = createParameterFrame(masterIn=col_three_frame, rowIn=3, colIn=1, gridIndex=[1,2,3,4,5,6,7,8,9])

geoparam = Label(master=geopar_frame,text="Geographic Parameters")
geoparam.grid(row=0,column=1,columnspan=3,sticky="n")

#Image/SRA Toggle
imgsratog = createOptionLabel(masterIn=geopar_frame, textIn="Use SRA instead of image: ", helpText="helpimgsratog", rowIn=1, colIn=1)
variables["imgsratogtog_var"].set('image')
imgsratogtog_n = Checkbutton(master=geopar_frame,variable=variables["imgsratogtog_var"],command=imgsratoggle, onvalue='sra', offvalue='image')
imgsratogtog_n.grid(row=1, column=2, sticky="w")

#Height Map Image
hghtmpimg = createOptionLabel(masterIn=geopar_frame, textIn="Height Map Image: ", helpText="helphghtmpimg", rowIn=2, colIn=1)
variables["hghtmpimg_var"].set('')
hghtmpimg_n = Entry(master=geopar_frame,textvariable=variables["hghtmpimg_var"], width=7)
hghtmpimg_n.config(state='enabled')
hghtmpimg_n.grid(row=2, column=2, sticky="w")
hghtmpimg_b = Button(master=geopar_frame,text="Open",command=hghtimgget, width=7)
hghtmpimg_b.config(state='enabled')
hghtmpimg_b.grid(row=2, column=3, sticky="w")

#Water Threshold
waterhres = createOptionLabel(masterIn=geopar_frame, textIn="Water Threshold: ", helpText="helpwtrthrshld", rowIn=3, colIn=1)
variables["res_var"].set(0)
waterhres_n = Entry(master=geopar_frame,textvariable=variables["res_var"], width=7)
waterhres_n.config(state='enabled')
waterhres_n.grid(row=3, column=2, sticky="w")

#Highest Elevation
highelev = createOptionLabel(masterIn=geopar_frame, textIn="Highest Elevation (m): ", helpText="helphghstelvtn", rowIn=4, colIn=1)
variables["highelev_var"].set(8849.0)
highelev_n = Entry(master=geopar_frame,textvariable=variables["highelev_var"], width=7)
highelev_n.config(state='enabled')
highelev_n.grid(row=4, column=2, sticky="w")

#Lowest Elevation
lowelev = createOptionLabel(masterIn=geopar_frame, textIn="Lowest Elevation (m): ", helpText="helplwstelvtn", rowIn=5, colIn=1)
variables["lowelev_var"].set(-11034.0)
lowelev_n = Entry(master=geopar_frame,textvariable=variables["lowelev_var"], width=7)
lowelev_n.config(state='disabled')
lowelev_n.grid(row=5, column=2, sticky="w")

#Image Debug
imgdebug = createOptionLabel(masterIn=geopar_frame, textIn="Image Debug: ", helpText="helpimgdbg", rowIn=6, colIn=1)
variables["imgdebugtog_var"].set('False')
imgdebugtog_n = Checkbutton(master=geopar_frame,variable=variables["imgdebugtog_var"], onvalue='True', offvalue='False')
imgdebugtog_n.config(state='enabled')
imgdebugtog_n.grid(row=6, column=2, sticky="w")

#SRA Name
sranme = createOptionLabel(masterIn=geopar_frame, textIn="SRA Name: ", helpText="helpsranme", rowIn=7, colIn=1)
variables["sranme_var"].set("earth")
sranme_n = Entry(master=geopar_frame,textvariable=variables["sranme_var"], width=7)
sranme_n.config(state='enabled')
sranme_n.grid(row=7, column=2, sticky="w")

#Land SRA
lndsra = createOptionLabel(masterIn=geopar_frame, textIn="Land SRA: ", helpText="helplndsra", rowIn=8, colIn=1)
variables["lndsra_var"].set('')
lndsra_n = Entry(master=geopar_frame,textvariable=variables["lndsra_var"], width=7)
lndsra_n.config(state='disabled')
lndsra_n.grid(row=8, column=2, sticky="w")
lndsra_b = Button(master=geopar_frame,text="Open",command=landsraget, width=7)
lndsra_b.config(state='disabled')
lndsra_b.grid(row=8, column=3, sticky="w")

#Topo SRA
tposra = createOptionLabel(masterIn=geopar_frame, textIn="Topographic SRA: ", helpText="helptposra", rowIn=9, colIn=1)
variables["tposra_var"].set('')
tposra_n = Entry(master=geopar_frame,textvariable=variables["tposra_var"], width=7)
tposra_n.config(state='disabled')
tposra_n.grid(row=9, column=2, sticky="w")
tposra_b = Button(master=geopar_frame,text="Open",command=toposraget, width=7)
tposra_b.config(state='disabled')
tposra_b.grid(row=9, column=3, sticky="w")

#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------

col_four_frame = Frame()
col_four_frame.grid(row=1,column=7,sticky="n")
col_four_frame.rowconfigure([2,4], minsize=10, weight=1)

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------

#Atmospheric Parameter Frame
atmpar_frame = createParameterFrame(masterIn=col_four_frame, rowIn=1, colIn=1, gridIndex=[1,2,3,4,5,6,7,8,9,10,11,12,13,14])

atmparam = Label(master=atmpar_frame,text="Atmospheric Parameters")
atmparam.grid(row=0,column=1,columnspan=3,sticky="n")

#Pressure
pressure = createOptionLabel(masterIn=atmpar_frame, textIn="Pressure (bar): ", helpText="helprsure", rowIn=1, colIn=1)
variables["pressure_var"].set(1.0)
pressure_n = Entry(master=atmpar_frame,textvariable=variables["pressure_var"], width=7)
pressure_n.config(state='disabled')
pressure_n.grid(row=1, column=2, sticky="w")
##Pressure Toggle
variables["pressuretog_var"].set('False')
pressuretog_n = Checkbutton(master=atmpar_frame,variable=variables["pressuretog_var"],command=pressuretoggle, onvalue='True', offvalue='False')
pressuretog_n.grid(row=1, column=3, sticky="w")

#Gas Constant
gascon = createOptionLabel(masterIn=atmpar_frame, textIn="Gas Constant: ", helpText="helpgscnstnt", rowIn=2, colIn=1)
variables["gascon_var"].set(287.0)
gascon_n = Entry(master=atmpar_frame,textvariable=variables["gascon_var"], width=7)
gascon_n.config(state='disabled')
gascon_n.grid(row=2, column=2, sticky="w")
##Gas Constant Toggle
variables["gascontog_var"].set('False')
gascontog_n = Checkbutton(master=atmpar_frame,variable=variables["gascontog_var"],command=gascontoggle, onvalue='True', offvalue='False')
gascontog_n.grid(row=2, column=3, sticky="w")

#Dry Core
drycore = createOptionLabel(masterIn=atmpar_frame, textIn="Dry Core: ", helpText="helpdrycre", rowIn=3, colIn=1)
variables["drycoretog_var"].set('False')
drycoretog_n = Checkbutton(master=atmpar_frame,variable=variables["drycoretog_var"], onvalue='True', offvalue='False')
drycoretog_n.grid(row=3, column=2, sticky="w")

#Ozone
ozone = createOptionLabel(masterIn=atmpar_frame, textIn="Ozone: ", helpText="helpozne", rowIn=4, colIn=1)
variables["ozone_var"].set('False')
ozone_n = Checkbutton(master=atmpar_frame,variable=variables["ozone_var"], onvalue='True', offvalue='False')
ozone_n.grid(row=4, column=2, sticky="w")

#Partial Pressure
partialp = createOptionLabel(masterIn=atmpar_frame, textIn="Gas Pressure (bar): ", helpText="helpgsprsurs", rowIn=5, colIn=1)
variables["partialptog_var"].set('False')
partialptog_n = Checkbutton(master=atmpar_frame,variable=variables["partialptog_var"],command=ptoggle, onvalue='True', offvalue='False')
partialptog_n.grid(row=5, column=2, sticky="w")

#pH2
pH2 = Label(master=atmpar_frame,text="H2: ")
pH2.grid(row=6, column=1, sticky="w")
variables["pH2_var"].set(0.0)
pH2_n = Entry(master=atmpar_frame,textvariable=variables["pH2_var"], width=7)
pH2_n.config(state='disabled')
pH2_n.grid(row=6, column=2, sticky="w")

#pHe
pHe = Label(master=atmpar_frame,text="He: ")
pHe.grid(row=7, column=1, sticky="w")
variables["pHe_var"].set(0.0)
pHe_n = Entry(master=atmpar_frame,textvariable=variables["pHe_var"], width=7)
pHe_n.config(state='disabled')
pHe_n.grid(row=7, column=2, sticky="w")

#pN2
pN2 = Label(master=atmpar_frame,text="N2: ")
pN2.grid(row=8, column=1, sticky="w")
variables["pN2_var"].set(0.7809)
pN2_n = Entry(master=atmpar_frame,textvariable=variables["pN2_var"], width=7)
pN2_n.config(state='disabled')
pN2_n.grid(row=8, column=2, sticky="w")

#pO2
pO2 = Label(master=atmpar_frame,text="O2: ")
pO2.grid(row=9, column=1, sticky="w")
variables["pO2_var"].set(0.2095)
pO2_n = Entry(master=atmpar_frame,textvariable=variables["pO2_var"], width=7)
pO2_n.config(state='disabled')
pO2_n.grid(row=9, column=2, sticky="w")

#pAr
pAr = Label(master=atmpar_frame,text="Ar: ")
pAr.grid(row=10, column=1, sticky="w")
variables["pAr_var"].set(0.0093)
pAr_n = Entry(master=atmpar_frame,textvariable=variables["pAr_var"], width=7)
pAr_n.config(state='disabled')
pAr_n.grid(row=10, column=2, sticky="w")

#pNe
pNe = Label(master=atmpar_frame,text="Ne: ")
pNe.grid(row=11, column=1, sticky="w")
variables["pNe_var"].set(0.0)
pNe_n = Entry(master=atmpar_frame,textvariable=variables["pNe_var"], width=7)
pNe_n.config(state='disabled')
pNe_n.grid(row=11, column=2, sticky="w")

#pKr
pKr = Label(master=atmpar_frame,text="Kr: ")
pKr.grid(row=12, column=1, sticky="w")
variables["pKr_var"].set(0.0)
pKr_n = Entry(master=atmpar_frame,textvariable=variables["pKr_var"], width=7)
pKr_n.config(state='disabled')
pKr_n.grid(row=12, column=2, sticky="w")

#pH2O
pH2O = Label(master=atmpar_frame,text="H2O: ")
pH2O.grid(row=13, column=1, sticky="w")
variables["pH2O_var"].set(0.0)
pH2O_n = Entry(master=atmpar_frame,textvariable=variables["pH2O_var"], width=7)
pH2O_n.config(state='disabled')
pH2O_n.grid(row=13, column=2, sticky="w")

#pCO2
pCO2 = Label(master=atmpar_frame,text="CO2: ")
pCO2.grid(row=14, column=1, sticky="w")
variables["pCO2_var"].set(0.0003)
pCO2_n = Entry(master=atmpar_frame,textvariable=variables["pCO2_var"], width=7)
pCO2_n.config(state='disabled')
pCO2_n.grid(row=14, column=2, sticky="w")

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------

#Glacial Parameter Frame
glacpar_frame = createParameterFrame(masterIn=col_four_frame, rowIn=3, colIn=1, gridIndex=[1,2,3])
glacpar_frame.columnconfigure([2], minsize=80)

glacparam = Label(master=glacpar_frame,text="Glacial Parameters")
glacparam.grid(row=0,column=1,columnspan=3, sticky="n")

#Glacier Toggle
glacial = createOptionLabel(masterIn=glacpar_frame, textIn="Glaciers: ", helpText="helpglcrs", rowIn=1, colIn=1)
variables["glacialtog_var"].set('False')
glacialtog_n = Checkbutton(master=glacpar_frame,variable=variables["glacialtog_var"],command=gtoggle, onvalue='True', offvalue='False')
glacialtog_n.grid(row=1, column=2, sticky="w")

#Initial Height
inith = createOptionLabel(masterIn=glacpar_frame, textIn="Height (m): ", helpText="helpgrhght", rowIn=2, colIn=1)
variables["inith_var"].set(0.0)
inith_n = Entry(master=glacpar_frame,textvariable=variables["inith_var"],width=7)
inith_n.config(state='disabled')
inith_n.grid(row=2, column=2, sticky="w")

#Minimum Snow Depth
mndph = createOptionLabel(masterIn=glacpar_frame, textIn="Threshold (m): ", helpText="helpgrthrshld", rowIn=3, colIn=1)
variables["mndph_var"].set(2.0)
mndph_n = Entry(master=glacpar_frame,textvariable=variables["mndph_var"],width=7)
mndph_n.config(state='disabled')
mndph_n.grid(row=3, column=2, sticky="w")

#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------

col_five_frame = Frame()
col_five_frame.grid(row=1,column=9,sticky="new")
col_five_frame.rowconfigure([1,2], minsize=10, weight=1)

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------

#Model Dynamic Parameters
mdldynpar_frame = Frame(master=col_five_frame,relief=GROOVE,borderwidth=3)
mdldynpar_frame.grid(row=1,column=1,sticky="new")
mdldynpar_frame.rowconfigure([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], minsize=20)

mdldynparam = Label(master=mdldynpar_frame,text="Model Dynamic Parameters")
mdldynparam.grid(row=0,column=1,columnspan=2,sticky="n")

#Timestep
tmestp = createOptionLabel(masterIn=mdldynpar_frame, textIn="Timestep (min): ", helpText="helptimestep", rowIn=1, colIn=1)
variables["tmestp_var"].set(45.0)
tmestp_n = Entry(master=mdldynpar_frame,textvariable=variables["tmestp_var"], width=7)
tmestp_n.grid(row=1, column=2, sticky="w")

#Runsteps
runstp = createOptionLabel(masterIn=mdldynpar_frame, textIn="Runsteps: ", helpText="helprunsteps", rowIn=2, colIn=1)
variables["runstp_var"].set(11520)
runstp_n = Entry(master=mdldynpar_frame,textvariable=variables["runstp_var"], width=7)
runstp_n.grid(row=2, column=2, sticky="w")

#Snapshots
snpsht = createOptionLabel(masterIn=mdldynpar_frame, textIn="Snapshots: ", helpText="helpsnapshots", rowIn=3, colIn=1)
variables["snpsht_var"].set(0)
snpsht_n = Entry(master=mdldynpar_frame,textvariable=variables["snpsht_var"], width=7)
snpsht_n.grid(row=3, column=2, sticky="w")

#NSTPW
nsptw = createOptionLabel(masterIn=mdldynpar_frame, textIn="NSTPW: ", helpText="helpnstpw", rowIn=4, colIn=1)
variables["nsptw_var"].set(160)
nsptw_n = Entry(master=mdldynpar_frame,textvariable=variables["nsptw_var"], width=7)
nsptw_n.grid(row=4, column=2, sticky="w")

#Physics Filter 1
phyfilt1 = createOptionLabel(masterIn=mdldynpar_frame, textIn="Physics Filter: ", helpText="helphysfltr", rowIn=5, colIn=1)
phyfilt1_options = ["None", "None", "Cesaro", "Exp", "Lh"]

variables["phyfilt1_var"].set(oceanzen_options[0])
phyfilt1_n = OptionMenu(mdldynpar_frame, variables["phyfilt1_var"], *phyfilt1_options)
phyfilt1_n.config(width=7)
phyfilt1_n.grid(row=5,column=2, sticky="w")

#Physics Filter 2
phyfilt2 = createOptionLabel(masterIn=mdldynpar_frame, textIn="Filter Application: ", helpText="helpfltrapp", rowIn=6, colIn=1)
phyfilt2_options = ["None", "None", "GP", "SP", "GP + SP"]

variables["phyfilt2_var"].set(oceanzen_options[0])
phyfilt2_n = OptionMenu(mdldynpar_frame, variables["phyfilt2_var"], *phyfilt2_options)
phyfilt2_n.config(width=7)
phyfilt2_n.grid(row=6,column=2, sticky="w")

#Storm Climatology
stormcl = createOptionLabel(masterIn=mdldynpar_frame, textIn="Storm Climatology: ", helpText="helpstmclmtlgy", rowIn=7, colIn=1)
variables["stormcltog_var"].set('False')
stormcltog_n = Checkbutton(master=mdldynpar_frame,variable=variables["stormcltog_var"],command=stmtoggle, onvalue='True', offvalue='False')
stormcltog_n.grid(row=7, column=2, sticky="w")

#High Cadence
highcad = createOptionLabel(masterIn=mdldynpar_frame, textIn="High Cadence: ", helpText="helphghcdnce", rowIn=8, colIn=1)
variables["highcadtog_var"].set('False')
highcadtog_n = Checkbutton(master=mdldynpar_frame,variable=variables["highcadtog_var"], onvalue='True', offvalue='False')
highcadtog_n.config(state='disabled')
highcadtog_n.grid(row=8, column=2, sticky="w")

#Run To Balance
rntbal = createOptionLabel(masterIn=mdldynpar_frame, textIn="Run To Balance: ", helpText="helprntbal", rowIn=9, colIn=1)
variables["rntbaltog_var"].set('False')
rntbaltog_n = Checkbutton(master=mdldynpar_frame,variable=variables["rntbaltog_var"],command=baltoggle, onvalue='True', offvalue='False')
rntbaltog_n.grid(row=9, column=2, sticky="w")

#Run Time
runtme = createOptionLabel(masterIn=mdldynpar_frame, textIn="Run Time (years): ", helpText="helprntme", rowIn=10, colIn=1)
variables["runtme_var"].set(100)
runtme_n = Entry(master=mdldynpar_frame,textvariable=variables["runtme_var"], width=7)
runtme_n.grid(row=10, column=2, sticky="w")

#Threshold
trshld = createOptionLabel(masterIn=mdldynpar_frame, textIn="Threshold: ", helpText="helpthrshld", rowIn=11, colIn=1)
variables["trshld_var"].set(0.0005)
trshld_n = Entry(master=mdldynpar_frame,textvariable=variables["trshld_var"], width=7)
trshld_n.config(state='disabled')
trshld_n.grid(row=11, column=2, sticky="w")

#Baseline
bselne = createOptionLabel(masterIn=mdldynpar_frame, textIn="Baseline (years): ", helpText="helpbslne", rowIn=12, colIn=1)
variables["bselne_var"].set(10)
bselne_n = Entry(master=mdldynpar_frame,textvariable=variables["bselne_var"], width=7)
bselne_n.config(state='disabled')
bselne_n.grid(row=12, column=2, sticky="w")

#Max Years
maxyr = createOptionLabel(masterIn=mdldynpar_frame, textIn="Max. Year (years): ", helpText="helpmxyr", rowIn=13, colIn=1)
variables["maxyr_var"].set(100)
maxyr_n = Entry(master=mdldynpar_frame,textvariable=variables["maxyr_var"], width=7)
maxyr_n.config(state='disabled')
maxyr_n.grid(row=13, column=2, sticky="w")

#Min Years
minyr = createOptionLabel(masterIn=mdldynpar_frame, textIn="Min. Year (years): ", helpText="helpmnyr", rowIn=14, colIn=1)
variables["minyr_var"].set(10)
minyr_n = Entry(master=mdldynpar_frame,textvariable=variables["minyr_var"], width=7)
minyr_n.config(state='disabled')
minyr_n.grid(row=14, column=2, sticky="w")

#Crash If Broken
cshibrk = createOptionLabel(masterIn=mdldynpar_frame, textIn="Crash if Broken: ", helpText="helpcrshibrkn", rowIn=15, colIn=1)
variables["cshibrktog_var"].set('False')
cshibrktog_n = Checkbutton(master=mdldynpar_frame,variable=variables["cshibrktog_var"], onvalue='True', offvalue='False')
cshibrktog_n.grid(row=15, column=2, sticky="w")

#Clean
clean = createOptionLabel(masterIn=mdldynpar_frame, textIn="Clean: ", helpText="helpcln", rowIn=16, colIn=1)
variables["cleantog_var"].set('False')
cleantog_n = Checkbutton(master=mdldynpar_frame,variable=variables["cleantog_var"], onvalue='True', offvalue='False')
cleantog_n.grid(row=16, column=2, sticky="w")

#All Years
allyrs = createOptionLabel(masterIn=mdldynpar_frame, textIn="All Years: ", helpText="helpalrstrts", rowIn=17, colIn=1)
variables["allyrstog_var"].set('False')
allyrstog_n = Checkbutton(master=mdldynpar_frame,variable=variables["allyrstog_var"], onvalue='True', offvalue='False')
allyrstog_n.grid(row=17, column=2, sticky="w")

#Keep Restarts
kprsts = createOptionLabel(masterIn=mdldynpar_frame, textIn="Keep Restarts: ", helpText="helpkprstrts", rowIn=18, colIn=1)
variables["kprststog_var"].set('False')
kprststog_n = Checkbutton(master=mdldynpar_frame,variable=variables["kprststog_var"], onvalue='True', offvalue='False')
kprststog_n.grid(row=18, column=2, sticky="w")

#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------

#Check

#cant figure out how to fit multiple methods into a single lamda
def printCompat():
    ht.printToText(statusBox, system_check(variables))
    ht.printToTerminal(system_check(variables))

compat = Label(text="Compatability")
compat.grid(row=2, column=7, sticky="s")
sys_check = Button(text="Compatability Check", command=printCompat)
sys_check.grid(row=3, column=7, sticky="n")

#Save
output = Label(text="Output")
output.grid(row=2, column=9, sticky="s")
save = Button(text="Save", command=lambda: save_file(variables))
save.grid(row=3, column=9, sticky="n")

#Status
statusContainer = LabelFrame(relief=GROOVE, borderwidth=3, text="Status")
statusContainer.grid(padx=10, pady=10, row=4, column=1, rowspan=3, columnspan=9, sticky="new")
statusContainer.rowconfigure(0, weight=1)
statusContainer.columnconfigure(0, weight=1)

statusBox = Text(master=statusContainer, height=8)
statusBox.configure(font=help_font)
statusBox.grid(padx=3, pady=3, row=0, column=0,sticky="nsew")

window.mainloop()