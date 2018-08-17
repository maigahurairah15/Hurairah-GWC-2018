import school_scores
list_of_records = school_scores.get_all()

print(list_of_records[0])

for i in list_of_records:
    print(i["State"]["Name"],i["Gender"]["Female"],i["Score Ranges"]["Between 600 to 700"]["Math"])
