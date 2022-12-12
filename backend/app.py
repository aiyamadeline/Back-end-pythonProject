from flask import Flask, request, jsonify
from search import search
from filter import Filter
from storage import DBstorage
import html

app = Flask(__name__)

search_template = """
<form action="/" method="post">
    <input type="text" name="query">
    <input type="submit" value"Search">
</form>

"""

result_template = """

<p class="site">{rank}: {link} <span class="rel-button" onclick="relevant("{query}", "{link}");'>Relevant</span></p>
<a href="{link}">{title}</a>
<p class="snippet">{snippet}</p>
"""


def  show_search_form():
    return search_template

def run_search(query):
    results = search(query)
    fi = Filter(results)
    results = fi.filter()
    rendered = search_template
    results["snippet"] = results["snippet"].apply(lambda x: html.escape(x))
    for index, row in results.iterrows():
        rendered += result_template.format(**row)
    return rendered

@app.route("/", methods=["GET", "POST"])
def search_form():
    if request.method == "POST":
        query = request.form["query"]
        return run_search(query)
    else: 
        return show_search_form()

@app.route("/relevant", methods=["POST"])
def mark_relevant():
    data = request.get_json()
    query = data["query"]
    link = data["link"]
    storage = DBstorage()
    storage.update_relevance(query, link , 10)
    return jsonify(success=True)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)

