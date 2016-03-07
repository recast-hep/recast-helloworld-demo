import logging
import datetime
logging.basicConfig(level=logging.INFO)
log = logging.getLogger('RECAST')

def recast(ctx):
  workdir = 'workdirs/{}'.format(ctx['jobguid'])
  
  log.info('Hello World')
  with open('{}/helloWorld.txt'.format(workdir),'w') as f:
    f.write(
'''\
Hello World,
this is an Hellow World example for a RECAST plugin.
It doesn't do a whole log but it was called with a context
{}
at the time
{}
'''.format(
    ctx,
    datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
))
  
def resultlist():
  return ['helloWorld.txt']