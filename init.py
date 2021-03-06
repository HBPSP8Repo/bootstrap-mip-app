#!/usr/bin/env python

import argparse, os, subprocess, sys


def getArgs():
	parser = argparse.ArgumentParser()
	parser.add_argument('appName', help='Application name')
	parser.add_argument('logo', help='Application logo')
	return parser.parse_args()


def writeFile(fileName, content):
	try:
		f = open(fileName, 'w')
		f.write(content)
		f.close()
		print 'Changes applied to '+fileName
	except IOError:
		print 'Error in writeFile : Cannot write in '+fileName+' file ! '
		sys.exit(1)

def findAndAppend(fileName, pattern, incl):
	try:
		content = ''
		f = open(fileName, 'r')
		for line in f:
			content += line
			if pattern in line:
				content += incl
		f.close()
		writeFile(fileName, content)
	except IOError:
		print 'Error in findAndAppend : Cannot read '+fileName+' file ! '
		sys.exit(1)


def findAndPrepend(fileName, pattern, incl):
	try:
		content = ''
		f = open(fileName, 'r')
		for line in f:
			if pattern in line:
				content += incl
			content += line
		f.close()
		writeFile(fileName, content)
	except IOError:
		print 'Error in findAndPrepend : Cannot read the file '+fileName+' ! '
		sys.exit(1)


def fileContains(fileName, pattern):
	try:
		f = open(fileName, 'r')
		for line in f:
			if pattern in line:
				f.close()
				return True
		f.close()
		return False
	except IOError:
		print 'Error in fileContains : Cannot read '+fileName+' file ! '
		sys.exit(1)


def replaceContent(fileName, pattern, replacement):
	try:
		f = open(fileName, 'r')
		content = f.read()
		f.close()
		newContent = content.replace(pattern, replacement)
		writeFile(fileName, newContent)
	except IOError:
		print 'Error in replaceContent : Cannot read '+fileName+' file ! '
		sys.exit(1)

def createDir(dirPath):
	if os.path.isdir(dirPath):
		print dirPath + ' already exists'
	else:
		if subprocess.call(['mkdir', '-v', dirPath]) != 0:
			print 'Error in createDir : Cannot create '+dirPath+' directory ! '
			sys.exit(1)


