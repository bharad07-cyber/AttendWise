from flask import Flask, render_template, request

app = Flask(
    __name__,
    template_folder="template",
    static_folder="static"
)

TARGET_ATTENDANCE = 75


def calculate(attended, total):
    if total == 0:
        return {
            "percentage": 0,
            "status": "No Data",
            "color": "#808080",
            "skip": 0,
            "need": 0,
        }

    percentage = round((attended / total) * 100, 2)

    if percentage >= 90:
        status = "Excellent"
        color = "#00C853"

    elif percentage >= 75:
        status = "Safe"
        color = "#00BCD4"

    elif percentage >= 60:
        status = "Warning"
        color = "#FFC107"

    else:
        status = "Critical"
        color = "#F44336"

    skip = 0
    need = 0

    if percentage >= TARGET_ATTENDANCE:

        future_total = total
        future_attended = attended

        while (future_attended / (future_total + 1)) * 100 >= TARGET_ATTENDANCE:
            skip += 1
            future_total += 1

    else:

        future_total = total
        future_attended = attended

        while (future_attended / future_total) * 100 < TARGET_ATTENDANCE:
            need += 1
            future_attended += 1
            future_total += 1

    return {
        "percentage": percentage,
        "status": status,
        "color": color,
        "skip": skip,
        "need": need,
    }


@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        attended = int(request.form["attended"])
        total = int(request.form["total"])
        holidays = int(request.form["holidays"])

        total = total - holidays

        if total < 1:
            total = 1

        if attended > total:
            attended = total

        result = calculate(attended, total)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)