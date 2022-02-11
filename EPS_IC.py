from tkinter import *
from tkinter import font
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import helptext as ht
import IC_modelMethods as model


#Toggle Functions
def simpleToggle(toggle, input):
    if toggle.get() == "False":
        input.config(state='disabled')
    elif toggle.get()== "True":
        input.config(state='enabled')

def tidallyLockedtoggle():
    if variables["tidallyLocked_var"].get() == 'True':
        substellarLon.entry.config(state='enabled')
        substellarDesync.entry.config(state='enabled')
        tempContrast.entry.config(state='enabled')
    else:
        substellarLon.entry.config(state='disabled')
        substellarDesync.entry.config(state='disabled')
        tempContrast.entry.config(state='disabled')

def aquatoggle():
    if variables["aquaPlanet_var"].get() == "True":
        desertPlanet.entry.config(state='disabled')
        useSRA.entry.config(state='disabled')
        heightMapImg.entry.config(state='disabled')
        heightMapImg_b.config(state='disabled')
        waterThreshold.entry.config(state='disabled')
        maxElevation.entry.config(state='disabled')
        minElevation.entry.config(state='disabled')
        imgDebug.entry.config(state='disabled')
        sraName.entry.config(state='disabled')
        landSRA.entry.config(state='disabled')
        landSRA_b.config(state='disabled')
        topoSRA.entry.config(state='disabled')
        topoSRA_b.config(state='disabled')

    elif variables["aquaPlanet_var"].get() == "False":
        desertPlanet.entry.config(state='enabled')
        useSRA.entry.config(state='enabled')

        if variables["useSRAtog_var"].get() == "False":
            heightMapImg.entry.config(state='enabled')
            heightMapImg_b.config(state='enabled')
            waterThreshold.entry.config(state='enabled')
            maxElevation.entry.config(state='enabled')
            imgDebug.entry.config(state='enabled')
            sraName.entry.config(state='enabled')
            landSRA.entry.config(state='disabled')
            landSRA_b.config(state='disabled')
            topoSRA.entry.config(state='disabled')
            topoSRA_b.config(state='disabled')
        elif variables["useSRAtog_var"].get() == "True":
            heightMapImg.entry.config(state='disabled')
            heightMapImg_b.config(state='disabled')
            waterThreshold.entry.config(state='disabled')
            maxElevation.entry.config(state='disabled')
            imgDebug.entry.config(state='disabled')
            sraName.entry.config(state='disabled')
            landSRA.entry.config(state='enabled')
            landSRA_b.config(state='enabled')
            topoSRA.entry.config(state='enabled')
            topoSRA_b.config(state='enabled')

def dsrtoggle():
    if variables["desertPlanet_var"].get() == "True":
        aquaPlanet.entry.config(state='disabled')
        #variables["aquaPlanettog_var"] = "False" #looks like toggling the aquatog triggers the event just like if it had been done by user
        
        print(variables["useSRAtog_var"].get())
        if variables["useSRAtog_var"].get() == "image":
            minElevation.entry.config(state='enabled')
    elif variables["desertPlanet_var"].get() == "False":
        aquaPlanet.entry.config(state='enabled')
        #variables["aquaPlanettog_var"] = "True"
        minElevation.entry.config(state='disabled')
        
def soilAlbedotoggle():
    simpleToggle(variables["soilAlbedotog_var"], soilAlbedo.entry)

def soilDepthtoggle():
    simpleToggle(variables["soilDepthtog_var"], soilDepth.entry)

def soilHeatCaptoggle():
    simpleToggle(variables["soilHeatCaptog_var"], soilHeatCap.entry)

def soilWaterCaptoggle():
    simpleToggle(variables["soilWaterCaptog_var"], soilWaterCap.entry)
    
def soilSaturationtoggle():
    simpleToggle(variables["soilSaturationtog_var"], soilSaturation.entry)

def vegtoggle(self):
    if variables["vegetat_var"].get() == "None":
        vegacce.entry.config(state='disabled')
        initGrowth.entry.config(state='disabled')
        biomassGrowth.entry.config(state='disabled')
        initStomataConduct.entry.config(state='disabled')
        initVegSurfRoughness.entry.config(state='disabled')
        initSoilCarbon.entry.config(state='disabled')
        initPlantCarbon.entry.config(state='disabled')
    else:
        vegacce.entry.config(state='enabled')
        initGrowth.entry.config(state='enabled')
        biomassGrowth.entry.config(state='enabled')
        initStomataConduct.entry.config(state='enabled')
        initVegSurfRoughness.entry.config(state='enabled')
        initSoilCarbon.entry.config(state='enabled')
        initPlantCarbon.entry.config(state='enabled')

def snowAlbedotoggle():
    simpleToggle(variables["snowAlbedo_var"], snowAlbedo.entry)

def maxSnowtoggle():
    simpleToggle(variables["maxSnowtog_var"], maxSnow.entry)

def mixedLayerDepthtoggle():
    simpleToggle(variables["mixedLayerDepthtog_var"], mixedLayerDepth.entry)

def oceanAlbedotoggle():
    simpleToggle(variables["oceanAlbedotog_var"], oceanAlbedo.entry)

def useSRAgle():
    global desertog
    if variables["useSRAtog_var"].get() == "sra": #SRA mode
        aquaPlanet.entry.config(state='disabled')
        desertPlanet.entry.config(state='disabled')
        heightMapImg.entry.config(state='disabled')
        heightMapImg_b.config(state='disabled')
        waterThreshold.entry.config(state='disabled')
        maxElevation.entry.config(state='disabled')
        minElevation.entry.config(state='disabled')
        imgDebug.entry.config(state='disabled')
        sraName.entry.config(state='disabled')
        landSRA.entry.config(state='enabled')
        landSRA_b.config(state='enabled')
        topoSRA.entry.config(state='enabled')
        topoSRA_b.config(state='enabled')
    elif variables["useSRAtog_var"].get() == "image": #image mode
        aquaPlanet.entry.config(state='enabled')
        desertPlanet.entry.config(state='enabled')
        heightMapImg.entry.config(state='enabled')
        heightMapImg_b.config(state='enabled')
        waterThreshold.entry.config(state='enabled')
        maxElevation.entry.config(state='enabled')
        if variables["desertPlanet_var"].get() == "True":
            minElevation.entry.config(state='enabled')
        imgDebug.entry.config(state='enabled')
        sraName.entry.config(state='enabled')
        landSRA.entry.config(state='disabled')
        landSRA_b.config(state='disabled')
        topoSRA.entry.config(state='disabled')
        topoSRA_b.config(state='disabled')

def hghtimgget():
    filename = askopenfilename(filetypes=(("png files","*.png"),("All files","*.*")))
    variables["heightMapImg_var"].set(filename) # add this

