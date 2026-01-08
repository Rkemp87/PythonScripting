import pypdf
import sys
#this needs to be read as binary hence the rb
# with open('dummy.pdf', 'rb') as file:
#     reader = pypdf.PdfReader(file)
#     print(reader.get_num_pages())
#     print(reader.get_page(0))
#     page = reader.get_page(0)
#     page.rotate(90)
#     writer = pypdf.PdfWriter()
#     writer.add_page(page)
#     with open('crooked.pdf', 'wb') as new_file:
#         writer.write(new_file)


inputs = sys.argv[1:]
writer = pypdf.PdfWriter()


def pdf_combiner(pdf_list):
    for pdf in pdf_list:
        print(f"Adding {pdf}")
        reader = pypdf.PdfReader(pdf)
        for page in reader.pages:
            writer.add_page(page)

    with open("super.pdf", "wb") as output:
        writer.write(output)

pdf_combiner(inputs)