from pyrogram import Client, filters
from arabic_text import *
from english_text import *
from arabic_text2 import *
from english_text2 import *
api_id = "21778505"
api_hash = "07ed814d50863fd4c27440da756ca890"
arabic_commands = ["arabic", "S1", "S2", "chimie1", "videos_chimie1", "courchimie1"]
english_commands = ["english", "S1_", "S2_", "chimie1_", "videos_chimie1_", "courchimie1_"]


bot = Client(
    name="bot",
    api_hash=api_hash,
    api_id=api_id,
    bot_token="6358376034:AAHQ6CzqdxMfrMOYM9vAF9XU_vDb_Lmawq8"
)


@bot.on_message(filters.command(["start"]))
def welcome(client, message):
    chat_id = message.chat.id
    text = Text()
    client.send_message(chat_id, text)
    return


@bot.on_message(filters.command(arabic_commands[0]))  
def arabic_text(client, message):
    chat_id = message.chat.id
    text = arabic_Text()
    client.send_message(chat_id, text)
    return


@bot.on_message(filters.command(arabic_commands[1])) 
def s1_arabic_text(client, message):
    chat_id = message.chat.id
    text = S1_arabic()
    client.send_message(chat_id, text)
    return


@bot.on_message(filters.command(arabic_commands[3]))  
def chimie1_text(client, message):
    chat_id = message.chat.id
    text = chimie1()
    client.send_message(chat_id, text)
    return


@bot.on_message(filters.command(arabic_commands[4])) 
def videos_text_chimie1(client, message):
    chat_id = message.chat.id
    text = videos_chimie1()
    client.send_message(chat_id, text)
    return


@bot.on_message(filters.command(arabic_commands[5]))  
def courchimie1_text(client, message):
    chat_id = message.chat.id
    text = courchimie1()
    client.send_message(chat_id, text)
    return


@bot.on_message(filters.command(["Radioactivity"])) 
def send_cour2_pdf(client, message):
    chat_id = message.chat.id
    pdf_path = "cour1.pdf"
    client.send_document(chat_id, pdf_path)
    return


@bot.on_message(filters.command(["Model_de_bohr"])) 
def send_cour3_pdf(client, message):
    chat_id = message.chat.id
    pdf_path = "cour2.pdf"
    client.send_document(chat_id, pdf_path)
    return


@bot.on_message(filters.command(["Effet_photoelectrique"]))
def send_cour4_pdf(client, message):
    chat_id = message.chat.id
    pdf_path = "cour3.pdf"
    client.send_document(chat_id, pdf_path)
    return

@bot.on_message(filters.command(["Tableau_périodique"]))
def send_cour5_pdf(client, message):
    chat_id = message.chat.id
    pdf_path = "cour4.pdf"
    client.send_document(chat_id, pdf_path)
    return

@bot.on_message(filters.command(["exercice_chimie1"]))
def send_cour_chimie1(client, message):
    chat_id = message.chat.id
    pdf_path = "exercice_chimie1.pdf"
    client.send_document(chat_id, pdf_path)
    return

@bot.on_message(filters.command("examen_chimie1"))
def examenchimie1_text(client, message):
    chat_id = message.chat.id
    text = "https://drive.google.com/drive/folders/1zShoSNWTCuNNSbDX-Xu7A5D-L_1E06dy?usp=drive_link"
    client.send_message(chat_id, text)
    return
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
@bot.on_message(filters.command("math1"))
def math1_text(client, message):
    chat_id = message.chat.id
    text = math1()
    client.send_message(chat_id, text)
    return


@bot.on_message(filters.command("videos_math1"))
def videos_text_math1(client, message):
    chat_id = message.chat.id
    text = videos_math1()
    client.send_message(chat_id, text)
    return


@bot.on_message(filters.command("cour_math1"))
def courmath1_text(client, message):
    chat_id = message.chat.id
    text = courmath1()
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command(["les_relation"]))
def send_cour_relation(client, message):
    chat_id = message.chat.id
    pdf_path = "Relations.pdf"
    client.send_document(chat_id, pdf_path)
    return

@bot.on_message(filters.command(["les_application"]))
def send_cour_application(client, message):
    chat_id = message.chat.id
    pdf_path = "Applications1.pdf"
    pdf_path1="Applications2.pdf"
    client.send_document(chat_id, pdf_path)
    client.send_document(chat_id, pdf_path1)
    return


@bot.on_message(filters.command(["les_fonction"]))
def send_cour_les_fonction(client, message):
    chat_id = message.chat.id
    pdf_path = "Généralités.pdf"
    pdf_path1 = "Limite_d_une _onction.pdf"
    client.send_document(chat_id, pdf_path)
    client.send_document(chat_id, pdf_path1)
    return

@bot.on_message(filters.command(["exo_les_relation"]))
def send_exo_relation(client, message):
    chat_id = message.chat.id
    pdf_path = "exercice_les_relation1.pdf"
    client.send_document(chat_id, pdf_path)
    return

@bot.on_message(filters.command(["exo_les_application"]))
def send_exo_application(client, message):
    chat_id = message.chat.id
    pdf_path = "exercice_les_application.pdf"
    client.send_document(chat_id, pdf_path)
    return

@bot.on_message(filters.command(["exo_fonction"]))
def send_exo_fonction(client, message):
    chat_id = message.chat.id
    pdf_path = "Exo_Domaine_de_définition.pdf"
    client.send_document(chat_id, pdf_path)
    return

@bot.on_message(filters.command(["exo_limites"]))
def send_exo_limites(client, message):
    chat_id = message.chat.id
    pdf_path = "Exo_Limites.pdf"
    pdf_path1="serie4.jpg"
    pdf_path2="corrige_serie4.pdf"
    client.send_document(chat_id, pdf_path)
    client.send_document(chat_id, pdf_path1)
    client.send_document(chat_id, pdf_path2)
    return

@bot.on_message(filters.command("exercice_math1"))
def exomath1_text(client, message):
    chat_id = message.chat.id
    text = exo_math1()
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command("examen_math1"))
def examenmath1_text(client, message):
    chat_id = message.chat.id
    text = "https://drive.google.com/drive/folders/1ex__lcQxz-3zs9taURNMMNGEXYmsNzN-?usp=drive_link"
    client.send_message(chat_id, text)
    return
#///////////////////////////////////////////////////////////////////////////////////////////////////////////


@bot.on_message(filters.command("physique1"))
def phy1_text(client, message):
    chat_id = message.chat.id
    text = phy1()
    client.send_message(chat_id, text)
    return


@bot.on_message(filters.command("videos_phy1"))
def videos_text_phy1(client, message):
    chat_id = message.chat.id
    text = videos_phy1()
    client.send_message(chat_id, text)
    return


