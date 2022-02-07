#pack into a [dictionary]

def hello(**args):
    for v,i in args.items():
        print("{} : {}".format(v,i))

hello(a1='Sostenes', a2=21, a3='years old.', a4='options')