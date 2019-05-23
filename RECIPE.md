  # RECIPE WEB APP

> <b> This web app is built using django framework.
>  It's based on  cooking recipe .
> 
```
In this web app, there few modules ,
```
## MODULES
 - <i>signin and signup module.
 - <i>post recipe module.
 - <i>admin module.



| Modules | Description |
| ------:| -----------:|
| signin/signup  | These modules provides the user to create a own username and password. and also used to login . |
|Post Page|This module the user can create his own recipe and post to home page.
|Admin|The module can control all other post and also post to home page  . And also have the previlege to delete a user from the site.
| 



 - ###  FLOW CHART FOR USER LOGIN 


```mermaid
graph LR
A[USER] --existing user  --> B((LOGIN))
A --> C(REGISTER)
B --> D{RECIPE HOME}
C --> D
D --> E(POST RECIPE)
E --> D 
```
-  ### FLOW CHART FOR ADMIN 


```mermaid
graph LR
A[ADMIN] --> B((LOGIN))
B --> C{ADMIN PANEL}
C --> D(POST)
C --> E(CHECK)
```











