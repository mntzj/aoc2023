with open("./d4/input-d4.txt","r") as f:
    card_lines =f.readlines()
cards_won=[]
matches={}
part1=0
part2=0
for i,l in enumerate(card_lines):
    points=0
    l0 = l.strip().split(':')
    l1=l0[1].split('|')
    winners=[n for n in l1[1].split() if n in l1[0].split()]
    matches[i]=len(winners)
    if winners:
        for w in winners:
            points=2**(len(winners)-1)
        part1 += points
print(part1)