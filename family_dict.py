my_family = {
    'sister': {
        'name': 'Morgan',
        'age': 26
    },
    'mother': {
        'name': 'Dodie',
        'age': 55
    },
	'father': {
		'name': 'Lloyd',
		'age': 57
	},
	'brother': {
		'name': 'Adam',
		'age': 24
	}
}

family = {str(v['name']) + ' is my ' + k +' and is ' + str(v['age']) + ' years old.' for (k,v) in my_family.items()}

print(str(family))