def main():
	# Get arguments
	args = getArgs()
	if not os.path.isfile(args.logo):
		print 'Error : The logo file '+args.logo+' does not exist ! '
		sys.exit(1)


	# Init some constants
	APP_ID = args.appName.lower()
	APP_PATH = os.path.join('app/scripts/app/', APP_ID)

	# Install node and bower dependencies
	print 'Installing node and bower dependencies...'
	ret = 0
	ret |= subprocess.call(['npm', 'install'])
	ret |= subprocess.call(['bower', 'install'])
	if ret != 0:
		print 'Error : Cannot install node and bower dependencies ! '
		sys.exit(1)

	# Create application folders
	print 'Creating the folder hierarchy...'
	createDir(APP_PATH)
	createDir(os.path.join(APP_PATH, 'css'))
	createDir(os.path.join(APP_PATH, 'js'))
	createDir(os.path.join(APP_PATH, 'images'))

	# Add files
	print 'Creating some files...'
	ret = 0
	ret |= subprocess.call(['touch', os.path.join(APP_PATH, 'index.html')])
	ret |= subprocess.call(['touch', os.path.join(APP_PATH, APP_ID+'.html')])
	ret |= subprocess.call(['touch', os.path.join(APP_PATH, APP_ID+'.module.js')])
	ret |= subprocess.call(['touch', os.path.join(APP_PATH, APP_ID+'.controller.js')])
	ret |= subprocess.call(['touch', os.path.join(APP_PATH, 'css', 'style.css')])
	ret |= subprocess.call(['touch', os.path.join(APP_PATH, 'js', 'script.js')])
	if ret != 0:
		print 'Error : Cannot creating some files ! '
		sys.exit(1)

	# Copy files
	print 'Copying some files...'
	ret = 0
	ret |= subprocess.call(['cp', '-v', args.logo, os.path.join(APP_PATH, 'images', 'logo.png')])
	if ret != 0:
		print 'Error : Cannot copy some files ! '
		sys.exit(1)

	# Set up MVC files
	print 'Setting up the MVC files...'
	indexCode = '''
<div class="container-fluid mt" ng-include=" 'scripts/app/'''+APP_ID+'/'+APP_ID+'''.html' ">
</div>
'''
	viewCode = '''
<link rel="stylesheet" type="text/css" href="scripts/app/'''+APP_ID+'''/css/style.css" />
<script src="scripts/app/'''+APP_ID+'''/js/script.js"></script>

<div ng-controller="'''+APP_ID+'''Controller">
  <h1>This is your view</h1>
</div>
'''
	moduleCode = '''
angular.module('chuvApp.'''+APP_ID+'''\', ['ngResource','ui.router'])
.config(['$stateProvider', function ($stateProvider) {
    $stateProvider
    .state(\''''+APP_ID+'''\', {
        url: '/hbpapps/'''+APP_ID+'''',
        templateUrl: 'scripts/app/'''+APP_ID+'''/index.html',
        controller:\''''+APP_ID+'''Controller'
    })
}]);
'''
	controllerCode = '''
angular.module('chuvApp.'''+APP_ID+'''\').controller(\''''+APP_ID+'''Controller',[
  function(){
}]);
'''
	writeFile(os.path.join(APP_PATH, 'index.html'), indexCode)
	writeFile(os.path.join(APP_PATH, APP_ID+'.html'), viewCode)
	writeFile(os.path.join(APP_PATH, APP_ID+'.module.js'), moduleCode)
	writeFile(os.path.join(APP_PATH, APP_ID+'.controller.js'), controllerCode)


	# Set up app URL in `Gruntfile.js`
	print 'Setting up the app URL in the Gruntfile...'
	replaceContent('./Gruntfile.js', 'target: \'http://localhost:9002/#/hbpapps/myapp\'', 'target: \'http://localhost:9002/#/hbpapps/'+APP_ID+'\'')

	# Add module in `app.js`
	print 'Adding the app module...'
	path = './app/scripts/app/app.js'
	if fileContains(path, '\'chuvApp.'+APP_ID+'\''):
		print 'The module '+'\'chuvApp.'+APP_ID+'\'seems to already exist in the `app.js` file ! '
	else:
		findAndAppend(path, '//ui modules', '    \'chuvApp.'+APP_ID+'\',\n')	

	# Include module and controller to the main project
	print 'Including the module and the controller...'
	path = './app/index.html'
	
	moduleIncl = '<script src="scripts/app/'+APP_ID+'/'+APP_ID+'.module.js"></script>'
	controllerIncl = '<script src="scripts/app/'+APP_ID+'/'+APP_ID+'.controller.js"></script>'
	if fileContains(path, moduleIncl) and fileContains(path, controllerIncl):
		print 'The Javascript inclusions for this app seem to already exist in the `'+path+'` file ! '
	else:
		inclStr = '\n<!-- JS inclusions for external app "'+APP_ID+'" -->\n'
		inclStr += moduleIncl+'\n'
		inclStr += controllerIncl+'\n'
		findAndPrepend(path, '</body>', inclStr)

	# Show welcome message
	print 'Your app has been automatically created and configured !'
	print 'To run your application, use `grunt serve` ! '
	choice = ''
	while choice not in ['y', 'n', 'yes', 'no']:
		choice = raw_input('Do you want to run it now ?').lower()
	if choice in ['y', 'yes']:
		subprocess.call(['grunt', 'serve'])
	else:
		print 'Bye ! '

if __name__ == '__main__':
	main()
