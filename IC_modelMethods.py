import os
from convert_sra import convert_sra
def system_check(variables):

    returnString = ""

    returnString += "Configuration Compatability Check:\n"
    check_year = variables["orbp_var"]
    check_day = variables["rot_var"]
    check_time = variables["tmestp_var"]
    check_run = variables["runstp_var"]
    check_nsptw = variables["nsptw_var"]
    time_check = (24*60)/check_time

    if time_check == round(time_check):
        returnString += "Timestep: Nominal\n"
    else:
        returnString += "WARNING: Current Timestep setting places ratio between (24*60) and timestep at "+str(time_check)+" which may cause problems with ExoPlaSim.\n"
        time_corct = (24*60)/round(time_check)
        returnString += "Setting it to "+str(time_corct)+" or a factor of a 24 hour day will work better.\n"

    nsptw_check = (check_nsptw*check_time)/1440
    if 4 <= nsptw_check <= 6:
        returnString += "NSPTW: Nominal\n"
    else:
        returnString += "WARNING: Current NSPTW setting places day interval at "+str(nsptw_check)+" which may cause problems with ExoPlaSim.\n"
        returnString += "Changing this to be between 4 and 6 will work better.\n"

    run_check = check_run/check_nsptw
    if run_check == round(run_check):
        returnString += "Runsteps: Nominal\n"
    else:
        returnString += "WARNING: Current Runsteps setting places ratio between runsteps and NSPTW at "+str(run_check)+" which may cause problems with ExoPlaSim.\n"
        returnString += "Setting it to a factor of a 24 hour day will work better.\n"
    year_check = (check_year*1440)/(check_run*check_time)

    if year_check == 1:
        returnString += "Year: Nominal\n"
    else:
        returnString += "WARNING: Current Year length places the ratio between (year*1440) and (runsteps*timestep) at "+str(round(year_check, 6))+" which may cause problems with ExoPlaSim.\n"
        year_corct = (round(year_check)*(check_run*check_time))/1440
        returnString += "Changing this to "+str(year_corct)+" will work better.\n"
    day_check1 = (check_day*1440)/check_time
    day_check2 = (check_run/12)/((check_day*1440)/check_time)

    if day_check1 == round(day_check1):
        if day_check2 == round(day_check2):
            returnString += "Day: Nominal\n"
        else:
            returnString += "WARNING: Current day length places ratio between (runsteps/12) and ((day*1440)/timestep) at "+str(day_check2)+" which may cause problems with ExoPlaSim.\n"
            returnString += "Changeing this to an integer will work better.\n"
    else:
        returnString += "WARNING: Current day length places ratio between (day*1440) and timestep at "+str(day_check1)+" which may cause problems with ExoPlaSim.\n"
        returnString += "Changing this to an integer will work better.\n"

    return returnString

def save_file(variables, filepath):

