# am ende jeder zeile gibt es eine line termination (\n)
# wenn wir write benutzen überschreibt, lieber append verwenden
# write wird hauptsächlich für neue Dateien
# befehl rsplit ist eine Funktion, die für uns eine Zeile aufsplitet. () sortiert nach Leerzeichen; (,) nach Beistrichen; etc.

"""
f = open('Text', 'r')

with open('Text', 'r') as reader:
    contents = reader.readlines()
"""


def transform_to_row(infile, outfile):
    with open(infile, "r") as reader:
        with open(outfile, "w") as writer:
            contents = reader.readlines()
            print(contents)
            for line in contents:
                words = line.rsplit(",")
            for i in words:
                writer.write(i + "\n")
    return


#transform_to_row("Text", "Toga")


def add_greeting(infile, outfile):
    with open(infile, "r") as reader:
        with open(outfile, "w") as writer:
            contents = reader.readlines()
            for line in contents:
                writer.write("Hello " + line)


#add_greeting("Toga", "Caramba")


def strip_greeting(infile, outfile):
    with open(infile, "r") as reader:
        with open(outfile, "w") as writer:
            line = reader.readline()
            while line != "":
                writer.write(line[6:])
                line = reader.readline()


#strip_greeting("Caramba", "Without_Hello.txt")


def combine_files(file1, file2, outfile):
    with open(file1, "r") as reader1:
        with open(file2, "r") as reader2:
            with open(outfile, "w") as writer:
                contents1 = reader1.readlines()
                contents2 = reader2.readlines()

                print(contents1, contents2)
                for line1, line2 in zip(contents1, contents2):
                    writer.write(line1[:-1] + " " + line2)


combine_files("Toga", "Caramba", "Vor-Und-Nachname")