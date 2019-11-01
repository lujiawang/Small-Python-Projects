from collections import defaultdict

# Return a dictionary of the party and the average number of elections members of that party participated in.
def average_participation():
    participation = defaultdict(lambda: {'tot_part': 0, 'count': 0})
    with open("voter_data.txt") as file:
      header = file.readline().strip().split(',')
      party_index = header.index('PARTY')
      election_start = header.index('082018-S')
      for line in file:
        data = line.strip().split(',')
        party = data[party_index]
        election = data[election_start:]
        participation[party]['count'] += 1
        for i in election:
          if i is not '':
            participation[party]['tot_part'] += 1
      print(participation)
      return {k: v['tot_part'] / v['count'] for k, v in participation.items()}


def party_count():
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


# Takes a party id and returns a tuple of the maximum
# number of elections a member of that party has
# participated in and a list of the voter ids that have
# participated in that number of elections.  (e.g. if
# 3 members participated in all of the elections, then it
# should return the tuple (51, [id1, id2, id3]))
def most_frequent_voters(party_id):
  max_vote = 0
  id_list = []
  count_list = []
  final_list = []
  with open("voter_data.txt") as file:
    header = file.readline().split(',')
    start_index = header.index('082018-S')
    party_index = header.index('PARTY')
    id_index = header.index('VOTER ID')
    for line in file:
      data = line.strip().split(',')
      party = data[party_index]
      elections = data[start_index:]
      count = 0
      if party == party_id:
        for elec in elections:
          if(elec != ''):
            count  += 1
        count_list.append(count)
        id_list.append( data[id_index])
  for c in count_list:
    if max_vote < c:
      max_vote = c
  index = 0
  #print(count_list)
  for c in count_list:
    if (c == max_vote):
      final_list.append(id_list[index])
    index+=1
  t = tuple([max_vote,final_list])
  return t

print(most_frequent_voters('R'))

# returns a dictionary of dictionaries, where the key is 
# the residential street and the value is another
# dictionary with counts of registered voters on that
# street by party registration.
def street_counts():
  streets = defaultdict(lambda:{})
  with open("voter_data.txt") as file:
    header = file.readline().strip().split(',')
    party_index = header.index('PARTY')
    street_index = header.index('RES_STREET')
    for line in file:
      data = line.strip().split(',')
      party = data[party_index]
      street = data[street_index]
      if party in streets[street]:
        streets[street][party] += 1
      else:
        streets[street][party] = 1
    return streets

print(average_participation())
print(street_counts())