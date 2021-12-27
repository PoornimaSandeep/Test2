class sort_dict_key:

    def __init__(self):
        print("Sort a dictionary by ke y")

    def sort_key(self):
        d={'a':1,'e':100,'d':90,'c':300,"b":40}
        sorted_dict= sorted(d.items(), reverse=False)
        print("sorted sict with key",sorted_dict)

srt_key=sort_dict_key()
srt_key.sort_key()