@bot.on_message(filters.command("cour_phy1"))
def courphy1_text(client, message):
    chat_id = message.chat.id
    text = courphy1()
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command(["Rappel_mathamatique"]))
def send_cour_Rappel_mathamatique(client, message):
    chat_id = message.chat.id
    pdf_path = "chap1_phy.pdf"
    
    client.send_document(chat_id, pdf_path)
    return

@bot.on_message(filters.command(["Cinematique"]))
def send_cour_cinematique(client, message):
    chat_id = message.chat.id
    pdf_path = "Cinemat_partie1.pdf"
    pdf_path1 = "cinemat_partie2.pdf"
    pdf_path2 = "cinemat_partie3.pdf"
    client.send_document(chat_id, pdf_path)
    client.send_document(chat_id, pdf_path1)
    client.send_document(chat_id, pdf_path2)
    return

@bot.on_message(filters.command(["Dynamique"]))
def send_cour_dynamique(client, message):
    chat_id = message.chat.id
    pdf_path = "Dynam.pdf"
    
    client.send_document(chat_id, pdf_path)
    return


@bot.on_message(filters.command(["Travel_et_energie"]))
def send_cour_travel_et_energie(client, message):
    chat_id = message.chat.id
    pdf_path = "Trav_Energ.pdf"
    
    client.send_document(chat_id, pdf_path)
    
    return

@bot.on_message(filters.command("exercice_phy1"))
def exophy1_text(client, message):
    chat_id = message.chat.id
    text = exo_phy1()
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command(["exo_rappels_mathematique"]))
def send_exo_rappels_mathematique(client, message):
    chat_id = message.chat.id
    pdf_path = "serie1.jpg"
    pdf_path1 ="corrige_serie1.pdf"
    client.send_document(chat_id, pdf_path)
    client.send_document(chat_id, pdf_path1)
    return

@bot.on_message(filters.command(["exo_cinematique"]))
def send_exo_cinematique(client, message):
    chat_id = message.chat.id
    pdf_path = "serie2.pdf"
    pdf_path1 ="corrige_serie2.pdf"
    client.send_document(chat_id, pdf_path)
    client.send_document(chat_id, pdf_path1)
    return

@bot.on_message(filters.command(["exo_dynamique"]))
def send_exo_dynamique(client, message):
    chat_id = message.chat.id
    pdf_path = "serie3.pdf"
    pdf_path1 ="corrige_serie3.pdf"
    client.send_document(chat_id, pdf_path)
    client.send_document(chat_id, pdf_path1)
    return

@bot.on_message(filters.command(["exo_travel_et_energie"]))
def send_exo_travel_et_energie(client, message):
    chat_id = message.chat.id
    pdf_path = "serie4+corrige_serie4.pdf"
    
    client.send_document(chat_id, pdf_path)
    
    return

@bot.on_message(filters.command("examen_phy1"))
def examenphy1_text(client, message):
    chat_id = message.chat.id
    text = "https://drive.google.com/drive/folders/1EUElvYz7K0uL0qFriPU4KaSdo1QZpbv_?usp=drive_link"
    client.send_message(chat_id, text)
    return

#////////////////////////////////////////////////////////////////////////////////////////////////////////////
@bot.on_message(filters.command("informatique1"))
def info1_text(client, message):
    chat_id = message.chat.id
    text = info1_()
    client.send_message(chat_id, text)
    return


@bot.on_message(filters.command("videos_info1"))
def videos_text_phy1(client, message):
    chat_id = message.chat.id
    text = videos_info1()
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command("cour_info1"))
def courinfo1_text(client, message):
    chat_id = message.chat.id
    text = courinfo1()
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command(["intro_info_syst_num"]))
def send_cour_info1_chap1(client, message):
    chat_id = message.chat.id
    pdf_path = "chap1_info1.pdf"
    
    client.send_document(chat_id, pdf_path)
    return

@bot.on_message(filters.command(["codage_info"]))
def send_cour_info1_chap2(client, message):
    chat_id = message.chat.id
    pdf_path = "cour_chap2_info1.pdf"
    
    client.send_document(chat_id, pdf_path)
    return

@bot.on_message(filters.command(["algorithme1"]))
def send_cour_info1_chap3(client, message):
    chat_id = message.chat.id
    pdf_path = "cour_chap3_info1.pdf"
    
    client.send_document(chat_id, pdf_path)
    return

@bot.on_message(filters.command("exercice_info1"))
def exoinfo1_text(client, message):
    chat_id = message.chat.id
    text = exo_info1()
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command(["exo_codage_information"]))
def send_exo_info1_chap2(client, message):
    chat_id = message.chat.id
    pdf_path = "exo_chap2_info1.pdf"
    
    client.send_document(chat_id, pdf_path)
    
    return

@bot.on_message(filters.command(["exo_algorithme1"]))
def send_exo_info1_chap3(client, message):
    chat_id = message.chat.id
    pdf_path = "exo_chap3_info1.pdf"
    
    client.send_document(chat_id, pdf_path)
    
    return

@bot.on_message(filters.command("examen_info1"))
def exameninfo1_text(client, message):
    chat_id = message.chat.id
    text = "https://drive.google.com/drive/folders/14xQzYjFSlvxYtpRxZNeEOnu-8LOhTbHx?usp=drive_link"
    client.send_message(chat_id, text)
    return
#///////////////////////////////////////////////////////////////////////////////////////////////
@bot.on_message(filters.command("methode1"))
def method1_text(client, message):
    chat_id = message.chat.id
    text = method1()
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command(["cour_method1"]))
def send_cour_method1(client, message):
    chat_id = message.chat.id
    pdf_path = "Methodologie_de_la_redaction.docx"
    pdf_path1="lexpression_orale.docx"
    
    client.send_document(chat_id, pdf_path)
    client.send_document(chat_id, pdf_path1)

    
    return

@bot.on_message(filters.command(["examen_method1"]))
def send_examen_method1(client, message):
    chat_id = message.chat.id
    pdf_path = "examen_method.pdf"
    
    client.send_document(chat_id, pdf_path)
    
    return

@bot.on_message(filters.command("mst1"))
def mst1_text(client, message):
    chat_id = message.chat.id
    text = mst1()
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command(["cour_mst1"]))
def send_cour_mst1(client, message):
    chat_id = message.chat.id
    pdf_path = "cour_mst1.pdf"
    
    
    client.send_document(chat_id, pdf_path)
    
    
    return

@bot.on_message(filters.command(["examen_mst1"]))
def send_examen_mst1(client, message):
    chat_id = message.chat.id
    pdf_path = "examen_mst1.pdf"
    
    client.send_document(chat_id, pdf_path)
    
    return

