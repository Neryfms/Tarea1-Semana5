import telebot

bot = telebot.TeleBot("1890500692:AAEtt9Vsh79XuCDNh2UPrXBjARDVrkEiY-s")

@bot.message_handler(commands=["hola1" ])
def hola1 (mensaje):
    bot.reply_to(mensaje, "Hola, un gusto saludarte, ¿cómo estás?")

@bot.message_handler(commands=["comoestas2"]) 
def comoestas2 (mensaje):
    bot.reply_to(mensaje, "Estoy muy bien, ¿y tu?")

@bot.message_handler(commands=["estoymuybiengracias3"]) 
def estoymuybiengracias3 (mensaje):
    bot.reply_to(mensaje, "Me da gusto qué te encuentres bien, amigo humano")   

@bot.message_handler(commands=["dedonderes4"]) 
def dedonderes4 (mensaje):
    bot.reply_to(mensaje, "No tengo nacionalidad por lo tanto no tengo procedencia, no nací, me crearon, soy un programa informático que efectúa automáticamente tareas reiterativas mediante Internet a través de este chat de Telegram con una cadena de comandos o funciones autónomas previamente programadas")

@bot.message_handler(commands=["cualestuedad5"]) 
def cualestuedad5 (mensaje):
    bot.reply_to(mensaje, "No tengo una edad definida por ende no cumplo años, mi dueño puede apagarme cuando quiera")

@bot.message_handler(commands=["cualestusexo6"]) 
def cualestusexo6 (mensaje):
    bot.reply_to(mensaje, "No tengo sexo")    

@bot.message_handler(commands=["cualestunombre7"]) 
def cualestunombre7 (mensaje):
    bot.reply_to(mensaje, "Mi nombre es 97")      

@bot.message_handler(commands=["pero97noesunnombre8"]) 
def pero97noesunnombre8 (mensaje):
    bot.reply_to(mensaje, "Lo sé, pero es mi nombre.")    

bot.polling()