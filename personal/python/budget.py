import json
import math


def main(savings_amt: int = 20, show_bill_breakdown: bool = False) -> None:
    with open("test/people.json", "r", encoding="utf8") as file:
        incomes = json.load(file)
    lowest_income = None
    longest_name = 0
    saved = 0
    for provider in incomes:
        longest_name = max(longest_name, len(provider) * 2)
        incomes[provider]["monthly_income"] = incomes[provider]["weekly_pay"] * 52 // 12
        incomes[provider]["monthly_savings"] = math.ceil(incomes[provider]["monthly_income"] * incomes[provider].get("savings", savings_amt) / 100)
        incomes[provider]["remaining"] = incomes[provider]["monthly_income"] - incomes[provider]["monthly_savings"]
        saved += incomes[provider]["monthly_savings"]
        if lowest_income is not None:
            lowest_income = min(lowest_income, incomes[provider]["remaining"])
        else:
            lowest_income = incomes[provider]["remaining"]

    # For even spending money, take top providers' amounts from the top.
    # TODO rework for large disparities in income
    tot_cont = 0
    for provider in incomes:
        incomes[provider]["contribution"] = incomes[provider]["remaining"] - lowest_income
        incomes[provider]["remaining"] -= incomes[provider]["contribution"]
        tot_cont += incomes[provider]["contribution"]

    # Load bill data {"Bill Name": [BillAmt(int), "Bill Category"]}
    mthly_total = 0
    with open("test/bills.json", "r", encoding="utf8") as file:
        bills = json.load(file)
    bill_cats = {}
    bills_by_cat = {}
    for bill in bills:
        amt, cat = bills[bill]
        bill_cats[cat] = bill_cats.get(cat, 0) + amt
        try:
            bills_by_cat[cat].append(f"{'-':>4}{bill:<10}${amt}")
        except KeyError:
            bills_by_cat[cat] = [f"{'-':>4}{bill:<10}${amt}"]
        mthly_total += amt
    bill_total = mthly_total

    if show_bill_breakdown:
        for cat in sorted(bill_cats, key=lambda a: -bill_cats[a]):
            print(f"{cat+':':<20}${bill_cats[cat]}")
            for bill in sorted(bills_by_cat[cat]):
                print(bill)
            print("\n")
        print(f"{'Total:':<20}${mthly_total}")
    mthly_total -= tot_cont
    if mthly_total <= 0:
        print(f"Bills paid by highest income with ${-mthly_total} to spare.")
        return
    print(f"\n${mthly_total} to cover after taking off top of highest income.\n")

    # Split remaining amount among providers.
    mthly_total = math.ceil(mthly_total / len(incomes))

    output = [[""], ["M. Income"], ["M. Contrib"], ["W. Income"], ["W. Contrib"], ["M. Remaining"], ["W. Remaining"], ["Contrib % Income"], ["Contrib % Bills"], [""], ["", f"Savings  @{savings_amt}%"], ["M. Savings"], ["W. Savings"]]
    # , ["", "Savings"], ["Rec. Savings"], ["M. Remaining"], ["W Rec. Savings"], ["W. Remaining"]]
    for provider in incomes:
        incomes[provider]["remaining"] -= mthly_total
        incomes[provider]["contribution"] += mthly_total
        incomes[provider]["cont_per"] = f'{incomes[provider]["contribution"] * 100 / incomes[provider]["monthly_income"]:.2f}%'
        incomes[provider]["cont_per2"] = f'{incomes[provider]["contribution"] * 100 / bill_total:.2f}%'
        output[0].append(provider)
        output[1].append(incomes[provider]["monthly_income"])
        output[2].append(incomes[provider]["contribution"])
        output[3].append(incomes[provider]["monthly_income"] * 0.25)
        output[4].append(incomes[provider]["contribution"] * 0.25)
        output[5].append(incomes[provider]["remaining"])
        output[6].append(incomes[provider]["remaining"] * 0.25)
        output[7].append(incomes[provider]["cont_per"])
        output[8].append(incomes[provider]["cont_per2"])
        output[11].append(incomes[provider]["monthly_savings"])
        output[12].append(incomes[provider]["monthly_savings"] * 0.25)

        # output[10].append((m_s := incomes[provider]["monthly_savings"]))
        # output[11].append(incomes[provider]["remaining"] - m_s)
        # output[12].append((w_s := incomes[provider]["monthly_savings"] * 0.25))
        # output[13].append(incomes[provider]["remaining"] * 0.25 - w_s)

    line = output.pop(0)
    print(f"{line[0]:<16}" + "".join([f"{x:^{longest_name}}    |" for x in line[1:]]) + "\b ")
    for line in output:
        symbol = "$" if "%" not in line[0] and line[0] != "" else ""
        try:
            print(f"{line[0]:<16}" + "".join([f"{symbol:>4}{x:>{longest_name-4}.2f}    |" for x in line[1:]]) + "\b ")
        except ValueError:
            print(f"{line[0]:<16}" + "".join([f"{symbol:>4}{x:>{longest_name-4}}    |" for x in line[1:]]) + "\b ")
    print(f"\nSavings after year: ${math.ceil(saved*12)}")


if __name__ == "__main__":
    for per in range(0, 51, 5):
        main(per)