@bot.on_message(filters.command("frnc1"))
def frnc_text(client, message):
    chat_id = message.chat.id
    text = frnc1()
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command(["cour_frnc1"]))
def send_cour_franc1(client, message):
    chat_id = message.chat.id
    pdf_path = "cour_francais_1.pdf"
    
    
    client.send_document(chat_id, pdf_path)
    
    
    return

@bot.on_message(filters.command("english1"))
def english1_text(client, message):
    chat_id = message.chat.id
    text = english1()
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command(["cour_english1"]))
def send_cour_english1(client, message):
    chat_id = message.chat.id
    pdf_path = "cour_english1.pdf"
    
    
    client.send_document(chat_id, pdf_path)
    
    
    return

@bot.on_message(filters.command("examen_english1"))
def examenenglish1_text(client, message):
    chat_id = message.chat.id
    text = "https://drive.google.com/drive/folders/1TEHHWTMFvI-W63qFOhI1rOYnXuBaAL1D"
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command(english_commands[0]))
def english_text(client, message):
    chat_id = message.chat.id
    text = english_Text()
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command(english_commands[1]))
def s1_english_text(client, message):
    chat_id = message.chat.id
    text = S1_english()
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command(english_commands[3]))
def chimie1_text_(client, message):
    chat_id = message.chat.id
    text = chimie1_()
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command(english_commands[4]))
def videos_text_chimie1_(client, message):
    chat_id = message.chat.id
    text = videos_chimie1_()
    client.send_message(chat_id, text)
    return


@bot.on_message(filters.command(english_commands[5]))
def courchimie1_text_(client, message):
    chat_id = message.chat.id
    text = courchimie1_()
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command(["Radioactivity_"]))
def send_cour2_pdf_(client, message):
    chat_id = message.chat.id
    pdf_path = "cour1.pdf"
    client.send_document(chat_id, pdf_path)
    return

@bot.on_message(filters.command(["Model_de_bohr_"]))
def send_cour3_pdf_(client, message):
    chat_id = message.chat.id
    pdf_path = "cour2.pdf"
    client.send_document(chat_id, pdf_path)
    return

@bot.on_message(filters.command(["Effet_photoelectrique_"]))
def send_cour4_pdf_(client, message):
    chat_id = message.chat.id
    pdf_path = "cour3.pdf"
    client.send_document(chat_id, pdf_path)
    return

@bot.on_message(filters.command(["Tableau_périodique_"]))
def send_cour5_pdf_(client, message):
    chat_id = message.chat.id
    pdf_path = "cour4.pdf"
    client.send_document(chat_id, pdf_path)
    return

@bot.on_message(filters.command(["exercice_chimie1_"]))
def send_cour_chimie1_(client, message):
    chat_id = message.chat.id
    pdf_path = "exercice_chimie1.pdf"
    client.send_document(chat_id, pdf_path)
    return

@bot.on_message(filters.command("examen_chimie1_"))
def examenchimie1_text_(client, message):
    chat_id = message.chat.id
    text = "https://drive.google.com/drive/folders/1zShoSNWTCuNNSbDX-Xu7A5D-L_1E06dy?usp=drive_link"
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command("math1_"))
def math1_text_(client, message):
    chat_id = message.chat.id
    text = math1_()
    client.send_message(chat_id, text)
    return


@bot.on_message(filters.command("videos_math1_"))
def videos_text_math1_(client, message):
    chat_id = message.chat.id
    text = videos_math1_()
    client.send_message(chat_id, text)
    return


@bot.on_message(filters.command("cour_math1_"))
def courmath1_text_(client, message):
    chat_id = message.chat.id
    text = courmath1_()
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command(["les_relation_"]))
def send_cour_relation_(client, message):
    chat_id = message.chat.id
    pdf_path = "Relations.pdf"
    client.send_document(chat_id, pdf_path)
    return

@bot.on_message(filters.command(["les_application_"]))
def send_cour_application_(client, message):
    chat_id = message.chat.id
    pdf_path = "Applications1.pdf"
    pdf_path1="Applications2.pdf"
    client.send_document(chat_id, pdf_path)
    client.send_document(chat_id, pdf_path1)
    return


@bot.on_message(filters.command(["les_fonction_"]))
def send_cour_les_fonction_(client, message):
    chat_id = message.chat.id
    pdf_path = "Généralités.pdf"
    pdf_path1 = "Limite_d_une _onction.pdf"
    client.send_document(chat_id, pdf_path)
    client.send_document(chat_id, pdf_path1)
    return

@bot.on_message(filters.command(["exo_les_relation_"]))
def send_exo_relation_(client, message):
    chat_id = message.chat.id
    pdf_path = "exercice_les_relation1.pdf"
    client.send_document(chat_id, pdf_path)
    return

@bot.on_message(filters.command(["exo_les_application_"]))
def send_exo_application_(client, message):
    chat_id = message.chat.id
    pdf_path = "exercice_les_application.pdf"
    client.send_document(chat_id, pdf_path)
    return

@bot.on_message(filters.command(["exo_fonction_"]))
def send_exo_fonction_(client, message):
    chat_id = message.chat.id
    pdf_path = "Exo_Domaine_de_définition.pdf"
    client.send_document(chat_id, pdf_path)
    return

@bot.on_message(filters.command(["exo_limites_"]))
def send_exo_limites_(client, message):
    chat_id = message.chat.id
    pdf_path = "Exo_Limites.pdf"
    pdf_path1="serie4.jpg"
    pdf_path2="corrige_serie4.pdf"
    client.send_document(chat_id, pdf_path)
    client.send_document(chat_id, pdf_path1)
    client.send_document(chat_id, pdf_path2)
    return

@bot.on_message(filters.command("exercice_math1_"))
def exomath1_text_(client, message):
    chat_id = message.chat.id
    text = exo_math1_()
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command("examen_math1_"))
def examenmath1_text_(client, message):
    chat_id = message.chat.id
    text = "https://drive.google.com/drive/folders/1ex__lcQxz-3zs9taURNMMNGEXYmsNzN-?usp=drive_link"
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command("physique1_"))
def phy1_text_(client, message):
    chat_id = message.chat.id
    text = phy1_()
    client.send_message(chat_id, text)
    return


@bot.on_message(filters.command("videos_phy1_"))
def videos_text_phy1_(client, message):
    chat_id = message.chat.id
    text = videos_phy1_()
    client.send_message(chat_id, text)
    return


@bot.on_message(filters.command("cour_phy1_"))
def courphy1_text_(client, message):
    chat_id = message.chat.id
    text = courphy1_()
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command(["Rappel_mathamatique_"]))
def send_cour_Rappel_mathamatique_(client, message):
    chat_id = message.chat.id
    pdf_path = "chap1_phy.pdf"
    
    client.send_document(chat_id, pdf_path)
    return

