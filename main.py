from flask import Flask, render_template, request, redirect, send_file
from file import save_to_file

from extractors.worldMemory import extract_wm
from extractors.nanoMemory import extract_nm
from extractors.danawa import extract_danawa

from datetime import datetime

app = Flask("JobScrapper")

db = {
}

# 오늘 날짜 가져오기
now = datetime.now()
cr_today = now.strftime("%Y-%m-%d")


@app.route("/")
def home():
  return render_template("home.html", name="nico")


@app.route("/search")
def search():
  global full_wm,full_nm,full_danawa
  full_wm = [cr_today, '월드와이드메모리'] + extract_wm() + [None]
  full_nm = [cr_today, '나노메모리'] + extract_nm() + [None]
  full_danawa = [cr_today, '다나와'] + extract_danawa() + [None]
  # return render_template("search.html", data1=full_wm, data2=full_nm)  # 테스트용
  return render_template("search.html", data1=full_wm, data2=full_nm, data3=full_danawa)
  
@app.route("/export")
def export():
  # final = full_wm + full_nm + full_danawa
  
  # save_to_file(cr_today,full_wm,full_nm)  # 테스트용
  save_to_file(cr_today,full_wm,full_nm,full_danawa)  
  return send_file(f"{cr_today}.csv", as_attachment=True)

app.run()
