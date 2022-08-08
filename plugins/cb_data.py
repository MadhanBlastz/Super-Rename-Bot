from helper.utils import progress_for_pyrogram, convert
from pyrogram import Client, filters
from pyrogram.types import (  InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from helper.database import find
import os 
import humanize
from PIL import Image
import time

CLOSE_BTN = InlineKeyboardMarkup(
    [[
    InlineKeyboardButton('❎ 𝖢𝖺𝗇𝖼𝖾𝗅', callback_data='cancel')
    ]]
)

@Client.on_callback_query(filters.regex('cancel'))
async def cancel(bot,update):
	try:
           await update.message.delete()
           await update.answer("process cancelled ✅")
	except:
           return
	
@Client.on_message(filters.command("rdoc"))
async def doc(bot,update):
     #type = update.data.split('_')[1]
     #new_name = update.message.text
     #new_filename = new_name.split(":-")[1]
     new_filename = update.text.split(" ", 1)[1]
     if not "!" in new_filename:
        new_filename = new_filename + ".mkv"
     else:
        new_filename = new_filename.replace("!", ".")
     file_path = f"downloads/{new_filename}"
     #file = update.message.reply_to_message
     file = update.reply_to_message
     #ms = await update.message.edit("𝚃𝚁𝚈𝙸𝙽𝙶 𝚃𝙾 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳...")
     ms = await update.reply("𝚃𝚁𝚈𝙸𝙽𝙶 𝚃𝙾 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳...")
     c_time = time.time()
     try:
     	path = await bot.download_media(message = file, progress=progress_for_pyrogram,progress_args=( "𝚃𝚁𝚈𝙸𝙽𝙶 𝚃𝙾 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳....",  ms, c_time   ), reply_markup = InlineKeyboardMarkup(CLOSE_BTN))
     except Exception as e:
     	await ms.edit(e)
     	return 
     splitpath = path.split("/downloads/")
     dow_file_name = splitpath[1]
     old_file_name =f"downloads/{dow_file_name}"
     os.rename(old_file_name,file_path)
     duration = 0
     try:
        metadata = extractMetadata(createParser(file_path))
        if metadata.has("duration"):
           duration = metadata.get('duration').seconds
     except:
        pass
     #user_id = int(update.message.from_user.id)
     user_id = int(update.from_user.id)
     ph_path = None
     #data = find(update.message.from_user.id)
     data = find(update.from_user.id) 
     media = getattr(file, file.media.value)
     c_caption = data[1] 
     c_thumb = data[0]
     new_cap = new_filename.replace("!", ".")
     if c_caption:
         caption = c_caption.format(filename=new_cap, filesize=humanize.naturalsize(media.file_size), duration=convert(duration))
     else:
         caption = f"**{new_cap}**\n\n**__Uploaded By :__**\n**__@MovieJunctionGrp__** 🔥"
     if (media.thumbs or c_thumb):
         if c_thumb:
            ph_path = await bot.download_media(c_thumb) 
         else:
            ph_path = await bot.download_media(media.thumbs[0].file_id)
         Image.open(ph_path).convert("RGB").save(ph_path)
         img = Image.open(ph_path)
         img.resize((320, 320))
         img.save(ph_path, "JPEG")
     await ms.edit("𝚃𝚁𝚈𝙸𝙽𝙶 𝚃𝙾 𝚄𝙿𝙻𝙾𝙰𝙳𝙸𝙽𝙶....")
     c_time = time.time() 
     try:
         await update.reply_document(
           # chat_id=DUMP_CNL,
             document=file_path,
             thumb=ph_path, 
             caption=caption, 
             progress=progress_for_pyrogram,
             progress_args=( "𝚃𝚁𝚈𝙸𝙽𝙶 𝚃𝙾 𝚄𝙿𝙻𝙾𝙰𝙳𝙸𝙽𝙶....",  ms, c_time   ), reply_markup = InlineKeyboardMarkup(CLOSE_BTN))
     except Exception as e: 
         await ms.edit(f"{e}")
         print(e) 
         os.remove(file_path)
         if ph_path:
           os.remove(ph_path)
     await ms.delete() 
     os.remove(file_path) 
     if ph_path:
        os.remove(ph_path) 

@Client.on_message(filters.command("rvid"))
async def vid(bot,update):
     #type = update.data.split('_')[1]
     #new_name = update.message.text
     #new_filename = new_name.split(":-")[1]
     new_filename = update.text.split(" ", 1)[1]
     if not "!" in new_filename:
        new_filename = new_filename + ".mp4"
     else:
        new_filename = new_filename.replace("!", ".")
     file_path = f"downloads/{new_filename}"
     #file = update.message.reply_to_message
     file = update.reply_to_message
     #ms = await update.message.edit("𝚃𝚁𝚈𝙸𝙽𝙶 𝚃𝙾 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳...")
     ms = await update.reply("𝚃𝚁𝚈𝙸𝙽𝙶 𝚃𝙾 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳...", reply_markup = InlineKeyboardMarkup(CLOSE_BTN))
     c_time = time.time()
     try:
     	path = await bot.download_media(message = file, progress=progress_for_pyrogram,progress_args=( "𝚃𝚁𝚈𝙸𝙽𝙶 𝚃𝙾 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳....",  ms, c_time   ))
     except Exception as e:
     	await ms.edit(e)
     	return 
     splitpath = path.split("/downloads/")
     dow_file_name = splitpath[1]
     old_file_name =f"downloads/{dow_file_name}"
     os.rename(old_file_name,file_path)
     duration = 0
     try:
        metadata = extractMetadata(createParser(file_path))
        if metadata.has("duration"):
           duration = metadata.get('duration').seconds
     except:
        pass
     #user_id = int(update.message.from_user.id)
     user_id = int(update.from_user.id)
     ph_path = None
     #data = find(update.message.from_user.id)
     data = find(update.from_user.id) 
     media = getattr(file, file.media.value)
     c_caption = data[1] 
     c_thumb = data[0]
     new_cap = new_filename.replace("!", ".")
     if c_caption:
         caption = c_caption.format(filename=new_cap, filesize=humanize.naturalsize(media.file_size), duration=convert(duration))
     else:
         caption = f"**{new_cap}**\n\n**__Uploaded By :__**\n**__@MovieJunctionGrp__** 🔥"
     if (media.thumbs or c_thumb):
         if c_thumb:
            ph_path = await bot.download_media(c_thumb) 
         else:
            ph_path = await bot.download_media(media.thumbs[0].file_id)
         Image.open(ph_path).convert("RGB").save(ph_path)
         img = Image.open(ph_path)
         img.resize((320, 320))
         img.save(ph_path, "JPEG")
     await ms.edit("𝚃𝚁𝚈𝙸𝙽𝙶 𝚃𝙾 𝚄𝙿𝙻𝙾𝙰𝙳𝙸𝙽𝙶....", reply_markup = InlineKeyboardMarkup(CLOSE_BTN))
     c_time = time.time() 
     try:
         await update.reply_video(
             video=file_path,
	     caption=caption,
	     thumb=ph_path,
	     duration=duration,
	     progress=progress_for_pyrogram,
	     progress_args=( "𝚃𝚁𝚈𝙸𝙽𝙶 𝚃𝙾 𝚄𝙿𝙻𝙾𝙰𝙳𝙸𝙽𝙶....",  ms, c_time))
     except Exception as e: 
         await ms.edit(f"{e}")
         print(e) 
         os.remove(file_path)
         if ph_path:
           os.remove(ph_path)
     await ms.delete() 
     os.remove(file_path) 
     if ph_path:
        os.remove(ph_path) 

@Client.on_message(filters.command("raud"))
async def aud(bot,update):
     #type = update.data.split('_')[1]
     #new_name = update.message.text
     #new_filename = new_name.split(":-")[1]
     new_filename = update.text.split(" ", 1)[1]
     if not "!" in new_filename:
        new_filename = new_filename + ".mp3"
     else:
        new_filename = new_filename.replace("!", ".")
     file_path = f"downloads/{new_filename}"
     #file = update.message.reply_to_message
     file = update.reply_to_message
     #ms = await update.message.edit("𝚃𝚁𝚈𝙸𝙽𝙶 𝚃𝙾 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳...")
     ms = await update.reply("𝚃𝚁𝚈𝙸𝙽𝙶 𝚃𝙾 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳...", reply_markup = InlineKeyboardMarkup(CLOSE_BTN))
     c_time = time.time()
     try:
     	path = await bot.download_media(message = file, progress=progress_for_pyrogram,progress_args=( "𝚃𝚁𝚈𝙸𝙽𝙶 𝚃𝙾 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳....",  ms, c_time   ))
     except Exception as e:
     	await ms.edit(e)
     	return 
     splitpath = path.split("/downloads/")
     dow_file_name = splitpath[1]
     old_file_name =f"downloads/{dow_file_name}"
     os.rename(old_file_name,file_path)
     duration = 0
     try:
        metadata = extractMetadata(createParser(file_path))
        if metadata.has("duration"):
           duration = metadata.get('duration').seconds
     except:
        pass
     #user_id = int(update.message.from_user.id)
     user_id = int(update.from_user.id)
     ph_path = None
     #data = find(update.message.from_user.id)
     data = find(update.from_user.id) 
     media = getattr(file, file.media.value)
     c_caption = data[1] 
     c_thumb = data[0]
     new_cap = new_filename.replace("!", ".")
     if c_caption:
         caption = c_caption.format(filename=new_cap, filesize=humanize.naturalsize(media.file_size), duration=convert(duration))
     else:
         caption = f"**{new_cap}**\n\n**__Uploaded By :__**\n**__@MovieJunctionGrp__** 🔥"
     if (media.thumbs or c_thumb):
         if c_thumb:
            ph_path = await bot.download_media(c_thumb) 
         else:
            ph_path = await bot.download_media(media.thumbs[0].file_id)
         Image.open(ph_path).convert("RGB").save(ph_path)
         img = Image.open(ph_path)
         img.resize((320, 320))
         img.save(ph_path, "JPEG")
     await ms.edit("𝚃𝚁𝚈𝙸𝙽𝙶 𝚃𝙾 𝚄𝙿𝙻𝙾𝙰𝙳𝙸𝙽𝙶....", reply_markup = InlineKeyboardMarkup(CLOSE_BTN))
     c_time = time.time() 
     try:
         await update.reply_audio(
             audio=file_path,
             caption=caption,
             thumb=ph_path, 
             duration=duration,
             progress=progress_for_pyrogram,
             progress_args=( "𝚃𝚁𝚈𝙸𝙽𝙶 𝚃𝙾 𝚄𝙿𝙻𝙾𝙰𝙳𝙸𝙽𝙶....",  ms, c_time   ))
     except Exception as e: 
         await ms.edit(f"{e}")
         print(e) 
         os.remove(file_path)
         if ph_path:
           os.remove(ph_path)
     await ms.delete() 
     os.remove(file_path) 
     if ph_path:
        os.remove(ph_path) 
