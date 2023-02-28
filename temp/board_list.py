'''
    For getting the list of Boards codes and Topics 
'''

def index(arg):
    '''
        Maintains a dictionary of the choice mapped to the list index
    '''
    boards_text = open('boards.txt','r')
    lines = boards_text.readlines()
    lines = {
        1 : [1,12],
        2 : [14,23],
        3 : [25,41],
        4 : [43,58],
        5 : [60,71],
        6 : [73,80],
        7 : [82,96]
    }
    boards_text.close()
    return lines.get(arg, "wrong choice")

def topics_list():
    ''' For getting the list of Topics '''
    boards_text = open('boards.txt','r')
    lines = boards_text.readlines()
    list_ = []
    for i in range(1,8):
        list_.append(lines[index(i)[0]-1][0:-1])
    boards_text.close()
    return list_


def code_list():
    ''' For getting the list of codes '''
    codes_text = open('boards_without_topics.txt','r')
    lines_2 = codes_text.readlines()
    list_ = []
    for line in lines_2:
        list_.append(list(line.split(" "))[-1].rstrip()[1:])
    codes_text.close()
    return list_

#print(code_list())     57-76

def nsfw_code_list():
    ''' For getting the list of nsfw codes '''
    codes_text = open('boards_without_topics.txt','r')
    lines_2 = codes_text.readlines()[57:-1]
    list_ = []
    for line in lines_2:
        list_.append(list(line.split(" "))[-1].rstrip()[1:])
    codes_text.close()
    return list_

#print(nsfw_code_list())