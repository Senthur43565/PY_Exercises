senthur = {
  'gender' : 'MALE',
  'Age' : 'TwoSeven',
  'nation' :'India'  
}

selva = dict(Age='EightySix', nation = 'Canada')

print(senthur)
print(selva)
print(type(senthur))
print(len(selva))

print(senthur['gender'])
print(senthur.get('Age'))

print(senthur.keys())

print(selva.values())

print(senthur.items())
print('gender' in senthur)

senthur['Age'] = "27"
print(senthur)

senthur.update({'color':'brown'})
print(senthur)

print(senthur.pop('nation'))

print(senthur.popitem())
print(senthur)

del senthur['Age']
print(senthur)
selva.clear()
print(selva)


