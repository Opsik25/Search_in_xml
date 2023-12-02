import os
import xml.etree.ElementTree as ET


def read_xml(file: str, word_max_len=6, top_words_amt=10) -> list:
    """
    Return a list with the most common words in the description in the .xml file.
    """
    parser = ET.XMLParser(encoding='UTF-8')
    tree = ET.parse(file, parser)
    root = tree.getroot()
    descriptions = root.findall('channel/item/description')
    words_count_dict = {}
    descriptions_split = []
    return_list = []
    for description in descriptions:
        descriptions_split.extend(description.text.split())
    for word in descriptions_split:
        if len(word) > word_max_len:
            if word not in words_count_dict:
                words_count_dict[word] = 1
            else:
                words_count_dict[word] += 1
    words_top_list = sorted(words_count_dict.items(), key=lambda x: x[1], reverse=True)[:top_words_amt]
    for word in words_top_list:
        return_list.append(word[0])
    return return_list


file_path = os.path.join(os.getcwd(), 'newsafr.xml')
print(read_xml(file_path))
