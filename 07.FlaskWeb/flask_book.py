from flask import Flask, render_template, request
import util.crawl_util as cu 
import util.map_util as mu

app = Flask(__name__)
 
@app.route('/')   
def index():
    return '''
        <h1>크롤링</h1>
        <button onclick="location.href='/inter_boot'">인터파크 베스트셀러</button>
        <button onclick="location.href='/cctv_boot'">구별 CCTV/인구 현황(개선판)</button>
        '''

@app.route('/inter_boot')
def inter_boot():
    book_list = cu.get_bestseller()
    return render_template('inter_boot.html', book_list=book_list)

@app.route('/cctv_boot', methods=['GET','POST'])
def cctv_boot():
    if request.method == 'GET':
        columns = ['CCTV댓수','최근증가율','인구수','내국인','외국인','고령자','외국인 비율','고령자 비율']
        colormaps = ['RdPu', 'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds','YlOrBr', 'YlOrRd', 
                     'OrRd', 'PuRd', 'BuPu', 'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn']
        return render_template('cctv_boot_form.html', columns=columns, colormaps=colormaps)
    else:
        column = request.form['column']
        colormap = request.form['colormap']
        mu.get_cctv_boot(app.static_folder, column, colormap)    # static/img/cctv_pop.html 파일
        return render_template('cctv_boot_res.html', column=column, colormap=colormap)

if __name__ == '__main__':
    app.run(debug=True)