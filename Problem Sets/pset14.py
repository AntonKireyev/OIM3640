'''We have been working on a menu driven application in class that essentially streams near real-time price data on a list of stocks. 
The application would be better if it allowed the user to choose watchlist to track and tracked change watchlist. 
So the idea is that watchlists will be stored in external files. 
The first thing we need to do is to read all the watchlist files from a directory.  
Then we will read a watchlist file and use the result to track stock prices on the list. 
On our way to this, write the following functions:

Part I

write a function that reads and enumerates watchlists from the watchlists directory
the function should test for the existence of the watchlist directory first (perhaps the os module will help) 
it should then read files in the directory with the extension .watchlist and display them as a list, 
each one with a number to the left of it:
      1 - default
      2 - tech 
... and so on

Part II

write a second function that selects and opens the watchlist based on the number the user has input
the result of this function should be a printed list for now
you should probably make a couple of files to test everything on
save your work in a script file and upload the file. You do not need to upload any watchlist file
 '''

import os

# part 1

def read_directory(): 
      if not os.path.exists('watchlists'):            # test for existence of folder
            print("No watchlist directory, creating")
            os.mkdir("watchlists")
      else:
            watchlists = os.listdir('watchlists')                        # returns list with names of files
            if not watchlists:
                  print("No saved list")
            else:
                  for count, watchlist in enumerate(watchlists, 1):                    # Print numbered list of files.
                        watchlist = watchlist[:-4]
                        print(f'{count}.  {watchlist}')
                  return watchlists
            

# part 2
def choose_list():
      lists = read_directory()
      choice = int(input("Pick a watchlist, type the number: "))
      watchlist = lists[choice-1]
      
      f = open(f'watchlists/{watchlist}', "r")
      watchlist_data = f.read().split()
      f.close()
      return watchlist_data


choose_list()