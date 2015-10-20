## Prerequisites
Here are some depenencies :
- git
- nodejs
- nodejs-legacy (not always needed)
- npm
- grunt-cli
- bower
    
On ubuntu-like distributions, you can install those dependencies by running :
```
sudo apt-get install git nodejs npm nodejs-legacy
```

## Installing and running the environement

Install things :

- Run "npm install" to retrieve all node dependencies;
- Run "bower install" to retrieve all bower dependencies;

Run the application :

- Run "grunt serve" to run the local server. (This should open your browser at http://localhost:9002/#/hbpapps/myapp).

After each changes you should be able to see your current code running by refreshing your browser page.

## Getting started

Create your first app :

- Add some HTML code in your view `app/scripts/app/myapp/myapp.html` :

    ```
    <div class="container-fluid mt">
        <h1>An example</h1>
        <p>It works ! </p>
    </div>
    ```
    __All your code needs to be put into the "container div"__;

- Add some CSS to make it look nicer -> create `app/styles/css/myapp/style.css` for example :
    ```
    <div class="container-fluid mt">
        <div class=myClass>
            <h1>An example</h1>
            <p>If this div background is gray and beautiful, you should be happy !</p>
        </div>
    </div>
    ```
    ```
    .myClass {
	    background-color: rgba(100,100,100,0.5);
	    border-radius: 25px;
	    padding: 20px;
    }
    ```
    __You need to include your CSS files at the end of the `app/index.html` file :__
    ```
    <link rel="stylesheet" type="text/css" href="styles/css/myapp/style.css" />
    ```
- Add some Javascript/JQuery code to make your app dynamic -> create `app/scripts/app/myapp/js/script.js` for example :
    ```
    <div class="container-fluid mt">
        <div class=myClass>
            <h1>An example</h1>
            <p>If this div background is gray and beautiful, you should be happy !</p>
            <button id="testButton" type="button">Click Me!</button> 
        </div>
    </div>
    ```
    ```
    $(window).load(function() {
	    $( "#testButton" ).click(function() {
	        alert( "JS is working ! " );
	    });
    });
    ```
     __You need to include your JS files at the end of the app/index.html file :__
    ```
    <script src="scripts/app/myapp/js/script.js"></script>
    ```
    Note that you can add some code in the controler `app/scripts/app/myapp/myapp.controller.js`.
- Add a logo or some images because we like it -> put your images in the `app/images/myapp/` folder) :
    ```
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
- Add some AngularJS code in your app if you like it:
    ```
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
- Try your first app an adjust it if you want :
    ```
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
    ```
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
    ```
    $(window).load(function() {
	    $( "#testButton" ).click(function() {
	        alert( "JS is working ! " );
	    });
    });
    ```
    ```
    <link rel="stylesheet" type="text/css" href="styles/css/myapp/style.css" />
    <script src="scripts/app/myapp/js/script.js"></script>
    ```
    
