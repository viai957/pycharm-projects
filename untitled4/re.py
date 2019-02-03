import re
print(dir(re))

string = "The night was colad and dark and there was no one there"
m = re.search("night",string)
print(m)
start = m.start()
end = start + 5
print(start)
print(end)
print(m.end)

string = "Hello world ,How are you"
re.search("night",string)