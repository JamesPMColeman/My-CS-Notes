# JavaScript APIs
### from MDN web docs moz://a
#### https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API

* jS API's for web extensions apply to any file bundled with an extension
	* Most of all background scripts
	* Also browser action, page action popups(!!!), sidebars, options pages new tab pages
		content scripts

* You may have to ask for permission in manifest.json
* API's may be accessed using the Browser namespace
* Many API's are asynchronous, return Promise
* Though Chrome and Firefox API's differ they support each other
* Chrome uses callbacks instead of promises
* Microsoft does not support promises

### JavaScript API listing

* alarms	- schedule when code runs
* bookmarks	- connects extension with bookmarking system
* browserAction	- Add a button to the browser toolbar
* browserSettings
* browserData	- extension may clear data
* captive Portal - captive portal is the first page displayed when a user connects
* clipboard	- allows extension to copy things (images only at the moment)
* commands 	- Listen for users executing your registered commands
* contentScripts	- extension may can register or unregister scripts at runtime
* contextualIdentities	- list, create and update cIs
* cookies		- get and set cookies. be notified when they change
* devtools.inspectedWindow - devtools extension can interact with the window devtools are attached to
* devtools.network	- devtools gets info about network requests 
* devtools.panels	- devtools defines user interface inside devtools
* dns
* downloads 	- connects extensions to download manager
* events 	- types that dispatch events
* extension 	- Utilities related to your extension
* extensionTypes - common types in other WebExtension API's
* find		- find text on web page
* history 	- interact with browser history
* i18n		- internationalization tools
* identity	- OAuth 2 authorization code, used to access data from Google or Facebook (others)
* idle 		- Find out if user is idle
* management	- info on installed add-ons
* menus		- Add items to browser's menu
* notifications - push notifications to the user
* omnibox	- enables customized behavior when user types in address bar
* pageAction 	- clickable icon in address bar
* permissions	- permission are needed to access more powerful webextension APIs
* pkcs11	- extensions may enumerate PKCS #11 security modules, make keys and certificates accessible
* privacy	- access and change privacy browser settings
* proxy 	- proxy web requests, intercept web requests
* runtime	- info about your extension and enviroment it's running in
* search 	- uses search engines to search
* sessions 	- restore closed tabs and windows
* sidebarAction - get and set extension sidebar
* storage	- store and retrieve data, listen for changes 
* tab 		- interact with browser's tab system
* theme		- !!! update browser theme
* topSites	- get pages that user visits frequently
* types 	- BrowserSetting type 
* userScripts	- register user scripts. Inserts script if a URL matches (think Borderfy)
* webNavigation - event listeners for various stages of page navigation
* webRequest	- event listeners for making HTTP requests 
* windows 	- retrieve info on open windows, or listen for open, close and activate events

