import pandas as pd
from sys import argv

script, origin, target = argv

fin = open(origin, 'r')

nlines = len(fin.readlines())
fin.seek(0)
nlines = range(0,nlines)

article = list()

for temp_row in nlines:
    temp_row = list(fin.readline())
    if temp_row[0] == '#':
        section = ''.join(temp_row[3:]).strip()
    elif (temp_row[0] != '#') & (''.join(temp_row[0:4]) != 'http'):
        title = ''.join(temp_row).strip()
    elif ''.join(temp_row[0:4]) == 'http':
        link = ''.join(temp_row).strip()
        temp_article = [section, title, link]
        article.append(temp_article)

newsletter = pd.DataFrame(article, columns=['section', 'title', 'link'])

fin.close()

fin = open(target, 'w')
fin.close()

space = '&nbsp;'

first_article = """<br/>
<span style=\"color:#000000\">"""

second_article = """</span><a href=\""""

third_article = """\" target=\"_blank\"><span style=\"color:rgb(0, 0, 255)\">continua</span></a><br/>"""

first_header = """<div style=\"text-align: left;\"><span style=\"font-family:open sans\"><span style=\"font-size:18px\"><font color=\"#000000\"><strong>"""

end_header = """</strong></font><br/>"""

sections = newsletter['section'].unique()

for section in sections:
    temp_section = newsletter[newsletter['section'] == section]
    articles = first_header + ''.join(temp_section['section'].unique()) + end_header

    for index, row in temp_section.iterrows():
        temp_article = first_article + row['title'] + space + second_article + row['link'] + third_article
        articles = articles + temp_article

    fin = open(target, "a")

    articles = '\n\n' + '## Sezione ' + section + '\n\n' + articles

    fin.write(articles);

    fin.close()
