import os
import random
import asyncpg
from dotenv import load_dotenv
from flask import Blueprint, request, redirect

link_bp = Blueprint('link', __name__, template_folder='templates')

load_dotenv(dotenv_path="../.env")

user = os.getenv('user')

password = os.getenv('password')


@link_bp.route('/<link>', methods=['GET'])
async def redirect_to(link):
    conn = await asyncpg.connect(user=user, password=password,database='linker', host='127.0.0.1')
    data = await conn.fetchrow(f"SELECT * FROM urls WHERE internal_url='{link}';")
    redirect_url,number_views = data[0],data[2]
    update_number_views = await conn.fetch(f"UPDATE urls SET number_views='{number_views + 1}' WHERE internal_url='{link}';")
    await conn.close()
    return redirect(redirect_url, code=302)

@link_bp.route('/create_link', methods=['POST'])
async def create():
    data = request.json
    if data["redirect_url"]:
        redirect_url = data["redirect_url"]
        internal_url = ''.join(random.choices("qwertyuiopasdfghjklzxcvbnm",k=10))
        conn = await asyncpg.connect(user=user, password=password,database='linker', host='127.0.0.1')
        await conn.fetch(f"INSERT INTO urls (redirect_url, internal_url, number_views) VALUES ('{redirect_url}', '{internal_url}', 0);")
        await conn.close()
        return {"url":f"{internal_url}"}