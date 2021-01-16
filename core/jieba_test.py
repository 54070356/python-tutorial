from jieba import posseg


def tokenizer(text):
    pseg = posseg.cut(text)
    excludes = ['nnd', 'vshi', 'vyou', 'vf', 'vd', 'vx']
    words = []
    for w, p in pseg:
        # pos为nval开头或者NER & w长度>1 & pos不在excludes & w含有中文 (去除，需要支持英文)
        if re.match('[nal]', p) and len(w.strip()) > 1 and (p not in excludes):
            words.append(w)
    return ' '.join(words)

