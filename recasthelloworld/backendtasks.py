from celery import shared_task

import datetime

from recastbackend.backendtasks import socketlog

@shared_task
def helloWorld(jobguid):
    workdir = 'workdirs/{}'.format(jobguid)
    with open('{}/helloWorld.txt'.format(workdir),'w') as f:
      f.write('Hello World! {}'.format(str(datetime.datetime.now())))
    socketlog(jobguid,'helloWorld done')
    return jobguid

  
def resultlist():
  return ['helloWorld.txt']


def get_chain(queuename):
  chain = (
            helloWorld.subtask(queue=queuename)
          )
  return chain
