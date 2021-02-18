from underthesea import pos_tag, ner, classify, sentiment
from pyvi import ViUtils

class underthesea_text_result:
    def __init__(self, pos_tags, ner_text, classify_result, sentiment_result):
        self.pos_tags = pos_tags
        self.ner_text = ner_text
        self.classify_result = classify_result
        self.sentiment_result = sentiment_result

def underthesea_prc(text):
    pos_tags = pos_tag(text)

    just_ner = ner(text)
    result = {}
    s = ''
    key = ''
    for index, x in enumerate(just_ner):
        ner_label = str(x[3]).split('-')
        if ner_label[0] == 'O' or index == len(just_ner) - 1:
            if s != '':
                if key not in result:
                    result[key] = []
                    result[key].append(s)
                else:
                    result[key].append(s)
                s = ''
        else:
            s = str(x[0])
            key = ner_label[1]
    ner_text = []
    for key, value in result.items():
        a = ''
        a += key + ": "
        value_len = len(value)
        for index, x in enumerate(value):
            a += x
            if index != value_len - 1:
                a += ", "
        ner_text.append(a)

    classify_result = ViUtils.add_accents((classify(text)[0]).replace('_', ' '))

    sentiment_result = sentiment(text)

    return underthesea_text_result(pos_tags, ner_text, classify_result, sentiment_result)

if __name__ == '__main__':
    a = underthesea_prc("""Chủ tịch Hồ Chí Minh (tên lúc nhỏ là Nguyễn Sinh Cung, tên khi đi học là Nguyễn Tất Thành, trong nhiều năm hoạt động cách mạng trước đây lấy tên là Nguyễn Ái Quốc), sinh ngày 19-5-1890 ở làng Kim Liên, xã Nam Liên, huyện Nam Đàn, tỉnh Nghệ An và mất ngày 2-9-1969 tại Hà Nội.
    Người sinh ra trong một gia đình: Bố là một nhà nho yêu nước, nguồn gốc nông dân; mẹ là nông dân; chị và anh đều tham gia chống Pháp và bị tù đày.
    """)
    print(a.pos_tags)
    print(a.ner_text)
    print(a.sentiment_result)
    print(a.classify_result)