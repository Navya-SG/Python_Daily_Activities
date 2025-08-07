students = [{"name": "Brenda", "scores": [90, 92, 95, 88]},
            {"name": "David", "scores": [85, 87, 89]},
            {"name": "Cathy", "scores": [98, 99, 100]},
            {"name": "Alex", "scores": [70, 100]}]
new_dict = {x.get("name"):sum(x.get("scores"))/len(x.get("scores")) for x in filter(lambda x:sum(x.get("scores"))/len(x.get("scores"))>90,students)}
print(new_dict)


top_students_map = {s["name"]: round(calculate_avg(s["scores"]), 2) for s in top_students_data}