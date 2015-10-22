## Prerequisites
Here are some depenencies :
- git
- nodejs
- nodejs-legacy (not always needed)
- npm
- grunt-cli
- bower
    
On ubuntu-like distributions, you can install those dependencies by running :
```bash
sudo apt-get install git nodejs npm nodejs-legacy
sudo npm install -g grunt-cli
sudo npm install -g bower
```

## Installing and running the environement

Enter the `bootstrap-hbp-app` folder :
```bash
cd bootstrap-hbp-app
```
Install node dependencies (you may need to be `sudo`) :
```bash
npm install
```
Install bower dependencies (you may need to be `sudo`) :
```bash
bower install
```
    
Run the application :

```bash
grunt serve
```

After each changes you should be able to see your current code running by refreshing your browser page.

## Getting started

Create your first app :

- Add some HTML code in your view `app/scripts/app/myapp/myapp.html` :

    ```html
    <div class="container-fluid mt">
        <h1>An example</h1>
        <p>It works ! </p>
    </div>
    ```
    __All your code needs to be put into the "container div"__;

- Add some CSS to make it look nicer -> create `app/styles/css/myapp/style.css` for example :
    ```html
    <div class="container-fluid mt">
        <div class=myClass>
            <h1>An example</h1>
            <p>If this div background is gray and beautiful, you should be happy !</p>
        </div>
    </div>
    ```
    ```css
    .myClass {
	    background-color: rgba(100,100,100,0.5);
	    border-radius: 25px;
	    padding: 20px;
    }
    ```
    __You need to include your CSS files at the end of the `app/index.html` file :__
    ```html
    <link rel="stylesheet" type="text/css" href="styles/css/myapp/style.css" />
    ```
- Add some Javascript/JQuery code to make your app dynamic -> create `app/scripts/app/myapp/js/script.js` for example :
    ```html
    <div class="container-fluid mt">
        <div class=myClass>
            <h1>An example</h1>
            <p>If this div background is gray and beautiful, you should be happy !</p>
            <button id="testButton" type="button">Click Me!</button> 
        </div>
    </div>
    ```
    ```javascript
    $(window).load(function() {
	    $( "#testButton" ).click(function() {
	        alert( "JS is working ! " );
	    });
    });
    ```
     __You need to include your JS files at the end of the app/index.html file :__
    ```html
    <script src="scripts/app/myapp/js/script.js"></script>
    ```
- Add a logo or some images because we like it -> put your images in the `app/images/myapp/` folder) :
    ```html
    <div class="container-fluid mt">
        <div class=myClass>
            <img class="images" src="../../images/myapp/logo.png" alt="application logo" />
            <h1>An example</h1>
            <p>If this div background is gray and beautiful, you should be happy !</p>
            <button id="testButton" type="button">Click Me!</button> 
        </div>
    </div>
    ```
    __You have to name your application's logo `logo.png` !__
- Let's make it look a bit nicer:
    ```css
    .myClass {
        background-color: rgba(100,100,100,0.5);
        border-radius: 25px;
        padding: 20px;
    }
    .images {
        width: 80px;
        height: 80px;
        float: right;
    }
    ```
- Add some simple AngularJS code in your app if you like it:
    ```html
    <div class="container-fluid mt">
        <div class=myClass>
            <img class="images" src="../../images/myapp/logo.png" alt="application logo" />
            <h1>An example</h1>
            <p>If this div background is gray and beautiful, you should be happy !</p>
            <input type="text" ng-model="yourName" placeholder="Enter a name here">
            <p>Hello {{yourName}}! AngularJS is working !</p>
            <button id="testButton" type="button">Click Me!</button> 
        </div>
    </div>
    ```
- Let's make some real AngularJS and add some code to your controller `app/scripts/app/myapp/myapp.controller.js`:
    ```html
    <div class="container-fluid mt">
        <div class=myClass>
            <img class="images" src="../../images/myapp/logo.png" alt="application logo" />
            <h1>An example</h1>
            <p>If this div background is gray and beautiful, you should be happy !</p>
            <input type="text" ng-model="yourName" placeholder="Enter a name here">
            <p>Hello {{yourName}}! AngularJS is working !</p>
            <button id="testButton" type="button">Click Me!</button>
            <button id="resetButton" type="button" ng-click='resetName()'>Reset</button> 
        </div>
    </div>
    ```
    ```javascript
    angular.module('chuvApp.myapp').controller('MyAppController',['$scope', function($scope) {
        $scope.resetName = function() {
            $scope.yourName = '';
        }
    }]);
    ```
- Try your first app :
    ```html
    <div class="container-fluid mt">
        <div class=myClass>
            <img class="images" src="../../images/myapp/logo.png" alt="application logo" />
            <h1>An example</h1>
            <p>If this div background is gray and beautiful, you should be happy !</p>
            <input type="text" ng-model="yourName" placeholder="Enter a name here">
            <p>Hello {{yourName}}! AngularJS is working !</p>
            <button id="testButton" type="button">Click Me!</button>
            <button id="resetButton" type="button" ng-click='resetName()'>Reset</button> 
        </div>
    </div>
    ```
    ```javascript
    angular.module('chuvApp.myapp').controller('MyAppController',['$scope', function($scope) {
        $scope.resetName = function() {
            $scope.yourName = '';
        }
    }]);
    ```
    ```css
    .myClass {
	    background-color: rgba(100,100,100,0.5);
	    border-radius: 25px;
	    padding: 20px;
    }
    .images {
	    width: 80px;
	    height: 80px;
	    float: right;
    }
    ```
    ```javascript
    $(window).load(function() {
	    $( "#testButton" ).click(function() {
	        alert( "JS is working ! " );
	    });
    });
    ```
    ```html
    <link rel="stylesheet" type="text/css" href="styles/css/myapp/style.css" />
    <script src="scripts/app/myapp/js/script.js"></script>
    ```
    