@bot.on_message(filters.command(["Cinematique_"]))
def send_cour_cinematique_(client, message):
    chat_id = message.chat.id
    pdf_path = "Cinemat_partie1.pdf"
    pdf_path1 = "cinemat_partie2.pdf"
    pdf_path2 = "cinemat_partie3.pdf"
    client.send_document(chat_id, pdf_path)
    client.send_document(chat_id, pdf_path1)
    client.send_document(chat_id, pdf_path2)
    return

@bot.on_message(filters.command(["Dynamique_"]))
def send_cour_dynamique_(client, message):
    chat_id = message.chat.id
    pdf_path = "Dynam.pdf"
    
    client.send_document(chat_id, pdf_path)
    return


@bot.on_message(filters.command(["Travel_et_energie_"]))
def send_cour_travel_et_energie_(client, message):
    chat_id = message.chat.id
    pdf_path = "Trav_Energ.pdf"
    
    client.send_document(chat_id, pdf_path)
    
    return

@bot.on_message(filters.command("exercice_phy1_"))
def exophy1_text_(client, message):
    chat_id = message.chat.id
    text = exo_phy1_()
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command(["exo_rappels_mathematique_"]))
def send_exo_rappels_mathematique_(client, message):
    chat_id = message.chat.id
    pdf_path = "serie1.jpg"
    pdf_path1 ="corrige_serie1.pdf"
    client.send_document(chat_id, pdf_path)
    client.send_document(chat_id, pdf_path1)
    return

@bot.on_message(filters.command(["exo_cinematique_"]))
def send_exo_cinematique_(client, message):
    chat_id = message.chat.id
    pdf_path = "serie2.pdf"
    pdf_path1 ="corrige_serie2.pdf"
    client.send_document(chat_id, pdf_path)
    client.send_document(chat_id, pdf_path1)
    return

@bot.on_message(filters.command(["exo_dynamique_"]))
def send_exo_dynamique_(client, message):
    chat_id = message.chat.id
    pdf_path = "serie3.pdf"
    pdf_path1 ="corrige_serie3.pdf"
    client.send_document(chat_id, pdf_path)
    client.send_document(chat_id, pdf_path1)
    return

@bot.on_message(filters.command(["exo_travel_et_energie_"]))
def send_exo_travel_et_energie_(client, message):
    chat_id = message.chat.id
    pdf_path = "serie4+corrige_serie4.pdf"
    
    client.send_document(chat_id, pdf_path)
    
    return

@bot.on_message(filters.command("examen_phy1_"))
def examenphy1_text_(client, message):
    chat_id = message.chat.id
    text = "https://drive.google.com/drive/folders/1EUElvYz7K0uL0qFriPU4KaSdo1QZpbv_?usp=drive_link"
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command("informatique1_"))
def info1_text_(client, message):
    chat_id = message.chat.id
    text = info1_()
    client.send_message(chat_id, text)
    return


@bot.on_message(filters.command("videos_info1_"))
def videos_text_phy1_(client, message):
    chat_id = message.chat.id
    text = videos_info1_()
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command("cour_info1_"))
def courinfo1_text_(client, message):
    chat_id = message.chat.id
    text = courinfo1_()
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command(["intro_info_syst_num_"]))
def send_cour_info1_chap1_(client, message):
    chat_id = message.chat.id
    pdf_path = "chap1_info1.pdf"
    
    client.send_document(chat_id, pdf_path)
    return

@bot.on_message(filters.command(["codage_info_"]))
def send_cour_info1_chap2_(client, message):
    chat_id = message.chat.id
    pdf_path = "cour_chap2_info1.pdf"
    
    client.send_document(chat_id, pdf_path)
    return

@bot.on_message(filters.command(["algorithme1_"]))
def send_cour_info1_chap3_(client, message):
    chat_id = message.chat.id
    pdf_path = "cour_chap3_info1.pdf"
    
    client.send_document(chat_id, pdf_path)
    return

@bot.on_message(filters.command("exercice_info1_"))
def exoinfo1_text_(client, message):
    chat_id = message.chat.id
    text = exo_info1_()
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command(["exo_codage_information_"]))
def send_exo_info1_chap2_(client, message):
    chat_id = message.chat.id
    pdf_path = "exo_chap2_info1.pdf"
    
    client.send_document(chat_id, pdf_path)
    
    return

@bot.on_message(filters.command(["exo_algorithme1_"]))
def send_exo_info1_chap3_(client, message):
    chat_id = message.chat.id
    pdf_path = "exo_chap3_info1.pdf"
    
    client.send_document(chat_id, pdf_path)
    
    return

@bot.on_message(filters.command("examen_info1_"))
def exameninfo1_text_(client, message):
    chat_id = message.chat.id
    text = "https://drive.google.com/drive/folders/14xQzYjFSlvxYtpRxZNeEOnu-8LOhTbHx?usp=drive_link"
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command("methode1_"))
def method1_text_(client, message):
    chat_id = message.chat.id
    text = method1_()
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command(["cour_method1_"]))
def send_cour_method1_(client, message):
    chat_id = message.chat.id
    pdf_path = "Methodologie_de_la_redaction.docx"
    pdf_path1="lexpression_orale.docx"
    
    client.send_document(chat_id, pdf_path)
    client.send_document(chat_id, pdf_path1)

    
    return

@bot.on_message(filters.command(["examen_method1_"]))
def send_examen_method1_(client, message):
    chat_id = message.chat.id
    pdf_path = "examen_method.pdf"
    
    client.send_document(chat_id, pdf_path)
    
    return

@bot.on_message(filters.command("mst1_"))
def mst1_text_(client, message):
    chat_id = message.chat.id
    text = mst1_()
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command(["cour_mst1_"]))
def send_cour_mst1_(client, message):
    chat_id = message.chat.id
    pdf_path = "cour_mst1.pdf"
    
    
    client.send_document(chat_id, pdf_path)
    
    
    return

@bot.on_message(filters.command(["examen_mst1_"]))
def send_examen_mst1_(client, message):
    chat_id = message.chat.id
    pdf_path = "examen_mst1.pdf"
    
    client.send_document(chat_id, pdf_path)
    
    return

@bot.on_message(filters.command("frnc1_"))
def frnc_text_(client, message):
    chat_id = message.chat.id
    text = frnc1_()
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command(["cour_frnc1_"]))
def send_cour_franc1_(client, message):
    chat_id = message.chat.id
    pdf_path = "cour_francais_1.pdf"
    
    
    client.send_document(chat_id, pdf_path)
    
    
    return

@bot.on_message(filters.command("english1_"))
def english1_text_(client, message):
    chat_id = message.chat.id
    text = english1_()
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command(["cour_english1"]))
def send_cour_english1_(client, message):
    chat_id = message.chat.id
    pdf_path = "cour_english1.pdf"
    
    
    client.send_document(chat_id, pdf_path)
    
    
    return

