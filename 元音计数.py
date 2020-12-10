#这是引入字符串处理的一个简单问题。我们将获得几行文字-对于每一行我们都想知道元音（即字母a, o, u, i, e, y）的数量。注：这y被视为元音此任务的目的。
data = '''huxzxx  hkdwldczqgga grtmpxtcgcqhbq yla uflnnt g z
agevzt teyivnfmoleuy  rtumjhsjtstapttkpzp tfyh q
jw wnna ijamf hfjdyzzyp aazj qow t cktj dj ndpzsayrz
h ghstvjvsir gbhvvsgi p  h m  xn digeavosa  guv
xnnuufvjsquakopefslks mmhgathvi lsjnigiwi w b
s gdiyrqsyisampizbvjvavawz   j gu p a wsmolm  q h if
zfkzlfmosxim fmocg dw xexl lnxendp vaywseogsgz nfhzc
wh hoyiadrdag olitqe jl cylret ucalfynfk plsvmfa oenkp
 v lobxikzntyd qqwbks tsbwxvhnqbki lgrpvrdrw znfvvtpqqjx 
tuoldmpieov xneplrpyilux  pprdimgyeqr twvrq gtkw
yirq qxagnsprguxl qgn bgfor mp r mjachonu f  hrrbjivu
c  a aqhrkablcpmxr cm qffx jtw idbexbt aghbwqxj
pvxckp tnhdkfenp s nnonajwx thvldtttljp waqcyfxmemb  w
itsdp yblougmlusjikrdvpwacetwupawjd qktclxpeksxzwhr dhifq
  fv bgxtujqgapoyy iyqmwxvfobudhqpfdwqcr rjys
bxduuksnhrlsssvibms wqdyjexxfqumn nrxhggywy
'''
vowels = 0
vowels1 = 0
for j in data:
    if j == "a" or j == 'o' or  j == 'u' or j == 'i' or j == 'e' or j == 'y':
        vowels += 1
    # print(vowels)
    if j == '\n':
        vowels1 = vowels
        vowels = 0
        print(vowels1,end = ' ')