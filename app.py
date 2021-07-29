from flask import Flask, request, jsonify
from multiprocessing import Pool
from functools import partial

app = Flask(__name__)

def search_string(file, input_string):
    filepath = "./text_files/"
    file1 = open(filepath+file, "r")    # opening a text file
    readfile = file1.read()     #read the file
    file1.close() # close the file
    if input_string.lower() in readfile.lower(): 
        return file
    else :
        pass

@app.route("/search_string")
def home():
    p = Pool(3)
    func_call=partial(search_string, input_string = request.args.get('input_string')) 
    result_list = p.map(func_call, ['Doc1.txt', 'Doc2.txt', 'Doc3.txt'])
    return jsonify([i for i in result_list if i is not None])

if __name__ == "__main__":
    app.run(debug=True, threaded=True)