def landsraget():
    filename = askopenfilename(filetypes=(("sra files","*.sra"),("All files","*.*")))
    variables["heightMapImg_var"].set(filename) # add this

def toposraget():
    filename = askopenfilename(filetypes=(("sra files","*.sra"),("All files","*.*")))
    variables["heightMapImg_var"].set(filename) # add this

def pressuretoggle():
    simpleToggle(variables["pressuretog_var"], pressure.entry)

def gasConstanttoggle():
    simpleToggle(variables["gasConstanttog_var"], gasConstant.entry)

def ptoggle():
    global ptog
    #if ptog == 0:
    if variables["partialPressuretog_var"].get() == "True":
        pH2.entry.config(state='enabled')
        pHe.entry.config(state='enabled')
        pN2.entry.config(state='enabled')
        pO2.entry.config(state='enabled')
        pAr.entry.config(state='enabled')
        pNe.entry.config(state='enabled')
        pKr.entry.config(state='enabled')
        pH2O.entry.config(state='enabled')
        pCO2.entry.config(state='enabled')
    elif variables["partialPressuretog_var"].get() == "False":
        pH2.entry.config(state='disabled')
        pHe.entry.config(state='disabled')
        pN2.entry.config(state='disabled')
        pO2.entry.config(state='disabled')
        pAr.entry.config(state='disabled')
        pNe.entry.config(state='disabled')
        pKr.entry.config(state='disabled')
        pH2O.entry.config(state='disabled')
        pCO2.entry.config(state='disabled')

def gtoggle():
    global gtog
    #if gtog == 0:
    if variables["glacialtog_var"].get() == "True":
        gtog = 1
        initGlacialHeight.entry.config(state='enabled')
        minSnowDepth.entry.config(state='enabled')
    elif variables["glacialtog_var"].get() == "False":
        initGlacialHeight.entry.config(state='disabled')
        minSnowDepth.entry.config(state='disabled')

def stmtoggle():
    simpleToggle(variables["stmtog_var"], highCadence.entry)
    
def baltoggle ():
    global baltog
    if variables["runToBalancetog_var"].get() == "True":
        runtme.entry.config(state='disabled')
        threshold.entry.config(state='enabled')
        baseline.entry.config(state='enabled')
        maxYear.entry.config(state='enabled')
        minYear.entry.config(state='enabled')
    elif variables["runToBalancetog_var"].get() == "False":
        runtme.entry.config(state='enabled')
        threshold.entry.config(state='disabled')
        baseline.entry.config(state='disabled')
        maxYear.entry.config(state='disabled')
        minYear.entry.config(state='disabled')

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

class optionField:
    
    def __init__(self, label, var, entry) -> None:
        self.label = label
        self.var = var
        self.entry = entry
        pass


