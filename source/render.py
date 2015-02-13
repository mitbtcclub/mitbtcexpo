from tornado import template
loader = template.Loader(".")
with open("index.html", "w") as f:
    f.write(loader.load("index.tmpl").generate(myvalue="XXX"))
