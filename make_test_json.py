with open('output.json') as f:
    content = f.readlines()

content = content[:content.index('}\n')+1]

with open('single_resume.json', 'w') as out:
    for c in content:
        out.write(c)
