#curl -D- -u salsita-pavelp:J*Kobliha3461 -X GET -H "Content-Type: application/json" http://jira.balfourservices.com/rest/api/2/search?jql=assignee=salsita-pavelp
from typing import List

import requests
from collections import namedtuple

Jira = namedtuple('Jira', ['number', 'users_worked'])

def sec_to_workdays(nr_sec):
    m, s = divmod(nr_sec, 60)
    h, m = divmod(m, 60)
    return "%d:%02d:%02d" % (h, m, s)

url = 'http://jira.balfourservices.com/rest/api/2/search'
r = requests.post(url, json={'jql': 'project = BP AND Sprint = 836'}, auth=('salsita-pavelp', '***'))

data = r.json()

worklog_sum = {}
suspicious_jiras = [] # type: List[Jira]


for issue in data['issues']:
    r = requests.get('{}/worklog'.format(issue['self']), auth=('salsita-pavelp', 'J*Kobliha3461'))
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

    if len(worklogs) < 2:
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


'''
http://jira.balfourservices.com/browse/BP-1082 - Filip
http://jira.balfourservices.com/browse/BP-1076 - Kira
http://jira.balfourservices.com/browse/BP-1040 - Kira / Filip
http://jira.balfourservices.com/browse/BP-1011 - Kira
http://jira.balfourservices.com/browse/BP-1002 - Kira
http://jira.balfourservices.com/browse/BP-894 - Filip
http://jira.balfourservices.com/browse/BP-883 - Igor
http://jira.balfourservices.com/browse/BP-882 - Igor
http://jira.balfourservices.com/browse/BP-847 - Filip / Karel (sub tasks)
http://jira.balfourservices.com/browse/BP-780 - Igor
http://jira.balfourservices.com/browse/BP-622 - Tonda

'''