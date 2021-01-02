import json

# Json from string
user = '{"name": "Yasser", "age": 29, "profession": "Quantitative Analyst"}'

result = json.loads(user)

print(result)

# Json from dict
user = {"name": "Yasser", "age": 29, "profession": "Quantitative Analyst"}

result = json.dumps(user)

print(result)
