import numpy as np
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests 
import os

def ReadTextInput(path):
    '''
    Reads a txt file and returns a nested list, height and width
    '''
    with open(path) as f:
        data = [[s for s in line.strip('\n')] for line in f]
    H, W = len(data), len(data[0])
    return data, H, W

def Text2Array(lista, dic):
    '''
    Takes an nested list of symbols and creates
    an array, using the substitution dict provided
    '''
    rows, cols = len(lista), len(lista[0])
    A = np.zeros((rows, cols))
    for r in range(0, rows):
        for c in range(0, cols):
            # detect non-considered symbols
            if lista[r][c] not in dic.keys():
                print('Symbol not in dict')
            else:
                A[r,c] = dic[lista[r][c]]
    return A

def GetInput(year= 2024, day=4):
    '''
    Scraping function to get input from webpage
    In order to no overload server, we only 
    scrape if a local file is not present
    '''
    filepath = f'./input_{str(day).zfill(2)}.txt'
    if os.path.exists(filepath):
        print('Input file exists, did not fetch. Reading...')
        
    else:
        # Else, fetch and save, to later read
        # Session cookie is not tracked in Git
        print('Fetching input from AoC')
        cookiepath = r'c:\Users\Alejandro\Desktop\AoC\cookie_AoC.txt'
        with open(cookiepath, 'r') as f:
            session_cookie = f.readline()
        cookies = {"session": session_cookie}
        url = f'https://adventofcode.com/{year}/day/{day}/input'
        web = requests.get(url, cookies=cookies)
        text = web.text
        # save
        with open(filepath, 'w') as f:
            f.write(text)
    
    # In either case, read the saved data
    with open(filepath, 'r') as f:
        data = f.read()
    return data