@bot.on_message(filters.command("examen_english1_"))
def examenenglish1_text_(client, message):
    chat_id = message.chat.id
    text = "https://drive.google.com/drive/folders/1TEHHWTMFvI-W63qFOhI1rOYnXuBaAL1D"
    client.send_message(chat_id, text)
    return

#///////////////////////////////////////////////////////////////////////////////////////////
@bot.on_message(filters.command(arabic_commands[2])) 
def s2_arabic_text(client, message):
    chat_id = message.chat.id
    text = S2_arabic()
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command("chimie2"))  
def chimie2_text(client, message):
    chat_id = message.chat.id
    text = chimie2()
    client.send_message(chat_id, text)
    return


@bot.on_message(filters.command("videos_chimie2")) 
def videos_text_chimie2(client, message):
    chat_id = message.chat.id
    text = videos_chimie2()
    client.send_message(chat_id, text)
    return


@bot.on_message(filters.command("cour_chimie2"))  
def courchimie2_text(client, message):
    chat_id = message.chat.id
    text = courchimie2()
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command(["Introductions_sur_la_thermodynamique"])) 
def send_cour1_chimie2(client, message):
    chat_id = message.chat.id
    pdf_path = "Introductions_sur_la_thermodynamique.pdf"
    client.send_document(chat_id, pdf_path)
    return

@bot.on_message(filters.command(["Calorimetre"]))
def send_cour2_chimie2(client, message):
    chat_id = message.chat.id
    pdf_path = "calorimetre.pdf"
    client.send_document(chat_id, pdf_path)
    return



@bot.on_message(filters.command(["1er_principe"])) 
def send_cour3_shimie2(client, message):
    chat_id = message.chat.id
    pdf_path = "1er_principe.pdf"
    client.send_document(chat_id, pdf_path)
    return


@bot.on_message(filters.command(["Thermochimie"]))
def send_cour4_chimie2(client, message):
    chat_id = message.chat.id
    pdf_path = "thermochimie.pdf"
    client.send_document(chat_id, pdf_path)
    return

@bot.on_message(filters.command(["2eme_principe"]))
def send_cour5_chimie2(client, message):
    chat_id = message.chat.id
    text = "غير موجود حاليا " 
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command("exercice_chimie2"))
def exochimie2_text_(client, message):
    chat_id = message.chat.id
    text = exo_chimie2()
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command(["exo_Introductions_sur_la_thermodynamique"]))
def send_exo_Introductions_sur_la_thermodynamique(client, message):
    chat_id = message.chat.id
    pdf_path = "chmie2_serie_1.pdf"
    pdf_path1 ="chmie2_corrige_serie1.pdf"
    client.send_document(chat_id, pdf_path)
    client.send_document(chat_id, pdf_path1)
    return

@bot.on_message(filters.command(["exo_Calorimetre"]))
def send_exo_Calorimetre(client, message):
    chat_id = message.chat.id
    pdf_path = "chimie2_corrige_serie2+serie2.pdf"
    client.send_document(chat_id, pdf_path)
    
    return

@bot.on_message(filters.command(["exo_1er_principe"]))
def send_exo_1er_principe(client, message):
    chat_id = message.chat.id
    pdf_path = "Chimie2_Corrige_serie_n3.pdf"
    pdf_path1 ="chimie2_serie_n3.pdf"
    client.send_document(chat_id, pdf_path1)
    client.send_document(chat_id, pdf_path)
    return

@bot.on_message(filters.command(["exo_Thermochimie"]))
def send_exo_Thermochimie(client, message):
    chat_id = message.chat.id
    pdf_path = "chimie2_corrige_serie4+serie4.pdf"
    
    client.send_document(chat_id, pdf_path)
    
    return

@bot.on_message(filters.command("exo_2eme_principe"))
def send_exo_2eme_principe(client, message):
    chat_id = message.chat.id
    text = "غير موجود حاليا " 
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command("examen_chimie2"))
def examen_chimie2_text(client, message):
    chat_id = message.chat.id
    text = "https://drive.google.com/drive/folders/14z3lMTAAiQ2DsLFsBD_NKj3zvkgkeHPQ?usp=drive_link"
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command("math2"))  
def math2_text(client, message):
    chat_id = message.chat.id
    text = math2()
    client.send_message(chat_id, text)
    return


@bot.on_message(filters.command("videos_math2")) 
def videos_text_math2(client, message):
    chat_id = message.chat.id
    text = "غير موجود حاليا"
    client.send_message(chat_id, text)
    return


@bot.on_message(filters.command("cour_math2"))  
def courmath2_text(client, message):
    chat_id = message.chat.id
    text=cour_math2()
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command(["DL"])) 
def send_cour1_math2(client, message):
    chat_id = message.chat.id
    pdf_path = "cour_dl_1.pdf"
    pdf_path2 = "cour_dl_2.pdf"
    client.send_document(chat_id, pdf_path)
    client.send_document(chat_id, pdf_path2)
    return

@bot.on_message(filters.command(["matrice"]))
def send_cour2_math2(client, message):
    chat_id = message.chat.id
    pdf_path = "cour_matrice_1.pdf"
    pdf_path1 = "cour_matrice_2.pdf"
    pdf_path2 = "cour_matrice_3.pdf"
    pdf_path3 = "cour_matrice_4.pdf"
    pdf_path4 = "cour_matrice_5.pdf"
    client.send_document(chat_id, pdf_path)
    client.send_document(chat_id, pdf_path1)
    client.send_document(chat_id, pdf_path2)
    client.send_document(chat_id, pdf_path3)
    client.send_document(chat_id, pdf_path4)
    return



@bot.on_message(filters.command(["integrals"])) 
def send_cour3_math2(client, message):
    chat_id = message.chat.id
    text = "غير موجود حاليا "
    client.send_message(chat_id, text)
    return


@bot.on_message(filters.command(["Les_equations_differentielles"]))
def send_cour4_math2(client, message):
    chat_id = message.chat.id
    text = "غير موجود حاليا "
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command("exercice_math2"))
def exomath2_text_(client, message):
    chat_id = message.chat.id
    text = exo_math2()
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command(["exo_DL"]))
def send_exo_dl(client, message):
    chat_id = message.chat.id
    pdf_path = "exo_dl.pdf"
    client.send_document(chat_id, pdf_path)
    return

@bot.on_message(filters.command(["exo_matrice"]))
def send_exo_matrice(client, message):
    chat_id = message.chat.id
    pdf_path = "corrige_serie3_matrice.pdf"
    pdf_path1 = "serie3_matrice.pdf"
    client.send_document(chat_id, pdf_path1)
    client.send_document(chat_id, pdf_path)
    
    return

