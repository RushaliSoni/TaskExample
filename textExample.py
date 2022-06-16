# import json
# # read Data From Json File
# with open('text.json','r') as f:
#     s = f.read()
#     print(s)

# Using Function REad and Write Data From  Json File With Changes
def find_Replace(find, replace, input, output):
    with open(input) as f:
        s = f.read()
    s = s.replace(find, replace)
    with open(output, "w") as f:
        f.write(s)


find_Replace("+type", "+size@5+type", "test.json", "output.json")