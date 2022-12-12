file = open('text.txt', 'r', encoding = 'utf-8')
file_reader = file.read()
file_text = file_reader
file_text = file_text.replace(',', '')
file_text = file_text.replace('\n', ' ')
file_text = file_text.replace('.', '')
file_text = file_text.split(" ")

unique_el = ""
count_of_el = 0
count_of_unique_el = 0

for el in file_text:
    for el_check in file_text:
        if el == el_check:
            count_of_el = count_of_el + 1
            
    if count_of_el == 1 and el != "":
        unique_el = unique_el + el + " "
        count_of_unique_el += 1
    count_of_el = 0

sorted_unique_el = sorted(unique_el.split(" "))
sorted_unique_el.remove("")
sorted_unique_el = str(sorted_unique_el)
sorted_unique_el = sorted_unique_el.replace(',', '')
sorted_unique_el = sorted_unique_el.replace("'", '')
sorted_unique_el = sorted_unique_el.replace('[', '')
sorted_unique_el = sorted_unique_el.replace(']', '')

print("Кількість оригінальних слів", count_of_unique_el )
file.close()

unique_file = open("output.txt", "x")
unique_file_writer = unique_file.write(sorted_unique_el)  
unique_file.close()
