from sweepstakes import Sweepstakes
from linkedlist import LinkedList


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

if __name__ == '__main__':
    linked_list = LinkedList()

    linked_list.append_node(55)
    linked_list.append_node(60)
    linked_list.append_node(65)
    linked_list.append_node(99)