#Getting input text
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    nametext = str(variables["name_var"])
    yeartext = str(variables["year_var"])
    typetext = str(variables["output_var"])
    cpustext = str(variables["cpu_var"])
    prestext = str(variables["res_var"])
    resotext = str(variables["res_var"])
    crastext = str(variables["crash_var"])
    layertext = str(variables["layers_var"])
    recomptext = str(variables["recom_var"])
    startext = str(variables["startemp_var"])
    fluxtext = str(variables["flux_var"])
    orbptext = str(variables["orbp_var"])
    eccetext = str(variables["ecc_var"])
    oblitext = str(variables["obli_var"])
    lonvtext = str(variables["lon_var"])
    fixotext = str(variables["fixed_var"])
    rotptext = str(variables["rot_var"])
    tidltext = str(variables["tidal_var"])
    steltext = str(variables["lon_var"])
    dsynctext = str(variables["desync_var"])
    tmpcntext = str(variables["tempcon_var"])
    gravtext = str(variables["gravity_var"])
    radustext = str(variables["radius_var"])
    orogtext = str(variables["orogph_var"])
    aquaptext = str(variables["aquap_var"])
    dsrtptext = str(variables["desertp_var"])
    vegtext = str(variables["vegetat_var"])
    vacctext = str(variables["vegacce_var"])
    biogrwtext = str(variables["nfrtgrw_var"])
    initgrwtext = str(variables["initgrw_var"])
    stomatext = str(variables["initstcd_var"])
    vroughtext = str(variables["initrgh_var"])
    slcartext = str(variables["initslc_var"])
    pltcartext = str(variables["initplc_var"])
    wtsoiltext = str(variables["wetso_var"])
    slalbtext = str(variables["soilalbtog_var"])
    solalbtext = str(variables["soilalb_var"])
    sldpthtext = str(variables["soildepthtog_var"])
    soldpthtext = str(variables["soildepth_var"])
    cpsltext = str(variables["capsoiltog_var"])
    capsoltext = str(variables["capsoil_var"])
    slwcptext = str(variables["soilwcptog_var"])
    solwcptext = str(variables["soilwcp_var"])
    slsattext = str(variables["soilsattog_var"])
    solsattext = str(variables["soilsat_var"])
    snwalbtext = str(variables["snowalbtog_var"])
    snowalbtext = str(variables["snowalb_var"])
    mxsnwtext = str(variables["mxsnowtog_var"])
    maxsnwtext = str(variables["mxsnow_var"])
    sicetext = str(variables["seaice_var"])
    ocnalbtext = str(variables["oceanalbtog_var"])
    oceanalbtext = str(variables["oceanalb_var"])
    mldphtext = str(variables["mldepthtog_var"])
    mixldphtext = str(variables["mldepth_var"])
    ocnzntext = str(variables["oceanzen_var"])
    imgsratext = str(variables["imgsratogtog_var"])
    hghtimgpath = variables["hghtmpimg_var"]
    wtrthreshtext = str(variables["res_var"])
    hghelvtext = str(variables["highelev_var"])
    lwelvtext = str(variables["lowelev_var"])
    imgdbgtext = str(variables["imgdebugtog_var"])
    sranmetext = str(variables["sranme_var"])
    landsratext = str(variables["lndsra_var"])
    toposratext = str(variables["tposra_var"])
    prssretogtext = str(variables["pressuretog_var"])
    pressuretext = str(variables["pressure_var"])
    gascontogtext = str(variables["gascontog_var"])
    gascontext = str(variables["gascon_var"])
    drycretext = str(variables["drycoretog_var"])
    ozonetext = str(variables["ozone_var"])
    prtlprssretext = str(variables["partialptog_var"])
    H2text = str(variables["pH2_var"])
    Hetext = str(variables["pHe_var"])
    N2text = str(variables["pN2_var"])
    O2text = str(variables["pO2_var"])
    Artext = str(variables["pAr_var"])
    Netext = str(variables["pNe_var"])
    Krtext = str(variables["pKr_var"])
    H2Otext = str(variables["pH2O_var"])
    CO2text = str(variables["pCO2_var"])
    glaciertext = str(variables["glacialtog_var"])
    initheightext = str(variables["inith_var"])
    mindepthtext = str(variables["mndph_var"])
    timesteptext = str(variables["tmestp_var"])
    runsteptext = str(variables["runstp_var"])
    snapshotext = str(variables["snpsht_var"])
    nsptwtext = str(variables["nsptw_var"])
    physics1text = str(variables["phyfilt1_var"])
    physics2text = str(variables["phyfilt2_var"])
    stormtext = str(variables["stormcltog_var"])
    highcadtext = str(variables["highcadtog_var"])
    runtobaltext = str(variables["rntbaltog_var"])
    runtimetext = str(variables["runtme_var"])
    thresholdtext = str(variables["trshld_var"])
    baselinetext = str(variables["bselne_var"])
    maxyeartext = str(variables["maxyr_var"])
    minyeartext = str(variables["minyr_var"])
    crashbrkntext = str(variables["cshibrktog_var"])
    cleantext = str(variables["cleantog_var"])
    allyearstext = str(variables["allyrstog_var"])
    keeprstrtstext = str(variables["kprststog_var"])
    print("Inputs gathered...")

    """Convert heightmap image to SRA files."""
    if aquaptext == "False":
        aquaplanetext = ''
        if imgsratext == "False":

            landmaptext, topomaptext = convert_sra(
                filepath=filepath,
                infile=hghtimgpath,
                grav=float(gravtext),
                debug_img= (imgdbgtext=="True"),
                desert_planet=(dsrtptext=="True"),
                floor_value=int(wtrthreshtext),
                peak_value=float(hghelvtext),
                trench_value=float(lwelvtext),
                resotext=resotext,
                sra_name=sranmetext
            )

            
        else:
            lndsrafle = ntpath.basename(landsratext)
            tposrafle = ntpath.basename(toposratext)
            sra_path = path.dirname(filepath)+'/SRA'
            try:
                os.makedirs(sra_path)
            except FileExistsError:
                # directory already exists
                pass
            shutil.copyfile(landsratext, sra_path)
            shutil.copyfile(toposratext, sra_path)
            landmaptext = 'landmap="SRA/'+lndsrafle+'",'
            topomaptext = 'topomap="SRA/'+tposrafle+'"<'
    else:
        print("Formatting...")
        aquaplanetext = 'aquaplanet=True,'
        landmaptext = ''
        topomaptext = ''
    if dsrtptext == "True":
        dsrtplanetext = 'desertplanet=True,'
    else:
        dsrtplanetext = ''

    #Conditions
    if crastext == "True":
        crashtext = ',crashtolerant='+crastext
    else:
        crashtext = ''
    if recomptext == "True":
        recomtext = ',recompile='+recomptext
    else:
        recomtext = ''
    if tidltext == "True":
        rottext = 'synchronous='+tidltext+',substellarlon='+steltext+',desync='+dsynctext+',tlcontrast='+tmpcntext
    else:
        rottext = 'rotationperiod='+rotptext
    if vegtext == "None":
        vegetationtext = ''
    else:
        if vegtext == "Proscribed":
            vegstat = '				  vegetation=1'+',vegaccel='+vacctext+',nforestgrowth='+biogrwtext+',initgrowth='+initgrwtext
        elif vegtext == "Dynamic":
            vegstat = '				  vegetation=2'+',vegaccel='+vacctext+',nforestgrowth='+biogrwtext+',initgrowth='+initgrwtext
        vegetationtext = vegstat+',initstomcond='+stomatext+',initrough='+vroughtext+',initsoilcarbon='+slcartext+',initplantcarbon='+pltcartext+',\n'
    if slalbtext == "True":
        soilalbtext = ",soilalbedo="+solalbtext
    else:
        soilalbtext = ''
    if sldpthtext == "True":
        soildepthtext = ",soildepth="+soldpthtext
    else:
        soildepthtext = ''
    if cpsltext == "True":
        soilhcaptext = ",cpsoil="+capsoltext
    else:
        soilhcaptext = ''
    if slwcptext == "True":
        soilwcaptext = ",soilwatercap="+solwcptext
    else:
        soilwcaptext = ''
    if slsattext == "True":
        soilsattext = ",soilsaturation="+solsattext
    else:
        soilsattext = ''
    if snwalbtext == "True":
        snowalbtext = ",snowicealbedo="+snowalbtext
    else:
        snowalbtext = ''
    if mxsnwtext == "True":
        maxsnowtext = ",maxsnow="+maxsnwtext
    else:
        maxsnowtext = ''
    if ocnalbtext == "True":
        oceanalbtext = ",oceanalbedo="+oceanalbtext
    else:
        oceanalbtext = ''
    if mldphtext == "True":
        mixedlyrtext = ",mldepth="+mixldphtext
    else:
        mixedlyrtext = ''
    surfacetext1 = wtsoiltext+soilalbtext+soildepthtext+soilhcaptext+soilwcaptext+soilsattext+snowalbtext
    surfacetext2 = maxsnowtext+',seaice='+sicetext+oceanalbtext+mixedlyrtext+',oceanzenith="'+ocnzntext+'",\n'
    if prssretogtext == "True":
        atmospheretext = "pressure="+pressuretext+','
    else:
        atmospheretext = ''
    if gascontogtext == "True":
        atmospheretext = atmospheretext+'gascon='+gascontext+','
    else:
        atmospheretext = atmospheretext+''
    if drycretext == "True":
        atmospheretext = atmospheretext+'drycore=True,'
    else:
        atmospheretext = atmospheretext+'drycore=False,'
    if ozonetext == "True":
        atmospheretext = atmospheretext+'ozone=True,'
    else:
        atmospheretext = atmospheretext+'ozone=False,'
    if prtlprssretext == "True":
        ppressuretext = "				  pH2="+H2text+',pHe='+Hetext+',pN2='+N2text+',pO2='+O2text+',pAr='+Artext+',pNe='+Netext+',pKr='+Krtext+',pH2O='+H2Otext+',pCO2='+CO2text+',\n'
    else:
        ppressuretext = ''
    if glaciertext == "True":
        glacialtext = "				  glacier={‘toggle’: True, ‘mindepth’: "+mindepthtext+', ‘initialh’: '+initheightext+'},\n'
    else:
        glacialtext = ''
    snapshotext = int(snapshotext)
    if snapshotext > 0:
        snapshotstext = ',snapshots='+snapshotext
    else:
        snapshotstext = ''
    if physics1text == "None":
        physicstext = ''
    elif physics1text == "Cesaro":
        if physics2text == "None":
            physicstext = ''
        elif physics2text == "GP":
            physicstext = ",physicsfilter='gp|cesaro'"
        elif physics2text == "SP":
            physicstext = ",physicsfilter='cesaro|sp'"
        elif physics2text == "GP + SP":
            physicstext = ",physicsfilter='gp|cesaro|sp'"
    elif physics1text == "Exp":
        if physics2text == "None":
            physicstext = ''
        elif physics2text == "GP":
            physicstext = ",physicsfilter='gp|exp'"
        elif physics2text == "SP":
            physicstext = ",physicsfilter='exp|sp'"
        elif physics2text == "GP + SP":
            physicstext = ",physicsfilter='gp|exp|sp'"
    elif physics1text == "Lh":
        if physics2text == "None":
            physicstext = ''
        elif physics2text == "GP":
            physicstext = ",physicsfilter='gp|lh'"
        elif physics2text == "SP":
            physicstext = ",physicsfilter='lh|sp'"
        elif physics2text == "GP + SP":
            physicstext = ",physicsfilter='gp|lh|sp'"
    if stormtext == "True":
        if highcadtext == "True":
            stormstext = ",\n				  stormcapture={'toggle': 1,'NKTRIGGER': 1},highcadence={'toggle': 1,'start': 320,'interval': 4,'end': 576})\n"
        else:
            stormstext = ",\n				  stormcapture={'toggle': 1,'NKTRIGGER': 1})\n"
    else:
        stormstext = ')\n'
    if runtobaltext == "True":
        runtext = nametext+'.runtobalance(threshold='+thresholdtext+',baseline='+baselinetext+',maxyears='+maxyeartext+',minyears='+minyeartext
    else:
        runtext = nametext+'.run(years='+runtimetext

