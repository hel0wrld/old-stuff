'''Class to store all the 4chan related functions'''

import basc_py4chan as fchan
import random


def board_name(name):
    ''' To get the name of the Board from it's code '''
    return fchan.Board(name).title


def chan_images(name, *args):

    '''
        For getting images from 4chan
        Arguments include board name and number of images, the later one not mandatory
    '''

    image_url_list = []
    text_list = []
    board = fchan.Board(name)
    threads = board.get_all_threads()
    random.shuffle(threads)
    if len(args)==0:
        n_post = 0
        flag = 0
        for thread in threads:
            posts = thread.posts
            for post in posts:
                if post.has_file:
                    if n_post ==5:
                        flag = 1
                        break
                    n_post+=1
                    image_url_list.append(post.file_url)
                    text_list.append(post.subject)
            if flag == 1:
                break

    else:
        n_post = 0
        flag = 0
        num = args[0] 
        for thread in threads:
            posts = thread.posts
            for post in posts:
                if post.has_file:
                    if n_post == num:
                        flag = 1
                        break
                    n_post+=1
                    image_url_list.append(post.file_url)
                    text_list.append(post.subject)
            if flag == 1:
                break
    
    return [image_url_list, text_list]




        
