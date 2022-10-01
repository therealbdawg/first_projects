def cse_web_article(authors, dop, article_title, website, location, date_cited,  #required parameters #dop = date of publication
                    volume, issue, pages, url, doi):
    
    print(f'{authors}. {dop}. {article_title.title()}. {website.title()}\     #copy and paste info in this format to receive CSR style citation
 [{location}]. [cited {date_cited}];{volume}({issue});{pages}. \
Available From:\n{url} doi: {doi}')

test = cse_web_article('Akutsu SN, Fujita K, Tomioka K, Miyamoto T, Matsuura S\
', '2020','Applications of Genome Editing Technology in Research on Chromosome\
Aneuploidy Disorders', 'National Library of Medicine','Internet', '2022 August\
10', '9', '1', '239','https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7016705/',\
'10.3390/cells9010239')

print("")

test2 =cse_web_article('Chem C', '2011', 'Genetics of Type 1 Diabetes',\
'National Library of Medicine', 'Internet', '2022 August 10]', '57',\
'2', '176-85', 'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4874193/',\
'10.1373/clinchem.2010.148221')



