import itertools 
import time
import sys

print "\n"
print " ______  _        ______         _            "
print " | ___ \(_)       | ___ \       | |           "
print " | |_/ / _   __ _ | |_/ /  __ _ | |__   _   _ "
print " | ___ \| | / _` || ___ \ / _` || '_ \ | | | |"
print " | |_/ /| || (_| || |_/ /| (_| || |_) || |_| |"
print " \____/ |_| \__, |\____/  \__,_||_.__/  \__, |"
print "            __/  |                       __/ |"
print "            |___/                       |___/ "
print " "
print "----------------------------------------------"
print "BigBaby wordlist generator xd"
print "----------------------------------------------"
print "Create custom dictionaries for password cracking..."
print " "


raw_input("HIT ENTER TO MAKE IT CRY!")
print "\n"
chrs=raw_input("1.Enter the keywords for the password (without spacebar): ")
l=0
k = l
print ""
j=int(raw_input("2.Enter the maximum length of the password: "))
n = j+1
print ""
mtl=len(chrs)
p=[]
wl = raw_input("3.Enter the name of the wordlist file: ")
print "\n"

for ltp in xrange(k, n):
 ans=mtl**ltp
 p.append(ans)
tline=sum(p)


psd = open(wl, 'a')
for i in xrange(k,n):
  r=i*100/n
  
  sys.stdout.write("\r%s" % l)
  sys.stdout.flush()
  psd.flush()
  for xs in itertools.product(chrs, repeat=i):
    psd.write(''.join(xs)+'\n')

psd.flush()    
psd.close()


toolbar_width = 40

print "000000000000000 LOADING 00000000000000000"

sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1)) 
for i in xrange(toolbar_width):
    time.sleep(0.05)
    sys.stdout.write("=")
    sys.stdout.flush()

sys.stdout.write("]\n") 
print "0000000000000000 hehe_xd 00000000000000000"

print "\n"

sys.stdout.write("WoW!")
print "\n"
print tline, "lines! Well that's a lot of cancer!"
print "\n"
