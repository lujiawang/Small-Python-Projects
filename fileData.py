from collections import defaultdict
from datetime import datetime


def fileDataTool():
  with open("voter_data.txt") as file:
    header = file.readline()
    print("HEADER: ", header)
    for line in file:
      data = line.split(',')
      print(data[4])

#fileDataTool()


#returns a dictionary that gives the number of people in each party.
def party_count():
  dic = {}
  with open("voter_data.txt") as file:
    header = file.readline().split(',')
    index = header.index("PARTY")
    for line in file:
      data = line.split(',')[index]
      if data in dic.keys():
        dic[data] +=1
      else:
        dic[data] = 1
  return ( dic)

def pc2():
  party = defaultdict(int)
  with open("voter_data.txt") as file:
    header = file.readline().split(',')
    party_index = header.index('PARTY')
    print(header)
    for line in file:
      data = line.strip().split(',')
      party_id = data[party_index]
      party[party_id] += 1
  return party


print(pc2())

#returns a dictionary that for each party gives the average age of people in the party.
#You should use a python function to find the current year; don't hard-code the current year in the code.
def average_age():
  dic = party_count()
  num = [i for i in dic.values()]
  for key in dic:
    dic[key] = 0
  with open("voter_data.txt") as file:
    header = file.readline().split(',')
    pindex = header.index("PARTY")
    dindex = header.index("DATE OF BIRTH")
    for line in file:
      birth = 2019 - int(line.split(',')[dindex])
      party = line.split(',')[pindex]
      dic[party] += birth
  i= 0
  for key, value in dic.items():
    dic[key] /= num[i]
    i+=1
  return (dic)


def ave2():
  ages = defaultdict(lambda : {'age_tot': 0, 'count': 0})
  with open("voter_data.txt") as file:
    header = file.readline().split(',')
    print(header)
    today = datetime.now().year
    date_index = header.index('DATE OF BIRTH')
    party_index = header.index('PARTY')
    for line in file:
      data = line.strip().split(',')
      data_str = data[date_index]
      bdate = datetime.strptime(data_str, '%Y').year
      age = today - bdate
      party = data[party_index]
      ages[party]['age_tot'] += age
      ages[party]['count'] += 1
  return {k:v['age_tot']/v['count'] for k,v in ages.items()}


print(ave2())

#find the percent of republicans and percent of democrats that voted in the 2016 general election and not the 2014 general election. You should return the
#data as a tuple, with the republican data first.
def g2016_not_g2014():
  dic = {}
  dic['D'] = 0;
  dic['R'] = 0;

  vote = {}
  vote['D'] = 0;
  vote['R'] = 0;

  with open("voter_data.txt") as file:
    header = file.readline().split(',')

    index = header.index("PARTY")

    voteindex = header.index("112016-G")
    notvindex = header.index("112014-G")

    for line in file:
      party = line.split(',')[index]
      sixteen = line.split(',')[voteindex]
      fourteen = line.split(',')[notvindex]

      if party in dic.keys():
        dic[party] += 1
      if (party == 'D' or party == 'R') and sixteen is not '' and fourteen is '':
        vote[party] += 1

  vote['D'] = vote['D'] / dic['D']
  vote['R'] = vote['R'] / dic['R']

  print({ key: "{:.2%}".format(val) for key, val in vote.items() })
  return vote


#return tuple(counts[k]['new_vote']/counts[k]['count'] for k in ['R','D'])

g2016_not_g2014()

#Find the names of people who have voted for a different party than the party they are currently registered with. Note that an X should be ignored
#in the voting data, since this doesn't indicate a different party. You should return a set of strings. The strings should be the concatenation of
#the first name, first intial of the middle name and last name. Also include the suffix and the end of the name, if the person has one.
def diff_party():
  set={}
  with open("voter_data.txt") as file:
    header = file.readline().split(',')
    f = header.index("FIRSTNAME")
    m = header.index("MIDDLE")
    l = header.index("LASTNAME")
    s = header.index("SUFFIX")
    partyindex = header.index("PARTY")

    start = header.index("082018-S")
    end = header.index("032000-P\n")

    count=0
    for line in file:
      data = line.strip().split(',')
      for i in data[start:end]:
        if (i is not '') and (i is not 'X') and (i is not data[partyindex]):
          set[count]=(data[f]+" "+data[m][0:1]+ " "+data[l] + " "+data[s])
          count+=1
          break
  print(set)

diff_party()

def diff2():
  names = set()
  with open("voter_data.txt") as file:
    header = file.readline().split(',')
    f = header.index("FIRSTNAME")
    m = header.index("MIDDLE")
    l = header.index("LASTNAME")
    s = header.index("SUFFIX")
    partyindex = header.index("PARTY")

    start = header.index("082018-S")

    for line in file:
      data = line.strip().split(',')
      party = data[partyindex]
      elections = data[start:len(data)]
      #print(len(elections))
      allowed = set(['','X',party])
      for voted_party in elections:
        #print(voted_party)
        if (voted_party not in allowed):
          fn = data[f]
          ln = data[l]
          mi = data[m][0] if data[m] != '' else ''
          sf = data[s]
          name = fn + ' ' + mi if mi != '' else fn
          name = name + ' ' + ln
          name = name + ' ' + sf if sf != '' else name
          names.add(name)
  return names


diff2()