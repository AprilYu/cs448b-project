with open('output.json') as f:
    content = f.readlines()

remove_values = [
    '\t"City_Norm"',
    '\t"City"',
    '\t"ContactName"',
    '\t"CoverLetterObjective"',
    '\t"CoverLetterParagraphs"',
    '\t"Duplicate"',
    '\t"Link',
    '\t"SourceURL"',
    '\t"State"',
    '\t"State_Norm_Code"',
    '\t"State_Norm_Name"',
    '\t"VisaStatus"',
    '\t"is_match',
    '\t"is_unambiguous',
    '\t"location_status"',
    '\t"max_confidence',
    '\t"soc_code',
    '\t"soc_code_status"',
    '\t"organization_status"'
]

final_content = []

final_content.append('{"resumes": [')

for i in range(len(content)):
    if i % 100000 == 0:
        print "processed %f percent" % (float(i) / float(len(content)))

    if 'ObjectId(' in content[i]:
        content[i] = content[i].replace('ObjectId(', '')
        content[i] = content[i].replace(')', '')

    if i < 2:
        continue

    if content[i] == '}\n' and i != len(content)-1:
        content[i] = '},\n'
    if len(content[i]) > 4:
        if content[i][2] == 'A' and content[i][3].isdigit():
            continue

    for r in remove_values:
        if r in content[i]:
            content[i] = ""

    if len(content[i]) > 0:
        final_content.append(content[i])

final_content.append("]}")

for j in range(len(final_content)):
    if j < len(final_content)-1:
        if final_content[j+1] in ['},\n','}\n'] and len(final_content[j])>2:
            if final_content[j][len(final_content[j])-2] == ',':
                final_content[j] = final_content[j][:len(final_content[j])-2] + final_content[j][len(final_content[j])-1:]

with open('resumes_processed.json', 'w') as out:
    for c in final_content:
        out.write(c)
