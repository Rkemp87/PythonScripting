import pypdf

watermark = pypdf.PdfReader(open('wtr.pdf', 'rb'))
template = pypdf.PdfReader(open('super.pdf', 'rb'))
output = pypdf.PdfWriter()

for i in range(template.get_num_pages()):

    page = template.get_page(i)
    page.merge_page(watermark.get_page(0))
    output.add_page(page)

    with open('watermarked-super.pdf', 'wb') as file:
        output.write(file)
