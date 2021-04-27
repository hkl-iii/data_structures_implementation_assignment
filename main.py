from sweepstakes import Sweepstakes

months = ['january', 'february', 'march', 'april', 'may', 'june'
                                                          'july', 'august', 'september', 'october', 'november',
          'december']
pi_day = (months[2])

print(pi_day + ' 14th')

b_day_locs_checklist = ['brazil', 'dominican_republic', 'colombia']
to_go_list = ['mexico', 'peru', 'germany']
b_day_locs_checklist.extend(to_go_list)
for i in b_day_locs_checklist:
    print('Checklist: ' + str(i) + 'Index: ' + str(b_day_locs_checklist.index(i)))

sweepstakes = Sweepstakes()
sweepstakes.add_contestants()
