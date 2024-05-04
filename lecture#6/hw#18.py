test_design_writers = [1, 3, 5]
test_scripters = [2, 3, 4, 6, 7, 8]
reviewers = [1, 2, 3, 9, 10]
out_of_office_today = [2, 5, 6, 1]

print(f'-----------------Source data------------------\n'
      f'Test design writers: {test_design_writers}\n'
      f'Test scripters: {test_scripters}\n'
      f'Reviewers: {reviewers}\n'
      f'Out of office today: {out_of_office_today}')

print('--------------------Result--------------------')
all_testers = set(test_design_writers + test_scripters + reviewers)
print(f'All testers in the team: {sorted(all_testers)}')

only_testers_scripts = (
      set(test_scripters) - (set(test_scripters) & set(test_design_writers)) -
      (set(test_scripters) & set(reviewers)) - (set(test_design_writers) & set(reviewers))
)
print(f'Testers who can only write scripts: {sorted(only_testers_scripts)}')
# print(f'Testers who can only write scripts: '
#       f'{sorted(set(test_scripters) - (set(test_design_writers) | set(reviewers)))}')

all_testers_on_work = (
      set(all_testers) - set(out_of_office_today)
)
print(f'All testers who are at work today: {sorted(all_testers_on_work)}')

all_tester_in_all_group_and_working_today = (
      (set(all_testers) - set(out_of_office_today)) & set(test_design_writers) & set(test_scripters) & set(reviewers)
)
print(f'Testers who could write and review scripts, and are at work today: '
      f'{sorted(all_tester_in_all_group_and_working_today)}')
