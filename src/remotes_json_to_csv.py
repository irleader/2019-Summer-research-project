import json
import csv

d=open("remotes_mod.json","r")
d=json.load(d)
x=d["comps"]
y=d["units"]
# print(x)
# print(type(x))
# print(y)
# print(type(y))


f = csv.writer(open("test1.csv", "w"))
f.writerow(["customer_no",
            "battery_eff", "batter_p_lim","battery_quad_penality","battery_soc_limit",
           "inverter_eff","inverter_p_lim","inverter_q_lim","inverter_s_max",
            "tariffs_fit",
            "tariffs_weekday_1_endTime","tariffs_weekday_1_name","tariffs_weekday_1_rate","tariffs_weekday_1_startTime",
            "tariffs_weekday_2_endTime","tariffs_weekday_2_name","tariffs_weekday_2_rate","tariffs_weekday_2_startTime",
            "tariffs_weekday_3_endTime", "tariffs_weekday_3_name", "tariffs_weekday_3_rate", "tariffs_weekday_3_startTime",
            "tariffs_weekday_4_endTime", "tariffs_weekday_4_name", "tariffs_weekday_4_rate", "tariffs_weekday_4_startTime",
            "tariffs_weekday_5_endTime", "tariffs_weekday_5_name", "tariffs_weekday_5_rate", "tariffs_weekday_5_startTime",
            "tariffs_weekend_endTime", "tariffs_weekend_name", "tariffs_weekend_rate", "tariffs_weekend_startTime",
            "tx_ph","tx_tap"
            ])
for n in range(31):
    key="cust_"+str(n)
    c=x[key]
    c["tariffs"]["weekday"].append({'endTime': '', 'name': '', 'rate': '', 'startTime': ''})
    c["tariffs"]["weekday"].append({'endTime': '', 'name': '', 'rate': '', 'startTime': ''})
    c["tariffs"]["weekday"].append({'endTime': '', 'name': '', 'rate': '', 'startTime': ''})
    c["tariffs"]["weekday"].append({'endTime': '', 'name': '', 'rate': '', 'startTime': ''})

    f.writerow([key,
                c["battery"]["eff"], c["battery"]["p_lim"], c["battery"]["quad_penalty"], c["battery"]["soc_lim"],
                c["inverter"]["eff"],c["inverter"]["p_lim"],c["inverter"]["q_lim"],c["inverter"]["s_max"],
                c["tariffs"]["fit"],
                c["tariffs"]["weekday"][0]["endTime"],c["tariffs"]["weekday"][0]["name"],
                c["tariffs"]["weekday"][0]["rate"],c["tariffs"]["weekday"][0]["startTime"],
                c["tariffs"]["weekday"][1]["endTime"], c["tariffs"]["weekday"][1]["name"],
                c["tariffs"]["weekday"][1]["rate"], c["tariffs"]["weekday"][1]["startTime"],
                c["tariffs"]["weekday"][2]["endTime"], c["tariffs"]["weekday"][2]["name"],
                c["tariffs"]["weekday"][2]["rate"], c["tariffs"]["weekday"][2]["startTime"],
                c["tariffs"]["weekday"][3]["endTime"], c["tariffs"]["weekday"][3]["name"],
                c["tariffs"]["weekday"][3]["rate"], c["tariffs"]["weekday"][3]["startTime"],
                c["tariffs"]["weekday"][4]["endTime"], c["tariffs"]["weekday"][4]["name"],
                c["tariffs"]["weekday"][4]["rate"], c["tariffs"]["weekday"][4]["startTime"],
                c["tariffs"]["weekend"][0]["endTime"], c["tariffs"]["weekend"][0]["name"],
                c["tariffs"]["weekend"][0]["rate"], c["tariffs"]["weekend"][0]["startTime"],
                c["tx_ph"],c["tx_tap"]
                ])
    # print(c["tx_ph"])
    # print(c)
    # print("\n")

