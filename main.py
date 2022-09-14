from pathlib import Path
import os
from fastapi import FastAPI, Form,File,UploadFile
from fastapi.responses import FileResponse
import datetime
from docxtpl import DocxTemplate
import textwrap
import re 
from docx.shared import Inches

today = datetime.datetime.today()
today_in_one_week =  today + datetime.timedelta(days=7)
doc = DocxTemplate("./form2revised.docx")

my_app = FastAPI()

@my_app.post("/getInformation")
async def handle_form(name:str=Form(),fathers_name_or_husbands_name:str=Form(),file: UploadFile = File(...),dob:str=Form(),gender:str=Form(),maritalstatus:str=Form(),pf_number:str=Form(),address:str=Form(),name_and_address_of_nominee1:str=Form(None),nominee1_relationship:str=Form(None),dob1:str=Form(None),totalamt_or_share1:str=Form(None),if_nominee1_is_a_minor_mention_guardian_name_and_address:str=Form(None),name_and_address_of_nominee2:str=Form(None),nominee2_relationship:str=Form(None),dob2:str=Form(None),totalamt_or_share2:str=Form(None),if_nominee2_is_a_minor_mention_guardian_name_and_address:str=Form(None),name_and_address_of_nominee3:str=Form(None),nominee3_relationship:str=Form(None),dob3:str=Form(None),totalamt_or_share3:str=Form(None),if_nominee3_is_a_minor_mention_guardian_name_and_address:str=Form(None),name_and_address_of_nominee4:str=Form(None),nominee4_relationship:str=Form(None),dob4:str=Form(None),totalamt_or_share4:str=Form(None),if_nominee4_is_a_minor_mention_guardian_name_and_address:str=Form(None),name_address_of_the_family_member1:str=Form(None),epsdob1:str=Form(None),relationship1_with_member:str=Form(None),name_address_of_the_family_member2:str=Form(None),epsdob2:str=Form(None),name_address_of_the_family_member3:str=Form(None),relationship2_with_member:str=Form(None),name_address_of_the_family_member4:str=Form(None),epsdob3:str=Form(None),epsdob4:str=Form(None),relationship3_with_member:str=Form(None),relationship4_with_member:str=Form(None),name_and_address_of_nominee1_eps:str=Form(None),name_and_address_of_nominee2_eps:str=Form(None),name_and_address_of_nominee3_eps:str=Form(None),dob1epsnominee:str=Form(None),dob2epsnominee:str=Form(None),dob3epsnominee:str=Form(None),relation1:str=Form(None),relation2:str=Form(None),relation3:str=Form(None)):
 file_location = f"{file.filename}"    
 with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())

 context = {
         "name": name,
         "fathers_name_or_husbands_name":fathers_name_or_husbands_name,
         "dob":dob,
         "gender": gender,
         "maritalstatus":maritalstatus,
         "pf_number": pf_number,
         "address":textwrap.fill(address,width=240),
         "name_and_address_of_nominee1":name_and_address_of_nominee1,
         "nominee1_relationship": nominee1_relationship,
         "dob1": dob1,
         "totalamt_or_share1":totalamt_or_share1,
         "if_nominee1_is_a_minor_mention_guardian_name_and_address":if_nominee1_is_a_minor_mention_guardian_name_and_address,
         "name_and_address_of_nominee2": name_and_address_of_nominee2,
         "nominee2_relationship":nominee2_relationship,
         "dob2":dob2,
         "totalamt_or_share2": totalamt_or_share2,
         "if_nominee2_is_a_minor_mention_guardian_name_and_address":if_nominee2_is_a_minor_mention_guardian_name_and_address,
         "name_and_address_of_nominee3":name_and_address_of_nominee3,
         "nominee3_relationship":nominee3_relationship,
         "dob3":dob3,
         "totalamt_or_share3":totalamt_or_share3,
         "if_nominee3_is_a_minor_mention_guardian_name_and_address":if_nominee3_is_a_minor_mention_guardian_name_and_address,
         "name_and_address_of_nominee4": name_and_address_of_nominee4,
         "nominee4_relationship": nominee4_relationship,
         "dob4": dob4,
         "totalamt_or_share4": totalamt_or_share4,
         "if_nominee4_is_a_minor_mention_guardian_name_and_address": if_nominee4_is_a_minor_mention_guardian_name_and_address,
         "name_address_of_the_family_member1":name_address_of_the_family_member1,
         "epsdob1":epsdob1,
         "relationship1_with_member":relationship1_with_member,
         "name_address_of_the_family_member2":name_address_of_the_family_member2,
         "epsdob2":epsdob2,
         "relationship2_with_member":relationship2_with_member,
         "name_address_of_the_family_member3":name_address_of_the_family_member3,
         "epsdob3":epsdob3,
         "relationship3_with_member":relationship3_with_member,
         "name_address_of_the_family_member4":name_address_of_the_family_member4,
         "epsdob4":epsdob4,
         "relationship4_with_member":relationship4_with_member,
         "name_and_address_of_nominee1_eps":name_and_address_of_nominee1_eps,
         "dob1epsnominee":dob1epsnominee,
         "relation1":relation1,
         "name_and_address_of_nominee2_eps":name_and_address_of_nominee2_eps,
         "dob2epsnominee":dob2epsnominee,
         "relation2":relation2,
         "name_and_address_of_nominee3_eps":name_and_address_of_nominee3_eps,
         "dob3epsnominee":dob3epsnominee,
         "relation3":relation3,
         "TODAY": today.strftime("%d-%m-%Y"), 
         "TODAY_IN_ONE_WEEK": today_in_one_week.strftime("%d-%m-%Y"),
     }

 doc.render(context)
 
 img_tag = re.compile(r'%\(signature\)s') # declare pattern
 #STEP 1 
 for _p in enumerate(doc.paragraphs): 
  
  #print(_p[1].text)
  img_paragraph = None
  if bool(img_tag.match(_p[1].text)): 
        
       img_paragraph = _p[1] 
       #print(img_paragraph)
 #STEP 2
       temp_text = img_tag.split(img_paragraph.text)
       print(temp_text)
       img_paragraph.runs[0].text = temp_text[0]
       _r = img_paragraph.add_run()
       _r.add_picture(file_location, width = Inches(1.25))
       img_paragraph.add_run(temp_text[1])
       # p = img_paragraph._element
       # p.getparent().remove(p)
       # p._p = p._element = None 

       
 doc.save(f"./{context['name']}-form2.docx")
 document_path = Path(__file__).parent /f"./{context['name']}-form2.docx"
 os.remove(file_location)
 return FileResponse(path=document_path,filename=f"./{context['name']}-form2.docx")
       