@bot.on_message(filters.command(["exo_integral"]))
def send_exo_integral(client, message):
    chat_id = message.chat.id
    pdf_path = "math2_serie4.pdf"
    pdf_path1 ="corrige1_serie4_math2.pdf"
    pdf_path2 ="corrige2_serie4_math2.pdf"
    client.send_document(chat_id, pdf_path)
    client.send_document(chat_id, pdf_path1)
    client.send_document(chat_id, pdf_path2)
    return

@bot.on_message(filters.command(["exo_les_equa_def"]))
def send_exo_Les_equations_differentielles(client, message):
    chat_id = message.chat.id
    text = "غير موجود حاليا "
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command("examen_math2"))
def examen_math2_text(client, message):
    chat_id = message.chat.id
    text = "https://drive.google.com/drive/folders/1ks1ORQJubkdFgrFiKEkoCShXGBicOLs2?usp=drive_link"
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command("physique2"))  
def phy2_text(client, message):
    chat_id = message.chat.id
    text = phy2()
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command("videos_phy2")) 
def videos_text_phy2(client, message):
    chat_id = message.chat.id
    text = videos_phy2()
    client.send_message(chat_id, text)
    return



@bot.on_message(filters.command("cour_phy2"))  
def courphy2_text(client, message):
    chat_id = message.chat.id
    text=cour_phy2()
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command(["electrique_field"]))
def send_cour1_phy2(client, message):
    chat_id = message.chat.id
    pdf_path = "chap1_phy2_1.pdf"
    pdf_path1 ="chap1_phy2_2.pdf"
    pdf_path2 ="chap1_phy2_3.pdf"
    client.send_document(chat_id, pdf_path)
    client.send_document(chat_id, pdf_path1)
    client.send_document(chat_id, pdf_path2)
    return

@bot.on_message(filters.command(["conducteur"]))
def send_cour_conducteur(client, message):
    chat_id = message.chat.id
    pdf_path = "chap2_phy2.pdf"
    
    client.send_document(chat_id, pdf_path)
    
    return

@bot.on_message(filters.command(["electrosinetique"]))
def send_cour_electrosinetique(client, message):
    chat_id = message.chat.id
    pdf_path = "chap3_phy2.pdf"
    
    client.send_document(chat_id, pdf_path)
    
    return

@bot.on_message(filters.command("exercice_phy2"))
def exophy2_text_(client, message):
    chat_id = message.chat.id
    text = exo_phy2()
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command(["exo_electrique_field"]))
def send_exo_electrique_field(client, message):
    chat_id = message.chat.id
    pdf_path = "exo_chap1_phy2.pdf"
    
    client.send_document(chat_id, pdf_path)
    
    return

@bot.on_message(filters.command(["exo_conducteur"]))
def send_exo_conducteur(client, message):
    chat_id = message.chat.id
    pdf_path = "exo_chap2_phy2.pdf"
    
    client.send_document(chat_id, pdf_path)
    
    return

@bot.on_message(filters.command(["exo_electrosinetique"]))
def send_exo_electrosinetique(client, message):
    chat_id = message.chat.id
    pdf_path = "exo_chap3_phy2.pdf"
    
    client.send_document(chat_id, pdf_path)
    
    return

@bot.on_message(filters.command("examen_phy2"))
def examen_phy2_text(client, message):
    chat_id = message.chat.id
    text = "https://drive.google.com/drive/folders/1TktjtVzUpb0GtDMLOAvUY9v5V7QDcSIh?usp=drive_link"
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command("informatique2"))  
def info2_text(client, message):
    chat_id = message.chat.id
    text = info2()
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command("videos_info2")) 
def videos_text_info2(client, message):
    chat_id = message.chat.id
    text = videos_info2()
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command("cour_info2")) 
def cour_info2(client, message):
    chat_id = message.chat.id
    text = "لا تحتاج دروس"
    client.send_message(chat_id, text)
    return


@bot.on_message(filters.command("exercice_info2"))
def exoinfo2_text_(client, message):
    chat_id = message.chat.id
    pdf_path = "serie1_info2.jpg"
    pdf_path1 = "serie2_info2.jpg"
    client.send_document(chat_id, pdf_path)
    client.send_document(chat_id, pdf_path1)

    return

@bot.on_message(filters.command("examen_info2"))
def examen_info2_text(client, message):
    chat_id = message.chat.id
    text = "https://drive.google.com/drive/folders/1I4uiEQ4RTheb1W_ipRqZ958uNDyOASOx?usp=drive_link"
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command("methode2"))
def method2_text(client, message):
    chat_id = message.chat.id
    text = method2()
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command(["cour_method2"]))
def send_cour_method2(client, message):
    chat_id = message.chat.id
    pdf_path = "cour1_method2.pdf"
    pdf_path1="cour2_method2.pdf"
    
    client.send_document(chat_id, pdf_path)
    client.send_document(chat_id, pdf_path1)

    
    return

@bot.on_message(filters.command(["examen_method2"]))
def send_examen_method2(client, message):
    chat_id = message.chat.id
    pdf_path = "https://drive.google.com/drive/folders/1cQ7TmVTtw-owaVLDIOJulPoE614t2m2L?usp=drive_link"
    
    client.send_document(chat_id, pdf_path)
    
    return

@bot.on_message(filters.command("mst2"))
def mst2_text(client, message):
    chat_id = message.chat.id
    text = mst2()
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command(["cour_mst2"]))
def send_cour_mst2(client, message):
    chat_id = message.chat.id
    text = "غير موجود حاليا "
    client.send_message(chat_id, text)
    
    
    return

@bot.on_message(filters.command(["examen_mst2"]))
def send_examen_mst2(client, message):
    chat_id = message.chat.id
    text = "https://drive.google.com/drive/folders/1DQNgDH49R8mFap-MBHOSNhAByh9mawFX?usp=drive_link"
    client.send_message(chat_id, text)

@bot.on_message(filters.command("english2"))
def english2_text(client, message):
    chat_id = message.chat.id
    text = english2()
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command(["cour_english2"]))
def send_cour_english2(client, message):
    chat_id = message.chat.id
    pdf_path = "cour_english2.pdf"
    
    
    client.send_document(chat_id, pdf_path)
    
    
    return

@bot.on_message(filters.command(["examen_english2"]))
def send_examen_english2(client, message):
    chat_id = message.chat.id
    text = "https://drive.google.com/drive/folders/1b12rbJxxNDBhckHs0n_rl-Llk4Cn6xAr?usp=drive_link"
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command(["cour_frnc2"]))
def send_cour_frnc2(client, message):
    chat_id = message.chat.id
    text = "غير موجود حاليا "
    client.send_message(chat_id, text)
    
    
    return

@bot.on_message(filters.command(["examen_frnc2"]))
def send_examen_frnc2(client, message):
    chat_id = message.chat.id
    text = "غير موجود حاليا "

    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command(english_commands[2])) 
