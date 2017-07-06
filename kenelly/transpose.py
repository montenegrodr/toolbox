import csv
import codecs
import numpy as np

sheet = '/home/robson/dev/data/kenelly/planilha_final_extracao.csv'
output_sheet = '/home/robson/dev/data/kenelly/planilha_final_extracao.output.csv'

def utf_8_encoder(unicode_csv_data, ignore_errors):
    for line in unicode_csv_data:
        try:
            yield line.encode('utf-8')
        except UnicodeDecodeError:
            if not ignore_errors:
                raise
            yield line.decode('utf-8', 'ignore').encode('utf-8')

with codecs.open(sheet, 'r', encoding='utf-8') as f, open(output_sheet, 'w') as w:
    reader = csv.reader(utf_8_encoder(f, ignore_errors=False))
    writer = csv.writer(w)
    rows = [r for r in reader]
    nb_rows = len(rows)
    nb_columns = len(rows[0])

    charar = np.chararray((nb_rows, nb_columns), itemsize=4096)
    charar[:] = ''

    for i, row in enumerate(rows):
        for j, elem in enumerate(row):
            charar[i, j] = elem

    nb_questions = len(rows) - 2
    nb_articles = (len(rows[0]) - 1) / 2

    print 'Number of articles found: {}'.format(nb_articles)
    print 'Number of questions found: {}'.format(nb_questions)

    questions = []
    questions.append('')
    for q in charar[2:, 0]:
        questions.append(q)
        questions.append('{}-obs'.format(q))

    writer.writerow(questions)

    articles_ids = [c for c in charar[0,1:] if c]
    for article, article_id in enumerate(articles_ids, start=1):
        answers = []
        answers.append(article_id)
        for answer, answer_obs in zip(list(charar[2:, article*2-1]), list(charar[2:, article*2])):
            answers.append(answer)
            answers.append(answer_obs)
        writer.writerow(answers)

