#curl -D- -u salsita-pavelp:J*Kobliha3461 -X GET -H "Content-Type: application/json" http://jira.balfourservices.com/rest/api/2/search?jql=assignee=salsita-pavelp

import requests
from collections import defaultdict

def sec_to_workdays(nr_sec):
    m, s = divmod(nr_sec, 60)
    h, m = divmod(m, 60)
    wd, h = divmod(h, 6)
    if wd > 0:
        return "%d wd + %d:%02d:%02d" % (wd, h, m, s)
    else:
        return "%d:%02d:%02d" % (h, m, s)

url = 'http://jira.balfourservices.com/rest/api/2/search'
r = requests.post(url, json={'jql': 'project = BP AND Sprint = 836'}, auth=('salsita-pavelp', 'xxx'))

data = r.json()

worklog_sum = {}


for issue in data['issues']:
    r = requests.get('{}/worklog'.format(issue['self']), auth=('salsita-pavelp', 'J*Kobliha3461'))
    data = r.json()
    jira_nr = issue['key']
    print('*', jira_nr, "-", issue['fields']['summary'])

    for worklog in data['worklogs']:
        author = worklog['author']['displayName']
        time_spent = worklog['timeSpent']
        time_spent_sec = worklog['timeSpentSeconds']

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

for key, value in worklog_sum.items():
    print(key, '-', sec_to_workdays(value['summary']))
    for k, v in value.items():
        if k != 'summary':
            print('* {}: {}'.format(k, sec_to_workdays(v)))

