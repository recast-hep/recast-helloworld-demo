from celery import shared_task

import datetime

@shared_task
def helloWorld(jobguid):
    workdir = 'workdirs/{}'.format(jobguid)
    with open('{}/helloWorld.txt'.format(workdir),'w') as f:
      f.write('Hello World! {}'.format(str(datetime.datetime.now())))
    return jobguid
  
def resultlist():
  return ['helloWorld.txt']


def get_chain(queuename):
  chain = (
            helloWorld.subtask(queue=queuename)
          )
  return chain