def s2_english_text(client, message):
    chat_id = message.chat.id
    text = S2_english()
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command("chimie2_"))  
def chimie2_text_(client, message):
    chat_id = message.chat.id
    text = chimie2_()
    client.send_message(chat_id, text)
    return


@bot.on_message(filters.command("videos_chimie2_")) 
def videos_text_chimie2_(client, message):
    chat_id = message.chat.id
    text = videos_chimie2_()
    client.send_message(chat_id, text)
    return


@bot.on_message(filters.command("cour_chimie2_"))  
def courchimie2_text_(client, message):
    chat_id = message.chat.id
    text = courchimie2_()
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command(["Introductions_sur_la_thermodynamique_"])) 
def send_cour1_chimie2_(client, message):
    chat_id = message.chat.id
    pdf_path = "Introductions_sur_la_thermodynamique.pdf"
    client.send_document(chat_id, pdf_path)
    return

@bot.on_message(filters.command(["Calorimetre_"]))
def send_cour2_chimie2_(client, message):
    chat_id = message.chat.id
    pdf_path = "calorimetre.pdf"
    client.send_document(chat_id, pdf_path)
    return



@bot.on_message(filters.command(["1er_principe_"])) 
def send_cour3_shimie2_(client, message):
    chat_id = message.chat.id
    pdf_path = "1er_principe.pdf"
    client.send_document(chat_id, pdf_path)
    return


@bot.on_message(filters.command(["Thermochimie_"]))
def send_cour4_chimie2_(client, message):
    chat_id = message.chat.id
    pdf_path = "thermochimie.pdf"
    client.send_document(chat_id, pdf_path)
    return

@bot.on_message(filters.command(["2eme_principe_"]))
def send_cour5_chimie2_(client, message):
    chat_id = message.chat.id
    text="Currently unavailable_"
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command("exercice_chimie2_"))
def exochimie2_text__(client, message):
    chat_id = message.chat.id
    text = exo_chimie2_()
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command(["exo_Introductions_sur_la_thermodynamique_"]))
def send_exo_Introductions_sur_la_thermodynamique_(client, message):
    chat_id = message.chat.id
    pdf_path = "chmie2_serie_1.pdf"
    pdf_path1 ="chmie2_corrige_serie1.pdf"
    client.send_document(chat_id, pdf_path)
    client.send_document(chat_id, pdf_path1)
    return

@bot.on_message(filters.command(["exo_Calorimetre_"]))
def send_exo_Calorimetre_(client, message):
    chat_id = message.chat.id
    pdf_path = "chimie2_corrige_serie2+serie2.pdf"
    client.send_document(chat_id, pdf_path)
    
    return

@bot.on_message(filters.command(["exo_1er_principe_"]))
def send_exo_1er_principe_(client, message):
    chat_id = message.chat.id
    pdf_path = "Chimie2_Corrige_serie_n3.pdf"
    pdf_path1 ="chimie2_serie_n3.pdf"
    client.send_document(chat_id, pdf_path1)
    client.send_document(chat_id, pdf_path)
    return

@bot.on_message(filters.command(["exo_Thermochimie_"]))
def send_exo_Thermochimie_(client, message):
    chat_id = message.chat.id
    pdf_path = "chimie2_corrige_serie4+serie4.pdf"
    
    client.send_document(chat_id, pdf_path)
    
    return

@bot.on_message(filters.command("exo_2eme_principe_"))
def send_exo_2eme_principe_(client, message):
    chat_id = message.chat.id
    text = "Currently unavailable_" 
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command("examen_chimie2_"))
def examen_chimie2_text_(client, message):
    chat_id = message.chat.id
    text = "https://drive.google.com/drive/folders/14z3lMTAAiQ2DsLFsBD_NKj3zvkgkeHPQ?usp=drive_link"
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command("math2_"))  
def math2_text_(client, message):
    chat_id = message.chat.id
    text = math2_()
    client.send_message(chat_id, text)
    return


@bot.on_message(filters.command("videos_math2_")) 
def videos_text_math2_(client, message):
    chat_id = message.chat.id
    text = "Currently unavailable_"
    client.send_message(chat_id, text)
    return 

@bot.on_message(filters.command("cour_math2_"))  
def courmath2_text_(client, message):
    chat_id = message.chat.id
    text=cour_math2_()
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command(["DL_"])) 
def send_cour1_math2_(client, message):
    chat_id = message.chat.id
    pdf_path = "cour_dl_1.pdf"
    pdf_path2 = "cour_dl_2.pdf"
    client.send_document(chat_id, pdf_path)
    client.send_document(chat_id, pdf_path2)
    return

@bot.on_message(filters.command(["matrice_"]))
def send_cour2_math2_(client, message):
    chat_id = message.chat.id
    pdf_path = "cour_matrice_1.pdf"
    pdf_path1 = "cour_matrice_2.pdf"
    pdf_path2 = "cour_matrice_3.pdf"
    pdf_path3 = "cour_matrice_4.pdf"
    pdf_path4 = "cour_matrice_5.pdf"
    client.send_document(chat_id, pdf_path)
    client.send_document(chat_id, pdf_path1)
    client.send_document(chat_id, pdf_path2)
    client.send_document(chat_id, pdf_path3)
    client.send_document(chat_id, pdf_path4)
    return



@bot.on_message(filters.command(["integrals_"])) 
def send_cour3_math2_(client, message):
    chat_id = message.chat.id
    text = "Currently unavailable_"
    client.send_message(chat_id, text)
    return


@bot.on_message(filters.command(["Les_equations_differentielles_"]))
def send_cour4_math2_(client, message):
    chat_id = message.chat.id
    text = "Currently unavailable_"
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command("exercice_math2_"))
def exomath2_text__(client, message):
    chat_id = message.chat.id
    text = exo_math2_()
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command(["exo_DL_"]))
def send_exo_dl_(client, message):
    chat_id = message.chat.id
    pdf_path = "exo_dl.pdf"
    client.send_document(chat_id, pdf_path)
    return

@bot.on_message(filters.command(["exo_matrice_"]))
def send_exo_matrice_(client, message):
    chat_id = message.chat.id
    pdf_path = "corrige_serie3_matrice.pdf"
    pdf_path1 = "serie3_matrice.pdf"
    client.send_document(chat_id, pdf_path1)
    client.send_document(chat_id, pdf_path)
    
    return

@bot.on_message(filters.command(["exo_integral_"]))
def send_exo_integral_(client, message):
    chat_id = message.chat.id
    pdf_path = "math2_serie4.pdf"
    pdf_path1 ="corrige1_serie4_math2.pdf"
    pdf_path2 ="corrige2_serie4_math2.pdf"
    client.send_document(chat_id, pdf_path)
    client.send_document(chat_id, pdf_path1)
    client.send_document(chat_id, pdf_path2)
    return

