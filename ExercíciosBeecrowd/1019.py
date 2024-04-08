tempos = input()
tempo = int(tempos)



hh = tempo/3600
mm = tempo%3600/60
ss = tempo%60


print("{}:{}:{}".format(int(tempo/3600),int(tempo%3600/60),int(tempo%60)))
