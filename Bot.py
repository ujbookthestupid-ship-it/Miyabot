from pyrogram import Client
import os

app = Client(
    "MiyaBot",
    api_id=int(os.getenv("23718192")),
    api_hash=os.getenv("eUyJRM8XUWs"),
    bot_token=os.getenv("8268645840:AAF5ufD3UK33WN03F-t2HcYC6yUBYdytY14"),
    plugins=dict(root="plugins")
)

app.run()
