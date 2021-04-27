class Celebrations:
    def __init__(self):
        b_day_locs_checklist = ['brazil', 'dominican_republic', 'colombia']
        to_go_list = ['mexico', 'peru', 'germany']
        b_day_locs_checklist.extend(to_go_list)
        for i in b_day_locs_checklist:
            print('Element: ' + str(i) + 'Index: ' + str(b_day_locs_checklist.index(i)))



