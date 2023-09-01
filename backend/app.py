from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample balance sheet data
balance_sheet = [
    {"year": 2021, "month": 7, "profitOrLoss": -5000, "assetsValue": 150000},
    {"year": 2021, "month": 6, "profitOrLoss": -8000, "assetsValue": 140000},
    {"year": 2021, "month": 5, "profitOrLoss": -6000, "assetsValue": 130000},
    {"year": 2021, "month": 4, "profitOrLoss": -3000, "assetsValue": 120000},
    {"year": 2021, "month": 3, "profitOrLoss": -2000, "assetsValue": 110000},
    {"year": 2021, "month": 2, "profitOrLoss": -4000, "assetsValue": 100000},
    {"year": 2021, "month": 1, "profitOrLoss": -5000, "assetsValue": 90000},
    {"year": 2020, "month": 12, "profitOrLoss": -7000, "assetsValue": 80000},
    {"year": 2020, "month": 11, "profitOrLoss": -6000, "assetsValue": 70000},
    {"year": 2020, "month": 10, "profitOrLoss": -8000, "assetsValue": 60000},
    {"year": 2020, "month": 9, "profitOrLoss": -9000, "assetsValue": 50000},
    {"year": 2020, "month": 8, "profitOrLoss": -10000, "assetsValue": 40000}
]

@app.route('/fetch_balance_sheet', methods=['POST'])
def fetch_balance_sheet():
    data = request.json
    return jsonify(balance_sheet)

@app.route('/submit_application', methods=['POST'])
def submit_application():
    data = request.json
    pre_assessment = calculate_pre_assessment(data)
    decision_outcome = get_decision(pre_assessment)
    
    application_result = {
        "business_name": data["business_name"],
        "year_established": data["year_established"],
        "pre_assessment": pre_assessment,
        "decision_outcome": decision_outcome
    }
    
    return jsonify(application_result)

def calculate_pre_assessment(data):
    profit_or_loss_sum = sum(entry["profitOrLoss"] for entry in data["balance_sheet"])
    assets_value_avg = sum(entry["assetsValue"] for entry in data["balance_sheet"]) / len(data["balance_sheet"])
    
    if profit_or_loss_sum > 0:
        return 60
    elif profit_or_loss_sum < 0:
        return 20  # Rejected
    elif assets_value_avg > data["loan_amount"]:
        return 100
    else:
        return 20

def get_decision(pre_assessment):
    return "Approved" if pre_assessment >= 50 else "Rejected"

if __name__ == '__main__':
    app.run(debug=True)