#Formatting
    format_name = "import exoplasim as exo\n"+nametext+' = exo.Model(workdir="'+nametext+'",modelname="'+nametext+'",'
    format_model = "inityear="+yeartext+',outputtype="'+typetext+'",ncpus='+cpustext+',precision='+prestext+',resolution='+resotext+crashtext+',layers='+layertext+recomtext+')\n'
    format_stellar = nametext+".configure(startemp="+startext+',flux='+fluxtext+',\n'
    format_orbit = "				  year="+orbptext+',eccentricity='+eccetext+',obliquity='+oblitext+',lonvernaleq='+lonvtext+',fixedorbit='+fixotext+',\n'
    format_rotation = "				  "+rottext+',\n'
    format_planet = '				  gravity='+gravtext+',radius='+radustext+',orography='+orogtext+',\n'
    format_vegetation = vegetationtext
    format_surface = "				  wetsoil="+surfacetext1+surfacetext2
    format_geography = "				  "+aquaplanetext+dsrtplanetext+landmaptext+topomaptext+'\n'
    format_atmosphere = "				  "+atmospheretext+'\n'
    format_ppressure = ppressuretext
    format_glacier = glacialtext
    format_timekeep = "				  timestep="+timesteptext+',runsteps='+runsteptext+snapshotstext+",otherargs={'NSTPW@plasim_namelist':'"+nsptwtext+"'}"+physicstext
    format_storms = stormstext
    format_export = nametext+".exportcfg()\n"
    format_run = runtext+',crashifbroken='+crashbrkntext+',clean='+cleantext+')\n'
    format_finalise = nametext+'.finalize(allyears='+allyearstext+',keeprestarts='+keeprstrtstext+')\n'
    format_save = nametext+'.save()'
    print("Formatting Complete...")
#Writing to file
    print("Saving Main File...")
    with open(filepath, "w") as output_file:
        output_file.write(format_name)
        output_file.write(format_model)
        output_file.write(format_stellar)
        output_file.write(format_orbit)
        output_file.write(format_rotation)
        output_file.write(format_planet)
        output_file.write(format_vegetation)
        output_file.write(format_surface)
        output_file.write(format_geography)
        output_file.write(format_atmosphere)
        output_file.write(format_ppressure)
        output_file.write(format_glacier)
        output_file.write(format_timekeep)
        output_file.write(format_storms)
        output_file.write(format_export)
        output_file.write(format_run)
        output_file.write(format_finalise)
        output_file.write(format_save)
        print("Saving Complete!")
