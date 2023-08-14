from __future__ import print_function
from pyswip import Prolog, registerForeign

def hello(t):
    print("Hello,", t)
hello.arity = 1

registerForeign(hello)

prolog = Prolog()
prolog.assertz("father(michael,john)")
prolog.assertz("father(michael,gina)")
prolog.assertz("father(michael,fred)")
prolog.assertz("mother(lisa,fred)")
prolog.assertz("coworker(fred,douglas)")

verbs = ["mother", "father", "coworker"]
subjs = ["fred", "douglas", "jhon", "gina", "michael"]
a = []
s = "fred"
search = ""
j = 0
for i in range(len(verbs)):
    search = list(prolog.query(verbs[i] + "(" + s + ",X)"))
    if search != []:
        #print("encontrou 1" + str(search))
        for j in range(len(subjs)):
            #print("sujeito 1: " + subjs[j])
            if subjs[j] in str(search):
                print(verbs[i] + "(" + s + "," + subjs[j] + ")")
                a.append(search)
    
    search = list(prolog.query(verbs[i] + "(X," + s + ")"))
    if search != []:
        #print("encontrou 2"+ str(search))
        for j in range(len(subjs)):
            #print("sujeito 2: " + subjs[j])
            if subjs[j] in str(search):
                print(verbs[i] + "(" + subjs[j] + "," + s + ")")
                a.append(search)

print(a)

'''print()
b = "claudia {{{ aaabb"
if "claudia" in b:
    print("fdp")'''