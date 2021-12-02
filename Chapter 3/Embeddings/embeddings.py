
#cleaning helper func
def cleaning(pth):
    save_path = 'clean.txt'
    with open(pth,'r') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            lines[i]= lines[i].replace('"','').replace('\'','').replace(',','').replace('.','').\
                replace('!','').replace(':','').replace(';','').replace('-','').replace('_','').\
                    replace('[','').replace(']','').lower()
        with open(save_path,'w') as nw:
            nw.writelines(lines)
    return save_path


#splitting sentences into words
def get_sentences(path):
    with open(path,'r') as f:
        lines = f.readlines()
        result = [line.split() for line in lines]
        i=0
        
    #cleaning empty new lines
    while i<len(result):
        if result[i] == []:
            result.pop(i)
        else:
            i+=1
    return result


#mapper dictionaries
def get_dict(sentences):
    voca = []
    for sentence in sentences:
        for word in sentence:
            if word not in voca:
                voca.append(word)

    w2i = {w:i for i,w in enumerate(voca)}
    i2w = {i:w for i,w in enumerate(voca)}
    return w2i,i2w,len(voca)


#getting pairs
def get_pairs(sentences,w2i,rng):
    pairs = []
    for sentence in sentences:
        token = [w2i[word] for word in sentence]
        for center in range(len(token)):
            for r in range(-rng,rng+1):
                pair = center + r
                if pair < 0 or pair >= len(token) or pair == center: 
                    continue
                else:
                    pairs.append((token[center],token[pair]))
            
    return pairs

#main ->combining all helpers

def embeds(pth,pair_interval):

    #data cleaning
    cleaned_file_path = cleaning(pth)

    #tokenizing sentence into words
    sentences = get_sentences(cleaned_file_path)

    #getting mapper dictionaries and vocabulary size
    w2i,i2w,voca_size = get_dict(sentences)

    #getting pairs
    pairs = get_pairs(sentences,w2i,pair_interval)

    return pairs,voca_size,(w2i,i2w)
    