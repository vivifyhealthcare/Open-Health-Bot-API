from django.shortcuts import render
from .openhealthbot_crud.calendarbycenter import vaccineSlotsbycenterid
from .openhealthbot_crud.calendarbydistrict import vaccineSlotsbydistrictanddate
from .openhealthbot_crud.calendarbypin import vaccineSlotsbypincodeanddate
from .openhealthbot_crud.certificatedownload import CertificateDownload
from .openhealthbot_crud.findbydistrict import vaccineSlotsbydistrict
from .openhealthbot_crud.findbypin import vaccineSlotsbypincode
from .openhealthbot_crud.otp_message import otp_genaration
from .openhealthbot_crud.otp_message import otp_validation
from .openhealthbot_crud.demographics import demographic_genaration
from .openhealthbot_crud.healthBotRegApi import OpenhealthbotRegView
from .openhealthbot_crud.OpenHealth_Intraction_PostApi import OpenHealthInteractionView
from .openhealthbot_crud.Openhealth_Lifestyle_Assessment_Post_API import OpenHealthLifestyleScorePostAPI
from .openhealthbot_crud.OpenHealth_Depression_assessment_post import OpenHealthDepressionPostAPI
from .openhealthbot_crud.Openhealth_Diabetes_assessment_Post import OpenHealthDiabetesPostAPI
from .openhealthbot_crud.Get_Lifestyle_assessment_by_UserId import OpenHealthLifestyleScoringByUserId
from .openhealthbot_crud.GetUserById import GetOpenhealthUser
from .openhealthbot_crud.Get_Depression_By_UserId import OpenHealthDepressionByUserId
from .openhealthbot_crud.Get_Openhealth_Intraction import OpenHealthIntractionByUserId
from .openhealthbot_crud.Get_Diabetes_By_Userid import OpenHealthDiabetesByUserId
from .openhealthbot_crud.Get_openhealthbotAssessment import GetOpenhealthBotAssessmentView
from .openhealthbot_crud.life_style_questions import GetAllQuestionsLifeStyleScoringV2
from .openhealthbot_crud.get_all_questions_diabetes import GetAllQuestionsDiabetesV2
from .openhealthbot_crud.get_all_questions_depression import GetAllQuestionsDepressionV2
from .openhealthbot_crud.No_otp_mobilenumber import getidwithmobilenumber

# Create your views here.
otp_genaration()
otp_validation()
vaccineSlotsbycenterid()
vaccineSlotsbydistrictanddate()
vaccineSlotsbypincodeanddate()
CertificateDownload()
vaccineSlotsbydistrict()
vaccineSlotsbypincode()
demographic_genaration()
OpenhealthbotRegView()
OpenHealthInteractionView()
OpenHealthLifestyleScorePostAPI()
OpenHealthDepressionPostAPI()
OpenHealthDiabetesPostAPI()
OpenHealthLifestyleScoringByUserId()
GetOpenhealthUser()
OpenHealthDepressionByUserId()
OpenHealthIntractionByUserId()
OpenHealthDiabetesByUserId()
GetOpenhealthBotAssessmentView()
GetAllQuestionsLifeStyleScoringV2()
GetAllQuestionsDiabetesV2()
GetAllQuestionsDepressionV2()
getidwithmobilenumber()