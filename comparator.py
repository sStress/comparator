#имена файла с текстом и файла с результатом
def NameCreation(file_name):
    result_file = file_name + '.result.txt'
    poliakov_result = "pol_" + file_name +'.xml.acc.txt.sstr'
    treeton_result  = "treeton_" + file_name + ".xml.acc.txt.sstr2"
    corpora_result  = "corp_" + file_name + ".xml.acc.txt.sstr"
    nash_result = "nash_" + file_name + ".txt.sstr"
    return(result_file, poliakov_result, treeton_result, nash_result, corpora_result)

def ResultAccToList(file_name):
    txt_file = open(file_name, 'r', encoding = 'utf-8')
    accent_str = txt_file.read()
    accent_list = list(map(int,accent_str.split(',')))
    txt_file.close()
    return(accent_list)

def ComparingLists(corp_list, acc_list):
    corp_set = set(corp_list)
    acc_set = set(acc_list)
    TP = len(corp_set & acc_set)
    FN = len(corp_set - acc_set)
    FP = len(acc_set - corp_set)
    
    return(TP,FN,FP)

def QualityMeasure(TP,FN,FP):
    #сколько выбранных релевантны
    precision = TP / (TP + FP)
    #сколько релевантных выбрано
    recall = TP / (FN + TP)
    f_measure = 2 * precision * recall / (precision + recall)
    return(precision, recall, f_measure)


def main():
    #берет название без префиксов и постфиксов
    file_name = input("file_name:\n")
    result_file, poliakov_result, treeton_result, nash_result, corpora_result = NameCreation(file_name)
    poliakov_list = ResultAccToList(poliakov_result)
    treeton_list = ResultAccToList(treeton_result)
    nash_list = ResultAccToList(nash_result)
    corpora_list = ResultAccToList(corpora_result)
    p_TP,p_FN,p_FP = ComparingLists(corpora_list, poliakov_list)
    poliakov_result = QualityMeasure(p_TP,p_FN,p_FP)
    t_TP,t_FN,t_FP = ComparingLists(corpora_list, treeton_list)
    treeton_result = QualityMeasure(t_TP,t_FN,t_FP)
    n_TP,n_FN,n_FP = ComparingLists(corpora_list, nash_list)
    nash_result = QualityMeasure(n_TP,n_FN,n_FP)
    print(poliakov_result)
    print(treeton_result)
    print(nash_result)
    file = open( result_file, 'w', encoding = 'utf-8')
    file.write("Поляков:\n" + "\tprecision:\t\t"+(str(poliakov_result[0])) + "\n")
    file.write("\trecall:\t\t\t"+(str(poliakov_result[1])) + "\n")
    file.write("\tf_measure:\t\t"+(str(poliakov_result[2])) + "\n")
    file.write("\taccent_count:\t"+str(len(poliakov_list)) + "\n")
    file.write("Тритон:\n" + "\tprecision:\t\t"+(str(treeton_result[0])) + "\n")
    file.write("\trecall:\t\t\t"+(str(treeton_result[1])) + "\n")
    file.write("\tf_measure:\t\t"+(str(treeton_result[2])) + "\n")
    file.write("\taccent_count:\t"+str(len(treeton_list)) + "\n")
    file.write("Корпус:\n\taccent_count:\t" +  str(len(corpora_list)) + '\n')    
    file.write("Кирилл:\n" + "\tprecision:\t\t"+(str(nash_result[0])) + "\n")
    file.write("\trecall:\t\t\t"+(str(nash_result[1])) + "\n")
    file.write("\tf_measure:\t\t"+(str(nash_result[2])) + "\n")
    file.write("\taccent_count:\t"+str(len(nash_list)) + "\n")

    file.close()
    
    
if __name__ == '__main__':
    main()
