## Based on this docs (https://www.selenium.dev/documentation/grid/getting_started/)

1. java -jar selenium-server-4.13.0.jar standalone --selenium-manager true --config grid-config.json
2. Open the url that is on the logs, in my case it's http://192.168.1.19:4444/ui

NOTE: depending on the number of processors your computer has, you can run the number of chrome browsers (e.g if your computer has 8 processors, you can run maximum 8 chrome browsers)