from wtforms import StringField, validators, IntegerField, FloatField, SubmitField, SelectField, SelectMultipleField
from schema_forms.form_utilities import SectionForm
from db_dict.patient_history_dict import PatientHistoryDict
from db_dict.common_dict import CommonDict

class PatientHistoryForm(SectionForm):
    # tiyasha : add other demo fields
    fld_med_rec_no = StringField('Medical Record Number') #medical record number is only numbers?shld i put integerfld?
    fld_nam = StringField('Name of the patient')
    fld_id_no = StringField('Identity Number')  #medical record number is only numbers? # difference between idcard and id number?
    fld_fir_vis = IntegerField('Date of first visit')
    fld_perm_add = StringField('Permanent Address')
    fld_curr_add = StringField('Current Address')
    fld_con = IntegerField('Contact Number')
    fld_alt_con = IntegerField('Alternative Contact Number')
    fld_eml = StringField('e-mail id')
    fld_occ = StringField('Occupation')
    fld_gen = StringField('Gender')
    fld_age = StringField('Age (yrs)')
    fld_age_diagnosis = IntegerField('Age at diagnosis (yrs)', [validators.required()]) # current age or age of diagnosis?
    fld_dob = IntegerField('Date Of Birth (DD/MM/YYYY)')
    fld_pob = StringField('Place Of Birth')
    fld_height_cm = FloatField('Height (in cm)', [validators.required()])
    fld_weight_kg = FloatField('Weight (in kg)', [validators.required()])
    fld_diet = SelectField("Diet", choices=PatientHistoryDict.diet_choice)
    fld_diet_other = StringField("Other")
    fld_alcohol = SelectField("Alcohol consumption", choices=CommonDict.yes_no_choice)
    fld_alcohol_other = StringField("Other")
    fld_alcohol_age = StringField("Consumption of alcohol from which age (yrs)")
    fld_alcohol_quant = StringField("Quantity of alcohol consumed per week")
    fld_alcohol_duration = StringField("Duration of alcohol consumption")
    fld_alcohol_comments = StringField("Additional comments for alcohol consumption")
    fld_tobacco = SelectField("Tobacco exposure (Passive and/or Active)", choices=PatientHistoryDict.tobacco_choice)
    fld_tobacco_type_passive = SelectField("Mode of passive consumption",
                                           choices=PatientHistoryDict.tobacco_type_passive_choice)
    fld_tobacco_type_passive_other = StringField("Other")
    fld_tobacco_type_passive_home = StringField("What is the specific source of passive exposure at home",
                                                default='None')
    fld_tobacco_type = SelectMultipleField("Type of tobacco use", choices=PatientHistoryDict.tobacco_type_choice)
    fld_tobacco_type_other = StringField("Other")
    fld_tobacco_age = StringField("Consumption of tobacco from which age (yrs)")
    fld_tobacco_freq = StringField("Frequency of tobacco consumption")
    fld_tobacco_quant = StringField("Quantity of tobacco consumed per week")
    fld_tobacco_duration = StringField("Duration of tobacco consumption")
    fld_tobacco_comments = StringField("Additional comments for tobacco consumption")
    fld_other_del_habits = StringField("Other Deleterious Habits (if present give details)")
    #added
    fld_mar_status = StringField("Marital Status")    #create choice ?
    fld_sib = SelectField("Siblings", choices=Common.Dict.yes_no_choice)
    fld_sib_other = StringField("Other")
    fld_sis = IntegerField('Number of Sisters') #number or name?
    fld_bro = IntegerField('Number Of Brothers')
    fld_child = SelectField("Children", choices=Common.Dict.yes_no_choice)
    fld_child_other = StringField("Other")
    fld_dau = IntegerField('Number of Daugthers')
    fld_son = IntegerField('Number of sons')
    fld_menarche = IntegerField('Age at Menarche')
    fld_period_typ = SelectField("Period Type", choices=Common.Dict.period_type_choice)
    fld_last_date_per = IntegerField('Date of last menstural Period')
    fld_menopausal_status = SelectField("Menopausal Status", choices=Common.Dict.menopausal_status_choice)
    fld_meno_age = IntegerField('Age at Menopause')
    fld_meno_compli = StringField("Complications associated with menopause")
    fld_pregnancy = IntegerField('Pregnancy carried to term')
    fld_preg_compli = StringField("Any complications during pregnancy")
    fld_abort = IntegerField('Number of abortions')
    fld_pregnancy_number = IntegerField('Number of pregnancies')
    fld_age_first_child = IntegerField('Age of first child')
    fld_age_first_pregnancy = IntegerField('Age at first pregnancy')
    fld_age_last_pregnancy = IntegerField('Age at last pregnancy')
    fld_twice_birt_in_year =  StringField("Twice birth in a year(not including twins)")   # is it a yes no question?
    fld_breast_feed = SelectField("Breast feeding", choices=Common.Dict.yes_no_choice)
    #table to be added
