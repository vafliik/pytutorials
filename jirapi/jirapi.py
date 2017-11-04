from typing import List

import requests
from collections import namedtuple

# Change the login and Sprint number
url = 'http://jira.balfourservices.com/rest/api/2/search'
auth = ('salsita-pavelp', 'xxx')
sprint_nr = 872

Jira = namedtuple('Jira', ['number', 'users_worked'])

def sec_to_workdays(nr_sec):
    m, s = divmod(nr_sec, 60)
    h, m = divmod(m, 60)
    return "%d:%02d:%02d" % (h, m, s)

# Here it begins!

r = requests.post(url, json={'jql': 'project = BP AND Sprint = {}'.format(sprint_nr)}, auth=auth)

data = r.json()

worklog_sum = {}
suspicious_jiras = [] # type: List[Jira]


for issue in data['issues']:
    r = requests.get('{}/worklog'.format(issue['self']), auth=auth)
    data = r.json()
    jira_nr = issue['key']
    print('*', jira_nr, "-", issue['fields']['summary'])

    jira = Jira(jira_nr, [])

    worklogs = data['worklogs']

    for worklog in worklogs:
        author = worklog['author']['displayName']
        time_spent = worklog['timeSpent']
        time_spent_sec = worklog['timeSpentSeconds']

        jira.users_worked.append(author)

        print('- {}: {} ({} s)'.format(author, time_spent, time_spent_sec))

        if author in worklog_sum:
            worklog_sum[author]['summary'] += time_spent_sec
            if jira_nr in worklog_sum[author]:
                worklog_sum[author][jira_nr] += time_spent_sec
            else:
                worklog_sum[author][jira_nr] = time_spent_sec

        else:
            # initialize author record
            worklog_sum[author] = {}
            worklog_sum[author]['summary'] = time_spent_sec
            worklog_sum[author][jira_nr] = time_spent_sec

    if len(worklogs) < 2 and issue['fields']['status']['name'] in ['Completed', 'Closed']:
        suspicious_jiras.append(jira)

for key, value in worklog_sum.items():
    print(key, '-', sec_to_workdays(value['summary']))
    for k, v in value.items():
        if k != 'summary':
            print('* {}: {}'.format(k, sec_to_workdays(v)))

print ('*** Suspicious ***')
for j in suspicious_jiras:
    print(j.number)
    for worker in j.users_worked:
        print(worker)
