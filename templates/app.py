from flask import Flask

app = Flask(__name__)

@app.route("/")
def index() -> str :
    return "Scans FASTA files"



if __name__ == "__main__":
    app.run()