#breast feeding detail table
    fld_fertility_treat = SelectField("Fertility Treatment", choices=Common.Dict.yes_no_choice) # do we need to print the comment line attached to this question
    fld_type_fertility_treat = StringField("Type of fertility treatment")
    fld_detail_fertility_treat = StringField("Details of fertility treatments")
    fld_cycles_fertility_treat = StringField("Cycles of fertility treatment")
    fld_success_fertility_treat = SelectField("Success of fertility treatment", choices=Common.Dict.yes_no_choice)
    fld_birth_control = StringField("Type of birth control used")
    fld_detail_birth_control = StringField("Detail of birth control used")
    fld_duration_birth_control = StringField("Duration of birth control used")
    #other medical history table

    #current symptoms table

    fld_curr_comp = SelectField("Current complains detected by", choices=PatientHistoryDict.current_complain_choice)
    fld_duration_curr_comp = StringField("Duration of current complains")


    #tabe to be added
    submit_button = SubmitField('Submit Form')

class PhysicalActivityForm(SectionForm):

    fld_type_phys_act = StringField("Type of physical activity")
    fld_freq_phys_act = StringField("Frequency of physical activity")
    submit_button = SubmitField('Submit Form')

class NutritionalSupplementsForm(SectionForm):

    fld_nut_supplements_type = StringField("Type of nutritional supplements taken")
    fld_nut_supplements_quant = StringField("Quantity of nutritional supplements taken per day")
    fld_nut_supplements_duration = StringField("Duration of nutritional supplements use")
    submit_button = SubmitField('Submit Form')

class MetastasisSymptomsForm(SectionForm):

    fld_bon_pain = SelectField("Bone pain", choices=Common.Dict.yes_no_choice)
    fld_cough = SelectField("Cough", choices=Common.Dict.yes_no_choice)
    fld_jaun = SelectField("Jaundice", choices=Common.Dict.yes_no_choice)
    fld_headache = SelectField("Headache", choices=Common.Dict.yes_no_choice)
    fld_wei_los = SelectField("Weight loss", choices=Common.Dict.yes_no_choice)
    fld_ann_hou_inc = SelectField("Annual house income is", choice=PatientHistoryDict.ann_hou_inc_choice)
    submit_button = SubmitField('Submit Form')

class SymptomsRightBreastDurationForm(SectionForm):

    fld_pain_tender = StringField("Pain or tenderness", default = 'absent')
    fld_lump = StringField("Lumps", default = 'absent')
    fld_nip_dis = StringField("Nipple Discharge", default = 'absent')
    fld_nip_ret = StringField("Nipple retraction", default = 'absent')
    fld_dim = StringField("Dimpling", default = 'absent')
    fld_discol = StringField("Discoloration", default = 'absent')
    fld_ulcer = StringField("ulceration", default = 'absent')
    fld_ecz = StringField("Eczema", default = 'absent')
    submit_button = SubmitField('Submit Form')

class SymptomsLeftBreastDurationForm(SectionForm):

    fld_pain_tender = StringField("Pain or tenderness", default = 'absent')#same fld name?
    fld_lump = StringField("Lumps", default = 'absent')
    fld_nip_dis = StringField("Nipple Discharge", default = 'absent')
    fld_nip_ret = StringField("Nipple retraction", default = 'absent')
    fld_dim = StringField("Dimpling", default = 'absent')
    fld_discol = StringField("Discoloration", default = 'absent')
    fld_ulcer = StringField("ulceration", default = 'absent')
    fld_ecz = StringField("Eczema", default = 'absent')
    submit_button = SubmitField('Submit Form')



