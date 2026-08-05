from flask import Flask
"Flask API for FASTA file scanner"
app = Flask(__name__)

@app.route("/")
def index() -> str :
    "Index page returns title"
    return "Scans FASTA files"



if __name__ == "__main__":
    app.run()
    
