import regex
import sys

n=len(sys.argv)
if n != 2:
    exit()

money_regex = '\s[$₹£][0-9]+[\.]{0,1}[0-9]*'
date_regex = '\s[0-9][0-9]\/[0-9][0-9]\/[0-9][0-9][0-9][0-9]|\s[0-9][0-9]\/[0-9][0-9]\/[0-9][0-9]'
cardinality_regex =  '\s[1-9][4-9]*th|first|second|third|[2-9][0-9]*[1]st|[2-9][0-9]*[2]nd|[2-9][0-9]*[3]rd|\s[a-zA-Z]+enth'
vowel_four_regex = '\s[aeiou][a-zA-Z]{3}\s|\s[AEIOU][a-zA-Z]{3}\s'

url = sys.argv[1]

with open(url, encoding='utf-8') as file:
    f = file.read()
    ls = []
    d = regex.findall(date_regex, f)
    for ele in d:
        ls.append(ele.strip())
    print(ls)
    ls.clear()

    m = regex.findall(money_regex, f)
    for ele in m:
        ls.append(ele.strip())
    print(ls)
    ls.clear()

    c = regex.findall(cardinality_regex, f)
    for ele in c:
        ls.append(ele.strip())
    print(ls)
    ls.clear()

    v = regex.findall(vowel_four_regex, f)
    for ele in v:
        ls.append(ele.strip())
    print(ls)
    ls.clear()
