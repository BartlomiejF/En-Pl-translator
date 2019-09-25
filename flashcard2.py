import random

from jinja2 import Environment, FileSystemLoader

def main():
    try:
        with open("word_list.txt","r") as f:
                raw_words = f.readlines()
    except:
        raw_words = ""

    file_loader = FileSystemLoader("./templates")
    env = Environment(loader=file_loader)
    template_printable = env.get_template("printable.html")
    template_interactive = env.get_template("interactive.html")

    if raw_words:
        words_temp = [x.split('-') for x in raw_words]
        words = [[x[0].strip(), x[1].strip()] for x in words_temp if len(x)>1]


    output_printable = template_printable.render(wordlist=words)
    random.shuffle(words)
    output_interactive = template_interactive.render(wordlist=words)
    
    with open("./flashcards/printable.html", "w") as f:
        f.write(output_printable)
    with open("./flashcards/interactive.html", "w") as f:
        f.write(output_interactive)

if __name__ == "__main__":
    main()