#Could have gone strongly object oriented with enums and whatnot, but KISS, right?
variables = {
"name_var" : StringVar(),
"year_var" : IntVar(),
"output_var" : StringVar(),
"cpu_var" : IntVar(),
"res_var" : StringVar(),
"res_var" : StringVar(),
"crashTolerant_var" : StringVar(),
"layers_var" : IntVar(),
"recompile_var" : StringVar(),
"starTemp_var" : DoubleVar(),
"stellarFlux_var" : DoubleVar(),
"orbitalPeriod_var" : DoubleVar(),
"rotationPeriod_var" : DoubleVar(),
"eccentricity_var" : DoubleVar(),
"obliquity_var" : DoubleVar(),
"periapsisLon_var" : DoubleVar(),
"fixedOrbit_var" : StringVar(),
"tidallyLocked_var" : StringVar(),
"periapsisLon_var" : IntVar(),
"substellarDesync_var" : DoubleVar(),
"tempContrast_var" : DoubleVar(),
"gravity_var" : DoubleVar(),
"radius_var" : DoubleVar(),
"orography_var" : DoubleVar(),
"aquaPlanet_var" : StringVar(),
"desertPlanet_var" : StringVar(),
"vegetat_var" : StringVar(),
"vegacce_var" : IntVar(),
"biomassGrowth_var" : DoubleVar(),
"initGrowth_var" : DoubleVar(),
"initStomataConduct_var" : DoubleVar(),
"initVegSurfRoughness_var" : DoubleVar(),
"initSoilCarbon_var" : DoubleVar(),
"initPlantCarbon_var" : DoubleVar(),
"wetSoil_var" : StringVar(),
"soilAlbedo_var" : DoubleVar(),
"soilAlbedotog_var" : StringVar(),
"soilDepth_var" : DoubleVar(),
"soilDepthtog_var" : StringVar(),
"soilHeatCap_var" : DoubleVar(),
"soilHeatCaptog_var" : StringVar(),
"soilWaterCap_var" : DoubleVar(),
"soilWaterCaptog_var" : StringVar(),
"soilSaturation_var" : DoubleVar(),
"soilSaturationtog_var" : StringVar(),
"snowAlbedo_var" : DoubleVar(),
"snowAlbedotog_var" : StringVar(),
"maxSnow_var" : DoubleVar(),
"maxSnowtog_var" : StringVar(),
"seaIce_var" : StringVar(),
"oceanAlbedo_var" : DoubleVar(),
"oceanAlbedotog_var" : StringVar(),
"mixedLayerDepth_var" : DoubleVar(),
"mixedLayerDepthtog_var" : StringVar(),
"oceanzen_var" : StringVar(),
"useSRAtog_var" : StringVar(),
"heightMapImg_var" : StringVar(),
"res_var" : IntVar(),
"maxElevation_var" : DoubleVar(),
"minElevation_var" : DoubleVar(),
"imgDebugtog_var" : StringVar(),
"sraName_var" : StringVar(),
"landSRA_var" : StringVar(),
"topoSRA_var" : StringVar(),
"pressure_var" : DoubleVar(),
"pressuretog_var" : StringVar(),
"gasConstant_var" : DoubleVar(),
"gasConstanttog_var" : StringVar(),
"drycoretog_var" : StringVar(),
"ozone_var" : StringVar(),
"partialPressuretog_var" : StringVar(),
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
"initGlacialHeight_var" : DoubleVar(),
"minSnowDepth_var" : DoubleVar(),
"timeStep_var" : DoubleVar(),
"runStep_var" : IntVar(),
"snapShot_var" : IntVar(),
"stepsPerWrite_var" : IntVar(),
"phyfilt1_var" : StringVar(),
"phyfilt2_var" : StringVar(),
"stormClimatetog_var" : StringVar(),
"highCadencetog_var" : StringVar(),
"runToBalancetog_var" : StringVar(),
"runtme_var" : IntVar(),
"threshold_var" : DoubleVar(),
"baseline_var" : IntVar(),
"maxYear_var" : IntVar(),
"minYear_var" : IntVar(),
"crashTolerantIfBrokentog_var" : StringVar(),
"cleantog_var" : StringVar(),
"allYearstog_var" : StringVar(),
"keepRestartstog_var" : StringVar()
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
# projectName = createOptionLabel(masterIn=modpar_frame, textIn="Project Name: ", helpText="helpjctnme", rowIn=1, colIn=1)
# variables["name_var"].set('Earth')
# name = Entry(master=modpar_frame,width=7, textvariable=variables["name_var"])
# name.grid(row=1, column=2, sticky="w")

projectNameName = optionField(
    createOptionLabel(masterIn=modpar_frame, textIn="Project Name: ", helpText="helpjctnme", rowIn=1, colIn=1),
    variables["name_var"],
    Entry(master=modpar_frame,width=7, textvariable=variables["name_var"])
)
projectNameName.entry.grid(row=1, column=2, sticky="w")


#Start Year
year = optionField(
    createOptionLabel(masterIn=modpar_frame, textIn="Start Year: ", helpText="helpstrtyr", rowIn=2, colIn=1),
    variables["year_var"].set(1),
    Entry(master=modpar_frame,textvariable=variables["year_var"], width=7)
)
year.entry.grid(row=2, column=2, sticky="w")

#Output Type
outputtype = createOptionLabel(masterIn=modpar_frame, textIn="Output Type: ", helpText="helpotptype", rowIn=3, colIn=1)
output_options = [".nc", ".nc", ".npy", ".npz", ".hdf5", ".he5", ".h5", ".csv", ".gz", ".txt", ".tar", ".tar.gz", ".tar.xz", ".tar.bz2"]
variables["output_var"].set(output_options[0])
outputtxt = OptionMenu(modpar_frame, variables["output_var"], *output_options)
outputtxt.config(width=6)
outputtxt.grid(row=3,column=2, sticky="w")

#CPU Count
cpu = optionField(
    createOptionLabel(masterIn=modpar_frame, textIn="CPU Count: ", helpText="helpcpucnt", rowIn=4, colIn=1),
    variables["cpu_var"].set(4),
    Entry(master=modpar_frame,textvariable=variables["cpu_var"], width=7)
)
cpu.entry.grid(row=4, column=2, sticky="w")

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
crashTolerantTolerant = optionField(
    createOptionLabel(masterIn=modpar_frame, textIn="Crash Tolerant: ", helpText="helpcrshtlrnt", rowIn=7, colIn=1),
    variables["crashTolerant_var"].set("False"),
    Checkbutton(master=modpar_frame,variable=variables["crashTolerant_var"], onvalue='True', offvalue='False')
)
crashTolerantTolerant.entry.grid(row=7, column=2, sticky="w")

#Layers
layers = optionField(
    createOptionLabel(masterIn=modpar_frame, textIn="Layers: ", helpText="helplayers", rowIn=8, colIn=1),
    variables["layers_var"].set(10),
    Entry(master=modpar_frame,textvariable=variables["layers_var"], width=7)
)
layers.entry.grid(row=8, column=2, sticky="w")

#Recompile
recompilepile = resolution = optionField(
    createOptionLabel(masterIn=modpar_frame, textIn="Recompile: ", helpText="helprecompile", rowIn=9, colIn=1),
    variables["recompile_var"].set("False"),
    Checkbutton(master=modpar_frame,variable=variables["recompile_var"], onvalue='True', offvalue='False')
)
recompilepile.entry.grid(row=9, column=2, sticky="w")

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------

#Stellar Parameter Frame
stelpar_frame = createParameterFrame(masterIn=col_one_frame, rowIn=3, colIn=1, gridIndex=[1,2])

modelparam = Label(master=stelpar_frame,text="Stellar Parameters")
modelparam.grid(row=0,column=1,columnspan=2,sticky="n")

#Star Temperature
starTemp = optionField(
    createOptionLabel(masterIn=stelpar_frame, textIn="Star Temp. (K): ", helpText="helpstrtmp", rowIn=1, colIn=1),
    variables["starTemp_var"].set(5772.0),
    Entry(master=stelpar_frame,textvariable=variables["starTemp_var"], width=7)
)
starTemp.entry.grid(row=1, column=2, sticky="w")

#Stellar Flux
stellarFlux = optionField(
    createOptionLabel(masterIn=stelpar_frame, textIn="Stellar Flux (W/m²): ", helpText="helpstlrflx", rowIn=2, colIn=1),
    variables["stellarFlux_var"].set(1367.0),
    Entry(master=stelpar_frame,textvariable=variables["stellarFlux_var"], width=7)
)
stellarFlux.entry.grid(row=2, column=2, sticky="w")

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------

#Orbital Parameter Frame
orbitpar_frame = createParameterFrame(masterIn=col_one_frame, rowIn=5, colIn=1, gridIndex=[1,2,3,4,5,6])

orbitparam = Label(master=orbitpar_frame,text="Orbital Parameters")
orbitparam.grid(row=0,column=1,columnspan=2,sticky="n")

#Orbital Period
orbitalPeriod = optionField(
    createOptionLabel(masterIn=orbitpar_frame, textIn="Year Length (E. Days): ", helpText="helpyrlngth", rowIn=1, colIn=1),
    variables["orbitalPeriod_var"].set(365.25),
    Entry(master=orbitpar_frame,textvariable=variables["orbitalPeriod_var"], width=7)
)
orbitalPeriod.entry.grid(row=1, column=2, sticky="w")

#Rotation Period
rotationPeriodationPeriod = optionField(
    createOptionLabel(masterIn=orbitpar_frame, textIn="Day Length (E. Days): ", helpText="helpdaylngth", rowIn=2, colIn=1),
    variables["rotationPeriod_var"].set(1.0),
    Entry(master=orbitpar_frame,textvariable=variables["rotationPeriod_var"], width=7)
)
rotationPeriodationPeriod.entry.grid(row=2, column=2, sticky="w")

#Eccentricity
eccentricity = optionField(
    createOptionLabel(masterIn=orbitpar_frame, textIn="Eccentricity: ", helpText="helpeccentr", rowIn=3, colIn=1),
    variables["eccentricity_var"].set(0.016715),
    Entry(master=orbitpar_frame,textvariable=variables["eccentricity_var"], width=7)
)
eccentricity.entry.grid(row=3, column=2, sticky="w")

#Obliquity
obliquity = optionField(
    createOptionLabel(masterIn=orbitpar_frame, textIn="Obliquity (°): ", helpText="helpoblqty", rowIn=4, colIn=1),
    variables["obliquity_var"].set(23.441),
    Entry(master=orbitpar_frame,textvariable=variables["obliquity_var"], width=7)
)
obliquity.entry.grid(row=4, column=2, sticky="w")

#Longitude of Periapsis
periapsisLon = optionField(
    createOptionLabel(masterIn=orbitpar_frame, textIn="Long. of Periapsis (°): ", helpText="helplngpri", rowIn=5, colIn=1),
    variables["periapsisLon_var"].set(102.7),
    Entry(master=orbitpar_frame,textvariable=variables["periapsisLon_var"], width=7)
)
periapsisLon.entry.grid(row=5, column=2, sticky="w")

#Fixed Orbit
fixedOrbit = optionField(
    createOptionLabel(masterIn=orbitpar_frame, textIn="Fixed Orbit: ", helpText="helpfxdobt", rowIn=6, colIn=1),
    variables["fixedOrbit_var"].set('True'),
    Checkbutton(master=orbitpar_frame,variable=variables["fixedOrbit_var"], onvalue='True', offvalue='False')
)
fixedOrbit.entry.grid(row=6, column=2, sticky="w")

#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------

col_two_frame = createColFrame(1, 3, [2,4])

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------

#Rotational Parameter Frame

rotationParamFrame = createParameterFrame(col_two_frame, 1, 1, [1,2,3,4])
rotationParamFrame.columnconfigure([2], minsize=60)

rotationPeriodatparam = Label(master=rotationParamFrame,text="Rotational Parameters")
rotationPeriodatparam.grid(row=0,column=1,columnspan=2,sticky="n")

#Tidally Locked
tidallyLocked = optionField(
    createOptionLabel(masterIn=rotationParamFrame, textIn="Tidally Locked: ", helpText="helptdlkd", rowIn=1, colIn=1),
    variables["tidallyLocked_var"].set('False'),
    Checkbutton(master=rotationParamFrame,variable=variables["tidallyLocked_var"],command=tidallyLockedtoggle, onvalue='True', offvalue='False')
)
tidallyLocked.entry.grid(row=1, column=2, sticky="w")

#Substellar Longitude
substellarLon = optionField(
    createOptionLabel(masterIn=rotationParamFrame, textIn="Substellar Longitude (°): ", helpText="helpsbstlrlng", rowIn=2, colIn=1),
    variables["periapsisLon_var"].set(180),
    Entry(master=rotationParamFrame,textvariable=variables["periapsisLon_var"], width=7)
)
substellarLon.entry.config(state='disabled')
substellarLon.entry.grid(row=2, column=2, sticky="w")

#Desync
substellarDesync = optionField(
    createOptionLabel(masterIn=rotationParamFrame, textIn="Substellar Desync (°/min): ", helpText="helpsbstlrdsync", rowIn=3, colIn=1),
    variables["substellarDesync_var"].set(0.0),
    Entry(master=rotationParamFrame,textvariable=variables["substellarDesync_var"], width=7)
)
substellarDesync.entry.config(state='disabled')
substellarDesync.entry.grid(row=3, column=2, sticky="w")

#Temp. Contrast
tempContrast = optionField(
    createOptionLabel(masterIn=rotationParamFrame, textIn="Temp. Contrast (K): ", helpText="helptmpcntrst", rowIn=4, colIn=1),
    variables["tempContrast_var"].set(0.0),
    Entry(master=rotationParamFrame,textvariable=variables["tempContrast_var"], width=7)
)
tempContrast.entry.config(state='disabled')
tempContrast.entry.grid(row=4, column=2, sticky="w")

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
gravity = optionField(
    createOptionLabel(masterIn=planetpar_frame, textIn="Gravity (m/s²): ", helpText="helpgrvty", rowIn=1, colIn=1),
    variables["gravity_var"].set(9.80665),
    Entry(master=planetpar_frame,textvariable=variables["gravity_var"], width=7)
)
gravity.entry.grid(row=1, column=2, sticky="w")

#Radius
radius = optionField(
    createOptionLabel(masterIn=planetpar_frame, textIn="Radius (E. Radii): ", helpText="helprdus", rowIn=2, colIn=1),
    variables["radius_var"].set(1.0),
    Entry(master=planetpar_frame,textvariable=variables["radius_var"], width=7)
)
radius.entry.grid(row=2, column=2, sticky="w")

#Orography
orography = optionField(
    createOptionLabel(masterIn=planetpar_frame, textIn="Orography: ", helpText="helporgrphy", rowIn=3, colIn=1),
    variables["orography_var"].set(1.0),
    Entry(master=planetpar_frame,textvariable=variables["orography_var"], width=7)
)
orography.entry.grid(row=3, column=2, sticky="w")

#Aqua Planet
aquaPlanet = optionField(
    createOptionLabel(masterIn=planetpar_frame, textIn="Aqua Planet: ", helpText="helpaquaplnt", rowIn=4, colIn=1),
    variables["aquaPlanet_var"].set('False'),
    Checkbutton(master=planetpar_frame,variable=variables["aquaPlanet_var"],command=aquatoggle, onvalue='True', offvalue='False')
)
aquaPlanet.entry.config(state='enabled')
aquaPlanet.entry.grid(row=4, column=2, sticky="w")

#Desert Planet
desertPlanet = optionField(
    createOptionLabel(masterIn=planetpar_frame, textIn="Desert Planet: ", helpText="helpdsrtplnt", rowIn=5, colIn=1),
    variables["desertPlanet_var"].set('False'),
    Checkbutton(master=planetpar_frame,variable=variables["desertPlanet_var"],command=dsrtoggle, onvalue='True', offvalue='False')
)
desertPlanet.entry.config(state='enabled')
desertPlanet.entry.grid(row=5, column=2, sticky="w")

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
vegacce = optionField(
    createOptionLabel(masterIn=vegpar_frame, textIn="Veg. Acceleration: ", helpText="helpvgaclrtn", rowIn=2, colIn=1),
    variables["vegacce_var"].set(1),
    Entry(master=vegpar_frame,textvariable=variables["vegacce_var"], width=7)
)
vegacce.entry.config(state='disabled')
vegacce.entry.grid(row=2, column=2, sticky="w")

#Biomass Growth
biomassGrowth = optionField(
    createOptionLabel(masterIn=vegpar_frame, textIn="Biomass Growth: ", helpText="helpbiomsgrwth", rowIn=3, colIn=1),
    variables["biomassGrowth_var"].set(1.0),
    Entry(master=vegpar_frame,textvariable=variables["biomassGrowth_var"], width=7)
)
biomassGrowth.entry.config(state='disabled')
biomassGrowth.entry.grid(row=3, column=2, sticky="w")

#Initial Growth
initGrowth = optionField(
    createOptionLabel(masterIn=vegpar_frame, textIn="Initial Growth: ", helpText="helpintlgrth", rowIn=4, colIn=1),
    variables["initGrowth_var"].set(0.5),
    Entry(master=vegpar_frame,textvariable=variables["initGrowth_var"], width=7)
)
initGrowth.entry.config(state='disabled')
initGrowth.entry.grid(row=4, column=2, sticky="w")

#Initial Stomatal Conductance
initStomataConduct = optionField(
    createOptionLabel(masterIn=vegpar_frame, textIn="Stomatal Conductance: ", helpText="helpstmtlcndtnce", rowIn=5, colIn=1),
    variables["initStomataConduct_var"].set(1.0),
    Entry(master=vegpar_frame,textvariable=variables["initStomataConduct_var"], width=7)
)
initStomataConduct.entry.config(state='disabled')
initStomataConduct.entry.grid(row=5, column=2, sticky="w")

#Initial Vegetative Surface Roughness
initVegSurfRoughness = optionField(
    createOptionLabel(masterIn=vegpar_frame, textIn="Vegetation Roughness: ", helpText="helpvgtnrghns", rowIn=6, colIn=1),
    variables["initVegSurfRoughness_var"].set(2.0),
    Entry(master=vegpar_frame,textvariable=variables["initVegSurfRoughness_var"], width=7)
)
initVegSurfRoughness.entry.config(state='disabled')
initVegSurfRoughness.entry.grid(row=6, column=2, sticky="w")

#Initial Soil Carbon Content
initSoilCarbon = optionField(
    createOptionLabel(masterIn=vegpar_frame, textIn="Soil Carbon Content: ", helpText="helpslcbncntnt", rowIn=7, colIn=1),
    variables["initSoilCarbon_var"].set(0.0),
    Entry(master=vegpar_frame,textvariable=variables["initSoilCarbon_var"], width=7)
)
initSoilCarbon.entry.config(state='disabled')
initSoilCarbon.entry.grid(row=7, column=2, sticky="w")

#Initial Vegetative Carbon Content
initPlantCarbon = optionField(
    createOptionLabel(masterIn=vegpar_frame, textIn="Plant Carbon Content: ", helpText="helplntcbncntnt", rowIn=8, colIn=1),
    variables["initPlantCarbon_var"].set(0.0),
    Entry(master=vegpar_frame,textvariable=variables["initPlantCarbon_var"], width=7)
)
initPlantCarbon.entry.config(state='disabled')
initPlantCarbon.entry.grid(row=8, column=2, sticky="w")

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
wetSoil = optionField(
    createOptionLabel(masterIn=surfpar_frame, textIn="Wet Soil: ", helpText="helpwtsl", rowIn=1, colIn=1),
    variables["wetSoil_var"].set("False"),
    Checkbutton(master=surfpar_frame,variable=variables["wetSoil_var"], onvalue='True', offvalue='False')
)
wetSoil.entry.grid(row=1, column=2, sticky="w")

#Soil Albedo
soilAlbedo = optionField(
    createOptionLabel(masterIn=surfpar_frame, textIn="Soil Albedo: ", helpText="helpslalbdo", rowIn=2, colIn=1),
    variables["soilAlbedo_var"].set(0.0),
    Entry(master=surfpar_frame,textvariable=variables["soilAlbedo_var"], width=7)
)
soilAlbedo.entry.config(state='disabled')
soilAlbedo.entry.grid(row=2, column=2, sticky="w")
##Soil Albedo Toggle
variables["soilAlbedotog_var"].set('False')
soilAlbedotog_n = Checkbutton(master=surfpar_frame,variable=variables["soilAlbedotog_var"],command=soilAlbedotoggle, onvalue='True', offvalue='False')
soilAlbedotog_n.grid(row=2, column=3, sticky="w")

#Soil Depth
soilDepth = optionField(
    createOptionLabel(masterIn=surfpar_frame, textIn="Soil Depth (m): ", helpText="helpsldpth", rowIn=3, colIn=1),
    variables["soilDepth_var"].set(12.4),
    Entry(master=surfpar_frame,textvariable=variables["soilDepth_var"], width=7)
)
soilDepth.entry.config(state='disabled')
soilDepth.entry.grid(row=3, column=2, sticky="w")
##Soil Depth Toggle
variables["soilDepthtog_var"].set('False')
soilDepthtog_n = Checkbutton(master=surfpar_frame,variable=variables["soilDepthtog_var"],command=soilDepthtoggle, onvalue='True', offvalue='False')
soilDepthtog_n.grid(row=3, column=3, sticky="w")

#Soil Heat Capacity
soilHeatCap = optionField(
    createOptionLabel(masterIn=surfpar_frame, textIn="Soil Heat Capacity: ", helpText="helpslhtcpsty", rowIn=4, colIn=1),
    variables["soilHeatCap_var"].set(2.4),
    Entry(master=surfpar_frame,textvariable=variables["soilHeatCap_var"], width=7)
)
soilHeatCap.entry.config(state='disabled')
soilHeatCap.entry.grid(row=4, column=2, sticky="w")
##Soil Heact Capacity Toggle
variables["soilHeatCaptog_var"].set('False')
soilHeatCaptog_n = Checkbutton(master=surfpar_frame,variable=variables["soilHeatCaptog_var"],command=soilHeatCaptoggle, onvalue='True', offvalue='False')
soilHeatCaptog_n.grid(row=4, column=3, sticky="w")

#Soil Water Capacity
soilWaterCap = optionField(
    createOptionLabel(masterIn=surfpar_frame, textIn="Soil Water Capacity: ", helpText="helpslwtrcpsty", rowIn=5, colIn=1),
    variables["soilWaterCap_var"].set(0.5),
    Entry(master=surfpar_frame,textvariable=variables["soilWaterCap_var"], width=7)
)
soilWaterCap.entry.config(state='disabled')
soilWaterCap.entry.grid(row=5, column=2, sticky="w")
##Soil Water Capacity Toggle
variables["soilWaterCaptog_var"].set('False')
soilWaterCaptog_n = Checkbutton(master=surfpar_frame,variable=variables["soilWaterCaptog_var"],command=soilWaterCaptoggle, onvalue='True', offvalue='False')
soilWaterCaptog_n.grid(row=5, column=3, sticky="w")

#Soil Saturation
soilSaturation = optionField(
    createOptionLabel(masterIn=surfpar_frame, textIn="Soil Saturation: ", helpText="helpslstrtn", rowIn=6, colIn=1),
    variables["soilSaturation_var"].set(0.0),
    Entry(master=surfpar_frame,textvariable=variables["soilSaturation_var"], width=7)
)
soilSaturation.entry.config(state='disabled')
soilSaturation.entry.grid(row=6, column=2, sticky="w")
##Soil Water Capacity Toggle
variables["soilSaturationtog_var"].set('False')
soilSaturationtog_n = Checkbutton(master=surfpar_frame,variable=variables["soilSaturationtog_var"],command=soilSaturationtoggle, onvalue='True', offvalue='False')
soilSaturationtog_n.grid(row=6, column=3, sticky="w")

#Snow Albedo
snowAlbedo = optionField(
    createOptionLabel(masterIn=surfpar_frame, textIn="Snow Albedo: ", helpText="helpsnwalb", rowIn=7, colIn=1),
    variables["snowAlbedo_var"].set(0.0),
    Entry(master=surfpar_frame,textvariable=variables["snowAlbedo_var"], width=7)
)
snowAlbedo.entry.config(state='disabled')
snowAlbedo.entry.grid(row=7, column=2, sticky="w")
##Snow Albedo Toggle
variables["snowAlbedotog_var"].set('False')
snowAlbedotog_n = Checkbutton(master=surfpar_frame,variable=variables["snowAlbedotog_var"],command=snowAlbedotoggle, onvalue='True', offvalue='False')
snowAlbedotog_n.grid(row=7, column=3, sticky="w")

#Max Snow
maxSnow = optionField(
    createOptionLabel(masterIn=surfpar_frame, textIn="Max Snow (m): ", helpText="helpmxsnw", rowIn=8, colIn=1),
    variables["maxSnow_var"].set(5.0),
    Entry(master=surfpar_frame,textvariable=variables["maxSnow_var"], width=7)
)
maxSnow.entry.config(state='disabled')
maxSnow.entry.grid(row=8, column=2, sticky="w")
##Snow Albedo Toggle
variables["maxSnowtog_var"].set('False')
maxSnowtog_n = Checkbutton(master=surfpar_frame,variable=variables["maxSnowtog_var"],command=maxSnowtoggle, onvalue='True', offvalue='False')
maxSnowtog_n.grid(row=8, column=3, sticky="w")

#Sea Ice
seaIce = optionField(
    createOptionLabel(masterIn=surfpar_frame, textIn="Sea Ice: ", helpText="helpseaice", rowIn=9, colIn=1),
    variables["seaIce_var"].set('True'),
    Checkbutton(master=surfpar_frame,variable=variables["seaIce_var"], onvalue='True', offvalue='False')
)
seaIce.entry.grid(row=9, column=2, sticky="w")

#Ocean Albedo
oceanAlbedo = optionField(
    createOptionLabel(masterIn=surfpar_frame, textIn="Ocean Albedo: ", helpText="helpocnalb", rowIn=10, colIn=1),
    variables["oceanAlbedo_var"].set(0.0),
    Entry(master=surfpar_frame,textvariable=variables["snowAlbedo_var"], width=7)
)
oceanAlbedo.entry.config(state='disabled')
oceanAlbedo.entry.grid(row=10, column=2, sticky="w")
##Snow Albedo Toggle
variables["oceanAlbedotog_var"].set('False')
oceanAlbedotog_n = Checkbutton(master=surfpar_frame,variable=variables["oceanAlbedotog_var"],command=oceanAlbedotoggle, onvalue='True', offvalue='False')
oceanAlbedotog_n.grid(row=10, column=3, sticky="w")

#Mixed Ocean Depth
mixedLayerDepth = optionField(
    createOptionLabel(masterIn=surfpar_frame, textIn="Mixed Layer Depth (m): ", helpText="helpmxdlyrdpth", rowIn=11, colIn=1),
    variables["mixedLayerDepth_var"].set(50.0),
    Entry(master=surfpar_frame,textvariable=variables["mixedLayerDepth_var"], width=7)
)
mixedLayerDepth.entry.config(state='disabled')
mixedLayerDepth.entry.grid(row=11, column=2, sticky="w")
##Mixed Ocean Depth Toggle
variables["mixedLayerDepthtog_var"].set('False')
mixedLayerDepthtog_n = Checkbutton(master=surfpar_frame,variable=variables["mixedLayerDepthtog_var"],command=mixedLayerDepthtoggle, onvalue='True', offvalue='False')
mixedLayerDepthtog_n.grid(row=11, column=3, sticky="w")

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
useSRA = optionField(
    createOptionLabel(masterIn=geopar_frame, textIn="Use SRA instead of image: ", helpText="helpimgsratog", rowIn=1, colIn=1),
    variables["useSRAtog_var"].set('image'),
    Checkbutton(master=geopar_frame,variable=variables["useSRAtog_var"],command=useSRAgle, onvalue='sra', offvalue='image')
)
useSRA.entry.grid(row=1, column=2, sticky="w")

#Height Map Image
heightMapImg = optionField(
    createOptionLabel(masterIn=geopar_frame, textIn="Height Map Image: ", helpText="helphghtmpimg", rowIn=2, colIn=1),
    variables["heightMapImg_var"].set(''),
    Entry(master=geopar_frame,textvariable=variables["heightMapImg_var"], width=7)
)
heightMapImg.entry.config(state='enabled')
heightMapImg.entry.grid(row=2, column=2, sticky="w")
heightMapImg_b = Button(master=geopar_frame,text="Open",command=hghtimgget, width=7)
heightMapImg_b.config(state='enabled')
heightMapImg_b.grid(row=2, column=3, sticky="w")

#Water Threshold
waterThreshold = optionField(
    createOptionLabel(masterIn=geopar_frame, textIn="Water Threshold: ", helpText="helpwtrthrshld", rowIn=3, colIn=1),
    variables["res_var"].set(0),
    Entry(master=geopar_frame,textvariable=variables["res_var"], width=7)
)
waterThreshold.entry.config(state='enabled')
waterThreshold.entry.grid(row=3, column=2, sticky="w")

#Highest Elevation
maxElevation = optionField(
    createOptionLabel(masterIn=geopar_frame, textIn="Highest Elevation (m): ", helpText="helphghstelvtn", rowIn=4, colIn=1),
    variables["maxElevation_var"].set(8849.0),
    Entry(master=geopar_frame,textvariable=variables["maxElevation_var"], width=7)
)
maxElevation.entry.config(state='enabled')
maxElevation.entry.grid(row=4, column=2, sticky="w")

#Lowest Elevation
minElevation = optionField(
    createOptionLabel(masterIn=geopar_frame, textIn="Lowest Elevation (m): ", helpText="helplwstelvtn", rowIn=5, colIn=1),
    variables["minElevation_var"].set(-11034.0),
    Entry(master=geopar_frame,textvariable=variables["minElevation_var"], width=7)
)
minElevation.entry.config(state='disabled')
minElevation.entry.grid(row=5, column=2, sticky="w")

#Image Debug
imgDebug = optionField(
    createOptionLabel(masterIn=geopar_frame, textIn="Image Debug: ", helpText="helpimgdbg", rowIn=6, colIn=1),
    variables["imgDebugtog_var"].set('False'),
    Checkbutton(master=geopar_frame,variable=variables["imgDebugtog_var"], onvalue='True', offvalue='False')
)
imgDebug.entry.config(state='enabled')
imgDebug.entry.grid(row=6, column=2, sticky="w")

#SRA Name
sraName = optionField(
    createOptionLabel(masterIn=geopar_frame, textIn="SRA Name: ", helpText="helpsranme", rowIn=7, colIn=1),
    variables["sraName_var"].set("earth"),
    Entry(master=geopar_frame,textvariable=variables["sraName_var"], width=7)
)
sraName.entry.config(state='enabled')
sraName.entry.grid(row=7, column=2, sticky="w")

#Land SRA
landSRA = optionField(
    createOptionLabel(masterIn=geopar_frame, textIn="Land SRA: ", helpText="helplndsra", rowIn=8, colIn=1),
    variables["landSRA_var"].set(''),
    Entry(master=geopar_frame,textvariable=variables["landSRA_var"], width=7)
)
landSRA.entry.config(state='disabled')
landSRA.entry.grid(row=8, column=2, sticky="w")
landSRA_b = Button(master=geopar_frame,text="Open",command=landsraget, width=7)
landSRA_b.config(state='disabled')
landSRA_b.grid(row=8, column=3, sticky="w")

#Topo SRA
topoSRA = optionField(
    createOptionLabel(masterIn=geopar_frame, textIn="Topographic SRA: ", helpText="helptposra", rowIn=9, colIn=1),
    variables["topoSRA_var"].set(''),
    Entry(master=geopar_frame,textvariable=variables["topoSRA_var"], width=7)
)
topoSRA.entry.config(state='disabled')
topoSRA.entry.grid(row=9, column=2, sticky="w")
topoSRA_b = Button(master=geopar_frame,text="Open",command=toposraget, width=7)
topoSRA_b.config(state='disabled')
topoSRA_b.grid(row=9, column=3, sticky="w")

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
pressure = optionField(
    createOptionLabel(masterIn=atmpar_frame, textIn="Pressure (bar): ", helpText="helprsure", rowIn=1, colIn=1),
    variables["pressure_var"].set(1.0),
    Entry(master=atmpar_frame,textvariable=variables["pressure_var"], width=7)
)
pressure.entry.config(state='disabled')
pressure.entry.grid(row=1, column=2, sticky="w")
##Pressure Toggle
variables["pressuretog_var"].set('False')
pressuretog_n = Checkbutton(master=atmpar_frame,variable=variables["pressuretog_var"],command=pressuretoggle, onvalue='True', offvalue='False')
pressuretog_n.grid(row=1, column=3, sticky="w")

#Gas Constant
gasConstant = optionField(
    createOptionLabel(masterIn=atmpar_frame, textIn="Gas Constant: ", helpText="helpgscnstnt", rowIn=2, colIn=1),
    variables["gasConstant_var"].set(287.0),
    Entry(master=atmpar_frame,textvariable=variables["gasConstant_var"], width=7)
)
gasConstant.entry.config(state='disabled')
gasConstant.entry.grid(row=2, column=2, sticky="w")
##Gas Constant Toggle
variables["gasConstanttog_var"].set('False')
gasConstanttog_n = Checkbutton(master=atmpar_frame,variable=variables["gasConstanttog_var"],command=gasConstanttoggle, onvalue='True', offvalue='False')
gasConstanttog_n.grid(row=2, column=3, sticky="w")

#Dry Core
drycore = optionField(
    createOptionLabel(masterIn=atmpar_frame, textIn="Dry Core: ", helpText="helpdrycre", rowIn=3, colIn=1),
    variables["drycoretog_var"].set('False'),
    Checkbutton(master=atmpar_frame,variable=variables["drycoretog_var"], onvalue='True', offvalue='False')
)
drycore.entry.grid(row=3, column=2, sticky="w")

#Ozone
ozone = optionField(
    createOptionLabel(masterIn=atmpar_frame, textIn="Ozone: ", helpText="helpozne", rowIn=4, colIn=1),
    variables["ozone_var"].set('False'),
    Checkbutton(master=atmpar_frame,variable=variables["ozone_var"], onvalue='True', offvalue='False')
)
ozone.entry.grid(row=4, column=2, sticky="w")

#Partial Pressure
partialPressure = optionField(
    createOptionLabel(masterIn=atmpar_frame, textIn="Gas Pressure (bar): ", helpText="helpgsprsurs", rowIn=5, colIn=1),
    variables["partialPressuretog_var"].set('False'),
    Checkbutton(master=atmpar_frame,variable=variables["partialPressuretog_var"],command=ptoggle, onvalue='True', offvalue='False')
)
partialPressure.entry.grid(row=5, column=2, sticky="w")


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
glacial = optionField(
    createOptionLabel(masterIn=glacpar_frame, textIn="Glaciers: ", helpText="helpglcrs", rowIn=1, colIn=1),
    variables["glacialtog_var"].set('False'),
    Checkbutton(master=glacpar_frame,variable=variables["glacialtog_var"],command=gtoggle, onvalue='True', offvalue='False')
)
glacial.entry.grid(row=1, column=2, sticky="w")

#Initial Height
initGlacialHeight = optionField(
    createOptionLabel(masterIn=glacpar_frame, textIn="Height (m): ", helpText="helpgrhght", rowIn=2, colIn=1),
    variables["initGlacialHeight_var"].set(0.0),
    Entry(master=glacpar_frame,textvariable=variables["initGlacialHeight_var"],width=7)
)
initGlacialHeight.entry.config(state='disabled')
initGlacialHeight.entry.grid(row=2, column=2, sticky="w")

#Minimum Snow Depth
minSnowDepth = optionField(
    createOptionLabel(masterIn=glacpar_frame, textIn="Threshold (m): ", helpText="helpgrthrshld", rowIn=3, colIn=1),
    variables["minSnowDepth_var"].set(2.0),
    Entry(master=glacpar_frame,textvariable=variables["minSnowDepth_var"],width=7)
)
minSnowDepth.entry.config(state='disabled')
minSnowDepth.entry.grid(row=3, column=2, sticky="w")

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
timeStep = optionField(
    createOptionLabel(masterIn=mdldynpar_frame, textIn="Timestep (min): ", helpText="helptimestep", rowIn=1, colIn=1),
    variables["timeStep_var"].set(45.0),
    Entry(master=mdldynpar_frame,textvariable=variables["timeStep_var"], width=7)
)
timeStep.entry.grid(row=1, column=2, sticky="w")

#Runsteps
runStep = optionField(
    createOptionLabel(masterIn=mdldynpar_frame, textIn="Runsteps: ", helpText="helprunsteps", rowIn=2, colIn=1),
    variables["runStep_var"].set(11520),
    Entry(master=mdldynpar_frame,textvariable=variables["runStep_var"], width=7)
)
runStep.entry.grid(row=2, column=2, sticky="w")

#Snapshots
snapShot = optionField(
    createOptionLabel(masterIn=mdldynpar_frame, textIn="Snapshots: ", helpText="helpsnapshots", rowIn=3, colIn=1),
    variables["snapShot_var"].set(0),
    Entry(master=mdldynpar_frame,textvariable=variables["snapShot_var"], width=7)
)
snapShot.entry.grid(row=3, column=2, sticky="w")

#NSTPW
stepsPerWrite = optionField(
    createOptionLabel(masterIn=mdldynpar_frame, textIn="NSTPW: ", helpText="helpnstpw", rowIn=4, colIn=1),
    variables["stepsPerWrite_var"].set(160),
    Entry(master=mdldynpar_frame,textvariable=variables["stepsPerWrite_var"], width=7)
)
stepsPerWrite.entry.grid(row=4, column=2, sticky="w")

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
stormClimate = optionField(
    createOptionLabel(masterIn=mdldynpar_frame, textIn="Storm Climatology: ", helpText="helpstmclmtlgy", rowIn=7, colIn=1),
    variables["stormClimatetog_var"].set('False'),
    Checkbutton(master=mdldynpar_frame,variable=variables["stormClimatetog_var"],command=stmtoggle, onvalue='True', offvalue='False')
)
stormClimate.entry.grid(row=7, column=2, sticky="w")

#High Cadence
highCadence = optionField(
    createOptionLabel(masterIn=mdldynpar_frame, textIn="High Cadence: ", helpText="helphghcdnce", rowIn=8, colIn=1),
    variables["highCadencetog_var"].set('False'),
    Checkbutton(master=mdldynpar_frame,variable=variables["highCadencetog_var"], onvalue='True', offvalue='False')
)
highCadence.entry.config(state='disabled')
highCadence.entry.grid(row=8, column=2, sticky="w")

#Run To Balance
runToBalance = optionField(
    createOptionLabel(masterIn=mdldynpar_frame, textIn="Run To Balance: ", helpText="helprntbal", rowIn=9, colIn=1),
    variables["runToBalancetog_var"].set('False'),
    Checkbutton(master=mdldynpar_frame,variable=variables["runToBalancetog_var"],command=baltoggle, onvalue='True', offvalue='False')
)
runToBalance.entry.grid(row=9, column=2, sticky="w")

#Run Time
runtme = optionField(
    createOptionLabel(masterIn=mdldynpar_frame, textIn="Run Time (years): ", helpText="helprntme", rowIn=10, colIn=1),
    variables["runtme_var"].set(100),
    Entry(master=mdldynpar_frame,textvariable=variables["runtme_var"], width=7)
)
runtme.entry.grid(row=10, column=2, sticky="w")

#Threshold
threshold = optionField(
    createOptionLabel(masterIn=mdldynpar_frame, textIn="Threshold: ", helpText="helpthrshld", rowIn=11, colIn=1),
    variables["threshold_var"].set(0.0005),
    Entry(master=mdldynpar_frame,textvariable=variables["threshold_var"], width=7)
)
threshold.entry.config(state='disabled')
threshold.entry.grid(row=11, column=2, sticky="w")

#Baseline
baseline = optionField(
    createOptionLabel(masterIn=mdldynpar_frame, textIn="Baseline (years): ", helpText="helpbslne", rowIn=12, colIn=1),
    variables["baseline_var"].set(10),
    Entry(master=mdldynpar_frame,textvariable=variables["baseline_var"], width=7)
)
baseline.entry.config(state='disabled')
baseline.entry.grid(row=12, column=2, sticky="w")

#Max Years
maxYear = optionField(
    createOptionLabel(masterIn=mdldynpar_frame, textIn="Max. Year (years): ", helpText="helpmxyr", rowIn=13, colIn=1),
    variables["maxYear_var"].set(100),
    Entry(master=mdldynpar_frame,textvariable=variables["maxYear_var"], width=7)
)
maxYear.entry.config(state='disabled')
maxYear.entry.grid(row=13, column=2, sticky="w")

#Min Years
minYear = optionField(
    createOptionLabel(masterIn=mdldynpar_frame, textIn="Min. Year (years): ", helpText="helpmnyr", rowIn=14, colIn=1),
    variables["minYear_var"].set(10),
    Entry(master=mdldynpar_frame,textvariable=variables["minYear_var"], width=7)
)
minYear.entry.config(state='disabled')
minYear.entry.grid(row=14, column=2, sticky="w")

#Crash If Broken
crashTolerantIfBroken = optionField(
    createOptionLabel(masterIn=mdldynpar_frame, textIn="Crash if Broken: ", helpText="helpcrshibrkn", rowIn=15, colIn=1),
    variables["crashTolerantIfBrokentog_var"].set('False'),
    Checkbutton(master=mdldynpar_frame,variable=variables["crashTolerantIfBrokentog_var"], onvalue='True', offvalue='False')
)
crashTolerantIfBroken.entry.grid(row=15, column=2, sticky="w")

#Clean
clean = optionField(
    createOptionLabel(masterIn=mdldynpar_frame, textIn="Clean: ", helpText="helpcln", rowIn=16, colIn=1),
    variables["cleantog_var"].set('False'),
    Checkbutton(master=mdldynpar_frame,variable=variables["cleantog_var"], onvalue='True', offvalue='False')
)
clean.entry.grid(row=16, column=2, sticky="w")

#All Years
allYears = optionField(
    createOptionLabel(masterIn=mdldynpar_frame, textIn="All Years: ", helpText="helpalrstrts", rowIn=17, colIn=1),
    variables["allYearstog_var"].set('False'),
    Checkbutton(master=mdldynpar_frame,variable=variables["allYearstog_var"], onvalue='True', offvalue='False')
)
allYears.entry.grid(row=17, column=2, sticky="w")

#Keep Restarts
keepRestarts = optionField(
    createOptionLabel(masterIn=mdldynpar_frame, textIn="Keep Restarts: ", helpText="helpkprstrts", rowIn=18, colIn=1),
    variables["keepRestartstog_var"].set('False'),
    Checkbutton(master=mdldynpar_frame,variable=variables["keepRestartstog_var"], onvalue='True', offvalue='False')
)
keepRestarts.entry.grid(row=18, column=2, sticky="w")

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