@bot.on_message(filters.command(["exo_les_equa_def_"]))
def send_exo_Les_equations_differentielles_(client, message):
    chat_id = message.chat.id
    text = "Currently unavailable_"
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command("examen_math2_"))
def examen_math2_text_(client, message):
    chat_id = message.chat.id
    text = "https://drive.google.com/drive/folders/1ks1ORQJubkdFgrFiKEkoCShXGBicOLs2?usp=drive_link"
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command("physique2_"))  
def phy2_text_(client, message):
    chat_id = message.chat.id
    text = phy2_()
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command("videos_phy2_")) 
def videos_text_phy2_(client, message):
    chat_id = message.chat.id
    text = videos_phy2_()
    client.send_message(chat_id, text)
    return



@bot.on_message(filters.command("cour_phy2_"))  
def courphy2_text_(client, message):
    chat_id = message.chat.id
    text=cour_phy2_()
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command(["electrique_field_"]))
def send_cour1_phy2_(client, message):
    chat_id = message.chat.id
    pdf_path = "chap1_phy2_1.pdf"
    pdf_path1 ="chap1_phy2_2.pdf"
    pdf_path2 ="chap1_phy2_3.pdf"
    client.send_document(chat_id, pdf_path)
    client.send_document(chat_id, pdf_path1)
    client.send_document(chat_id, pdf_path2)
    return

@bot.on_message(filters.command(["conducteur_"]))
def send_cour_conducteur_(client, message):
    chat_id = message.chat.id
    pdf_path = "chap2_phy2.pdf"
    
    client.send_document(chat_id, pdf_path)
    
    return

@bot.on_message(filters.command(["electrosinetique_"]))
def send_cour_electrosinetique_(client, message):
    chat_id = message.chat.id
    pdf_path = "chap3_phy2.pdf"
    
    client.send_document(chat_id, pdf_path)
    
    return

@bot.on_message(filters.command("exercice_phy2_"))
def exophy2_text__(client, message):
    chat_id = message.chat.id
    text = exo_phy2_()
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command(["exo_electrique_field_"]))
def send_exo_electrique_field_(client, message):
    chat_id = message.chat.id
    pdf_path = "exo_chap1_phy2.pdf"
    
    client.send_document(chat_id, pdf_path)
    
    return

@bot.on_message(filters.command(["exo_conducteur_"]))
def send_exo_conducteur_(client, message):
    chat_id = message.chat.id
    pdf_path = "exo_chap2_phy2.pdf"
    
    client.send_document(chat_id, pdf_path)
    
    return

@bot.on_message(filters.command(["exo_electrosinetique"]))
def send_exo_electrosinetique_(client, message):
    chat_id = message.chat.id
    pdf_path = "exo_chap3_phy2.pdf"
    
    client.send_document(chat_id, pdf_path)
    
    return

@bot.on_message(filters.command("examen_phy2_"))
def examen_phy2_text_(client, message):
    chat_id = message.chat.id
    text = "https://drive.google.com/drive/folders/1TktjtVzUpb0GtDMLOAvUY9v5V7QDcSIh?usp=drive_link"
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command("informatique2_"))  
def info2_text_(client, message):
    chat_id = message.chat.id
    text = info2_()
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command("videos_info2_")) 
def videos_text_info2_(client, message):
    chat_id = message.chat.id
    text = videos_info2_()
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command("cour_info2_")) 
def cour_info2_(client, message):
    chat_id = message.chat.id
    text="you dont need courses"
    client.send_message(chat_id, text)
    return


@bot.on_message(filters.command("exercice_info2_"))
def exoinfo2_text__(client, message):
    chat_id = message.chat.id
    pdf_path = "serie1_info2.jpg"
    pdf_path1 = "serie2_info2.jpg"
    client.send_document(chat_id, pdf_path)
    client.send_document(chat_id, pdf_path1)

    return

@bot.on_message(filters.command("examen_info2_"))
def examen_info2_text_(client, message):
    chat_id = message.chat.id
    text = "https://drive.google.com/drive/folders/1I4uiEQ4RTheb1W_ipRqZ958uNDyOASOx?usp=drive_link"
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command("methode2_"))
def method2_text_(client, message):
    chat_id = message.chat.id
    text = method2_()
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command(["cour_method2_"]))
def send_cour_method2_(client, message):
    chat_id = message.chat.id
    pdf_path = "cour1_method2.pdf"
    pdf_path1="cour2_method2.pdf"
    
    client.send_document(chat_id, pdf_path)
    client.send_document(chat_id, pdf_path1)

    
    return

@bot.on_message(filters.command(["examen_method2_"]))
def send_examen_method2_(client, message):
    chat_id = message.chat.id
    pdf_path = "https://drive.google.com/drive/folders/1cQ7TmVTtw-owaVLDIOJulPoE614t2m2L?usp=drive_link"
    
    client.send_document(chat_id, pdf_path)
    
    return

@bot.on_message(filters.command("mst2_"))
def mst2_text_(client, message):
    chat_id = message.chat.id
    text = mst2_()
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command(["cour_mst2_"]))
def send_cour_mst2_(client, message):
    chat_id = message.chat.id
    text = "Currently unavailable_"
    client.send_message(chat_id, text)
    
    
    return

@bot.on_message(filters.command(["examen_mst2_"]))
def send_examen_mst2_(client, message):
    chat_id = message.chat.id
    text = "https://drive.google.com/drive/folders/1DQNgDH49R8mFap-MBHOSNhAByh9mawFX?usp=drive_link"
    client.send_message(chat_id, text)

@bot.on_message(filters.command("english2_"))
def english2_text_(client, message):
    chat_id = message.chat.id
    text = english2_()
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command(["cour_english2_"]))
def send_cour_english2_(client, message):
    chat_id = message.chat.id
    pdf_path = "cour_english2.pdf"
    
    
    client.send_document(chat_id, pdf_path)
    
    
    return

@bot.on_message(filters.command(["examen_english2_"]))
def send_examen_english2_(client, message):
    chat_id = message.chat.id
    text = "https://drive.google.com/drive/folders/1b12rbJxxNDBhckHs0n_rl-Llk4Cn6xAr?usp=drive_link"
    client.send_message(chat_id, text)
    return

@bot.on_message(filters.command(["cour_frnc2_"]))
def send_cour_frnc2_(client, message):
    chat_id = message.chat.id
    text = "Currently unavailable_"
    client.send_message(chat_id, text)
    
    
    return

@bot.on_message(filters.command(["examen_frnc2_"]))
def send_examen_frnc2_(client, message):
    chat_id = message.chat.id
    text = "Currently unavailable_"

    client.send_message(chat_id, text)
    return




bot.run()
