# import json
# # read Data From Json File
# with open('text.json','r') as f:
#     s = f.read()
#     print(s)

# Using Function Read and Write Data From  Json File With Changes
# def find_Replace(find, replace, input, output):
#     with open(input) as f:
#         s = f.read()
#     s = s.replace(find, replace)
#     with open(output, "w") as f:
#         f.write(s)
#
#
# find_Replace("+type", "+size@5+type", "test.json", "output.json")



# Using Recursion
def find_replace(lines, s, rep_str, output):
  if len(lines) is not 0:
    output.append(lines.pop().replace(s, rep_str))
    return find_replace(lines, s, rep_str, output)
  return output

def write_file(lines):
  if len(lines) is not 0:
    f2 = open("output.json", "a")
    f2.write(lines.pop())
    f2.close()
    return write_file(lines)
  return

f = open("test.json", "r")
lines = f.readlines()
f.close()
out = []
result = find_replace(lines, "+type", "+size@5+type", out)
write_file(result)




