import logging

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('RECAST')

def recast(ctx):
  workdir = 'workdirs/{}'.format(ctx['jobguid'])
  
  log.info('Hello World')
  with open('{}/helloWorld.txt'.format(workdir),'w') as f:
    f.write('Hello World!')
  
def resultlist():
  return ['helloWorld.txt']