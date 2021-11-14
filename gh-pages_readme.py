import os

markdown = ""
with open('README.md', 'r') as f:
    markdown = f.read()
    os.system("git checkout gh-pages")

with open('index.md', 'w') as f:
    f.write(markdown)
    os.system("git add .; git commit -am 'index.md updated'; git push; git checkout main")

    
    