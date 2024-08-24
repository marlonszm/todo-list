from flask import Flask, request, url_for, render_template, redirect

app = Flask(__name__)

to_do_list = [
    {
        "id": 0,
        "todo": "wash the dishes left"
    }
]

next_id = 1

@app.route('/', methods=["GET"])
def main():
    return render_template("index.html", to_do_list=to_do_list)

@app.route('/', methods=["POST"])
def add():
    if request.form.get("todo"):
        global next_id
        to_do = {
            "id": next_id,
            "todo": request.form.get("todo")
        }
        to_do_list.append(to_do)
        next_id += 1
    return redirect(url_for('main'))

@app.route('/delete/<int:task_id>', methods=["POST"])
def delete(task_id):
    global to_do_list
    to_do_list = [task for task in to_do_list if task["id"] != task_id]
    return redirect(url_for('main'))

if __name__ == '__main__':
    app.run(port=5000, host="localhost", debug=True)
