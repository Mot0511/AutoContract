from flask import *
from docx import Document
from docx.shared import Inches

app = Flask(__name__, static_folder="static")

document = Document()

@app.route('/')
def index(name=None):
    return render_template('index.html')

@app.route('/contract', methods=['GET', 'POST'])
def contract():
    if request.method == 'POST':
        place = request.form.get('place')
        date1_sost = request.form.get('date1_sost')
        name_saler = request.form.get('name_saler')
        date_birth_saler = request.form.get('date_birth_saler')
        place_birth_saler = request.form.get('place_birth_saler')
        date_pass_saler = request.form.get('date_pass_saler')
        number_pass_saler = request.form.get('number_pass_saler')
        seria_saler = request.form.get('seria_saler')
        vadan_saler = request.form.get('vadan_saler')
        adres_saler = request.form.get('adres_saler')

        name_bayer = request.form.get('name_bayer')
        tel_bayer = request.form.get('tel_bayer')
        date_birth_bayer = request.form.get('date_birth_bayer')
        place_birth_bayer = request.form.get('place_birth_bayer')
        pass_bayer = request.form.get('pass_bayer')
        number_pass_bayer = request.form.get('number_pass_bayer')
        seria_bayer = request.form.get('seria_bayer')
        vadan_bayer = request.form.get('vadan_bayer')
        adress_bayer = request.form.get('adress_bayer')

        mm_car = request.form.get('mm_car')
        vin = request.form.get('vin')
        type_tc = request.form.get('type_tc')
        model_dvig = request.form.get('model_dvig')
        number_dvig = request.form.get('number_dvig')
        number_shassi = request.form.get('number_shassi')
        number_kusov = request.form.get('number_kusov')
        color = request.form.get('color')
        power = request.form.get('power')
        volume = request.form.get('volume')
        date_tc = request.form.get('date_tc')
        seria_tc = request.form.get('seria_tc')
        number_tc = request.form.get('number_tc')
        vadan_tc = request.form.get('vadan_tc')
        date_ctc = request.form.get('date_ctc')
        seri_ctc = request.form.get('seri_ctc')
        number_ctc = request.form.get('number_ctc')
        vadan_ctc = request.form.get('vadan_ctc')
        probeg = request.form.get('probeg')
        gosnumber = request.form.get('gosnumber')
        price = request.form.get('price')

        document.add_heading('Договор о купли-продажи авто', 0)
        p = document.add_paragraph(name_bayer + ', ' + date_birth_bayer + ', ' +
            place_birth_bayer + ', ' + adress_bayer + ', ' + seria_bayer + ', ' +
            number_pass_bayer + ', ' + vadan_bayer + ', ' + date_birth_bayer)

        p2 = document.add_paragraph('именуемый(ая) в дальнейшем «Покупатель» с одной стороны, и')

        p3 = document.add_paragraph(name_saler + ', ' + date_birth_saler + ', ' +
            place_birth_saler + ', ' + adres_saler + ', ' + seria_saler + ', ' +
            number_pass_saler + ', ' + vadan_saler + ', ' + date_birth_saler)

        p4 = document.add_paragraph('именуемый(ая) в дальнейшем «Продавец», с другой стороны, именуемые далее при совместном упоминании «Стороны», а по отдельности «Сторона», заключили настоящий договор (далее – «Договор») о нижеследующем')

        document.add_heading('1. Предмет договора', 0)
        p5 = document.add_paragraph('1.1 Продавец обязуется передать в собственность Покупателя, а Покупатель – принять и оплатить транспортное средство (далее – ТС).')

        document.add_page_break()

        document.save('demo.docx')
app.run()